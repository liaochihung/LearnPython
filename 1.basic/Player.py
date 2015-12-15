class Player:
    def __init__(self, id, name, health, items):
        self.id = id
        self.name = name
        self.health = health
        self.items = items

    def __str__(self):
        return "My id: " + str(self.id) + \
               " \nMy Name: " + str(self.name) + \
               " \nMy Health: " + str(self.health) + \
               " \nMy Items: " + str(self.items) + "."
