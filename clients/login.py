from .session_manager import session
import pwinput
base_path='http://127.0.0.1:8000'
def login():
    acc_no=str(input('Enter Account Number : '))
    password=pwinput.pwinput(prompt='Enter Password : ',mask='*')
    response=session.post(f'{base_path}/Login',json={'acc_no':acc_no,'pwd':password})
    return response.json()

def signup():
    name=str(input('Enter Name : '))
    password=pwinput.pwinput(prompt='Enter Password : ',mask='*')
    pin=pwinput.pwinput(prompt='Enter Pin : ',mask='*')
    response=session.post(f'{base_path}/Signup',json={'name':name,'pwd':password,'pin':pin})
    return(response.json())