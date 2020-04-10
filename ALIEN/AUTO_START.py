'''
DJANGO-ABSTRACT-STARTPOINT STARTER.PY
MAKE SURE YOU DON'T TAMPER WITH THIS FILE
AND JUST RUN THIS FILE WITH PYTHON
'''

import os
import properties
import secrets
import string

parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#parent_directory refers to the project folder
current_directory = os.path.dirname(os.path.abspath(__file__))
#current directory refers to the directory with this file in it (i.e ALIEN)

#target directory would be defind later on and used to refer to the folder that has the root 'settings.py'

parent_files_and_folders = []
#parent_files_and_folders is empty for now but would be temporarily prepoluted automatically with the files...
#...and folders in the parent_directory, which would be used as a checklist

#now auto prepopulate the parent_files_and_folders temporaroily with the files and folders in the parent_directory
for everything in os.listdir(parent_directory):
	parent_files_and_folders.append(everything)

#Below is the initial value of the project's main app name
Initial_App_Name = properties.PROJECT_USER_APP
#do not refer to Initial_App_Name directly to enable the system reverse all work done if there...
#is an error....instead refer to properties.PROJECT_USER_APP
	
proj = input("Input title of your Django Project: ")
title = input("What do you want to name the app that contains the AbstractBaseUser model?: ")

#Generate_Secret_key generates random a 60-digit django secret key which excludes forbidden characters
def Generate_Secret_Key(number=60):
	ready = True
	forbidden = ["'", '"', "\\"] #the forbidden characters

	SECRET_KEY = ''.join([secrets.SystemRandom().choice(
		"{}{}{}".format(string.ascii_letters, string.digits, string.punctuation)
		) for i in range(number)]) #Secret_Key Generator
	for characters in forbidden:
		if characters in SECRET_KEY: #if there is any of the forbidden characters in the Secret_key...
			ready = False #...change ready to Fals
	if not ready:
		#if secret key contains any forbidden_key,....
		return Generate_Secret_Key()# start this process all over until the generated secret_key contains no forbidden character
	return SECRET_KEY


def Capitalize_First_Letter(word):
	#as the name suggests, it capitalizes only the first letter of a given string
	word = word.lower()
	return word.replace(word[0], word[0].upper(), 1)



if proj in parent_files_and_folders: #if the inputed project name exists in the parent_directory
	print("Initiating Django-Abstract-StartPoint protocol...")
	target_directory = os.path.join(parent_directory, proj)
	#target_directory refers to the django folder where django settings.py lives
	try:
		print("Locating all neccesary files and folders...")
		target_settings = os.path.join(target_directory, 'settings.py') 
		target_urls = os.path.join(target_directory, 'urls.py')
		#traget_settings and target_urls refer to the the settings.py and urls.py in the actual django project folder

		#base_settings and base_urls refer to the ones within the DJANGO ABSTRACT STARTPOINT i.e the ALIEN folder
		base_settings = os.path.join(current_directory, 'source_settings.py')
		base_urls = os.path.join(current_directory, 'source_urls.py')

		print("All necessary files located, preparing to edit...")
		
		#Now write a new settings.py with appropriate input
		with open(target_settings, 'w') as sets:
			src = open(base_settings, 'r')
			for texts in src:
				if 'DjangoAbstractStartPoint' in texts:
					sets.write(texts.replace('DjangoAbstractStartPoint', proj))
				elif 'DjangoAbstractBasics' in texts:
					sets.write(texts.replace('DjangoAbstractBasics', title))
				elif '__SECRET_KEY__' in texts:
					sk = Generate_Secret_Key()
					sets.write(texts.replace('__SECRET_KEY__', sk))
				else:
					sets.write(texts)
			src.close()
			print('Edited 1 from 3...')

		#Write a new urls.py with appropriate input
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
			print('Edited 2 from 3...')

		#inside the created by DJANGO ABSTRACT STARTPOINT, change the apps.py to suit the name changes
		target_app = os.path.join(parent_directory, 'DjangoAbstractBasics', 'apps.py')
		base_app = os.path.join(current_directory, 'apps.py')
		with open(target_app, 'w') as app:
			src = open(base_app, 'r')
			for texts in src:
				if 'DjangoAbstractBasics' in texts:
					app.write(texts.replace('DjangoAbstractBasics', title))
				elif Capitalize_First_Letter('DjangoAbstractBasics') in texts:
					app.write(texts.replace(Capitalize_First_Letter('DjangoAbstractBasics'), Capitalize_First_Letter(title)))
				else:
					app.write(texts)
			src.close()


		#also edit the properties.py in this folder for future re-usage purposes
		with open(os.path.join(current_directory, 'properties.py'), 'w') as props:
			props.write("DJANGO_PROJECT_NAME = '" + proj +"' \n")
			props.write("PROJECT_USER_APP = '" + title +"' \n")
			props.write("FIRST_SETUP = False")
		print("All files ready to go...")

		os.rename(os.path.join(parent_directory, Initial_App_Name), os.path.join(parent_directory, title))
		print("All Processes Successfully Completed")

	except:
		print('Ooooops!! Something has gone horribly wrong....')


else:
	print('COULD NOT LOCATE ' + proj + '; check if the folder exist or consider manual approch')

	
t = input('Press enter to exit: ')