lass Account:
    def __init__(self, name: str, bal=0) -> None:
        """
        Constructor used to create a new instance of the account class
        :param name: Name of account
        """
        self._account_name = name
        self._account_balance = bal

    def deposit(self, amount: int) -> None:
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

    def withdraw(self, amount: int) -> None:
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

    def get_balance(self) -> int:
        """
        returns account balance
        :return: account balance
        """
        return self._account_balance

    def get_name(self) -> str:
        """
        returns account name
        :return: account name
        """
        return self._account_name
