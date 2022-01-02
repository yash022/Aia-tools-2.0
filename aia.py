import zipfile
import os
from pathlib import Path
import json

__author__ = 'Yash Sehgal <@yash@yashsehgal.tech>'

aia_path = input("Please enter the aia path : ")
aia_rename = Path(aia_path)
aia_rename.rename(aia_rename.with_suffix('.zip'))

aia_converted_to_zip_path = aia_path.replace(".aia", ".zip")

def remove_space(string):
    return string.replace(" ", "")

username = os.getlogin()
aia_name = os.path.basename(aia_rename)
path_to_extracted_files = str(os.path.join(r"C:\Users", username)) + "\Desktop" + r"\aiainfo_"+remove_space(str(aia_name).replace(".aia"," "))

with zipfile.ZipFile(aia_converted_to_zip_path, 'r') as zip:
    zip.extractall(path_to_extracted_files)


class Project_properties:
    @staticmethod
    def project_created_on():
        project_properties_path = open(Path(path_to_extracted_files + "\youngandroidproject\project.properties"))
        print(str(project_properties_path.readlines()).split(',')[1].replace("#", " ").replace("'", " ").replace("\n"," "))

    @staticmethod
    def app_name():
        project_properties_path = open(Path(path_to_extracted_files + "\youngandroidproject\project.properties"))
        print(str(project_properties_path.readlines()).split(',')[3].replace("name=", " ").replace("'", " ").replace("\n"," "))

    @staticmethod
    def defaultfilescope():
        project_properties_path = open(Path(path_to_extracted_files + "\youngandroidproject\project.properties"))
        print(str(project_properties_path.readlines()[4]).split("=")[1])

    @staticmethod
    def username_for_ai2():
        project_properties_path = open(Path(path_to_extracted_files + "\youngandroidproject\project.properties"))
        print(str(project_properties_path.readlines()[5]).split("=")[1].split(".")[1])

    @staticmethod
    def accent_color():
        project_properties_path = open(Path(path_to_extracted_files + "\youngandroidproject\project.properties"))
        print(str(project_properties_path.readlines()[6]).split("=")[1])

    @staticmethod
    def sizing():
        project_properties_path = open(Path(path_to_extracted_files + "\youngandroidproject\project.properties"))
        print(str(project_properties_path.readlines()[7]).split("=")[1])

    @staticmethod
    def theme():
        project_properties_path = open(Path(path_to_extracted_files + "\youngandroidproject\project.properties"))
        print(str(project_properties_path.readlines()[8]).split("=")[1])

    @staticmethod
    def showlistsasjson():
        project_properties_path = open(Path(path_to_extracted_files + "\youngandroidproject\project.properties"))
        print(str(project_properties_path.readlines()[9]).split("=")[1])

    @staticmethod
    def useslocation():
        project_properties_path = open(Path(path_to_extracted_files + "\youngandroidproject\project.properties"))
        print(str(project_properties_path.readlines()[10]).split("=")[1])

    @staticmethod
    def primary_color():
        project_properties_path = open(Path(path_to_extracted_files + "\youngandroidproject\project.properties"))
        print(str(project_properties_path.readlines()[13]).split("=")[1])

    @staticmethod
    def versioncode():
        project_properties_path = open(Path(path_to_extracted_files + "\youngandroidproject\project.properties"))
        print(str(project_properties_path.readlines()[16]).split("=")[1])

    @staticmethod
    def color_primary_dark():
        project_properties_path = open(Path(path_to_extracted_files + "\youngandroidproject\project.properties"))
        print(str(project_properties_path.readlines()[17]).split("=")[1])

def Extesnion_list():
    for extensions in os.listdir(path_to_extracted_files+"\\assets\external_comps"):
        file_json_text = json.loads(open(path_to_extracted_files+"\\assets\external_comps"+"\\"+extensions+"\\"+"components.json").read())
        json_to_dict = dict(file_json_text[0])
        print(json_to_dict['name'])

project_properties_path = open (Path (path_to_extracted_files + "\youngandroidproject\project.properties"))
username = (str (project_properties_path.readlines ()[5]).split ("=")[1].split (".")[1])
project_properties_path = open (Path (path_to_extracted_files + "\youngandroidproject\project.properties"))
app_name = (str (project_properties_path.readlines ()).split (',')[3].replace ("name=", " ").replace ("'", " ").replace ("\n", " "))
path_for_blocks_info = (path_to_extracted_files +"\\"+"src\\appinventor"+"\\"+username+"\\"+str(remove_space(app_name)).replace("\\n"," "))

for file in os.listdir(remove_space(path_for_blocks_info)):
    if file.split(".")[1] == "scm":
        Json_data = (str(open(remove_space(path_for_blocks_info+"\\"+file)).read()).removeprefix("#|").removesuffix("|#").replace("$JSON"," "))


p = Project_properties
print(p.username_for_ai2())