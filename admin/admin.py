import requests
import subprocess
import os
import pwinput
admin_session=requests.session()
while True:
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    print('1. Add Account \n2. Add Money \n3. Deduct Money \n4. Status \n5. Delete User \n6. History \n7. Show All Accounts \n8. Show All Transactions \n9. Exit')
    opt=str(input('Select you opt :'))
    
    if opt=='1':
        name=str(input('Enter Name : '))
        password=pwinput.pwinput(prompt='Enter Password : ',mask='*')
        balance=float(input('Enter Balance : '))
        pin=pwinput.pwinput(prompt='Enter Pin : ',mask='*')
        response=admin_session.post('http://127.0.0.1:8000/Signup',json={'name':name,'pwd':password,'balance':balance,'pin':pin})
        print(response.json())
    elif opt=='2':
        acc_no=str(input('Enter Account Number : '))
        amount=int(input('Enter Amount : '))
        pin=pwinput.pwinput(prompt='Enter Pin : ',mask='*')
        response=admin_session.patch(f'http://127.0.0.1:8000/AddMoney',json={'acc_no':acc_no,'pin':pin,'credit':amount})
        print(response.json())
    elif opt=='3':
        acc_no=str(input('Enter Account Number : '))
        amount=int(input('Enter Amount : '))
        pin=pwinput.pwinput(prompt='Enter Pin : ',mask='*')
        response=admin_session.patch(f'http://127.0.0.1:8000/Deductmoney',json={'acc_no':acc_no,'pin':pin,'debit':amount})
        print(response.json())
    elif opt=='4':
        acc_no=str(input('Enter Account Number : '))
        pin=pwinput.pwinput(prompt='Enter Pin : ',mask='*')
        response=admin_session.post(f'http://127.0.0.1:8000/Status',json={'acc_no':acc_no,'pin':pin})
        print(response.json())
    elif opt=='5':
        acc_no=str(input('Enter Account Number : '))
        pin=pwinput.pwinput(prompt='Enter Pin : ',mask='*')
        response=admin_session.delete(f'http://127.0.0.1:8000/DeleteUser',json={'acc_no':acc_no,'pin':pin})
        print(response.json())
    elif opt=='6':
        acc_no=str(input('Enter Account Number : '))
        pin=pwinput.pwinput(prompt='Enter Pin : ',mask='*')
        response=admin_session.post('http://127.0.0.1:8000/History',json={'acc_no':acc_no,'pin':pin})
        print(response.json())
    elif opt=='7':
        response=admin_session.get('http://127.0.0.1:8000/ShowAllAccounts')
        print(response.json())
    elif opt=='8':
        response=admin_session.get('http://127.0.0.1:8000/ShowAllTransactions')
        print(response.json())
    elif opt=='9':
        break
    else:
        print('Wrong Input')
    input('Enter to continue..')
