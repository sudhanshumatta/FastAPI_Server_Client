from .session_manager import session

import subprocess
import os
import time 
import pwinput
base_path='http://127.0.0.1:8000'
def clients(acc_no):
    while True:
        subprocess.run('cls'if os.name=='nt' else 'clear',shell=True)
        print('--Welcome to SB Banking--')
        print('1. Transfer  \n2. Status \n3. Delete Profile \n4. History \n5. Logout')
        opt=str(input('Enter Your Operation : '))
        if opt=='1':
            print('--Welcome To Transfer Window--')
            receiver_acc_no=str(input('Enter Receiver\'s Account Number : '))
            pin=pwinput.pwinput(prompt='Enter Pin : ',mask='*')
            amount=int(input('Enter Amount : '))
            response=session.patch(f'{base_path}/Transfer',json={'your_acc_no':acc_no,'receiver_acc_no':receiver_acc_no,'pin':pin,'credit':amount,'debit':amount})
            print(response.json())
        elif opt=='2':
            print('--Showing Your Bank Status--')
            pin=pwinput.pwinput(prompt='Enter Pin : ',mask='*')
            response=session.post(f'{base_path}/Status',json={'acc_no':acc_no,'pin':pin})
            print(response.json())
        elif opt=='3':
            print('--Thanks For Using Our banking Service--')
            pin=pwinput.pwinput(prompt='Enter Pin : ',mask='*')
            response=session.delete(f'{base_path}/DeleteUser',json={'acc_no':acc_no,'pin':pin})
            print(response.json())
            time.sleep(3)
            break
        elif opt=='4':
            pin=pwinput.pwinput(prompt='Enter Pin : ',mask='*')
            response=session.post(f'{base_path}/History',json={'acc_no':acc_no,'pin':pin})
            print(response.json())
        elif opt=='5':
            print('--Logging Out--')
            break
        else:
            print('wrong input!')
        
        input('Press Enter To Continue')