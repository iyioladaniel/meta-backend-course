'''
How to make an instant coffee

-Get a cup
-Get s spoon
-Instant coffee mix
-Hot water

'''

algo = '''
Solution algorithm
Input 
Ingredients required:

Cup

Hot water

Coffee granules

Optional:

Milk

Cream 

Sugar

Output
A cup of coffee.

Steps
1. Add drinking water to an electric kettle. 

2. Put the kettle on to boil water.

3. While waiting, prepare coffee.

4. Add coffee granules to the cup.

5. If water is boiled, pour water into a cup, else continue to wait.

6. If milk or cream is required, add and stir.

7. If sugar is required, add and stir.

8. Return coffee.
'''

opening_text = '''
Learn how to make Instant Coffee
'''

ingredients = '''
You will need the following;

-Cup
-Spoon
-Coffee granules
'''

optional = '''
-Milk
-Cream
-Sugar
'''

#while True:

want_coffee = input("Would you like to make a Cup of Coffee? \nYes or No: ")
have_tools = input("Do you have all the tools listed? \nYes or No: ")

make_coffee = {
    1:"Add drinking water to an electric kettle.",
    2: "Put the kettle on to boil water.",
    3: "While waiting, prepare coffee.",
    4: "Add coffee granules to the cup.",
    5: "If water is boiled, pour water into a cup, else continue to wait.",
    6: "If milk or cream is required, add and stir.",
    7: "If sugar is required, add and stir.",
    8: "Return coffee."}

for num, step in make_coffee.items():
    if want_coffee.lower() == "yes":
        if have_tools.lower() == "yes":
            if num == 5:
                is_water_boiled = input("Is the water boiled? \nYes or No: ")
                if is_water_boiled.lower() == 'yes':
                    print("Step {}: {}".format(num,step))
                    continue
                    if num == 6:
                        want_milk_or_cream = input("Do want Milk or Cream? \nYes or No: ")
                        if want_milk_or_cream.lower() == 'yes':
                            print("Step {}: {}\n".format(num,step))
                        else:
                            continue
                        want_sugar = input("Do want Sugar? \nYes or No: ")
                        if want_sugar.lower() == 'yes':
                            print("Step {}: {}".format(num,step))
                        else:
                            continue
                else: print('Keep waiting for the water to boil.')
            else:  print("Step {}: {}\n".format(num,step))
        else: print("{}\nto make your Coffee.\nPlease go get them\n".format(ingredients))
        break
    else: print('Alright then, you can get something else. \nThank you.')
    break

