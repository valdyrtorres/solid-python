from .user import User


class Member(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    @staticmethod
    def members():
        return ['username1', 'username2', 'team1']

    # Aplicando principio do SOLID [I]nterface Segregation Principle
    def work(self):
        return "Coding..."
