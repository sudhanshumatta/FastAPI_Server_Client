from sqlalchemy import String,Float,Boolean,ForeignKey,DateTime
from sqlalchemy import Enum as sqlenum
from sqlalchemy.orm import Mapped,mapped_column,relationship
from database.database import Base,engine
from datetime import datetime
from .schema import TransactionType

class Users(Base):
    __tablename__='users'

    acc_no:Mapped[str]=mapped_column(String,primary_key=True)
    name:Mapped[str]=mapped_column(String)
    pwd:Mapped[str]=mapped_column(String)
    pin:Mapped[str]=mapped_column(String)
    bank=relationship('Bank',back_populates='users',uselist=False,cascade='all, delete-orphan')

    def __str__(self):
        output=''
        if self.acc_no is not None:
            output+=f'Account Number : {self.acc_no}\n'
        if self.name is not None:
            output+=f'Name : {self.name}'
        
        return output
    
    def __repr__(self):
        return self.__str__()
    

class Bank(Base):
    __tablename__='bank'

    acc_no:Mapped[str]=mapped_column(String,ForeignKey('users.acc_no'),primary_key=True)
    balance:Mapped[float]=mapped_column(Float,default=0)
    users=relationship('Users',back_populates='bank')

    def __str__(self):
        output=''
        if self.acc_no is not None:
            output+=f'Account Number : {self.acc_no}\n'
        if self.balance is not None:
            output+=f'Name : {self.balance}'
        
        return output
    
    def __repr__(self):
        return self.__str__()


class Transaction_table(Base):
    __tablename__='transactions'

    txn_id:Mapped[str]=mapped_column(String,primary_key=True)
    acc_no:Mapped[str]=mapped_column(String,ForeignKey('users.acc_no',ondelete='RESTRICT'),primary_key=True)
    trans_type:Mapped[TransactionType]=mapped_column(sqlenum(TransactionType))
    credit:Mapped[float]=mapped_column(Float)
    debit:Mapped[float]=mapped_column(Float)
    balance:Mapped[float]=mapped_column(Float)
    timestamp:Mapped[datetime]=mapped_column(DateTime,default=datetime.now)
    reference:Mapped[str]=mapped_column(String,default='-BANK-')

    def __str__(self):
        output=''
        if self.txn_id is not None:
            output+=f'Transaction ID : {self.txn_id}\n'
        if self.acc_no is not None:
            output+=f'Account Number : {self.acc_no}'
        if self.trans_type is not None:
            output+=f'Transaction Type : {self.trans_type}\n'
        if self.credit is not None:
            output+=f'Credit : {self.credit}'
        if self.debit is not None:
            output+=f'Debit : {self.debit}\n'
        if self.balance is not None:
            output+=f'Balance : {self.balance}'
        if self.timestamp is not None:
            output+=f'Timestamp : {self.timestamp}\n'
        if self.reference is not None:
            output+=f'Reference : {self.reference}'

        return output
    
    def __repr__(self):
        return self.__str__()

Base.metadata.create_all(engine)