
# WhatsApp Chatbot with GreenAPI Integration

## Overview

This is a WhatsApp chatbot developed using Python, integrated with GreenAPI for handling various user queries and interactions. The bot provides functionalities such as reporting problems, displaying office address, showing available rates, calling a support operator, and downloading YouTube videos.

## Requirements

- Python 3.10 and abobe
- Libraries:
  - `whatsapp_chatbot_python`
  - `pytube`
  - `ffmpeg`
  - `dotenv`

## Installation

1. Clone the repository:

   ```bash
   https://github.com/MuhammadRaffey/WhatsApp-Bot.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Download ffmpeg:

   - **Mega link for ffmpeg**: [Download ffmpeg](https://mega.nz/file/gGsXSZxY#95nf-S29McYpoqeFJ8oKWQnlkEdYIqxtdzr77zwhCHw)
   
   After downloading, place the ffmpeg executable in the root directory of the project.

4. Create a `.env` file in the root directory and add the following environment variables:

   ```plaintext
   id_instance="your_greenapi_id"
   api_token_instance="your_greenapi_api_token"
   ```

## Usage

Run the script `main.py`:

```bash
python main.py
```

The bot will start listening for incoming messages on the configured WhatsApp number.

## Functionality

### 1. Start

Upon receiving the message "start", the bot provides a list of available commands and options to the user.

### 2. Report a Problem

User can report a problem by selecting the corresponding option.

### 3. Show Office Address

User can request to display the office address, and the bot will send the location on the chat.

### 4. Show Available Rates

User can request to display available rates, and the bot will respond with a file containing the rates.

### 5. Call a Support Operator

User can request to call a support operator, and the bot acknowledges the request.

### 6. Download a YouTube Video

The bot detects YouTube video links in messages, downloads the video, compresses if necessary, and sends the downloaded video file to the user.

## Contributors

- [Muhammad Raffey](https://github.com/MuhammadRaffey)
