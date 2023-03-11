import smtplib
from imap_tools import MailBox, AND
import email.message
import os
import functools
import time
# import pathlib
# import io
# from PIL import Image
print = functools.partial(print, flush=True)



# func, which get directories from path
def get_dirs(path):
    os.chdir(f'/{path}')
    dirs = os.listdir()
    res = []
    for i in dirs: 
        res.append(i)
        res.append("#")
    result = "".join(res).replace("#", "~~~~~~~")
    return result

def mailing(pathing):
        # create a message object
        msg = email.message.Message()
        # auth
        msg['From'] = 'fromaddress'
        msg['To'] = 'toaddress'
        password = "password"
        # type the message
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(get_dirs(pathing))
        # connection
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # sending
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string())
    
# send the tree catalog
send_tree = mailing('')

def read_mails():
    global messages
    login = "login"
    password = "password"
    is_there = True
    while is_there:
        mb = MailBox("imap.gmail.com").login(login, password)
        messages = mb.fetch(criteria=AND(seen=False, from_="from___"))

        checker = 0
        for i in messages:
            res = i.text.replace("\r\n", "")
            checker += 1
        if checker == 1:
            print("THERE IS !!!!")
            print(res)
            mailing(res)
        else:
            print("CHECKING...")
            time.sleep(5)
read_mails()












