from session_manager import session
from login import *

import subprocess
import os

while True:
    subprocess.run('cls'if os.name=='nt' else 'clear',shell=True)
    print('--Welcome SB Banking--')
    print('1. Login \n2. Signup \n3. Exit')
    opt=str(input('Enter Your Operation : '))
    if opt=='1':
        a=login()
        print(a)
        if a=={'message':'Login Sucessfull.'}:
            print('--Welcome To Transfer Window--')
            acc_no=str(input('Enter Receiver\'s Account Number : '))
            amount=int(input('Enter Amount : '))
            response=session.post('http://127.0.0.1:8000/transfer',json={'receiver_acc_no':acc_no,'amount':amount})
            print(response.json())
    elif opt=='2':
        b=signup()
        print(b)
    elif opt=='3':
        break
    else:
        print('wrong input')
    input('Press Enter To Continue..')