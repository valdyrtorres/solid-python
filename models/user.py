class User():
    def __init__(self, username, email):
        self._username = username
        self._email = email

    #Simulando interface
    def pay_bill(self):
        raise NotImplementedError

    def code(self):
        raise NotImplementedError
