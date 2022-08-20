class Tomato:
    states = {'green': 0, 'orange': 1, 'red': 2}

    def __init__(self, index, state):
        self.__index = index
        self.__state = 0

    def grow(self):
        if self.__state < 2:
            self.__state += 1
        else:
            self.__state += 0

    def is_ripe(self):
        if self.__state == 2:
            return True
        else:
            return False

class TomatoBush:

    def __init__(self, amount):
        self.tomatoes = [Tomato(index) for index in range(amount)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes.clear()

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Gardener is working...')
        self._plant_all()
        print('Gardener finished')

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Gardener is good!')
        else:
            print('very bad!')


    def knowledge_base():
        print('''Harvest time for tomatoes should ideally occur
when the fruit is a mature green and
then allowed to ripen off the vine.
This prevents splitting or bruising
and allows for a measure of control over the ripening process.''')

    def __name__ == '__num3__':
        Gardener.knowledge_base()
        great_tomato_bush = TomatoBush(4)
        gardener = Gardener('Emilio', great_tomato_bush)
        gardener.work()
        gardener.work()
        gardener.harvest()
        gardener.work()
        gardener.harvest()