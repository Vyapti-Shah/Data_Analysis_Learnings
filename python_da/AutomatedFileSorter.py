#Automated File Sorter in File Explorer
import os, shutil
path = r"C:/Users/vyapti shah/OneDrive\Desktop/python_da/automated file sorter file/" #r - w/o r it will read all the :,\,etc but with r it will read it as a raw string
print(os.listdir(path))
file_name = os.listdir(path)

folder_names = ['excel_files','image_files','text_files']
for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])

for file in file_name:
    if '.xlsx' in file and not os.path.exists(path + "excel_files/" + file):
        shutil.move(path + file, path + "excel_files/" + file)
    if '.jpg' in file and not os.path.exists(path + "image_files/" + file):
        shutil.move(path + file, path + "image_files/" + file)
    if '.txt' in file and not os.path.exists(path + "text_files/" + file):
        shutil.move(path + file, path + "text_files/" + file)