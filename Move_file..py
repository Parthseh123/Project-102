import os
import shutil
from_dir="C:/Users/User/Downloads"
to_dir="H:/Projects/Pythonfull/whitejr/project 102/Document_files"

list_of_files=os.listdir(from_dir)
for file in list_of_files:
    name,extension=os.path.splitext(file)
    if(extension==''):
        continue
    if(extension in ['.txt', '.doc', '.docx', '.pdf']):
        path1=f"{from_dir}/{file}"
        path2=f"{to_dir}"
        path3=f"{to_dir}/{file}"

        if(os.path.exists(path1) and os.path.exists(path2)):
            shutil.move(path1,path3)
            print(f"Moving {file} ....")
        elif(os.path.exists(path1)):
            os.mkdir(path2)
            shutil.move(path1,path3)
            print(f"Moving {file} ....")
print("succesfully moved all the files")