from .login import *
from .client_task import clients
import subprocess
import os

while True:
    subprocess.run('cls'if os.name=='nt' else 'clear',shell=True)
    print('--Welcome to SB Banking--')
    print('1. Login \n2. Signup \n3. Exit')
    opt=str(input('Enter Your Operation : '))
    if opt=='1':
        a=login()
        print(a)
        if a['message']=='Login Successfully':
            acc_no=a['acc_no']
            clients(acc_no)
    elif opt=='2':
        b=signup()
        print(b)
    elif opt=='3':
        break
    else:
        print('wrong input')
    input('Press Enter To Continue..')