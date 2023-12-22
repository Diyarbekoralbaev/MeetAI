from eskiz.client import SMSClient
from deepgram import Deepgram
import asyncio, json
from moviepy.editor import VideoFileClip
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

DEEPGRAM_API_KEY = "fe0c0e395d0788cf1d1b130eb6c5abfd2e8baf2b"

client = SMSClient(
    api_url="https://notify.eskiz.uz/api/",
    email="diyarbekdev@gmail.com",
    password="EdnkqFQpEvEOxUH5vOKhU8oGwrXGo5Gyz6a01z4a",
)

smtp_server = "smtp.gmail.com"
smtp_port = 587 
smtp_username = "everest.meetai@gmail.com"
smtp_password = "scvs sarj zxuj psho"
recipient_email = "cobocoinweb3@gmail.com"

def send_gmail_message(subject, body):
    
    message = MIMEMultipart()
    message["From"] = smtp_username
    message["To"] = recipient_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    context = ssl.create_default_context()
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls(context=context)

    server.login(smtp_username, smtp_password)

    server.sendmail(smtp_username, recipient_email, message.as_string())

    server.quit()




async def transcribe_audio(FILE):
  
  MIMETYPE = 'audio/mp3'
  # Initialize the Deepgram SDK
  deepgram = Deepgram(DEEPGRAM_API_KEY)

  # Check whether requested file is local or remote, and prepare source
  if FILE.startswith('http'):
    # file is remote
    # Set the source
    source = {
      'url': FILE
    }
  else:
    # file is local
    # Open the audio file
    audio = open(FILE, 'rb')

    # Set the source
    source = {
      'buffer': audio,
      'mimetype': MIMETYPE
    }

  # Send the audio to Deepgram and get the response
  response = await asyncio.create_task(
    deepgram.transcription.prerecorded(
      source,
      {
            "model": "nova-2",
            "language": "en",
            "smart_format": True,
            "diarize": True,
            "summarize": "v2",
      }
    )
  )

  return response


    
def send_sms(number, message):
    resp = client._send_sms(
        phone_number=number,
        message=message
    )
    return resp