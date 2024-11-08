import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Lista di partecipanti con nomi e email
partecipanti = [
    {"nome": "nome1", "email": "email1"},
    {"nome": "nome 2", "email": "email2"}
]


# Funzione per creare le coppie senza scambi reciproci
def crea_coppie(partecipanti):
    while True:
        donatori = partecipanti[:]
        destinatari = partecipanti[:]
        random.shuffle(destinatari)

        coppie = list(zip(donatori, destinatari))

        # Controllo per evitare autogifting o scambi reciproci
        if all(donatore["nome"] != destinatario["nome"] for donatore, destinatario in coppie):
            return coppie


# Funzione per inviare l'email
def invia_email(mittente_email, mittente_password, destinatario_email, destinatario_nome, nome_regalato):
    # Configura l'email
    msg = MIMEMultipart()
    msg['From'] = mittente_email
    msg['To'] = destinatario_email
    msg['Subject'] = "oggetto email"

    body = (f"Testo della mail, ciao {destinatario_nome}, fai un regalo a {nome_regalato}")

    # Corpo del messaggio
    msg.attach(MIMEText(body, 'plain'))


    # Invia l'email tramite SMTP
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(mittente_email, mittente_password)
            server.sendmail(mittente_email, destinatario_email, msg.as_string())
            print(f"Email inviata a {destinatario_nome} ({destinatario_email})")
    except Exception as e:
        print(f"Errore nell'invio dell'email a {destinatario_nome}, che deve regalare a {nome_regalato}: {e}")


# Imposta i parametri email
mittente_email = "email_mittente@email.com"
mittente_password = "password"

# Genera le coppie e invia le email
coppie = crea_coppie(partecipanti)
for donatore, destinatario in coppie:
    invia_email(mittente_email, mittente_password, donatore["email"], donatore["nome"], destinatario["nome"])
