Conor Conlon X14499688
BSHC4 - SD
To run - 
	Have python3 installed and on your environment variable path - PATH : 
	\bin;C:\Users\Conor\AppData\Local\Programs\Python\Python36-32\Scripts\;C:\Users\Conor\AppData\Local\Programs\Python\Python36-32
	
	PYTHONPATH set as a environment variable - System Variable  - PYTHONPATH : C:\Python27\Lib;C:\Python27\DLLs;C:\Users\Conor\Desktop		\Python-3.4.6\Lib
	

	To begin you will need to edit the venv\scripts\activate file - on line 43 you muset
	change these paths to allign with wherever you have this project. The path shoud lead
	to the project and then to the vemv for example C:\Yourname\Desktop\cg\venv This
	
	Now the virtual environment must be started, in command line cd into the projects main folder
	then tyoe - venv\scripts\activate
	This will start the virtual environment, now cd into the djangorest folder
	then type - python manage.py runserver 

	The app should be now available on localhost:8000
 	 
	in the case that imports are not retained in the environment
	In most cases a pip install NAMEOFMODELE/APP
	will do the trick	
	
	A list of the requirements is in requirements.txt and the error thrown should point to the missing import
	

