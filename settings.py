from selenium import webdriver
from genericlib.FileLib import fileData

obj_file=fileData()
data=obj_file.fileOpen()
username = data["Username"]
pwd = data["Password"]
url = data["url"]
origin=data["origin"]
destination=data["Destination"]

if data["browser"] == "chrome":
     driver = webdriver.Chrome(executable_path=r'C:\Users\Vidyashree\PycharmProjects\makeMyTrip\drivers\chromedriver.exe')

elif data["browser"] == "firefox":
     driver = webdriver.Firefox(executable_path=r'C:\Users\Vidyashree\PycharmProjects\makeMyTrip\drivers\geckodriver.exe')













