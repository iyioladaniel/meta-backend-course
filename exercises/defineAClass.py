class House:
    '''
    This is a stub for a class representing a house that can be used to create objects 
    and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2

    def cost_evaluation(self, rate):
        cost = rate * self.num_rooms
        return cost

#Getting costs for my house
#1. Create my instance of the House class
myHouse = House()

#2. Update the number of rooms available in my house
myHouse.num_rooms = 2

#3. Calculate the cost evaluation given the rate of 5k per room
print(myHouse.cost_evaluation(5000))

