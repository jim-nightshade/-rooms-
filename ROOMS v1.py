import random

class Map:
    def __init__(self):
        '''
        self.path - players path through the rooms
                    written to txt file
        '''
        self.path = []

    def stuff_generator(self):
        '''
        _____
        stuff & artifacts generator
        _______________________________________________
        randomly generated things player finds in rooms
        '''
        stuff_names = ['sword', 'stuff', 'rock', 'gold', 'crown', 'artifact', 'tobacco', 'silver', 'old book', 'python tutorial', 'lantern']
        stuff_list = []
        for i in range(random.randint(1,6)):
            stuff_list.append(Stuff(random.choice(stuff_names), random.choice([True, False])))
        return stuff_list
    def room_generator(self):
        room_list = []
        for i in range(10):
            room_list.append(Room(i + 1 , self.stuff_generator()))
        return room_list

    def room_stuff_display(self, room_list):
        for room in room_list:
            print("ROOM: ", room.number)
            print('STUFF: ', end=" ")
            for i in range(len(room.stuff)):
                print(room.stuff[i].name, '(useful: ', room.stuff[i].useful, ')', end=", ")
            print()
    def stuff_display(self, room):
        for i in range(len(room.stuff)):
            print('\t', room.stuff[i].name, '(useful: ', room.stuff[i].useful, ',value: ', room.stuff[i].value,')')
    def path_display(self):
        print('Path of rooms visited : ', [room.number for room in self.path])
        
    

class Room:
    def __init__(self, number, stuff_list):
        self.number = number
        self.door = True
        self.stuff = stuff_list


class Stuff:
    def __init__(self, name, useful):
        self.name = name
        self.useful = useful

        if self.useful:
            self.value = random.randint(1,51) * 10
        else:
            self.value = 0

class Player:
    def __init__(self, name, equipment = []):
        self.name = name
        self.equipment = equipment

    def equipment_value(self):
        eq_value = 0
        for item in self.equipment:
            eq_value += item.value
        return eq_value

    def display(self):
        print ()
        print ("Player's Name :", self.name)
        print (self.name, "'s equipment list :")
        for n, stuff in enumerate(self.equipment):
            print (str(n+1) + '.' + stuff.name)
        print ('All things you\'ve found are worth :', self.equipment_value() ,' in gold.')
        print ('Thank you for visiting our ROOMS. Hope to see you again !')
        print ()
        
def main(game, player):
    '''
    DOCSTRINGS: updated soon
    '''
    
    rooms = game.room_generator()
    while rooms:
        x = random.randint(0, len(rooms)-1)
        print ()
        print ('You are in the room number', rooms[x].number, 'and you\'ve found following treasures: ')
        game.stuff_display(rooms[x])
        if input('Do you want to take anything from this pile of garbage? y/n ') == 'y':
            for _ in rooms[x].stuff:
                if input('Would you like to take : ' + _.name + '? y/n ') == 'y':
                    player.equipment.append(_)                   
        game.path.append(rooms[x])
        rooms.pop(x)
        
    player.display()
    game.path_display()


    player_path = str([room.number for room in game.path])
    player_eq_val = str(player.equipment_value())
    with open(player.name + '\'s path.txt', 'a') as file:
        file.write(player_path + '\t' + player_eq_val + '\n')


    
game = Map()
me = Player('Henio')
main(game, me)




#rooms = game.room_generator()
#print(game.room_stuff_display(rooms))

#print('Room ' + str(i + 1) + ' :', _.number)
#print('Stuff ' + ' :', _.stuff.name)

#print('FOUND STUFF')
#for i, _ in enumerate(stuff_list):
#    print('Stuff ' + str(i + 1) + ' :', _.name)

#print('ROOMS')
#for i, _ in enumerate(room_list):
#    print('Room ' + str(i + 1) + ' :', _.number)
#    print('Stuff ' + ' :', _.stuff.name)

#random.choice([True, False])
