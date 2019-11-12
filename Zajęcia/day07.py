# import myModule
#
# myModule.hello()

#
# import myModule
#
# from myModule import hello
#
# myModule.hello()
#
# hello()

# import myModule
# from myModule import hello as helloFromModule
#
# def hello():
#     print("Dzien dobry")
#
# myModule.hello()
# hello()
# helloFromModule()

#
# import myModule
# from myModule import hello as helloFromModule
#
# import Zajęcia.otherModule as otherModule
#
# result = otherModule.add (1,2,45,12)
# print(result)

#########1. Utworzyc plik z dysku z wykorzystaniem modulu "os" 2. Przeniesc utworzony plik do kosza uzywajac modulu sen2trash 3. otworzyc gre Saper
# import os
# path = "Kosz/plik_do_usuniecia.txt"
# dir_path=os.path.dirname(path)
#
# os.makedirs(dir_path)
# open(path, "w").close()


# # tworzymy nowy katalog przy użyciu funkcji os.mkdir()
# import os
# # tworzymy plik "plikUsun.txt"
# plik = open("plikdoUsun.txt", "w")
# plik.close()
#nie dziala na linuxie
#
# import os
# import send2trash
#
#
# try:
#     os.mknod("plik_do_usuniecia.txt")
# except FileExistsError:
#     print("plik juz istnieje")
#
# send2trash.send2trash("plik_do_usuniecia.txt")
# os.system('gnome-mines')
#
#
##### dane do poczty
# login: isapy@int.pl
# hasło: isapython;
# serwer: poczta.int.pl
# uwierzytelnianie: SS



# Import smtplib for the actual sending function, nawiazuje polaczenie z serwerem
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.MIMEImage import MIMEimage

subject=input("Podaj temat")
body=input("Podaj tresc emaila")
recipient =input("Podaj adresata")

mail_body=MIMEText(body)


mail = MIMEMultipart() #ustawiamy schemat wiadomosci tekstowej
mail['Subject'] = subject
mail['From'] = "isapy@int.pl"
mail['To'] = recipient
mail.attach(MIMEText(file("pan_tadeusz.txt").read()))

server =smtplib.SMTP("poczta.int.pl")
server.starttls() #uruchomienie szyfrowanie polaczenia
server.login("isapy@int.pl", "isapython;")
server.send_message(mail)
server.quit()



#
#
# # Open a plain text file for reading.  For this example, assume that
# # the text file contains only ASCII characters.
# fp = open(textfile, 'rb')
# # Create a text/plain message
# msg = MIMEText(fp.read())
# fp.close()
#
# # me == the sender's email address
# # you == the recipient's email address
# msg['Subject'] = 'The contents of %s' % textfile
# msg['From'] = me
# msg['To'] = you
#
# # Send the message via our own SMTP server, but don't include the
# # envelope header.
# s = smtplib.SMTP('localhost')
# s.sendmail(me, [you], msg.as_string())
# s.quit()