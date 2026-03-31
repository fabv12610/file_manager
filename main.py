import os
import getpass
import sys
import shutil

try:
	def check_os():
		if os.name =='nt':
			os_name = 'windows'
		elif os.name == 'posix':
			os_name = 'posix'
		else:
			print('None detected')
		return os_name

	os_used = check_os()
	username = getpass.getuser()

	def check_args():

		arguments = sys.argv  # List of arguments   
		script_name = sys.argv[0]  # Name of the script   

		# Checking if an argument is provided before accessing it   
		if len(sys.argv) > 1:   
		  first_argument = sys.argv[1]  # First argument   
		else:   
		  first_argument = None  # No argument provided 
		
		return first_argument

	args = check_args()

	def main():
		if args == None :
			if os_used == 'nt':
				folder = os.chdir(f"C:\\\\users\\\\{username}")
				os.mkdir('Videos')
				os.mkdir('Music')
				os.mkdir('Documents')
				os.mkdir('Images')
				os.mkdir('Others')

			elif os_used == 'posix':
				folder = os.chdir(f"/home/{username}/Downloads")
				os.mkdir('Videos')
				os.mkdir('Music')
				os.mkdir('Documents')
				os.mkdir('Images')
				os.mkdir('Others')
			else:
				print('Error has occured with detecting os')

		else:
			os.chdir(args)
			os.mkdir('Videos')
			os.mkdir('Music')
			os.mkdir('Documents')
			os.mkdir('Images')
			os.mkdir('Others')

		return (os.getcwd())

	main = main()

	def sort():
		files = os.listdir(main)

		for file in files:
		    path = os.path.join(main, file)

		    if not os.path.isfile(path):
		        continue

		    if file.endswith(('.avi', '.mov', '.mp4', '.ogg', '.wmv', '.webm')):
		        folder = 'Videos'

		    elif file.endswith(('.mp3', '.wav', '.ogg')):
		        folder = 'Music'

		    elif file.endswith(('.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pdf', '.odt', '.ods', '.odp', '.rtf')):
		        folder = 'Documents'

		    elif file.endswith(('.jpg', '.png', '.gif', '.tiff', '.ico', '.svg', '.webp')):
		        folder = 'Images'

		    else:
		        folder = 'Others'

		    dest = os.path.join(main, folder)
		    os.makedirs(dest, exist_ok=True)

		    shutil.move(path, os.path.join(dest, file))

	sort()

except:
	print('Error handling')