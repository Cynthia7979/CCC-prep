limit = int(input("Enter the speed limit: "))
speed = int(input("Enter the recorded speed of the car: "))
if speed <= limit: print("Congratulations, you are within the speed limit!")
else:
    if speed - limit < 21:
        print("You are speeding and your fine is $100.")
    elif speed - limit < 31:
        print("You are speeding and your fine is $270.")
    else:
        print("You are speeding and your fine is $500.")
