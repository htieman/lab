class Account:
    def __init__(self, name):
        """
        Constructor used to create a new instance of the account class
        :param name: Name of account
        """
        self._account_name = name
        self._account_balance = 0

    def deposit(self, amount):
        """
        deposits a given amount into an account
        :param amount: amount of money to be deposited
        :return: true if transaction is successful, false if transaction is unsuccessful
        """
        if amount <= 0:
            return False
        elif amount > 0:
            self._account_balance += amount
            return True

    def withdraw(self, amount):
        """
        withdraws a given amount from an account
        :param amount: amount of money to be withdrawn
        :return: true if transaction is successful, false if transaction is unsuccessful
        """
        if amount <= 0:
            return False
        elif amount > 0:
            self._account_balance -= amount
            return True

    def get_balance(self):
        """
        returns account balance
        :return: account balance
        """
        return self._account_balance

    def get_name(self):
        """
        returns account name
        :return: account name
        """
        return self._account_name
