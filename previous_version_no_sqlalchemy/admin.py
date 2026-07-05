import requests
import subprocess
import os
admin_session=requests.session()
while True:
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    print('1. Add Account \n2. Add Money \n3. Dedeuct Money \n4. Status \n5. Delete User \n6. Show All Accounts \n7. Exit')
    opt=str(input('Select you opt :'))
    
    if opt=='1':
        name=str(input('Enter Name : '))
        password=str(input('Enter Your Password : '))
        balance=float(input('Enter Balance : '))
        pin=str(input('Enter Your Pin : '))
        response=admin_session.post('http://127.0.0.1:8000/addaccount',json={'name':name,'pwd':password,'balance':balance,'pin':pin})
        print(response.json())
    elif opt=='2':
        acc_no=str(input('Enter Account Number : '))
        amount=int(input('Enter Amount : '))
        response=admin_session.post(f'http://127.0.0.1:8000/addmoney/{acc_no}/{amount}')
        print(response.json())
    elif opt=='3':
        acc_no=str(input('Enter Account Number : '))
        amount=int(input('Enter Amount : '))
        response=admin_session.post(f'http://127.0.0.1:8000/dedmoney/{acc_no}/{amount}')
        print(response.json())
    elif opt=='4':
        acc_no=str(input('Enter Account Number : '))
        response=admin_session.get(f'http://127.0.0.1:8000/status/{acc_no}')
        print(response.json())
    elif opt=='5':
        acc_no=str(input('Enter Account Number : '))
        response=admin_session.delete(f'http://127.0.0.1:8000/delete/{acc_no}')
        print(response.json())
    elif opt=='6':
        response=admin_session.get('http://127.0.0.1:8000/showallaccounts')
        print(response.json())
    elif opt=='7':
        break
    else:
        print('Wrong Input')
    input('Enter to continue..')
