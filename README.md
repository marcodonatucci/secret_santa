# Secret Santa Email Bot 🎅📧

This project is a simple Python bot that helps organize a Secret Santa event by automatically sending an email to each participant with the name of the person they should buy a gift for. Through interactive inputs, the program allows easy entry of participant names and emails, as well as a personalized message for each email.

## Features

- **Pair Generation:** Avoids self-pairing and reciprocal assignments.
- **Automated Email Sending:** Personalizes each email with the recipient's name and the assigned gift recipient.
- **SMTP Compatibility:** Uses an SMTP server (such as Gmail) to send emails.

## Requirements

- Python 3.x
- `smtplib` module for email sending (already included in Python)
- Access to an SMTP server, like Gmail.

> ⚠️ **Note:** To send emails from a Gmail account, you may need to enable access for less secure apps or use an app password if two-factor authentication is enabled.

## Installation and Run

1. **Clone the repository**:

    ```bash
    git clone https://github.com/marcodonatucci/secret_santa.git
    cd secret_santa
    ```

2. **Run the program**:

    Start the script by running:

    ```bash
    python main.py
    ```

3. **Enter participants**:

    - Enter each participant's name and email.
    - Type `stop` as the name or email to finish input.

4. **Configure email details**:

    - Enter the email and password of the account that will send the emails.
    - Specify the email subject and body text. Use `{destinatario_nome}` and `{nome_regalato}` to automatically personalize the message.

5. **Send emails**:

    The bot will automatically send emails, assigning each participant a person to buy a gift for and notifying you of the delivery.

## Usage Example

Here is an example of a message you might use:
```plaintext
Hello {destinatario_nome}, you are the Secret Santa for {nome_regalato}! 🎁
