import base64

from email.mime.text import MIMEText


class EMailHepler:
    def __init__(self, sender, to, subject, message_text):
        self.message = self.create_message(sender, to, subject, message_text)

    @staticmethod
    def create_message(sender, to, subject, message_text):
        """Create a message for an email.

        Args:
          sender: Email address of the sender.
          to: Email address of the receiver.
          subject: The subject of the email message.
          message_text: The text of the email message.

        Returns:
          An object containing a base64url encoded email object.
        """
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        return base64.urlsafe_b64encode(message.as_string())

    def send_message(self, user_id="me"):
        """Send an email message.

        Args:
          service: Authorized Gmail API service instance.
          user_id: User's email address. The special value "me"
          can be used to indicate the authenticated user.
          message: Message to be sent.

        Returns:
          Sent Message.
        """

        return service.users().messages().send(userId=user_id, body=self.message.execute())

