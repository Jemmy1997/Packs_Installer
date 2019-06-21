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
        5-Atom          6-VLC           7-opera     8-g++ compiler
        or simply type "all" to install all packs   
              ''')


def install_all():
    # Anaconda
    os.system(
        'wget https://repo.anaconda.com/archive/Anaconda3-5.3.1-Linux-x86_64.sh')
    os.system('bash Anaconda3-5.3.1-Linux-x86_64.sh')
    # VS code
    os.system('sudo apt install software-properties-common apt-transport-https wget')
    os.system(
        'wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -')
    os.system(
        'sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"')
    os.system('sudo apt install code')
    # Chrome
    os.system(
        'wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
    os.system('sudo dpkg -i google-chrome-stable_current_amd64.deb')
    # sublime
    os.system(
        'wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -')
    os.system('echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list')
    os.system('sudo apt install sublime-text')
    # Atom
    os.system('sudo add-apt-repository ppa:webupd8team/atom')
    os.system('sudo apt-get update')
    os.system('sudo apt-get install atom')
    # VLC
    os.system('sudo apt-get install vlc')
    # opera
    os.system('wget -qO- https://deb.opera.com/archive.key | sudo apt-key add -')
    os.system(
        'sudo add-apt-repository "deb [arch=i386,amd64] https://deb.opera.com/opera-stable/ stable non-free"')
    os.system('sudo apt install opera-stable')
    ##g++ compiler
    os.system('sudo apt-get install g++')


try:
    hello = input(
        'Enter numbers of packs to be installed seperated by comma "ie: 1,2,.." :\n ')
    setup_list = hello.split(',')
    os.system('sudo apt update')
    os.system('sudo apt upgrade')
    if 'all' or 'All' or 'ALL' in setup_list:
        install_all()
    else:
        for i in setup_list:
            if i == '1':  # Anaconda
                os.system(
                    'wget https://repo.anaconda.com/archive/Anaconda3-5.3.1-Linux-x86_64.sh')
                os.system('bash Anaconda3-5.3.1-Linux-x86_64.sh')
            elif i == '2':  # VS code
                os.system(
                    'sudo apt install software-properties-common apt-transport-https wget')
                os.system(
                    'wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -')
                os.system(
                    'sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"')
                os.system('sudo apt install code')
            elif i == '3':  # Google chrome
                os.system(
                    'wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
                os.system('sudo dpkg -i google-chrome-stable_current_amd64.deb')
            elif i == '4':  # Sublime
                os.system(
                    'wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -')
                os.system(
                    'echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list')
                os.system('sudo apt install sublime-text')
            elif i == '5':  # Atom
                os.system('sudo add-apt-repository ppa:webupd8team/atom')
                os.system('sudo apt-get update')
                os.system('sudo apt-get install atom')
            elif i == '6':  # VLC
                os.system('sudo apt-get install vlc')
            elif i == '7':
                os.system(
                    'wget -qO- https://deb.opera.com/archive.key | sudo apt-key add -')
                os.system(
                    'sudo add-apt-repository "deb [arch=i386,amd64] https://deb.opera.com/opera-stable/ stable non-free"')
                os.system('sudo apt install opera-stable')
            elif i == '8':
                os.system('sudo apt-get install g++')
except:
    print("\n ERROR, You didn't select any package to install \n Try to run the script again to select packs \n")
