from pyrogram import Client, filters
from pydub import AudioSegment
from pytube import YouTube
from urllib.parse import parse_qs, urlparse
import os 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Client(
    "bot_token",  # Use os.environ.get("BOT_TOKEN")
    api_id=int(os.environ.get("API_ID")),  # Convert to integer
    api_hash=os.environ.get("API_HASH")
)

@app.on_message(filters.command("start"))
def start(_, message):
    message.reply_text("Hi! I am your music bot. Send me a YouTube link, and I will download the audio. use /download with youtube link  for which Mp3 file you want")

@app.on_message(filters.command("download"))
def download_command(_, message):
    text = message.text.replace('/download ', '').strip()

    # Check if the link is a valid YouTube link
    if "youtube.com" in text or "youtu.be" in text:
        try:
            # Extract video ID
            video_id = parse_qs(urlparse(text).query).get('v') or [text.rsplit('/', 1)[-1]]
            if not video_id:
                message.reply_text("Error extracting video ID from the link.")
                return

            video_id = video_id[0]

            # Download the audio
            yt = YouTube(f'https://www.youtube.com/watch?v={video_id}')
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_file = audio_stream.download()

            # Convert to MP3
            audio = AudioSegment.from_file(audio_file)
            audio.export("temp.mp3", format="mp3")

            # Send the audio to the chat
            sent_message = app.send_audio(message.chat.id, "temp.mp3", title=yt.title, performer=yt.author)

            # Tag the bot in the sent message (handle the absence of message_id)
            if hasattr(sent_message, "message_id"):
                app.send_message(message.chat.id, f"@{app.get_me().username} Audio file ready to play!", reply_to_message_id=sent_message.message_id)
            else:
                app.send_message(message.chat.id, f"@{app.get_me().username} Audio file ready to play!")

            # Delete temporary files
            os.remove(audio_file)
            os.remove("temp.mp3")

        except Exception as e:
            error_message = str(e)
            print(error_message)
            message.reply_text(f"Error processing the YouTube link: {error_message}")
    else:
        message.reply_text("Please send a valid YouTube link.")

if __name__ == "__main__":
    app.run()
