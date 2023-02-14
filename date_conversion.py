from tkinter import *
from tkcalendar import DateEntry
import nepali_datetime
from bikram import samwat
from tkinter import messagebox
import datetime


def convert_to_nepali_date(date):
    while date <= datetime.date.today():
        try:
            ad_to_bs = samwat.from_ad(date)
            nepali_date = nepali_datetime.date(ad_to_bs.year, ad_to_bs.month, ad_to_bs.day).strftime('%K-%n-%D (%K %N %G)')
            return nepali_date
        except:
            return "Invalid date format. Use YYYY-MM-DD."
    return "date_greater_than_today_date"

    
def history_save(birth, nepali_date):
    with open("history/conversion_history.txt", "a") as file:
        file.write(f"{birth} -> {nepali_date}\n")

def show_history():
    master = Tk()
    text_widget = Text(master, height=60, width=60)

    scroll_bar = Scrollbar(master)

    scroll_bar.pack(side=RIGHT)

    text_widget.pack(side=LEFT)
    file_status = check_file()
    if file_status == True:
        with open("history/conversion_history.txt", "r") as f:
            text_widget.insert(END, f.read())
    else:
        text_widget.insert(END, 'Nothing to show')
    
def check_file():
    import os
    if os.stat('history/conversion_history.txt').st_size > 0:
        return True
    else:
        return False

def clear_history():
    file = open("history/conversion_history.txt","r+")
    file.truncate(0)
    file.close()
    messagebox.showinfo('Success', 'History has been clear')
        

class main():
    def __init__(self, root):
        self.root = root
        self.root.title("English to Nepali DOB")
        self.root.geometry("300x500")
        self.root.config(bg='black')

        # date entry
        Label(root, text="English to Nepali Date Convertor", bg='black', fg='white', font=('times_new_roman 12 bold')).place(x=10, y=10)
        Label(root, text="Date of birth", bg='black', fg='white', font=('times_new_roman 11 bold')).place(x=10, y=50)
        self.birth_date = DateEntry(root, background='black', date_pattern='MM/DD/yyyy')
        self.birth_date.place(x=200, y=55)

        # Claculate button
        Button(root, text="Calculate", bg="#ff5d00", command=self.calculate).place(x=10, y=110, width=280)

        # main result frame
        result_frame = Frame(root, bg='#222426')
        result_frame.place(x=10, y=150, width=280, height=310)

        frame_1 = Frame(result_frame, bg='#222426', bd=1, relief=GROOVE)
        frame_1.place(x=0, y=0, width=280, height=160)
        Label(frame_1, text="Result", bg='#222426', fg='#ff5d00', font=('arial 11 bold')).place(x=90, y=10)
        

        self.result = Label(frame_1, text="YYYY MM DD", bg='#222426', fg='white', font=('arial 11 bold'))
        self.result.place(x=20, y=40)

        Button(frame_1, text="Show History", bg="#ff5d00", command=show_history).place(x=20, y=80, width=200)
        Button(frame_1, text="Clear History", bg="#ff5d00", command=clear_history).place(x=20, y=120, width=200)

        

    def calculate(self):
        nepali_date = convert_to_nepali_date(self.birth_date.get_date())
        if nepali_date == 'date_greater_than_today_date':
            messagebox.showinfo('Error', 'Date should be less than today date')
        else:
            self.result.config(text=nepali_date)
            history_save(self.birth_date.get_date(),nepali_date)


root = Tk()
obj = main(root)
mainloop()