from fastapi import FastAPI,Depends,Cookie,Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app=FastAPI()
accounts={}
bank={}

@app.get('/')
def home():
    return 'Welcome Home'

def gen_acc_no():
    if bank=={}:
        return 'SB1'
    else:
        last_bank_acc=list(bank.keys())
        last_bank_acc=last_bank_acc[-1]
        last_bank_acc=int(last_bank_acc[2:])
        last_bank_acc='SB'+str(last_bank_acc+1)
        return last_bank_acc

class Login(BaseModel):
    acc_no:str
    pwd:str

@app.post('/login')
def login(data:Login):
    acc_no=data.acc_no
    pwd=data.pwd
    if acc_no in accounts.keys() and accounts[acc_no]['pwd']==pwd:
        response=JSONResponse({'message':'Login Sucessfull.'})
        response.set_cookie('acc_no',acc_no)
        response.headers['authorization']=acc_no
        accounts[acc_no]['authorization']=acc_no
        return response
    return 'Invalid Credentials!'

class Signup(BaseModel):
    name:str
    pwd:str
    pin:str

@app.post('/signup')
def signup(data:Signup,acc_no=Depends(gen_acc_no)):
    acc_no=acc_no
    name=data.name
    pwd=data.pwd
    balance=float(0)
    pin=data.pin
    accounts[acc_no]={'pwd':pwd,'authorization':''}
    bank[acc_no]={'name':name,'balance':balance,'pin':pin}
    return bank



class User(BaseModel):
    name:str
    pwd:str
    balance:float
    pin:str

@app.post('/addaccount')
def add_account(data:User,acc_no=Depends(gen_acc_no)):
    acc_no=acc_no
    name=data.name
    pwd=data.pwd
    balance=data.balance
    pin=data.pin
    accounts[acc_no]={'pwd':pwd,'authorization':''}
    bank[acc_no]={'name':name,'balance':balance,'pin':pin}
    return bank

@app.post('/addmoney/{acc_no}/{amount}')
def add_money(acc_no:str,amount:float):
    if acc_no not in bank.keys():
        return 'User Not Found'
    if amount<0:
        return 'Wrong Input enter positive value'
    bank[acc_no]['balance']+=amount
    print(bank)
    return 'Money Added'

@app.post('/dedmoney/{acc_no}/{amount}')
def ded_money(acc_no:str,amount:float):
    if acc_no not in bank.keys():
        return 'User Not Found'
    if amount<0:
        return 'Wrong Input enter positive value'
    if bank[acc_no]['balance']<amount:
        return 'Insuficient amount'
    bank[acc_no]['balance']-=amount
    print(bank)
    return 'Money Deducted'

@app.get('/status/{acc_no}')
def status(acc_no:str):
    if acc_no not in bank.keys():
        return 'User Not Found'
    return bank[acc_no]

@app.delete('/delete/{acc_no}')
def delete(acc_no:str):
    accounts.pop(acc_no)
    bank.pop(acc_no)
    return 'user deleted'

@app.get('/showallaccounts')
def show_all_accounts():
    data=[]
    for a,b in bank.items():
        data.append({'account number':a,'name':b['name'],'balance':b['balance']})
    return data

class Transfer(BaseModel):
    receiver_acc_no:str
    amount:float

@app.post('/transfer')
def client_transfer(data:Transfer,acc_no:str=Cookie()):
    receiver_acc_no=data.receiver_acc_no
    amount=data.amount
    if amount<0:
        return{'message':'Invalid Amount'}
    if receiver_acc_no not in accounts.keys():
        return {'message':'Receiver Not Found'}
    else:
        if bank[acc_no]['balance']<amount:
            return{'message':'Insuffiecient Balance'}
        else:
            bank[acc_no]['balance']-=amount
            bank[receiver_acc_no]['balance']+=amount
            return{'message':'Transfer Successful'}
