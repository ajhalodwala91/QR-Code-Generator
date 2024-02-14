from tkinter import *
from customtkinter import *
from PIL import Image
import qrcode

def make_qr():
    name = name_entry.get()
    link = link_entry.get()

    if len(name)>1 and len(link)>1:
        code = qrcode.make(link)
        code.save(str(name)+'.png')
    
        global main_img, qr_image
        qr_image = CTkImage(Image.open(str(name)+'.png'), size = (250, 250)) 
        main_img = CTkLabel(img_frame, text = '', image = qr_image, fg_color = '#00532b')
        main_img.place(relx = 0.5, rely = 0.47, anchor = CENTER)
        img_saved_lbl = CTkLabel(img_frame, text = f'Image Saved Successfully..!!', text_color = 'white', font = ('Arial', 16))
        img_saved_lbl.place(relx = 0.5, rely = 0.87, anchor = CENTER)
    
window = CTk()
window.geometry('700x400')
window.title('QR Code Generator')
window.resizable(False, False)

data_frame = CTkFrame(window, fg_color = 'white', corner_radius = 0)
data_frame.place(relx = 0, relheight = 1, relwidth = 0.5)

img_frame = CTkFrame(window, fg_color = '#3a7ff6', corner_radius = 0)
img_frame.place(relx = 0.5, relheight = 1, relwidth = 0.52)

title_lbl = CTkLabel(data_frame, text = 'QR Code Generator', font = ('Arial', 28))
title_lbl.place(relx = 0.5, rely = 0.15, anchor = CENTER)

name_frame = CTkFrame(data_frame, fg_color = '#dce4f3', height = 55)
name_frame.place(relx = 0.5, rely = 0.38, anchor = CENTER, relwidth = 0.75)

name_lbl = CTkLabel(name_frame, text = 'Name', fg_color = '#dce4f3', font = ('Arial', 12)) 
name_lbl.place(relx = 0.1, rely = 0.2, anchor = CENTER)

name_entry = CTkEntry(name_frame, fg_color = '#dce4f3', font = ('Arial', 16), border_color = '#dce4f3')
name_entry.place(relx = 0.01, rely = 0.65, anchor = W, relwidth = 0.9)

link_frame = CTkFrame(data_frame, fg_color = '#dce4f3', height = 55)
link_frame.place(relx = 0.5, rely = 0.55, anchor = CENTER, relwidth = 0.75)

link_lbl = CTkLabel(link_frame, text = 'Link', fg_color = '#dce4f3', font = ('Arial', 12)) 
link_lbl.place(relx = 0.08, rely = 0.2, anchor = CENTER)

link_entry = CTkEntry(link_frame, fg_color = '#dce4f3', font = ('Arial', 16), border_color = '#dce4f3')
link_entry.place(relx = 0.01, rely = 0.65, anchor = W, relwidth = 0.9)

submit_btn = CTkButton(data_frame, text = 'Generate', fg_color = '#3a7ff6', font = ('Arial', 20), height = 50, command = make_qr)
submit_btn.place(relx = 0.5, rely = 0.8, anchor = CENTER)

window.mainloop()