from session_manager import session

def login():
    acc_no=str(input('Enter Account Number : '))
    password=str(input('Enter Your Password : '))
    response=session.post('http://127.0.0.1:8000/login',json={'acc_no':acc_no,'pwd':password})
    return response.json()

def signup():
    name=str(input('Enter Name : '))
    password=str(input('Enter Your Password : '))
    pin=str(input('Enter Your Pin : '))
    response=session.post('http://127.0.0.1:8000/signup',json={'name':name,'pwd':password,'pin':pin})
    return(response.json())