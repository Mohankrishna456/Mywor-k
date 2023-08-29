import tkinter as tk
import pyshorteners

top = tk.Tk()
top.geometry("800x700")
top.title("Link - Shortener")
top.iconbitmap('C:\\Users\\bhamm\\Desktop\\UrlShortener\\urle2.ico')
top.config(bg="aqua")
label1 = tk.Label(top, text="Enter the Link Below...", font=("Helvetica",30))
label1.pack(pady = 20)
def select():
     if entry2.get():
          entry2.delete(0,"end")
     if entry1.get():
          #converting to short URL
          url = pyshorteners.Shortener().tinyurl.short(entry1.get())
          #output link to screen
          entry2.insert("end", url)
          #printing Reverse URL to terminal
          print(pyshorteners.Shortener().tinyurl.expand(entry1.get()))


entry1 = tk.Entry(top, font = ("Helvetica",11), width=30)
entry1.pack(pady = 20)



buttono = tk.Button(top, text="CLICK HERE TO SHORTEN", fg = "green",command=select)
buttono.pack(pady = 30)

label2 = tk.Label(top, text="SHORTENED LINK", fg="red", bg="Yellow", font=("Courier",12))
label2.pack(pady = 40)

label3 = tk.Label(top, text="HERE", font=("Times",25), fg="red")
label3.pack(pady=15)

entry2 = tk.Entry(top, font = ("Helvetica",11), justify= "center",width=30)
entry2.pack(pady = 20)

top.mainloop()