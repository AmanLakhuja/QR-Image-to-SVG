import tkinter as tk
from tkinter import filedialog, messagebox
import os
from ctypes import windll

from PIL import Image
from pyzbar.pyzbar import decode

import json
import qrcode
import qrcode.image.svg


#=====================================================
#                QR-Image-to-SVG-V1
#-----------------------------------------------------
# Created By Aman Lakhuja
# https://github.com/AmanLakhuja?tab=repositories
# https://github.com/AmanLakhuja
#=====================================================
# It Requires pyzbar qrcode pillow libraries to run.
# pip install pyzbar qrcode pillow
#-----------------------------------------------------


def extract_qr(root, output_box):
    # Open file dialog
    file_path = filedialog.askopenfilename(
        title="Select QR Code Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    
    if not file_path:
        return  # user canceled


    # Extract base filename without extension
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    
    try:
        # Open image
        img = Image.open(file_path)
        
        # Decode QR
        decoded_objects = decode(img)
        
        if decoded_objects:
            qr_data = decoded_objects[0].data.decode("utf-8")
            
            # Show the content [Enable this if you want a message box that shows your QR Code info, you can also see it directly in the output .json file]
            #messagebox.showinfo("QR Code Content", qr_data)

            # Save to JSON file named after the image
            json_filename = f"{base_name}_content.json"

            with open(json_filename, "w", encoding="utf-8") as f:
                f.write(qr_data)

            output_box.insert(tk.END, f"\n✅ Qr Code content saved As :-\n")
            output_box.insert(tk.END, f"▶ {json_filename}\n")
            output_box.see(tk.END)  # Scroll to end

            # Use these print statement instead for easy debuging or if you wish to remove the output_box 
            #print(f"✅ Qr Code content saved to {json_filename}")

            svg_filename = f"{base_name}_qr.svg"
            json_to_qr_svg(json_filename, svg_filename,output_box)

            # ✅ Close the Tkinter window after success , currently disable so you can view output_box 
            # root.destroy()

        else:
            messagebox.showwarning("No QR Found", "No QR code detected in the image.")
    except Exception as e:
        messagebox.showerror("Error", str(e))





def json_to_qr_svg(json_file, output_file="qr_code.svg" ,output_box=None):
    
    # Read the JSON file
    with open(json_file, "r", encoding="utf-8") as f:
        data = f.read().strip()  # Keep raw JSON string

    # Create an SVG factory
    factory = qrcode.image.svg.SvgImage

    # Generate QR code
    qr = qrcode.QRCode(
        version=None,  # auto-size
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Save as SVG
    img = qr.make_image(image_factory=factory)
    img.save(output_file)

    # Use these print statement for easy debuging.
    #print(f"✅ QR code generated from {json_file} and saved as {output_file}")

    if output_box:
        output_box.insert(tk.END, f"\n✅ New Qr code Generated\n")
        output_box.insert(tk.END, f"\n✅ New Qr code Saved as :-\n")
        output_box.insert(tk.END, f"▶ {output_file}\n")

        output_box.see(tk.END)
        

def main():

    # Tkinter window setup
    root = tk.Tk()
    windll.shcore.SetProcessDpiAwareness(1)
    root.title("QR-Image-to-SVG")
    root.geometry("480x400")
    
    main_frame = tk.Frame(root, bg='#333333' ,pady=20)
    main_frame.pack(fill=tk.BOTH , expand = True)

    # 🔼 Creator label at the top
    creator_label = tk.Label(
        main_frame,
        text="Created by Aman Lakhuja \n https://github.com/AmanLakhuja",
        font=("Arial", 12, "italic"),
        bg="#333333",
        fg="#aaaaaa",
        pady=10
    )
    creator_label.pack(anchor="n")

    btn = tk.Button(
        main_frame,
        text="Select QR Code Image",
        command=lambda: extract_qr(root, output_box),
        font=("Arial", 14),
        bg="#5fabb3",          
        fg="white",            
        activebackground="#2a5c5f",  
        activeforeground="white"
    )
    btn.pack(expand=True)

    output_box = tk.Text(main_frame, height=8, bg="#222222", fg="white", font=("Consolas", 12), padx=20)
    output_box.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()



    
