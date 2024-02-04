[![Bot Image](https://yablyk.com/wp-content/uploads/2019/03/audio-from-youtube-in-telegram.jpg)]





# youtube-to-mp3

This repository contains the source code for a music bot built using Python, Pyrogram, and Pydub. The bot is designed to download audio from YouTube links and send them as playable audio files on Telegram.

### Features:

- **YouTube Link Processing:** Accepts YouTube links and extracts audio for download.
- **Audio Conversion:** Converts downloaded audio to MP3 format for easy playback.
- **Telegram Integration:** Sends the converted audio file to the Telegram chat.

### Instructions:

1. Send a YouTube link to the bot using the `/download` command.
2. The bot will process the link, download the audio, and send it back to the chat.
3. Enjoy your music!

### Requirements:

- Pyrogram
- Pydub
- Pytube3

### Setup:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MrMehulkhanna/youtube-to-mp3 && cd youtube-to-mp3
   ```

2. **Install the required dependencies:**

   ```bash
   source venv/bin/activate
   ```

3. **Run the bot script:**

   ```bash
   python youtube-to-mp3.py
   ```
   


Install tmux to keep running your bot when you close the terminal by 
  ```bash
sudo apt install tmux && tmux
  ```
For getting out from tmux session : Press   ```bash Ctrl+b    ```  and  ```bash then d```



### Contribution:

Feel free to contribute to this project by creating issues, suggesting enhancements, or submitting pull requests.



