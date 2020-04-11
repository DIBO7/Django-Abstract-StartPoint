'''
THIS FILE CONTAINS FUNCTIONS USED IN THE MAIN FILE (AUTO_START.py)
'''
import secrets
import string


def Generate_Secret_Key(number=60):
	#Generate_Secret_key generates random a 60-digit django secret key which excludes forbidden characters
	ready = True
	forbidden = ["'", '"', "\\"] #the forbidden characters

	SECRET_KEY = ''.join([secrets.SystemRandom().choice(
		"{}{}{}".format(string.ascii_letters, string.digits, string.punctuation)
		) for i in range(number)]) #Secret_Key Generator
	for characters in forbidden:
		if characters in SECRET_KEY: #if there is any of the forbidden characters in the Secret_key...
			ready = False #...change ready to Fails
	if not ready:
		#if secret key contains any forbidden_key,....
		return Generate_Secret_Key()# start this process all over until the generated secret_key contains no forbidden character
	return SECRET_KEY


def Capitalize_First_Letter(word):
	#as the name suggests, it capitalizes only the first letter of a given string
	word = word.lower()
	return word.replace(word[0], word[0].upper(), 1)


def Reverse_Changes(progress, empty_file1, empty_file2, empty_file3, target_settings, target_urls, target_app):
	#this function takes the progress bar as argument and determines what should be undone..
	#it would need 6 files to work..so instead of import the 6 files and redefining them...i just passed them as argumets to the function
	if progress == 1:
		#just rewrite the empty file1 to contain no code
		with open(empty_file1, 'w') as file:
			file.write("'''\nLEAVE THIS FILE AS IT IS\n'''")
	elif progress == 2:
		#recopy the newly written contents in empty_file1.py (which is the previous settings.py) back to settings.py
		with open(empty_file1, 'r') as file:
			settings = open(target_settings, 'w')
			for lines in file:
				settings.write(lines)
			settings.close()
	elif progress ==3:
		#just rewrite empty_file2 to contain no codes again
		with open(empty_file2, 'w') as file:
			file.write("'''\nLEAVE THIS FILE AS IT IS\n'''")
	elif progress == 4:
		#recopy the newly written contens in empty_file2.py (which is the original urls.py) back to urls.py
		with open(empty_file2, 'r') as file:
			urls = open(target_urls, 'w')
			for lines in file:
				urls.write(lines)
			urls.close()
	elif progress == 5:
		#just rewrite empty_file3.py to contain no code
		with open(empty_file3, 'w') as file:
			file.write("'''\nLEAVE THIS FILE AS IT IS\n'''")
	elif progress == 6:
		#transfer the contents in empty_file3.py back to the apps.py
		with open(empty_file3, 'r') as file:
			app = open(target_app, 'w')
			for lines in file:
				app.write(lines)
			app.close()
	else:
		pass