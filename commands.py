import os
print('''
        **************************************************************  
        *    |\            /|     _ _ _ _ _ _ _ _ _    \          /  * 
        *    | \          / |    |                 |    \        /   *
        *    |  \        /  |    |                 |     \      /    *
        *    |   \      /   |    |                        \    /     *
        *    |    \    /    |    |                         \  /      *
        *    |     \  /     |    |      | _ _ _ _ _         \/       *
        *    |      \/      |    |      |          |        ||       *
        *    |              |    |                 |        ||       *
        *    |              |  . |                 | .      ||       *
        *    |              |    |                 |        ||       *
        *    |              |    |_ _ _ _ _ _ _ _ _|        ||       *
        **************************************************************
          ''')
print('''This script to provide your UBUNTU based distros with possible needed packages 
                        Here is the packages you may need \n
        1-Anaconda      2-VS code       3-Google Chrome     4-Sublime
        5-Atom          6-VLC           7-opera             8-g++ compiler
        9-git              
              ''')

def update_upgrade():
    os.system('sudo apt-get update')
    os.system('sudo apt-get upgrade')
def install_anaconda():
    os.system('wget https://repo.anaconda.com/archive/Anaconda3-5.3.1-Linux-x86_64.sh')
    os.system('bash Anaconda3-5.3.1-Linux-x86_64.sh')
def install_vscode():
    os.system('sudo apt install software-properties-common apt-transport-https wget')
    os.system('wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -')
    os.system('sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"')
    os.system('sudo apt install code')
def install_chrome():
    os.system('wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
    os.system('sudo dpkg -i google-chrome-stable_current_amd64.deb')
def install_sublime():
    os.system('wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -')
    os.system('echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list')
    os.system('sudo apt install sublime-text')
def install_atom():
    os.system('sudo add-apt-repository ppa:webupd8team/atom')
    os.system('sudo apt-get update')
    os.system('sudo apt-get install atom')
def install_vlc():
    os.system('sudo apt-get install vlc')
def install_opera():
    os.system('wget -qO- https://deb.opera.com/archive.key | sudo apt-key add -')
    os.system('sudo add-apt-repository "deb [arch=i386,amd64] https://deb.opera.com/opera-stable/ stable non-free"')
    os.system('sudo apt install opera-stable')
def install_gpp():
    os.system('sudo apt-get install g++')    
def install_git():
    os.system('sudo apt-get install git') 
try:
    hello = input('Enter numbers of packs to be installed seperated by comma "i.e.: 2,8,.." :\n ')
    setup_list = hello.split(',')
    if not setup_list:
        print("You didn't select any pack!")
    else:
        for i in setup_list:
            if i == '1':  # Anaconda
                install_anaconda()
            elif i == '2':  # VS code
                install_vscode () 
            elif i == '3':  # Google chrome
                install_chrome()
            elif i == '4':  # Sublime
                install_sublime()    
            elif i == '5':  # Atom
                install_atom()
            elif i == '6':  # VLC
                install_vlc()   
            elif i == '7':  # opera
                install_opera()         
            elif i == '8':  # g++ compiler
                install_gpp()
            elif i == '9':# git
                install_git()        
except:
    print("\n ERROR, Try to run the script again to select packs ")
