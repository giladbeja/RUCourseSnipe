def alert(subject, body, to):
    import smtplib
    from email.message import EmailMessage
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = os.getenv("fromEmail")
    
    user = os.getenv("fromEmail")
    passkey = os.getenv("passkey")

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()
    server.login(user, passkey)

    server.send_message(msg)
    server.quit()
