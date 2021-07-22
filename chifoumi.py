import random
nom = input("Veuillez saisir votre nom : ")
user_victoires = 0
bot_victoires = 0
nuls = 0

while True :
	print(nom," : ", user_victoires, "égalités : ",nuls, " bot : ", bot_victoires)

	joueur = input('Pour jouer : choisir entre (p)pierre, (f)feuille, (c)ciseaux", (q)quitter')
	if joueur == "q" :
		print("Vous avez quitté le jeu")
		break
	if joueur != "p" and joueur != "f" and joueur != "c":	
		continue


	if joueur == "p":
		print("PIERRE contre ...",end="")	
	elif joueur == "f":
		print("FEUILLE contre ...",end="")	
	else :
		print("CISEAUX contre ...",end="")	



	randomNombre = random.randint(1,3)
	if randomNombre == 1 :
		bot = "p"	
		print("PIERRE")	
	elif randomNombre == 2 :
		bot = "f"	
		print("FEUILLE")
	else :
		bot = "c"	
		print("CISEAUX")


	if joueur == bot :
		print("Partie est nulle !")
		nuls = nuls + 1
	elif joueur =="p" and bot =="c"	:
		print("Gagné !")
		user_victoires = user_victoires + 1
	elif joueur =="f" and bot =="p"	:
		print("Gagné !")
		user_victoires = user_victoires + 1	
	elif joueur =="c" and bot =="f"	:
		print("Gagné !")
		user_victoires = user_victoires + 1		
	elif joueur =="p" and bot =="f"	:
		print("Perdue !")
		bot_victoires = bot_victoires + 1		
	elif joueur =="f" and bot =="c"	:
		print("Perdue !")
		bot_victoires = bot_victoires + 1	
	elif joueur =="c" and bot =="p"	:
		print("Perdue !")
		bot_victoires = bot_victoires + 1					
		
















