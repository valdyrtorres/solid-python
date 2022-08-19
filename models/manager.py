from .user import User


class Manager(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    # Fere o princípio de Liskov
    # Possui o comportamento diferente da classe pai quando não pode imprimir members
    @staticmethod
    def members():
        raise Exception('Member is not authorized to do this!')
        
        