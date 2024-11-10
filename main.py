import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Funzione per acquisire i partecipanti tramite input
def acquisisci_partecipanti():
    partecipanti = []
    print("Inserisci i partecipanti. Digita 'stop' per terminare.")

    while True:
        nome = input("Nome: ")
        if nome.lower() == "stop":
            break
        email = input("Email: ")
        if email.lower() == "stop":
            break
        partecipanti.append({"nome": nome, "email": email})

    return partecipanti


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
def invia_email(mittente_email, mittente_password, destinatario_email, destinatario_nome, nome_regalato, oggetto,
                testo):
    # Configura l'email
    msg = MIMEMultipart()
    msg['From'] = mittente_email
    msg['To'] = destinatario_email
    msg['Subject'] = oggetto

    # Corpo del messaggio
    body = testo.replace("{destinatario_nome}", destinatario_nome).replace("{nome_regalato}", nome_regalato)
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


# Acquisizione dei partecipanti
partecipanti = acquisisci_partecipanti()

# Acquisizione dei dati per l'invio delle email
mittente_email = input("Inserisci l'email del mittente: ")
mittente_password = input("Inserisci la password del mittente: ")
oggetto = input("Inserisci l'oggetto dell'email: ")
testo = input("Inserisci il testo dell'email (usa {destinatario_nome} e {nome_regalato} per i nomi): ")

# Genera le coppie e invia le email
coppie = crea_coppie(partecipanti)
for donatore, destinatario in coppie:
    invia_email(mittente_email, mittente_password, donatore["email"], donatore["nome"], destinatario["nome"], oggetto,
                testo)
