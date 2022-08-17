class Repo():

    def __init__(self, id, name, stars):
        self.id = id
        self.name = name
        self.stars = stars

    @property
    def id(self):
        return self.id

    @property
    def name(self):
        return self.name

    @property
    def stars(self):
        return self.stars

    def __str__(self):
        return f'id: {self._id} name: {self.name} stars: {self._stars}'
