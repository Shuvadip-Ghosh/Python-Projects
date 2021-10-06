import os 
pwd = os.getcwd()
folder_to_track = r"{}".format(pwd)
folder_to_put = r""
filename = ""

src = r"{}\{}".format(folder_to_track,filename)
new_name = r"{}\{}".format(folder_to_put,filename)
os.rename(src,new_name)