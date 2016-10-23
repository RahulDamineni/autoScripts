sudo apt-get install python-pip python-dev build-essential
sudo pip install --upgrade pip
sudo pip install --upgrade virtualenv

sudo apt-get install python-opencv

sudo pip install ipython

sudo apt-get install python-imaging

sudo apt-get install git

sudo pip install selenium

sudo wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo  sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
sudo apt-get update
sudo apt-get install google-chrome-stable

sudo add-apt-repository ppa:webupd8team/atom
sudo apt-get update
sudo apt-get install atom

pip install python3-xlib
pip install pyautogui

sudo add-apt-repository ppa:mystic-mirage/pycharm
sudo apt update
sudo apt install pycharm

sudo apt-get install tesseract-ocr
sudo pip install pytesseract

sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose

sudo pip install -U scikit-learn

sudo pip install -U nltk
sudo python -m nltk.downloader -d /usr/local/share/nltk_data all
