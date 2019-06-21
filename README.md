# Packs_Installer
This is a python script used for installing some needed packs for UBUNTU based distros to help you save your time and don't waste it searching for commands to install these packs

## Note that: you have to change directory in terminal to the repo directory or open the terminal in the repo dir to run this program successfully, have python3 as a default interpreter and have an internet connection
to check the python version write in your terminal 
```
$ python --version
``` 
you may see something like that as python is installed with linux by default 
```
Python 2.7.15rc1

```
If Python 3.x.x exist instead of Python 2.x.x so you can **skip step 1** and just go for step 2 briefly.

## Step 1
* open the terminal in the repo directory
* write in the terminal:
```
$ bash py3_installer
```
* write password then you will need pressing ENTER so do and just wait for installing python 3
* you will get nano screen to edit as following 
![Alt text](1.png?raw=true "Title")
* write ``` alias python = python3``` as shown to make the default version is python3
* press (CTRL + O) then ENTER to save what you have done then press (CTRL + X) to exit from nano
* to make a double check write the version command and it will be 3.x.x this time  
```
$ python --version 
```
## Step 2
* write in the terminal 
```
$ python commands.py
```
* now you will have choices to select and setup any pack in the script 
### Congracts!, You just reached the end  