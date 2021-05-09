# PythonFinal
This is an app designed for the Audubon Society of Miami Valley. This app can be used help capture and analyze data for their Eastern Bluebird Nesting project. Features of this app include the ability to enter data, a tables to view the data, the ability to edit or delete a data record, a graph to show the data from past years, a map of the Hueston Woods, and a help page.

# To Download
To download these files click on the green "Code" button and click "download ZIP". Once the files are done downloading, unzip them and open in text editor of your choice. You can also download them by clicking the green "Code" button and copying the link. Then open GitBash in a selected folder and type git clone *link* and paste the link after "git clone" and push enter. This will clone all the files to the folder you chose. 

# To Use
Before using code you will need to create a virtual environment to place your code in. Details on how to do that can be found here: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/. Once your virtual enviornment is created, open Pycharm, click "New Project" and choose your virtual environment. If you do not currently have Pycharm downloaded, you can download it here: https://www.jetbrains.com/pycharm/. Then place the downloaded github code in the venv folder. To run the app open the terminal and enter 
``` 
set FLASK_APP=project
set FLASK_DEBUG=1
*NOTE: if using a Mac, use EXPORT instead of set 
```
Hit enter then type ```flask run``` the app should then be running in localhost:5000.

# App File Structure
```
flask_auth_app/
├─ project/
│  ├─ static/
│  │  ├─ styles/
│  │  │  ├─ custom.css
│  │  │  ├─ custom.css.map
│  │  ├─ graphs.js
│  │  ├─ logo.png
│  ├─ templates/
│  │  ├─ _formhelpers.html
│  │  ├─ base.html
│  │  ├─ edit-entry.html
│  │  ├─ entry.html
│  │  ├─ graph.html
│  │  ├─ help.html
│  │  ├─ index.html
│  │  ├─ login.html
│  │  ├─ map.html
│  │  ├─ profile.html
│  │  ├─ signup.html
│  │  ├─ table.html
│  ├─ __init__.py
│  ├─ auth.py
│  ├─ form.py
│  ├─ main.py
│  ├─ models.py
```
# Database Structure
```
user/
├─ id
├─ email
├─ password
├─ name
entry/
├─ houseId
├─ date
├─ id
├─ eggs
├─ alive
├─ dead
├─ species
├─ cowbird
├─ damaged
├─ comment
├─ entryId
```
