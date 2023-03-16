import os
from pathlib import Path
import logging

while True:
    project_name = input("Enter your project name: ")
    if project_name != "":
        break
logging.info(f"Creating the new project: {project_name}")   

list_of_files = [
    ".github/workflows/.giignore",
    ".github/workflows/main.yaml",
    "{project_name}/__init__.py",
    "{project_name}/components/__init__.py",
    "{project_name}/config/__init__.py",
    "{project_name}/constants/__init__.py",
    "{project_name}/entity/__init__.py",
    "{project_name}/exception/__init__.py",
    "{project_name}/logger/__init__.py",
    "{project_name}/pipeline/__init__.py",
    "{project_name}/utils/__init__.py",
    f"config/config.yaml",
    "requirements.txt",
    "setup.py",
    "main.py",
    "schema.yaml" 
]

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)
    
    if filedir != "": #ask1 if not defined
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating the new director at : {filedir} for file : {filename}")
        
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path, "w") as f :
            pass
            logging.info(f"Creating the new file : {filename} for path : {file_path}")
    else:
        logging.info(f"File is already present at : {file_path}")
        
    
        
    
    
    