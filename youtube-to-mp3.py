"""Telegram bot: send /download <YouTube link> and get the audio back as an MP3.

yt-dlp fetches the best audio stream, Pydub converts it to MP3, and Pyrogram
sends it back to the chat. Each request works in its own temporary folder,
so simultaneous downloads never overwrite each other.
"""
import os
import pathlib
import re
import tempfile

from dotenv import load_dotenv
from pydub import AudioSegment
from pyrogram import Client, filters
from yt_dlp import YoutubeDL

load_dotenv()

MAX_MINUTES = int(os.environ.get("MAX_MINUTES", "30"))   # keep uploads within Telegram's limits
YOUTUBE = re.compile(r"https?://(?:www\.|m\.|music\.)?(?:youtube\.com|youtu\.be)/\S+")


def env(name: str) -> str:
    value = os.environ.get(name, "")
    if not value or value.startswith("your_"):
        raise SystemExit(f"Set {name} in .env — see .env.example")
    return value


app = Client("yt2mp3-bot", api_id=int(env("API_ID")), api_hash=env("API_HASH"), bot_token=env("BOT_TOKEN"))


def too_long(info: dict, *, incomplete: bool = False) -> str | None:
    if (info.get("duration") or 0) > MAX_MINUTES * 60:
        return f"longer than {MAX_MINUTES} minutes"
    return None


@app.on_message(filters.command("start"))
def start(_, message):
    message.reply_text("Send /download followed by a YouTube link and I'll send the audio back as an MP3.")


@app.on_message(filters.command("download"))
def download(_, message):
    link = YOUTUBE.search(message.text or "")
    if not link:
        message.reply_text("Usage: /download https://youtu.be/…")
        return

    status = message.reply_text("Downloading…")
    with tempfile.TemporaryDirectory() as tmp:
        options = {"format": "bestaudio/best", "outtmpl": f"{tmp}/%(id)s.%(ext)s",
                   "noplaylist": True, "quiet": True, "match_filter": too_long}
        try:
            with YoutubeDL(options) as ydl:
                info = ydl.extract_info(link.group(0), download=True)
        except Exception as error:                       # unavailable, private, region-locked …
            status.edit_text(f"Couldn't download that: {error}")
            return

        source = next((p for p in pathlib.Path(tmp).iterdir() if p.is_file()), None)
        if source is None:
            status.edit_text(f"Skipped: the video is {too_long(info) or 'unavailable'}.")
            return

        status.edit_text("Converting to MP3…")
        mp3 = pathlib.Path(tmp) / "audio.mp3"
        AudioSegment.from_file(source).export(mp3, format="mp3", bitrate="192k")
        message.reply_audio(str(mp3), title=info.get("title"), performer=info.get("uploader"),
                            duration=int(info.get("duration") or 0))
        status.delete()


if __name__ == "__main__":
    app.run()
