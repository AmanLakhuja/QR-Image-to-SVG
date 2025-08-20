

# Guide To Create a New Executable (.exe) of this Project.

* If you modify this project code and want to create a new executable (.exe) version of it you will need to go through the following steps :-

1. Install `pyinstaller` library on your system

	```bash
	pip install pyinstaller
	```

2. You will need All of the file mentioned Bellow in same Folder/Directory :-
	* qr_image_to_svg.py
	* libiconv.dll
	* libzbar-64.dll  

3. After This Go to the same directory in Command prompt and run this :- 

	```bash
	pyinstaller --onefile --windowed qr_image_to_svg.py ^
	  --add-binary "libiconv.dll;." ^
 	 --add-binary "libzbar-64.dll;."
	```
	

* You will find your (.exe) file in :-

	```bash
	dist/
	   └── qr_image_to_svg.exe
	```

---

### Additional Information

* You can Also add an Icon if you use this comman and have an .icon file

	```bash
	pyinstaller --onefile --windowed qr_image_to_svg.py ^
	  --add-binary "libiconv.dll;." ^
	  --add-binary "libzbar-64.dll;." ^
	  --add-data "icon.ico;." ^
	  --icon=icon.ico
	```
	
---