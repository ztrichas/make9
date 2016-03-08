import random 


number = random.uniform(0,3)


hit = raw_input("Would you like to add a random number between 0 and 3? Enter: 'Yes' if so, or 'No' if not. ") 

while hit == "Yes":
	addition = random.uniform(0,3)
	number = number + addition 
	print (number)
	if number == 9:
		print("WOW! YOU WIN!!!")
		hit = "No"
	if number < 8:
		print("It might might be a good idea to hit")
	if number > 8:
		print("Be careful!")
	if number > 9:
		print("Sorry, you lost, try again.")
		number = 0
		hit = "No"
	
		


	hit = raw_input("Would you like to add a random number between 0 and 3? Enter: 'Yes' if so, or 'No' if not")	


if hit == "No":
	print("Your score is {}.").format(number)