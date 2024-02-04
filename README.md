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

<h1>1. Clone the repository:</h1>

   ```bash
   git clone https://github.com/MrMehulkhanna/youtube-to-mp3 && cd youtube-to-mp3
   ```
 <h2> 2. Edit the environment variables:</h2>
  ```bash
  vi .env
  ```
  Press  ```I ``` on the keyboard for editing env
  Press``` Ctrl+C ``` when you're done with editing env and ``` :wq ```to save the env

 <h3>3. All dependencies already installed:</h3>

   ```bash
   source venv/bin/activate
   ```

 <h4>4.Run the bot script:</h4>

   ```bash
   python youtube-to-mp3.py
   ```
   <t> it  asks "Enter phone number or bot token: "put **bot_token** only </t>
                                                                                 
**Install tmux to keep running your bot when you close the terminal by**
  ```bash
sudo apt install tmux && tmux
  ```
For getting out from tmux session : Press   ```bash Ctrl+b    ```  and  ```bash then d```



### Contribution:

Feel free to contribute to this project by creating issues, suggesting enhancements, or submitting pull requests.



