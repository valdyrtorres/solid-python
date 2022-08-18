class ReportsGenerator():
    # Para cumprir o princípio Open/Closed vamos injetar dependência
    # Note que agora a classe está aberta a extensão
    @classmethod
    def build(cls, generator, repos):
        return generator.build(repos)
