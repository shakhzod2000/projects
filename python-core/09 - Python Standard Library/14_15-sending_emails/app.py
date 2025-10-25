# MIME(multi-purpose internet mail extensions)
# MIME is a standard to define format for emails
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib # SMTP(Simple Mail Transfer Protocol)
# SMTP is communication protocol to send & receive emails over the internet

# .read_text() returns data as string
template = Template((Path(__file__).parent / "email_template.html").read_text())

message = MIMEMultipart()
# Set values for Headers
message["from"] = "Shakhzod Shermatov"
message["to"] = "sshermatov50@gmail.com"
message["subject"] = "This is a test email"
body = template.substitute({"name":"Shakhzod"})
# below format is also possible
# body = template.substitute(name="Shakhzod")
message.attach(MIMEText(body, "html"))
# .read_bytes() returns all data in binary
message.attach(MIMEImage((Path(__file__).parent / "PHOTO.JPG").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo() # it's greeting to SMTP server
    smtp.starttls() # puts SMTP connection in TLS mode
    # TLS(Transport Layer Security) - provides secure communication over the network. All commands sent to SMTP server are encrypted.
    smtp.login("shermatovshakhzod9@gmail.com", "mmnlbfjjhcosatol")
    smtp.send_message(message)
    print("Sent...")
