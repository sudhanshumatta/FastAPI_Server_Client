from fastapi import Depends,Cookie,Header,FastAPI
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from schema import *
from crud import *
from database import get_db

app=FastAPI()

@app.get('/')
def Welocme():
    return JSONResponse(content={'Welcome':'Thanks For Using SB Banking System'})

@app.post('/Login')
def User_Login(log:Login,db:Session=Depends(get_db)):
    return login(db,log)

@app.post('/Signup')
def User_Signup(sign:CreateUser,db:Session=Depends(get_db)):
    return create_acc(db,sign)

@app.patch('/AddMoney')
def credit_money(credit_money:AddMoney,db:Session=Depends(get_db)):
    return add_money(db,credit_money)

@app.patch('/DeductMoney')
def credit_money(deduct_money:DedMoney,db:Session=Depends(get_db)):
    return ded_money(db,deduct_money)

@app.patch('/Transfer')
def trans(tran:Transfer,db:Session=Depends(get_db)):
    return transfer(db,tran)

@app.post('/Status')
def stats(stat:Status,db:Session=Depends(get_db)):
    return status(db,stat)

@app.delete('/DeleteUser')
def del_user(deluser:DelUser,db:Session=Depends(get_db)):
    return del_account(db,deluser)

@app.post('/History')
def user_history(usertrans:History,db:Session=Depends(get_db)):
    return tran_hist(db,usertrans)

@app.get('/ShowAllAccounts')
def showallacc(db:Session=Depends(get_db)):
    return show_all_account(db)

@app.get('/ShowAllTransactions')
def showallacc(db:Session=Depends(get_db)):
    return show_all_transaction(db)