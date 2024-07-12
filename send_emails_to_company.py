import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


sender_email = "youremail@gmail.com"
sender_password = "********"
subject = "Software engineering "
body = "Dear Hiring Manager,"



recipient_emails = [
    "test@gmail.com", "test2@gmail.com"
]


resume_path = "E:\download/Sadiq Aldubaisi CV.pdf"

smtp_server = "smtp.gmail.com"  
smtp_port = 587


def send_email(recipient_email):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        with open(resume_path, "rb") as resume_file:
            resume = MIMEApplication(resume_file.read())
            resume.add_header('Content-Disposition', 'attachment', filename="Sadiq Aldubaisi CV.pdf")
            msg.attach(resume)
            
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}. Error: {e}")

for email in recipient_emails:
    send_email(email)
