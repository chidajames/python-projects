import random
class Game(object):
	def __init__(self):		
		self.flag=0

	def easy(self):
		self.value=int(input("enter the number between 1 and 100 \n"))
		self.rand_list = [[0] * 8 for i in range(1)]
		for j in range(8):
			self.rand_list[0][j]=random.sample(range(1,100),8)
		for j in range(8):
			if(self.value in self.rand_list[0][j]):
				print('\n---number is  present---\n')
				self.flag=1
				break
			else:
				self.flag=0
		if self.flag==0:
			print('\n---number is not present---\n')
		for j in range(8):
			print(self.rand_list[0][j],'\n')

	def hard(self):
		self.value=int(input("enter the number between 1 and 100 \n"))
		if self.value < 70:
			self.rand_list = [[0] * 8 for i in range(1)]
			for j in range(8):
				self.rand_list[0][j]=random.sample(range(1,70),8)
			for j in range(8):
				if(self.value in self.rand_list[0][j]):
					print('\n---number is  present---\n')
					self.flag=1
					break
				else:
					self.flag=0
			if self.flag==0:
				print('\n---number is not present---\n')
			for j in range(8):
				print(self.rand_list[0][j],'\n')
		else:
			print('\n---number is  present---\n')

	def legend(self):
		self.value=int(input("enter the number between 1 and 100 \n"))
		if self.value < 50:
			self.rand_list = [[0] * 8 for i in range(1)]
			for j in range(8):
				self.rand_list[0][j]=random.sample(range(1,50),8)
			for j in range(8):
				if(self.value in self.rand_list[0][j]):
					print('\n---number is  present---\n')
					self.flag=1
					break
				else:
					self.flag=0
			if self.flag==0:
				print('\n---number is not present---\n')
			for j in range(8):
				print(self.rand_list[0][j],'\n')
		else:
			print('\n---number is  present---\n')

	
