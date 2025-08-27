#Jeepney Fare

name = input("What is your name: ")
isPWD = input("Are you a PWD (Yes / No) --> ")
fare = eval(input("bayad --> ₱ "))


if isPWD.lower() == "yes":
	discount = fare * .2
	new_fare = fare - discount
	print("Hi", name, ",", "PWD discount is ₱",discount, " Discounted fare is ₱",new_fare)
else:
	print("Sorry!´•︵•`", name, "you are NOT eligible for PWD discount ,", "Amount to pay --> ₱", fare)