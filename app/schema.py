from pydantic import BaseModel,field_validator
from enum import Enum

class TransactionType(Enum):
    CREDIT='Amount Credited'
    DEBIT='Amount Debited'
    TRANSFER='Transfer OUT'
    RECEIVED='Transfer IN'

class Login(BaseModel):
    acc_no:str
    pwd:str

class CreateUser(BaseModel):
    name:str
    pwd:str
    pin:str
    balance:float=0
    @field_validator('pin')
    @classmethod
    def validate_pin(cls,pin):
        return pin_validator(pin)
    @field_validator('balance')
    @classmethod
    def validate_balance(cls,balance):
        return balance_validator(balance)
    

class AddMoney(BaseModel):
    acc_no:str
    credit:float
    debit:float=0
    pin:str
    @field_validator('pin')
    @classmethod
    def validate_pin(cls,pin):
        return pin_validator(pin)
    @field_validator('credit')
    @classmethod
    def validate_amount(cls,amount):
        return amount_validator(amount)

class DedMoney(BaseModel):
    acc_no:str
    credit:float=0
    debit:float
    pin:str
    @field_validator('pin')
    @classmethod
    def validate_pin(cls,pin):
        return pin_validator(pin)
    @field_validator('debit')
    @classmethod
    def validate_amount(cls,amount):
        return amount_validator(amount)

class Transfer(BaseModel):
    your_acc_no:str
    receiver_acc_no:str
    debit:float
    credit:float
    pin:str
    @field_validator('pin')
    @classmethod
    def validate_pin(cls,pin):
        return pin_validator(pin)
    @field_validator('credit','debit')
    @classmethod
    def validate_amount(cls,amount):
        return amount_validator(amount)

class Status(BaseModel):
    acc_no:str
    pin:str
    @field_validator('pin')
    @classmethod
    def validate_pin(cls,pin):
        return pin_validator(pin)

class History(BaseModel):
    acc_no:str
    pin:str
    @field_validator('pin')
    @classmethod
    def validate_pin(cls,pin):
        return pin_validator(pin)

class DelUser(BaseModel):
    acc_no:str
    pin:str
    @field_validator('pin')
    @classmethod
    def validate_pin(cls,pin):
        return pin_validator(pin)

def pin_validator(pin):
    if pin.isnumeric()==False:
        raise ValueError('PIN Should be numeric')
    else:
        if len(pin)==4:
            return pin
        else:
            raise ValueError('PIN Should be 4 digits long')
        
def amount_validator(amount):
    if amount<0:
        raise ValueError('Amount Cant be Negative')
    elif amount==0:
        raise ValueError('You Can\'t Transfer Zero Amount')
    else:
        return amount
    
def balance_validator(balance):
    if balance<0:
        raise ValueError('Balance Cant be Negative')
    else:
        return balance