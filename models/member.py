from .user import User


class Member(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    @staticmethod
    def members():
        return ['username1', 'username2', 'team1']

    # Infringe o 4 principio do SOLID, ao herdar, me obriga a implementar uma interface que não preciso
    def pay_bill(self):
        pass

    # Aqui está OK
    def code(self):
        return "Coding..."
        