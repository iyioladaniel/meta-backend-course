# Define class MyFirstClass
class MyFirstClass:
    print('Who wrote this?')

    # Define string variable called index
    #def __init__(self, index) -> None:
    index = "Author-Book"

    # Define function hand_list()
    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book)
        # variable + “ wrote the book: ” + variable
        

# Call function handlist()
whodunnit = MyFirstClass()
whodunnit.hand_list("Plato","Republic")
whodunnit.hand_list("Sun Tzu","The Art of War")

'''
Define Building 
1. Rooms - doors, windows, furniture
2. Floors - Rooms, verandah, walk way
3. Buildings - Floors, Compound
4. Estates - Buildings, School, Food court
'''

class Rooms:
    def __init__(self, name, door, window) -> None:
        self.name = name
        self.door = door 
        self.window = window
    
    def how_many(self):
        return "The {} room has {} door(s) and {} window(s)".format(self.name, self.door, self.window)
    
    def furniture(self):
        tables = int(input("How many tables do you want to get?: "))
        chairs = int(input("How many chairs do you want?: "))
        return "The {} room now has {} table(s) and {} chairs(s)".format(self.name, tables, chairs)
    
class Floors(Rooms):
    def __init__(self, name, door, window) -> None:
        super().__init__(name, door, window)
