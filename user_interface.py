from tkinter import *
from tkcalendar import *
from datetime import datetime


window = Tk()
window.title("Flight Search")
window.config(padx=0, pady=0)

canvas = Canvas(window, bg="white", height=300, width=300)
logo_img = PhotoImage(file="logo.gif")
canvas.create_image(200, 200, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3)


def save_location_city():
    origin_city = origin_city_entry.get()
    print(origin_city)


def save_destination_city():
    destination_city = destination_city_entry.get()
    print(destination_city)


def save_date():
    date_from = calendar.get_date()
    out_date = datetime.strptime(date_from, "%m/%d/%y")
    print(out_date.strftime("%d/%m/%y"))
    print(type(out_date))

# Labels

origin_city_label = Label(text="Enter your location city:")
origin_city_label.grid(row=1, column=0)
destination_city_label = Label(text="Enter your destination city:")
destination_city_label.grid(row=2, column=0)
date_from_label = Label(text="Enter start day of flight: ")
date_from_label.grid(row=3, column=0)

# Entries

origin_city_entry = Entry(width=21)
origin_city_entry.grid(row=1, column=1)
origin_city_entry.focus()
destination_city_entry = Entry(width=21)
destination_city_entry.grid(row=2, column=1)
# date_from_entry = Entry(width=21)
# date_from_entry.grid(row=3, column=1)
calendar = Calendar(window, selectmode='day', year=2022, month=9, day=14)
calendar.grid(row=3, column=1)


def grad_date():
    date.config(text="Selected Date is: " + calendar.get_date())


date = Label(window, text="")
date.grid(row=3, column=3)

# Buttons

location_city_button = Button(text="Add location city", width=13, command=save_location_city)
location_city_button.grid(row=1, column=3)
destination_city_button = Button(text="Add destination city", width=13, command=save_destination_city)
destination_city_button.grid(row=2, column=3)
out_date_button = Button(text="Get Date", command=save_date)
out_date_button.grid(row=3, column=3)
search_button = Button(text="Search flights", width=13)
search_button.grid(row=4, column=2, columnspan=2)

window.mainloop()
