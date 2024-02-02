from whatsapp_chatbot_python import GreenAPIBot, Notification
from pytube import YouTube
import os
import re
import ffmpeg  # Import ffmpeg directly
from dotenv import load_dotenv

load_dotenv()
id_instance = os.getenv("id_instance")
api_token_instance = os.getenv("api_token_instance")

bot = GreenAPIBot(id_instance, api_token_instance)


@bot.router.message(text_message="start")
def message_handler(notification: Notification) -> None:
    sender_data = notification.event["senderData"]
    sender_name = sender_data["senderName"]

    notification.answer(
        (
            f"Hello, {sender_name}. Here's what I can do:\n\n"
            "1. Report a problem\n"
            "2. Show office address\n"
            "3. Show available rates\n"
            "4. Call a support operator\n"
            "5. Download a YouTube video\n\n"
            "Choose a number or send a command."
        )
    )


@bot.router.message(text_message=[".", "1"])
def report_problem_handler(notification: Notification) -> None:
    sender_data = notification.event["senderData"]
    sender_name = sender_data["senderName"]
    notification.answer(f"```Hello, {sender_name}.```")


@bot.router.message(text_message=["2", "Show office address"])
def show_office_address_handler(notification: Notification) -> None:
    chat = notification.chat
    notification.api.sending.sendLocation(
        chatId=chat, latitude=55.7522200, longitude=37.6155600
    )


@bot.router.message(text_message=["3", "Show available rates"])
def show_available_rates_handler(notification: Notification) -> None:
    notification.answer_with_file("data/bg.png")


@bot.router.message(text_message=["4", "Call a support operator"])
def call_support_operator_handler(notification: Notification) -> None:
    notification.answer("A tech support operator will contact you soon.")

def clean_filename(filename):
    # Remove characters that are not allowed in a filename
    cleaned_filename = re.sub(r'[^\w\-_. ]', '_', filename)
    return cleaned_filename

# Full path to the ffmpeg executable
ffmpeg_executable = r'.\ffmpeg.exe'

@bot.router.message(regex=r"https?://youtu\.be/([0-9A-Za-z_-]{11})")
def download_video(notification: Notification) -> None:
    chat = notification.chat
    message_data = notification.event.get("messageData", {})
    extended_text_message_data = message_data.get("extendedTextMessageData", {})
    message_text = extended_text_message_data.get("text", "")

    video_id_match = re.search(r"https?://youtu\.be/([0-9A-Za-z_-]{11})", message_text)
    
    if video_id_match:
        video_id = video_id_match.group(1)
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        try:
            yt = YouTube(video_url)
            stream = yt.streams.get_highest_resolution()
            filename = clean_filename(stream.default_filename)
            stream.download(filename=filename)
            
            file_size_mb = os.path.getsize(filename) / (1024 * 1024)
            
            # Check if file size exceeds 100 MB
            if file_size_mb > 100:
                # Remove the original file

                compressed_filename = filename.replace(".mp4", "_compressed.mp4")
                # Compress using ffmpeg with full path to the executable
                ffmpeg.input(filename).output(compressed_filename, **{'c:v': 'libx264', 'b:v': 1000000}).run(overwrite_output=True, cmd=ffmpeg_executable)
                os.remove(filename)
                filename = compressed_filename
            
            print("Cleaned filename:", filename)
            
            notification.answer_with_file(file=filename,caption=f"Downloaded: {yt.title}")
            os.remove(filename)
        except Exception as e:
            notification.answer(f"Error: {str(e)}")
    else:
        notification.answer('Enter a Valid Link')

bot.run_forever()
