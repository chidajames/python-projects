def check_dis(len):
	if len<12.0:
		print('---status---')
		print('STAGE-1')
		print('Rocket in Troposphere')
		print('---END---')

	elif (len>=12.0) & (len<50.0):
		print('---status---')
		print('STAGE-1')
		print('Rocket in Stratosphere')	
		print('---END---')	

	elif (len>=50.0) & (len<80.0):
		print('---status---')
		print('STAGE-2')
		print('Rocket in Mesosphere')	
		print('---END---')	

	elif (len>=80.0) & (len<320.0):
		print('---status---')
		print('STAGE-3')
		print('Rocket in Thermosphere')	
		print('---END---')	

	elif (len>=320.0):
		print('---status---')
		print('STAGE-4')
		print('Rocket in Exosphere')
		print('**  ON ITS WAY TO MARS  **')	
		print('---END---')	

print('-----MISSION MARS-----')
while True:

	dis=eval(input('Enter the ditance in KM  :  '))
	check_dis(dis)
	if(dis>=320):
		break