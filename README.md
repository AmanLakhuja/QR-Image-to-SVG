# 🧾 QR Code Image To SVG Generator - (QR-Image-to-SVG)

A simple Tkinter GUI app to:

* Extract Qr code content from an image
* Save it as a `.json` file
* Generate a new QR code from that content and save it as an SVG

---
# Features

* It can convert multiple types of Qr Code Image into Qr Code SVG
* ☑️ Json QR Code Image to SVG
* ☑️ Plain text QR Code Image to SVG
* ☑️ URLs (links) QR Code Image to SVG
* ☑️ Email addresses QR Code Image to SVG
* ☑️ vCards or contact info QR Code Image to SVG
* ☑️ Any decodable string Image to SVG

---

## 📦 Requirements & Dependencies

1. Python 3.8 or newer

2. The following Python libraries:
	* pyzbar
	* qrcode
	* pillow
	* tkinter

* Note: `tkinter` is built into Python (Windows/macOS), no need to install it separately.

---

## Install Required Libraries

1. Step-1 : Open Command Prompt

2. Step-2 : Write the following command

	```bash
	pip install pyzbar qrcode pillow
	```

* Or you can Run this command if you open your command prompt in same directory as the requirements.txt file:- 

	```bash
	pip install -r requirements.txt
	```

---

## ▶️ How to Run

1. Run the app using: `python main.py`
2. It Prompts you to select a QR code image
3. Extracts and saves the content as `{filename}_content.json`
4. Generates a new QR code SVG: `{filename}_qr.svg`

---

## 📁 Output Files

*  `{your-image-name}_content.json`
*  `{your-image-name}_qr.svg`

---

## Project ASCII Tree

```bash
QR-Image-to-SVG/
├── qr_image_to_svg.py       -- Your script (rename from untitled.py or similar)
├── requirements.txt         -- Dependency list
├── README.md                -- Project description & instructions
├── LICENSE			             -- Project LICENSE agreement
└── dist/
	└── qr_image_to_svg.exe		-- Released Executable File		   
```

---

## 👤 Created by Aman Lakhuja

* [MY-GitHub](https://github.com/AmanLakhuja) 

---

## License

* Check out the license agrement file in the project directiory 




