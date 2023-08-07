from PIL import Image
from tkinter import filedialog as fd
print("Select an Image....")
fname = fd.askopenfilename(title='Select an Image',filetypes=(('images', ('*.png','*.jpg','*.webp')),('JPEG images', '*.jpg')))
im = Image.open(fname).convert("RGB")
ext = input("Select the extension to be converted to\npng  for png\njpg  for jpg\nwebp for webp\nEnter:- ")
fname = fname.replace(fname.split(".").pop(),"")
try:
	if ext == "png":
		im.save(f"{fname}png","png")
	elif ext == "jpg":
		im.save(f"{fname}jpg","jpeg")
	elif ext == "webp":
		im.save(f"{fname}webp","webp")
	print("The file has been converted and saved to the same location.....")
	input("Thank you for using this program\nPress any key to exit.......")
except:
	print("An error occured while converting the file.....")
	input("Please try again later.\nIf the error persists contact the develeoper...")