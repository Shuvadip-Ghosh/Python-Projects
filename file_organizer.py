import os 


videos_exts = ['3g2','3gp','avi','flv','h264','m4v','mkv','mov','mp4','mpg','mpeg','rm','swf','vob','wmv']
document_exts = ['txt','doc','ord','docx','odt ','rtf','pdf','ods','xlr','xls','xlsx','key','odp','pps','ppt','pptx']
music_exts = ['aif','cda','mid','midi','mp3','mpa','ogg','wav','wma','wpl','m3u']
images_exts = ['ai','bmp','gif','jpg','jpeg','png','ps','psd','svg','ico','tif','tiff','cr2']
data_exts = ['csv','dat','db','dbf','log','mdb','savsql','tar','xml','json']
executables_exts = ['apk','bat','com','exe','gadget','jar','wsf']
compressed = ['7z','arj','deb','pkg','rar','rpm','targz','z','zip']
system_exts = ['bak','cab','cfg','cpl','cur','dll','dmp','drv','icns','ini','lnk','msi','sys','tmp']
programming_exts = ['c','cgi','pl','class','javac','cpp','cs','h','py','pyw','php','sh','bat','swift','vb','js','cs','html']
others = []


def move(folder_name,filename):
    src = r"{}\{}".format(os.getcwd(),filename)
    new_name = r"{}\{}\{}".format(os.getcwd(),folder_name,filename)
    os.rename(src,new_name)

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        #print("creating {}".format(folder_name))
def list_checker(files):
    for file in files:
        if os.path.isfile(file):
            extension = os.path.splitext(file)[1].lower()
            extension = extension.replace(".","")
            if extension in videos_exts:
                create_folder("Videos")
                move("Videos",file)

            elif extension in document_exts:
                create_folder("Documents")
                move("Documents",file)

            elif extension in music_exts:
                create_folder("Music")
                move("Music",file)

            elif extension in images_exts:
                create_folder("Images")
                move("Images",file)

            elif extension in data_exts:
                create_folder("Data")
                move("Data",file)

            elif extension in executables_exts:
                create_folder("Executables")
                move("Executables",file)

            elif extension in compressed:
                create_folder("Compressed")
                move("Compressed",file)

            elif extension in system_exts:
                create_folder("System")
                move("System",file)

            elif extension in programming_exts:
                create_folder("Programming")
                move("Programming",file)

            else:
                create_folder("Others")
                move("Others",file)

if __name__ == "__main__":
    from tkinter import filedialog
    from tkinter import *
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    os.chdir(folder_selected)
    files = os.listdir()
    list_checker(files)



