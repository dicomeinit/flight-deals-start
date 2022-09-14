from tkinter import *

import tkcalendar
from tkcalendar import *

window = Tk()
window.title("Flight Search")
window.config(padx=0, pady=0)

canvas = Canvas(window, bg="white", height=300, width=300)
logo_img = PhotoImage(file="logo.gif")
canvas.create_image(200, 200, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3)

#Labels

origin_city_label = Label(text="Enter your location city:")
origin_city_label.grid(row=1, column=0)
destination_city_label = Label(text="Enter your destination city:")
destination_city_label.grid(row=2, column=0)
date_from_label = Label(text="Enter start day of flight: ")
date_from_label.grid(row=3, column=0)


#Entries

origin_city_entry = Entry(width=21)
origin_city_entry.grid(row=1, column=1)
destination_city_entry = Entry(width=21)
destination_city_entry.grid(row=2, column=1)
# Add Calendar
calendar = Calendar(window, selectmode='day',
               year=2022, month=9,
               day=14)

calendar.grid(row=3, column=1)


def grad_date():
    date.config(text="Selected Date is: " + calendar.get_date())


# Add Button and Label
Button(window, text="Get Date",
       command=grad_date).grid(row=3, column=2)

date = Label(window, text="")
date.grid(row=3, column=3)

# Buttons

location_city_button = Button(text="Add location city", width=13)
location_city_button.grid(row=1, column=3)
destination_city_button = Button(text="Add destination city", width=13)
destination_city_button.grid(row=2, column=3)





window.mainloop()

