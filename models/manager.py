from .user import User


class Manager(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    # Aplicando principio do SOLID [I]nterface Segregation Principle
    def work(self):
        return "Paying bills..."


        