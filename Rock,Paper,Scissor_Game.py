import random as rd
Game={1:"Rock",2:"Paper",3:"Scissors"}
k=input("Do you want to Start the game(y/n) ")
comp_pt=0
user_pt=0
while (k=='y'):
	while True:
		comp=rd.randint(1,3)
		user=int(input("1: Rock 2: Paper 3: Scissors"))
		print("User = ",Game[user])
		print("Computer = ",Game[comp])
		if(user==1):
			if(comp==1):
				print("Oops Same, Try Again")
			elif(comp==2):
				print("Computer Win")
				comp_pt=comp_pt+1
			elif (comp==3):
				print("User Win")
				user_pt=user_pt+1
		if(user==2):
			if(comp==1):
				print("User Win")
				user_pt=user_pt+1
			elif(comp==2):
				print("Oops Same, Try Again")
			elif (comp==3):
				print("Computer Win")
				comp_pt=comp_pt+1
		if(user==3):
			if(comp==1):
				print("Computer Win")
				comp_pt=comp_pt+1
			elif(comp==2):
				print("User Win")
				user_pt=user_pt+1
			elif (comp==3):
				print("Oops Same, Try Again")
		print("Compuer Point = ",comp_pt)
		print("User Point = ",user_pt)
		if(comp_pt==3):
			print("Computer wins the game")
			break
		if(user_pt==3):
			print("User wins the game")
			break
	k=input("Do you want to play again (y/n)")