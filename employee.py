class Employee(object):
	def __init__ (self):
		self.hourly={'Ram':500,'sam':500,'jack':500}
		self.salaried={'sansanman':10000,'cj':12000}
		self.manager={'ash':25000}
		self.executive={'james':50000}

	def hire(self):
		print('1.Hourly\n2.Salaried\n3.Mangeer\n4.Executive')
		choice=int(input('\nselect catogary : '))
		if choice == 1:
			name=input('enter the name : ')
			sal=input('enter the salary : ')
			self.hourly[name]=sal
			print('\n***Employee hired***\n')

		elif choice == 2:
			name=input('enter the name : ')
			sal=input('enter the salary : ')
			self.salaried[name]=sal			
			print('\n***Employee hired***\n')

		elif choice == 2:
			name=input('enter the name : ')
			sal=input('enter the salary : ')
			self.manager[name]=sal			
			print('\n***Employee hired***\n')

		elif choice == 2:
			name=input('enter the name : ')
			sal=input('enter the salary : ')
			self.executive[name]=sal			
			print('\n***Employee hired***\n')

	def fire(self):
		print('1.Hourly\n2.Salaried\n3.Mangeer\n4.Executive')
		choice=int(input('\nselect catogary : '))
		if choice == 1:
			name=self.hourly.keys()
			for i in name:
				print(i)
			emp=input('enter the name : ')
			self.hourly ={k : v for k , v in self.hourly.items() if emp != k}    #d = { k : v for k,v in d.iteritems() if v}
			print('\n***Employee fired***\n')

		elif choice == 2:
			name=self.salaried.keys()
			for i in name:
				print(i)
			emp=input('enter the name : ')
			self.salaried ={k : v for k , v in self.salaried.items() if emp != k}
			print('\n***Employee fired***\n')

		elif choice == 3:
			name=self.manager.keys()
			for i in name:
				print(i)
			emp=input('enter the name : ')
			self.manager ={k : v for k , v in self.manager.items() if emp != k}
			print('\n***Employee fired***\n')

		elif choice == 4:
			name=self.executive.keys()
			for i in name:
				print(i)
			emp=input('enter the name : ')
			self.executive ={k : v for k , v in self.executive.items() if emp != k}
			print('\n***Employee fired***\n')

	def raise1(self):
		print('1.Hourly\n2.Salaried\n3.Mangeer\n4.Executive')
		choice=int(input('\nselect catogary : '))
		if choice == 1:
			name=self.hourly.keys()
			sal=self.hourly.values()
			print('name  ','  salary')
			for i,j in self.hourly.items():
				print(i,'\t',j)
			emp=input('enter the name : ')
			new_sal=eval(input('enter the rise : '))
			self.temp ={k : v+new_sal for k , v in self.hourly.items() if emp == k}
			self.hourly.update(self.temp)
			print('\n***Salary raised***\n')

		elif choice == 2:
			name=self.salaried.keys()
			sal=self.salaried.values()
			print('name  ','  salary')
			for i,j in self.salaried.items():
				print(i,'\t',j)
			emp=input('enter the name : ')
			new_sal=eval(input('enter the rise : '))
			self.temp ={k : v+new_sal for k , v in self.salaried.items() if emp == k}
			self.salaried.update(self.temp)
			print('\n***Salary raised***\n')

		elif choice == 3:
			name=self.manager.keys()
			sal=self.manager.values()
			print('name  ','  salary')
			for i,j in self.manager.items():
				print(i,'\t',j)
			emp=input('enter the name : ')
			new_sal=eval(input('enter the rise : '))
			self.temp ={k : v+new_sal for k , v in self.manager.items() if emp == k}
			self.manager.update(self.temp)
			print('\n***Salary raised***\n')

		elif choice == 4:
			name=self.executive.keys()
			sal=self.executive.values()
			print('name  ','  salary')
			for i,j in self.executive.items():
				print(i,'\t',j)
			emp=input('enter the name : ')
			new_sal=eval(input('enter the rise : '))
			self.temp ={k : v+new_sal for k , v in self.executive.items() if emp == k}
			self.executive.update(self.temp)
			print('\n***Salary raised***\n')

employee = Employee()
print('----------WELCOME----------')
while True:
	print('Select operation\n1.Hire\n2.Fire\n3.Raise\n4.Exit')
	opt=int(input('entet choice : '))
	print('')
	if opt == 1:
		employee.hire()
	elif opt == 2:
		employee.fire()
	elif opt == 3:
		employee.raise1()
	elif opt ==4:
		print('----------END----------')
		break
