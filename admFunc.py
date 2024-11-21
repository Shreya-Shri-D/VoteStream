import tkinter as tk
import dframe as df
from dframe import *
from tkinter import *
from PIL import ImageTk, Image

def resetAll(root, frame1):
    for widget in frame1.winfo_children():
        widget.destroy()
    Label(frame1, text="Reset Complete",bg="#D4E4F7").grid(row=10, column=0)

def showVotes(root, frame1):
    
    result = df.show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()
    
    root.config(bg="#D4E4F7") 
   

    frame1.config(bg="#D4E4F7")  # Light blue background

    Label(frame1, text="Vote Count", font=('Helvetica', 18, 'bold'), bg="#D4E4F7").grid(row=0, column=1, rowspan=1)
    Label(frame1, text="", bg="#D4E4F7").grid(row=1, column=0)

    bjpLogo = ImageTk.PhotoImage((Image.open("img/bjp.png")).resize((35, 35), Image.BICUBIC))
    bjpImg = Label(frame1, image=bjpLogo, bg="#D4E4F7")
    bjpImg.grid(row=2, column=0)

    congLogo = ImageTk.PhotoImage((Image.open("img/cong.jpg")).resize((25, 38), Image.BICUBIC))
    congImg = Label(frame1, image=congLogo, bg="#D4E4F7")
    congImg.grid(row=3, column=0)

    aapLogo = ImageTk.PhotoImage((Image.open("img/aap.png")).resize((45, 30), Image.BICUBIC))
    aapImg = Label(frame1, image=aapLogo, bg="#D4E4F7")
    aapImg.grid(row=4, column=0)

    ssLogo = ImageTk.PhotoImage((Image.open("img/ss.png")).resize((40, 35), Image.BICUBIC))
    ssImg = Label(frame1, image=ssLogo, bg="#D4E4F7")
    ssImg.grid(row=5, column=0)

    notaLogo = ImageTk.PhotoImage((Image.open("img/nota.jpg")).resize((35, 25), Image.BICUBIC))
    notaImg = Label(frame1, image=notaLogo, bg="#D4E4F7")
    notaImg.grid(row=6, column=0)

    Label(frame1, text="BJP              :       ", font=('Helvetica', 12, 'bold'), bg="#D4E4F7").grid(row=2, column=1)
    Label(frame1, text=result['bjp'], font=('Helvetica', 12, 'bold'), bg="#D4E4F7").grid(row=2, column=2)

    Label(frame1, text=" Cong             :          ", font=('Helvetica', 12, 'bold'), bg="#D4E4F7").grid(row=3, column=1)
    Label(frame1, text=result['cong'], font=('Helvetica', 12, 'bold'), bg="#D4E4F7").grid(row=3, column=2)

    Label(frame1, text=" AAP               :          ", font=('Helvetica', 12, 'bold'), bg="#D4E4F7").grid(row=4, column=1)
    Label(frame1, text=result['aap'], font=('Helvetica', 12, 'bold'), bg="#D4E4F7").grid(row=4, column=2)

    Label(frame1, text=" Shiv Sena    :          ", font=('Helvetica', 12, 'bold'), bg="#D4E4F7").grid(row=5, column=1)
    Label(frame1, text=result['ss'], font=('Helvetica', 12, 'bold'), bg="#D4E4F7").grid(row=5, column=2)

    Label(frame1, text=" NOTA            :          ", font=('Helvetica', 12, 'bold'), bg="#D4E4F7").grid(row=6, column=1)
    Label(frame1, text=result['nota'], font=('Helvetica', 12, 'bold'), bg="#D4E4F7").grid(row=6, column=2)

    frame1.pack()
    root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x500')
    frame1 = tk.Frame(root, bg="#D4E4F7")  # Light blue background
    showVotes(root, frame1)
