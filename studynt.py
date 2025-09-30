from datetime import datetime
from dataclasses import dataclass
from time import sleep
import random
from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
from easygui import *

# class and list for all questions in the studyset. yes it is hardcoded 
@dataclass
class qapair:
  qtext: str
  qans: list[str]
q1=qapair("FTP","20, 21")
q2=qapair("SSH & SFTP","22")
q3=qapair("Telnet","23")
q4=qapair("SMTP","25")
q5=qapair("SSH & SFTP","22")
q6=qapair("DNS","53")
q7=qapair("DHCP","67, 68")
q8=qapair("Trival File Transfer Protocol","69")
q9=qapair("HTTP","80")
q10=qapair("POP3","110")
q11=qapair("Network Time Protocol","123")
q12=qapair("NetBIOS","139")
q13=qapair("IMAP","143")
q14=qapair("LDAP Lightweight Directory Access Protocol","389")
q15=qapair("HTTPS","443")
q16=qapair("SMB Server Message Block","445")
q17=qapair("Syslog","514")
q18=qapair("SMTP TLS Transport Layer Security","587")
q19=qapair("LDAPS Lightweight Directory Access Protocol Secure","636")
q20=qapair("SQL","1433")
q21=qapair("MySQL","3306")
q22=qapair("Remote Desktop Protocol","3389")

# list to end all lists
qlist=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22]

# pre define uans and ranq
ranq=0
uans=0

 # ui time: initial prompt
qtitle="ANSWER NOW RIGHT NOW NOW"
 # ui time: wrong prompt
qwrong="WRONG. DO IT AGAIN"
 # ui time: really wrong prompt
qwmsg="EXTREMELY LOUD INCORRECT BUZZER"
ok_btn="darn"

# pull system time at runtime and save it to a variable
while uans!= qlist[ranq].qans:
   # obsolete stuff i'm keeping here just in case
   # stime1 = datetime.now()
   # print ("stime1", stime1) 
    sleep (60)
   # stime2 = datetime.now()
   # print (stime2)
   # if stime2 != stime1:
    chancer = random.randint (0,19)
    if chancer >= 10:
        ranq = random.randint (0,21)
        print (ranq)
        print (qlist[ranq].qtext)
        qmsg = f"What port # is {qlist[ranq].qtext}?"
        uans = textbox(qmsg,qtitle)
        if uans== qlist[ranq].qans:
            print ("hooray. correct")
            uans=0
        else:
            print ("wrong")
            uans = textbox(qmsg,qwrong)
            if uans!=qlist[ranq].qans:
              qwrong2=f"WRONG AGAIN. ITS {qlist[ranq].qans}"
              msgbox(qwrong2,qwmsg,ok_btn)
              continue
            else:
              print ("hooray. correct")
              uans=0
    else: uans==0
