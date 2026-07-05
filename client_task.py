from session_manager import session

import subprocess
import os
def clients(acc_no):
    while True:
        subprocess.run('cls'if os.name=='nt' else 'clear',shell=True)
        print('--Welcome SB Banking--')
        print('1. Transfer  \n2. Status \n3. Delete Profile \n4. History \n5. Logout')
        opt=str(input('Enter Your Operation : '))
        if opt=='1':
            print('--Welcome To Transfer Window--')
            receiver_acc_no=str(input('Enter Receiver\'s Account Number : '))
            pin=str(input('Enter PIN : '))
            amount=int(input('Enter Amount : '))
            response=session.patch('http://127.0.0.1:8000/Transfer',json={'your_acc_no':acc_no,'receiver_acc_no':receiver_acc_no,'pin':pin,'credit':amount,'debit':amount})
            print(response.json())
        elif opt=='2':
            print('--Showing Your Bank Status--')
            pin=str(input('Enter PIN : '))
            response=session.post(f'http://127.0.0.1:8000/Status',json={'acc_no':acc_no,'pin':pin})
            print(response.json())
        elif opt=='3':
            print('--Thanks For Using Our banking Serveice--')
            pin=str(input('Enter PIN : '))
            response=session.delete(f'http://127.0.0.1:8000/DeleteUser',json={'acc_no':acc_no,'pin':pin})
            print(response.json())
            input('Press Enter To Continue..')
            break
        elif opt=='4':
            pin=str(input('Enter Your Pin : '))
            response=session.post('http://127.0.0.1:8000/History',json={'acc_no':acc_no,'pin':pin})
            print(response.json())
        elif opt=='5':
            print('--Loging Out--')
            break
        else:
            print('wrong input!')
        
        input('Press Enter To Continue')