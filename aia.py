# Importing modules
import json
import os
import zipfile
from pathlib import Path

__author__ = 'Yash Sehgal <@yash@yashsehgal.tech>'


# function to remove spaces from sentence
def remove_space(string):
    return string.replace(" ", "")


# to set the aia file path
def aia_file(file_path):
    return file_path


# changes the file extension to zip from aia
aia_rename_tozip = Path(str(aia_file)).with_suffix('.zip')

# stores the path where the zip file is stored , for further use
aia_converted_to_zip_path = str(aia_file).replace(".aia", ".zip")

# stores the username to format the path for the zip file
username = os.getlogin()

# stores the aia file name for later use
aia_name = os.path.basename(str(aia_file))

# makes the path for the zip file to be extracted
path_to_extracted_files = str(os.path.join(r"C:\Users", username))+"\\Desktop"+r"\aiainfo_"+remove_space(str(aia_name).replace(".aia", " "))

# extracts the zip file
with zipfile.ZipFile(aia_converted_to_zip_path, 'r') as zip_file:
    zip_file.extractall(path_to_extracted_files)


# class for ProjectProperties
class ProjectProperties:
    @staticmethod
    # method to find the date on which the aia was created
    def project_created_on():
        project_properties_file_path = open(Path(path_to_extracted_files+"\\"+"youngandroidproject"+"\\"+"project.properties"))
        return str(project_properties_file_path.readlines()).split(',')[1].replace("#", " ").replace("'", " ").replace("\n", " ")

    @staticmethod
    # method to get the name of the app
    def app_name():
        project_properties_file_path = open(Path(path_to_extracted_files+"\\"+"youngandroidproject"+"\\"+"project.properties"))
        return str(project_properties_file_path.readlines()).split(',')[3].replace("name=", " ").replace("'", " ").replace("\n", " ")

    @staticmethod
    # method to get file scope
    def defaultfilescope():
        project_properties_file_path = open(Path(path_to_extracted_files+"\\"+"youngandroidproject"+"\\"+"project.properties"))
        return str(project_properties_file_path.readlines()[4]).split("=")[1]

    @staticmethod
    # method to get the ai2 username
    def username_for_ai2():
        project_properties_file_path = open(Path(path_to_extracted_files+"\\"+"youngandroidproject"+"\\"+"project.properties"))
        return str(project_properties_file_path.readlines()[5]).split("=")[1].split(".")[1]

    @staticmethod
    # method to get the accent color of the app
    def accent_color():
        project_properties_file_path = open(Path(path_to_extracted_files+"\\"+"youngandroidproject"+"\\"+"project.properties"))
        return str(project_properties_file_path.readlines()[6]).split("=")[1]

    @staticmethod
    # method to check the sizing of the app
    def sizing():
        project_properties_file_path = open(Path(path_to_extracted_files+"\\"+"youngandroidproject"+"\\"+"project.properties"))
        return str(project_properties_file_path.readlines()[7]).split("=")[1]

    @staticmethod
    # method to get the theme of the app
    def theme():
        project_properties_file_path = open(Path(path_to_extracted_files+"\\"+"youngandroidproject"+"\\"+"project.properties"))
        return str(project_properties_file_path.readlines()[8]).split("=")[1]

    @staticmethod
    # method to check if list is shown as json or not (boolean)
    def showlistsasjson():
        project_properties_file_path = open(Path(path_to_extracted_files+"\\"+"youngandroidproject"+"\\"+"project.properties"))
        if str(project_properties_file_path.readlines()[9]).split("=")[1] == "True":
            return "True"
        else:
            return "False"

    @staticmethod
    # method to check if the app uses location or not (boolean)
    def useslocation():
        project_properties_file_path = open(Path(path_to_extracted_files+"\\"+"youngandroidproject"+"\\"+"project.properties"))
        if str(project_properties_file_path.readlines()[10]).split("=")[1] == "False":
            return "False"
        else:
            return "True"

    @staticmethod
    # method to get the primary color of the app
    def primary_color():
        project_properties_file_path = open(Path(path_to_extracted_files+"\\"+"youngandroidproject"+"\\"+"project.properties"))
        return str(project_properties_file_path.readlines()[13]).split("=")[1]

    @staticmethod
    # method to get the version code of the app
    def version_code():
        project_properties_file_path = open(Path(path_to_extracted_files+"\\"+"youngandroidproject"+"\\"+"project.properties"))
        return str(project_properties_file_path.readlines()[16]).split("=")[1]

    @staticmethod
    # method to get the primary dark color
    def color_primary_dark():
        project_properties_file_path = open(Path(path_to_extracted_files+"\\"+"youngandroidproject"+"\\"+"project.properties"))
        return str(project_properties_file_path.readlines()[17]).split("=")[1]


# function/method to get the list of extensions used in the aia
def extesnion_list():
    for extensions in os.listdir(path_to_extracted_files+"\\"+"assets"+"\\"+"external_comps"):
        file_json_text = json.loads(open(path_to_extracted_files+"\\"+"assets"+"\\"+"external_comps"+"\\"+extensions+"\\"+"components.json").read())
        json_to_dict = dict(file_json_text[0])
        return json_to_dict['name']


# makes the path for screen scm files
username = ProjectProperties().username_for_ai2()
app_name = ProjectProperties().app_name()
path_for_blocks_info = path_to_extracted_files+"\\"+"src\\appinventor"+"\\"+username+"\\"+str(remove_space(app_name)).replace("\\n", " ")

# extracts the json data from all screen scm files
for file in os.listdir(remove_space(path_for_blocks_info)):
    if file.split(".")[1] == "scm":
        Json_data = str(open(remove_space(path_for_blocks_info+"\\"+file)).read()).removeprefix("#|").removesuffix("|#").replace("$JSON", " ")

