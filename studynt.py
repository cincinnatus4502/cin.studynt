from datetime import datetime
from dataclasses import dataclass
from time import sleep
import random
from tkinter import *
import tkinter.messagebox

# this is how i do while loops
prgm = 1

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

qlist=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22]

# pull system time at runtime and save it to a variable
while prgm== 1:
    stime1 = datetime.now()
    print ("stime1", stime1) 
    sleep (5)
    stime2 = datetime.now()
    print (stime2)
    if stime2 != stime1:
        ranq = random.randint (0,21)
        print (ranq)
        print (qlist[ranq].qtext)
