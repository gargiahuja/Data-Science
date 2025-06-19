import smtplib
try:
    server=smtplib.SMTP("smtp.gmail.com",port=587)
    server.starttls()

    #reciever email
    receiver_mail=input("enter the receiver email: ")

    #mail credentials
    sender_mail="gargiahuja2425@gmail.com"
    password="pfwm azij safn hbkm"

    #login
    server.login(sender_mail,password)

    #sending main
    subject=input("Enter the Subject: ")
    body=input("Enter the body: ")
    message=f"subject: {subject}\n\n{body}"
    server.sendmail(sender_mail,receiver_mail,message)
    print("Mail sent successfully")

    server.quit()

except:
    print("An error occured\n")