class Test:
    def __init__(self):
        self.a1 = account('Joe')
        self.a2 = account(C3PO)
        self.a3 = account('C3PO')


    def init_test(self):
        assert self.a1.get_name() == 'Joe'
        assert self.a2.get_name() != 'C3PO'
        assert self.a3.get_name() == 'C3PO'
        assert self.a1.get_bal() == 0

    def deposit_test(self):
        assert self.a1.deposit(20) == ('Joe', 20)
        assert self.a1.deposit(0) == ('Joe', 20)
        assert self.a3.deposit(-100) == ('C3PO', 0)
        assert self.a3.deposit(500) == ('C3PO', 500)

    def withdraw_Test(self):
        assert self.a1.withdraw(50) == ('Joe', 0)
        assert self.a3.withdraw(85) == ('C3PO', 415)
        assert self.a3.withdraw(-5) == ('C3PO', 415)
        assert self.a3.withdraw(1000) == ('C3PO', 0)
