


class Accont:
    def __init__(self,acc_no, holder_name, balance, date):
      self.acc_no = acc_no
      self.holder_name = holder_name
      self.balance = balance
      self.date = date

    def debit(self):
        print(f"debited from {self.holder_name}'s account")
    def credit(self):
        print(f"credited to {self.holder_name} 's account")
 acc1 = Account(123456789, 'mr.herry', 9999, '22 Nov 2022')
 print(acc1.balance)
 acc1.credit()
 print(acc1.balance)
