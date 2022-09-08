#README.txt
#Sam Lojacono
#CSCI 77800 Fall 2022
#No collaborators

This file was written as a long term project for me to explore and analyze how often songs and artists are played on
radio stations.  It was a project that I started three years ago, asking the question about how often artists and songs are played
on air, as well as what the deejays' musical preferences are.

I am submitting one of the script files to you.  Some of these scripts are on their third or fourth edition to account for changes in the stations' websites.

Every time it is run, the script will write and save a spreadsheet with the song data collected from that specific radio station.  If it is run on a different time on the same day, it will open up the same spreadsheet and write the data on a new tab and ave it.  If it is a completely different day, it will create a new file for that specific new day.

In order to run this on your program, you need to install the following:
- geckodriver
- Python selenium module
- Mozilla Firefox

If in the unfortunate instance you are not able to get it to work, I am providing you with two links so you can see and watch how it runs:

Google Drive link: https://drive.google.com/file/d/1RSP7761TYa-p1TZbxnYuiYUSYhEEY2Md/view?usp=sharing
Youtube link: https://youtu.be/V6DwTFODUwU

PROCESS TO RUN PYTHON SCRIPTS:
1. 	Install Mozilla Firefox first if you have not already.

2. 	Go into your Command prompt (or Terminal if you use Linux) and then 
   	install the selenium module for python.  Use the command
	python2 install selenium to do so.

3.	Download geckodriver, which is the software that allows Python to 
	talk to and control Firefox.  To avoid any issues, you may
	have to install geckodriver in the /usr/bin or /usr/local/bin filepath.  

	If you have Linux, the following commands should work:
	sudo apt install geckodriver
	wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0 geckodriver-v0.24.0-linux64.tar.gz
	tar -xvzf geckodriver*
	chmod +x geckodriver
	export PATH=$PATH:/path-to-extracted-file/

	The wget command is all one line.  The export command puts in a filepath reference in your enviornment variable.  This will help tell Linux where geckodriver so it is accessible whenever you use it in your code.

4. 	Go into the code and in lines 46 and 164 change the code to the 
	filepath and change it to wherever you want to save the file that will be written.

5. 	Run the code in the python command line either in the command prompt 
	or in the terminal.  Either script you run will take a few minutes to run, but at the end you should see in the file or directory you put in your filepath an Excel spreadsheet file that will contain all the songs that were played in the station's playlist.
