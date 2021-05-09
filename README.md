# PythonFinal

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
