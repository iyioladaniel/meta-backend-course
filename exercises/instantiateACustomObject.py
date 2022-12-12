# Define class MyFirstClass
class MyFirstClass:
    print('Who wrote this?')

    # Define string variable called index
    #def __init__(self, index) -> None:
    index = "Author-Book"

    # Define function hand_list()
    def hand_list(self, philosopher, book):
        print(philosopher + " wrote the book: " + book)
        # variable + “ wrote the book: ” + variable
        

# Call function handlist()
whodunnit = MyFirstClass()
print(whodunnit.hand_list("Plato","Republic"))
print(whodunnit.hand_list("Sun Tzu","The Art of War"))
