'''
DJANGO-ABSTRACT-STARTPOINT STARTER.PY
MAKE SURE TO SAVE ANY CHANGES TO THIS FOLDER
AND RUN THIS FILE WITH PYTHON
'''

import os
import properties

parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#parent_directory refers to the project folder
current_directory = os.path.dirname(os.path.abspath(__file__))
#current directory refers to the directory whit this file in it (i.e ALIEN)
#target directory would be defind later on and used to refer to the folder that has the root 'settings.py'

parent_files_and_folders = []
#parent_files_and_folders is empty for now but would be temporarily prepoluted automatically with the files...
#...and folders in the parent_directory, which would be used as a checklist

#now auto prepopulate the parent_files_and_folders temporaroily with the files and folders in the parent_directory
for everything in os.listdir(parent_directory):
	parent_files_and_folders.append(everything)

#Below are the initial values,
Initial_Project_Name = properties.DJANGO_PROJECT_NAME
Initial_App_Name = properties.PROJECT_USER_APP
#do not refer to Initial_Project_Name or Initial_App_Name directly to enable the system revers all work done if there...
#is an error....rather refer to properties.DJANGO_PROJECT_NAME or properties.PROJECT_USER_APP
	
proj = input("Enter the name of your Django Project: ")
title = input("Enter the name of the Django App: ")


if proj in parent_files_and_folders: #if the inputed project name exists in the parent_directory
	print("Initiating Django-Abstract-StartPoint protocol...")
	target_directory = os.path.join(parent_directory, proj)
	#target_directory refers to the django folder where django settings.py lives
	try:
		print("Locating Neccesary files and folders...")
		target_settings = os.path.join(target_directory, 'settings.py') 
		target_urls = os.path.join(target_directory, 'urls.py')
		base_settings = os.path.join(current_directory, 'source_settings.py')
		base_urls = os.path.join(current_directory, 'source_urls.py')

		print("All Files located, preparing to edit...")
		
		with open(target_settings, 'w') as sets:
			src = open(base_settings, 'r')
			for texts in src:
				if properties.DJANGO_PROJECT_NAME in texts:
					sets.write(texts.replace(properties.DJANGO_PROJECT_NAME, proj))
				elif properties.PROJECT_USER_APP in texts:
					sets.write(texts.replace(properties.PROJECT_USER_APP, title))
				else:
					sets.write(texts)
			src.close()
			print('Edited 1 from 2...')

		with open(target_urls, 'w') as urls:
			src = open(base_urls, 'r')
			for texts in src:
				if properties.DJANGO_PROJECT_NAME in texts:
					urls.write(texts.replace(properties.DJANGO_PROJECT_NAME, proj))
				elif properties.PROJECT_USER_APP in texts:
					urls.write(texts.replace(properties.PROJECT_USER_APP, title))
				else:
					urls.write(texts)
			src.close()
			print('Edited 2 from 2...')

		with open(os.path.join(current_directory, 'properties.py'), 'w') as props:
			props.write("DJANGO_PROJECT_NAME = '" + proj +"' \n")
			props.write("PROJECT_USER_APP = '" + title +"' \n")
			props.write("FIRST_SETUP = False")
		print("All files ready to go...")

		os.rename(os.path.join(parent_directory, Initial_App_Name), os.path.join(parent_directory, properties.PROJECT_USER_APP))
		print("All Processes Successfully Completed")

	except:
		print('Something went wrong....Undoing all Processess...')


else:
	print('COULD NOT LOCATE ' + proj + '; check if the folder exist or consider manual approch')

	
t = input('Press enter to exit: ')