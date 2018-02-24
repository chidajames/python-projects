from game import Game	

player = Game()
while True:
	print('----------WELCOME TO THE GAME----------')
	decision = input('DO YOU WANT TO PLAY THE GAME ? y/n \n')
	if decision == 'y':
		while True:
			choice = input('select the difficulty\nEASY (e)\nHARD  (h)\nLEGEND  (l)\nchoice  : ')
			if choice == 'e':
				player.easy()
			elif choice == 'h':
				player.hard()
			elif choice == 'l':
				player.legend()
			else:
				break
	else:
		print('----------THANK YOU----------')
		break