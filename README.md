# YouTube → MP3 Telegram bot

A small Telegram bot: send it `/download <YouTube link>` and it replies with the audio as an MP3,
with title and artist filled in.

**Stack:** Python · [Pyrogram](https://docs.pyrogram.org) (Telegram) · [yt-dlp](https://github.com/yt-dlp/yt-dlp) (download) · [Pydub](https://github.com/jiaaro/pydub) (MP3 conversion)

## How it works

1. `/download` messages are matched against YouTube URL patterns (youtube.com, youtu.be, music.youtube.com).
2. yt-dlp fetches the best available audio stream; videos longer than `MAX_MINUTES` are skipped so uploads
   stay within Telegram's limits.
3. Pydub (ffmpeg under the hood) converts it to a 192 kbps MP3.
4. Pyrogram sends it back as an audio message. Every request works in its own temporary folder, so
   simultaneous downloads never overwrite each other, and nothing is left on disk.

## Run it

Requirements: Python 3.10+ and `ffmpeg` (e.g. `sudo apt install ffmpeg` or `sudo pacman -S ffmpeg`).

```bash
git clone https://github.com/MrMehulkhanna/youtube-to-mp3 && cd youtube-to-mp3
python -m venv .venv && .venv/bin/pip install -r requirements.txt
cp .env.example .env      # then fill it in:
                          #   API_ID / API_HASH  → https://my.telegram.org  (API development tools)
                          #   BOT_TOKEN          → @BotFather on Telegram
.venv/bin/python youtube-to-mp3.py
```

Then open your bot in Telegram and send:

```
/download https://youtu.be/dQw4w9WgXcQ
```

## Notes

- `.env` is git-ignored; never commit real credentials.
- Only download audio you have the right to — respect creators and YouTube's terms.
