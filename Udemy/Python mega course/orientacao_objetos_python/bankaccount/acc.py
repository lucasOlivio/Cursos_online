class Account:

    def __init__(self, file_path):
        self.file_path = file_path
        with open(self.file_path,'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.file_path, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    """Documentação da classe bla bla bla bla"""
    type = "Tá em tuudu"
    def __init__(self, file_path, fee):
        Account.__init__(self, file_path)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

checking = Checking("balance.txt", 12)
checking.transfer(150)
print(checking.balance)
print(checking.type)
checking.commit()
print(checking.__doc__)
