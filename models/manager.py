from .user import User


class Manager(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    # Aqui está OK
    def pay_bill(self):
        return "Paying bills..."

    # Infringe o 4 principio do SOLID, ao herdar, me obriga a implementar uma interface que não preciso
    def code(self):
        pass

        