print("Welcome to tip calculator!")
bill = int(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give?(in %) "))
people = int(input("How many people to split the bill? "))
product = round((100+tip)/100, 2)
amount = bill/people
print(f"Each person should pay: ${round(amount*product, 2)}")