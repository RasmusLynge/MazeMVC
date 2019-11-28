'''
class Subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print('{} Fik beskeden: "{}"'.format(self.name, message))
        
class Publisher:
    def __init__(self):
        self.subscribers = set()
    def register(self, who):
        self.subscribers.add(who)
    def unregister(self, who):
        self.subscribers.discard(who)
    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)

pub = Publisher()

bob = Subscriber('Bob')
alice = Subscriber('Alice')
john = Subscriber('John')

pub.register(bob)
pub.register(alice)
pub.register(john)

pub.dispatch("It's lunchtime!")

pub.unregister(john)

pub.dispatch("Time for dinner")
'''

MAZE = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, maze_list):
        # Kalder maze List og generere den nye liste ude i siden. 
        # Kalder loggen og fortæller at nye mazes er genereret.
        print('MazeList er opdateret:\n{} \n{} kan nu herfra opdatere sin liste'.format(maze_list, self.name))


class Observerable:
    def __init__(self):
        self.subscribers = set()

    def register(self, who):
        self.subscribers.add(who)

    def unregister(self, who):
        self.subscribers.discard(who)

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)



pub = Observerable()

show_maze_list = Observer('Show maze list')

pub.register(show_maze_list)

pub.dispatch(MAZE)


