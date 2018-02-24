from to_do import To_do
list_1= To_do()

while True:	
	choice=int(input('1.add\n2.mark as done\n3.view all\n4.exit\nenter a choice:'))
	if(choice == 1):
		list_1.add()
	elif(choice == 2):
		list_1.mark_done()
	elif(choice == 3):
		list_1.see_task()
	elif(choice == 4):
		break
	else:
			print('error')

	# choice=int(input('1.add\n2.mark as done\n3.view all\n4.exit\nenter a choice:'))
	# if(choice == 1):
	# 	list_1.add()
	# elif(choice == 2):
	# 	list_1.mark_done()
	# elif(choice == 3):
	# 	list_1.see_task()
	# elif(choice == 4):
	# 	break
	# else:
	# 	print('error')
