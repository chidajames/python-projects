class Manager(object):
	def __init__(self):
		self.free_slot=['10:30','11:00','01:30','02:45','04:00']
		self.slot={}
		self.allocated=[]

	def show_slot(self):
		print('----available time slots----\n')
		print('SLOT','  TIME','\n')
		for i,v in enumerate(self.free_slot):
			print(i,'    ',v,'\n')

	def select_slot(self):
		slot_time=int(input('enter the slot  :  '))
		name=input('enter the name  :  ')
		print('\nMeeting at {} for Mr/Ms {} has been scheduled'.format(self.free_slot[slot_time] , name))
		self.slot[self.free_slot[slot_time]]=name
		self.allocated.append(self.free_slot[slot_time])
		self.free_slot.remove(self.free_slot[slot_time])
		#print('---meeting has been scheduled---\n')
	def schedule(self):
		print('-----schedule-----')
		print('TIME','   ','NAME')
		for k,v in self.slot.items():
			print(k,'  ',v)

client = Manager()

while True:
	print('\nWhat would you like to do?\n')
	choice=int(input('1.check available time slot\n2.Book a time slot\n3.Schedule\n4.Exit\n'))
	if choice == 1:
		client.show_slot()
	elif choice == 2:
		client.select_slot()
	elif choice == 3:
		client.schedule()
	elif choice == 4:
		break
	else:
		print('choose a proper option')
print('----------THANK YOU----------\n')