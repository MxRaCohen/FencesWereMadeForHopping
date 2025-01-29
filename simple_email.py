# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage


# Addressee
dear = f'LovedCohen@gmail.com'

# Open the plain text file whose name is in textfile for reading.
with open('email_body.txt') as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

# Addresser
yours_truly = f'i@flourisher.live'


# Set Dressing
msg['Subject'] = f'Knock Knock'
msg['From'] = yours_truly
msg['To'] = dear

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()