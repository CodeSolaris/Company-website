import smtplib
import ssl
import os
from dotenv import load_dotenv

load_dotenv()


smtp_host = os.getenv("SMTP_HOST")
smtp_port = int(os.getenv("SMTP_PORT"))
owner_email = os.getenv("OWNER_EMAIL")
owner_password = os.getenv("OWNER_PASSWORD")

context = ssl.create_default_context()


def send_email(message: str, receiver_email: str = None) -> None:
    """
    Send an email using the owner's email account.

    Args:
        message (str): The message to be sent.
        receiver_email (str, optional): The receiver's email address. If not provided,
                                         the owner's email address will be used.
    """
    receiver_email = receiver_email if receiver_email else owner_email

    try:
        # Connect to the SMTP server
        with smtplib.SMTP_SSL(smtp_host, smtp_port, context=context) as server:
            # Login to the owner's email account
            server.login(owner_email, owner_password)
            message = message.encode("utf-8")
            # Send the email
            server.sendmail(owner_email, receiver_email, message)
    except smtplib.SMTPException:
        print("Error: Unable to send email. Please check your SMTP settings.")
