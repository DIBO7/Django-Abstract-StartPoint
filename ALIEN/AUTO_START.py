'''
DJANGO-ABSTRACT-STARTPOINT STARTER.PY
MAKE SURE YOU DON'T TAMPER WITH THIS FILE
AND JUST RUN THIS FILE WITH PYTHON
'''

import os
import properties
import supports

parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#parent_directory refers to the project folder
current_directory = os.path.dirname(os.path.abspath(__file__))
#current directory refers to the directory with this file in it (i.e ALIEN)

parent_files_and_folders = []
#parent_files_and_folders is empty for now but would be temporarily prepoluted automatically with the files...
#...and folders in the parent_directory, which would be used as a checklist

#now auto prepopulate the parent_files_and_folders temporaroily with the files and folders in the parent_directory
for everything in os.listdir(parent_directory):
	parent_files_and_folders.append(everything)

#Below is the initial value of the project's main app name
Initial_App_Name = properties.PROJECT_USER_APP
#do not refer overwrite Initial_App_Name...instead overwrite properties.PROJECT_USER_APP
	
proj = input("Input title of your Django Project: ")
title = input("What do you want to name the app that contains the AbstractBaseUser model?: ")

if proj in parent_files_and_folders: #if the inputed project name exists in the parent_directory
	print("Initiating Django-Abstract-StartPoint protocol...preparing to write...")
	target_directory = os.path.join(parent_directory, proj)
	#target_directory refers to the django folder where django settings.py lives

	#target_file refers to file in the actual django project's target folder
	target_settings = os.path.join(target_directory, 'settings.py') 
	target_urls = os.path.join(target_directory, 'urls.py')
	target_app = os.path.join(parent_directory, properties.PROJECT_USER_APP, 'apps.py')

	#base_file refers to the ones within the DJANGO ABSTRACT STARTPOINT i.e the ALIEN folder
	base_settings = os.path.join(current_directory, 'source_settings.py')
	base_urls = os.path.join(current_directory, 'source_urls.py')
	base_app = os.path.join(current_directory, 'apps.py')
	#and ofcourse the empty_files within the ALIEN folder
	empty_file1 = os.path.join(current_directory, 'empty_file1.py')
	empty_file2 = os.path.join(current_directory, 'empty_file2.py')
	empty_file3 = os.path.join(current_directory, 'empty_file3.py')

	try:
		#progress_bar contained within the try statement would be used as countermeasurements in case of any error in the try statement
		progress_bar = 0

		progress_bar += 1 #progress_bar = 1  #the progress bar monitors the progress...and incase of error, it would be used to reverse changes made
		#Now write a new settings.py with appropriate input, but first copy the settings to a safe place incase of an error
		with open(target_settings, 'r') as settings:
			#first open the empty_file1 and write the django settings to it.			
			file1 = open(empty_file1, 'w')
			for lines in settings:
				file1.write(lines)
			file1.close()
			
		progress_bar += 1 #progress_bar = 2  
		#then write the new settings into django settings
		with open(target_settings, 'w') as settings:
			src = open(base_settings, 'r')
			for texts in src:
				if 'DjangoAbstractStartPoint' in texts:
					settings.write(texts.replace('DjangoAbstractStartPoint', proj))
				elif 'DjangoAbstractBasics' in texts:
					settings.write(texts.replace('DjangoAbstractBasics', title))
				elif '__SECRET_KEY__' in texts:
					sk = supports.Generate_Secret_Key()
					settings.write(texts.replace('__SECRET_KEY__', sk))
				else:
					settings.write(texts)
			src.close()			
		progress_bar += 1 #progress_bar = 3

		#Write a new urls.py with appropriate input 
		with open(target_urls, 'r') as urls:
			#first open the empty_file1 and write the django urls.py to it.
			file2 = open(empty_file2, 'w')
			for lines in urls:
				file2.write(lines)
			file2.close()

		progress_bar += 1 #progress bar = 4 
		with open(target_urls, 'w') as urls:
			src = open(base_urls, 'r')
			for texts in src:
				if 'DjangoAbstractStartPoint' in texts:
					urls.write(texts.replace('DjangoAbstractStartPoint', proj))
				elif 'DjangoAbstractBasics' in texts:
					urls.write(texts.replace('DjangoAbstractBasics', title))
				else:
					urls.write(texts)
			src.close()

		progress_bar += 1 #progress_bar = 5
		#inside the created by DJANGO ABSTRACT STARTPOINT, change the apps.py to suit whatever title the user gives
		with open(target_app, 'r') as app:
			#first open the empty_file3 and write the django urls.py to it.
			file3 = open(empty_file3, 'w')
			for lines in app:
				file3.write(lines)
			file3.close()

		progress_bar += 1 #progress_bar = 6
		with open(target_app, 'w') as app:			
			src = open(base_app, 'r')
			for texts in src:
				if 'DjangoAbstractBasics' in texts:
					app.write(texts.replace('DjangoAbstractBasics', title))
				elif 'Djangoabstractbasics' in texts:
					app.write(texts.replace('Djangoabstractbasics', supports.Capitalize_First_Letter(title)))
				else:
					app.write(texts)
			src.close()			

		#also edit the properties.py in this folder for future re-usage purposes
		with open(os.path.join(current_directory, 'properties.py'), 'w') as props:
			props.write("PROJECT_USER_APP = '" + title +"' \n")

		os.rename(os.path.join(parent_directory, Initial_App_Name), os.path.join(parent_directory, title))
		print('All Done!')
		
	except:
		print('Ooooops!! Something has gone wrong. Restoring your files...')
		while progress_bar > 0:
			supports.Reverse_Changes(progress_bar, empty_file1, empty_file2, empty_file3, target_settings, target_urls, target_app)
			progress_bar -= 1


else:
	print('Unable to locate ' + proj + '; check if the folder exists or consider manual approch')

	
t = input('Press enter/return to exit...')