from sqlalchemy.orm import Session
from model import *
from schema import *
from datetime import datetime
import secrets
import string


def create_acc(db:Session,account:CreateUser):
    acc_no=gen_account(db)
    add_acc=Users(acc_no=acc_no,name=account.name,pwd=account.pwd,pin=account.pin)
    add_acc.bank=Bank(balance=account.balance)
    db.add(add_acc)
    db.commit()
    return {'message':'Account Created','acc_no':acc_no}

def login(db:Session,login:Login):
    user=db.query(Users).filter(Users.acc_no==login.acc_no,Users.pwd==login.pwd).first()
    if user==None:
        return {'message':'Invalid Credentials!'}
    else:
        return {'message':'Login Successfully','acc_no':user.acc_no}

def add_money(db:Session,add:AddMoney):
    acc_no=add.acc_no
    pin=add.pin
    check_a=check_acc(db,acc_no)
    check_p=check_pin(db,pin,acc_no)
    if check_a==False:
        return 'Account Number Not Found!'
    if check_p==False:
        return 'Wrong PIN!'
    user=db.query(Bank).filter(Bank.acc_no==acc_no).first()
    user.balance+=add.credit
    db.flush()
    rand = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    txn_id = f"TXN{acc_no}{datetime.now().strftime('%Y%m%d')}{rand}"
    transaction=Transaction_table(txn_id=txn_id,acc_no=acc_no,trans_type=TransactionType.CREDIT,credit=add.credit,debit=add.debit,balance=user.balance)
    db.add(transaction)
    db.commit()
    return {'message':'Amount Credited Successfully','transaction_id':txn_id,'amount':add.credit}

def ded_money(db:Session,ded:DedMoney):
    acc_no=ded.acc_no
    pin=ded.pin
    check_a=check_acc(db,acc_no)
    check_p=check_pin(db,pin,acc_no)
    if check_a==False:
        return 'Account Number Not Found!'
    if check_p==False:
        return 'Wrong PIN!'
    user=db.query(Bank).filter(Bank.acc_no==acc_no).first()
    if user.balance<ded.debit:
        return 'Insufficient Balance'
    user.balance-=ded.debit
    db.flush()
    rand = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    txn_id = f"TXN{acc_no}{datetime.now().strftime('%Y%m%d')}{rand}"
    transaction=Transaction_table(txn_id=txn_id,acc_no=acc_no,trans_type=TransactionType.DEBIT,credit=ded.credit,debit=ded.debit,balance=user.balance)
    db.add(transaction)
    db.commit()
    return {'message':'Amount Debited Successfully','transaction_id':txn_id,'amount':ded.debit}

def transfer(db:Session,transfer:Transfer):
    your_acc_no=transfer.your_acc_no
    receiver_acc_no=transfer.receiver_acc_no
    pin=transfer.pin
    if check_acc(db,your_acc_no)==False:
        return 'Wrong user account number!'
    if check_acc(db,receiver_acc_no)==False:
        return 'Receiver Account Number Not Found!'
    if check_pin(db,pin,your_acc_no)==False:
        return 'Wrong PIN!'
    user=db.query(Bank).filter(Bank.acc_no==your_acc_no).first()
    if user.balance<transfer.debit:
        return 'Insufficient Balance'
    user.balance-=transfer.debit
    receiver=db.query(Bank).filter(Bank.acc_no==receiver_acc_no).first()
    receiver.balance+=transfer.credit
    db.flush()
    rand = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    txn_id = f"TXN{your_acc_no}{datetime.now().strftime('%Y%m%d')}{rand}"
    transaction_u=Transaction_table(txn_id=txn_id,acc_no=your_acc_no,trans_type=TransactionType.TRANSFER,credit=0,debit=transfer.debit,balance=user.balance,reference=receiver_acc_no)
    transaction_r=Transaction_table(txn_id=txn_id,acc_no=receiver_acc_no,trans_type=TransactionType.RECEIVED,credit=transfer.credit,debit=0,balance=receiver.balance,reference=your_acc_no)
    db.add_all([transaction_u,transaction_r])
    db.commit()
    return {'message':'Transaction Successfull','transaction_id':txn_id,'amount':transfer.debit}

def del_account(db:Session,deluser:DelUser):
    if check_acc(db,deluser.acc_no)==False:
        return 'Account Number Not Found!'
    if check_pin(db,deluser.pin,deluser.acc_no)==False:
        return 'Wrong PIN!'
    user=db.query(Users).filter(Users.acc_no==deluser.acc_no).first()
    db.delete(user)
    db.commit()
    return {'message':'Account Successfully Removed','acc_no':deluser.acc_no}

def status(db:Session,status:Status):
    if check_acc(db,status.acc_no)==False:
        return 'Wrong Account Number!'
    if check_pin(db,status.pin,status.acc_no)==False:
        return 'Wrong PIN!'
    user=db.query(Users,Bank).join(Bank).filter(Bank.acc_no==status.acc_no).first()
    return {"acc_no": user.Users.acc_no,"name": user.Users.name,"balance": user.Bank.balance}

def tran_hist(db:Session,trans:History):
    if check_acc(db,trans.acc_no)==False:
        return 'Wrong Account Number!'
    if check_pin(db,trans.pin,trans.acc_no)==False:
        return 'Wrong PIN!'
    history=db.query(Transaction_table).filter(Transaction_table.acc_no==trans.acc_no).all()
    return [str(hist) for hist in history]

def check_acc(db:Session,acc_no:str):
    user=db.query(Users).filter(Users.acc_no==acc_no).first()
    if user==None:
        return False
    else:
        return True
    
def check_pin(db:Session,pin:str,acc_no):
    user=db.query(Users).filter(Users.acc_no==acc_no).first()
    if pin==user.pin:
        return True
    else:
        return False
    
def gen_account(db:Session):
    last_account=db.query(Users).order_by(Users.acc_no.desc()).first()
    if last_account==None:
        return 'SB1'
    else:
        last_acc_no=int(last_account.acc_no[2:])
        acc_no='SB'+str(last_acc_no+1)
        return acc_no
    
def show_all_account(db:Session):
    users=db.query(Users,Bank).join(Bank).all()
    return [{"acc_no": user.Users.acc_no,"name": user.Users.name,"balance": user.Bank.balance} for user in users]

def show_all_transaction(db:Session):
    trans=db.query(Transaction_table).all()
    return [str(t) for t in trans]