class To_do(object):
	
	done_list=[]
	to_do_list=[]	
	
	def add(self):
		x=input('enter the task')
		(self.to_do_list).append(x)

	def mark_done(self):
		for i,val in enumerate(self.to_do_list):
			print(i,"-",val)
		x=int(input("select the finished task"))
		self.done_list.append(self.to_do_list[x])
		self.to_do_list.remove(self.to_do_list[x])

	def see_task(self):
		print("pending:\t",self.to_do_list)
		print("done :\t",self.done_list)

