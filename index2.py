from tkinter import *
import tkinter as tk
from opencage.geocoder import OpenCageGeocode
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime, timedelta  # Add timedelta here
import requests
import pytz
from PIL import Image, ImageTk

root = Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False, False)

API_KEY = ''  # Replace with your OpenCage API key
WEATHER_API_KEY = ''  # Replace with your OpenWeatherMap API key

def getWeather():
    city = texfield.get()
    geocoder = OpenCageGeocode(API_KEY)
    results = geocoder.geocode(city)
    
    if results:
        location = results[0]
        lat = location['geometry']['lat']
        lng = location['geometry']['lng']
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=lng, lat=lat)
        timezone.config(text=result)
        
        # Get the region
        country = location['components']['country']
        continent = ""
        if country in ["Russia", "China", "India", "Japan", "Saudi Arabia", "Turkey", "South Korea", "Indonesia", "Pakistan", "Bangladesh", "Iran", "Thailand", "Myanmar", "Iraq", "Afghanistan"]:
            continent = "Asia"
        elif country in ["United States", "Canada", "Mexico", "Brazil", "Argentina", "Colombia", "Chile"]:
            continent = "Americas"
        elif country in ["France", "Germany", "United Kingdom", "Italy", "Spain", "Netherlands", "Greece", "Portugal", "Belgium", "Sweden", "Norway", "Denmark"]:
            continent = "Europe"
        elif country in ["Australia", "New Zealand"]:
            continent = "Oceania"
        elif country in ["South Africa", "Egypt", "Nigeria", "Kenya", "Ghana", "Ethiopia"]:
            continent = "Africa"
        
        long_lat.config(text=f"{lat:.2f}° N, {lng:.2f}° E")
        continent_label.config(text=continent)
        
        # Fetch weather data
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={WEATHER_API_KEY}&units=metric"
        json_data = requests.get(api).json()

        if 'main' in json_data:
            temp = json_data['main']['temp']
            humidity = json_data['main']['humidity']
            pressure = json_data['main']['pressure']
            wind = json_data['wind']['speed']
            description = json_data['weather'][0]['description']

            label1.config(text=f"Temperature: {temp}°C")
            label2.config(text=f"Humidity: {humidity}%")
            label3.config(text=f"Pressure: {pressure} hPa")
            label4.config(text=f"Wind Speed: {wind} m/s")
            label5.config(text=f"Description: {description}")
        else:
            messagebox.showerror("Error", "Weather data not found")
    else:
        messagebox.showerror("Error", "City not found")

    # days

    firstdayimage = json_data['weather'][0]['icon']
    photo1=ImageTk.PhotoImage(file=f"icon/00.png")
    firstimage.config(image=photo1)
    firstimage.image=photo1 


 

    seconddayimage = json_data['weather'][0]['icon']
    
    img= (Image.open(f"icon/02.png"))
    resized_image=img.resize((50,50))
    photo2=ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image=photo2

    thirddayimage = json_data['weather'][0]['icon']
    img= (Image.open(f"icon/03.png"))
    resized_image=img.resize((50,50))
    photo3=ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image=photo3
     
     
    fourthdayimage = json_data['weather'][0]['icon']
    img= (Image.open(f"icon/15.png"))
    resized_image=img.resize((50,50))
    photo4=ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image=photo4
     
    
    
    fifthdayimage = json_data['weather'][0]['icon']
    img= (Image.open(f"icon/09.png"))
    resized_image=img.resize((50,50))
    photo5=ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image=photo5
     
    
    sixdayimage = json_data['weather'][0]['icon']
    img= (Image.open(f"icon/12.png"))
    resized_image=img.resize((50,50))
    photo6=ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image=photo6


    img= (Image.open(f"icon/11.png"))
    resized_image=img.resize((50,50))
    photo7=ImageTk.PhotoImage(resized_image)
    sevenimage.config(image=photo7)
    sevenimage.image=photo7
     
     
    







 


     











    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second  = first + timedelta(days=1)  # Use timedelta
    day2.config(text=second.strftime("%A"))

    third  = first + timedelta(days=2)  # Use timedelta
    day3.config(text=third.strftime("%A"))

    fourth  = first + timedelta(days=3)  # Use timedelta
    day4.config(text=fourth.strftime("%A"))

    fifth = first + timedelta(days=4)  # Use timedelta
    day5.config(text=fifth.strftime("%A"))

    sixth= first + timedelta(days=5)  # Use timedelta
    day6.config(text=sixth.strftime("%A"))

    seventh = first + timedelta(days=6)  # Use timedelta
    day7.config(text=seventh.strftime("%A"))









# Ensure the image paths are correct and place the image code before root.mainloop()
image_icon = PhotoImage(file="image/logo.png")
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file="image/1.png")
Label(root, image=Round_box, bg="#57adff").place(x=30, y=110)

# Additional code for the Weather App
# Labels
label1 = Label(root, text="Temperature", font=("Helvetica", 11), fg="white", bg="#203243")
label1.place(x=50, y=120)

label2 = Label(root, text="Humidity", font=("Helvetica", 11), fg="white", bg="#203243")
label2.place(x=50, y=140)

label3 = Label(root, text="Pressure", font=("Helvetica", 11), fg="white", bg="#203243")
label3.place(x=50, y=160)

label4 = Label(root, text="Wind Speed", font=("Helvetica", 11), fg="white", bg="#203243")
label4.place(x=50, y=180)

label5 = Label(root, text="Description", font=("Helvetica", 11), fg="white", bg="#203243")
label5.place(x=50, y=200)

# Search box
Search_image = PhotoImage(file="image/4.png")
myimage = Label(image=Search_image, bg="#57adff")
myimage.place(x=270, y=120)

weat_image = PhotoImage(file="image/7.png")
weatherimage = Label(root, image=weat_image, bg="#203243")
weatherimage.place(x=290, y=127)

texfield = tk.Entry(root, justify='center', width=15, font=('poppins', 25, 'bold'), bg="#203243", border=0, fg="white")
texfield.place(x=370, y=130)
texfield.focus()

Search_icon = PhotoImage(file="image/6.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=getWeather)
myimage_icon.place(x=645, y=125)

bottom_frame = Frame(root, width=900, height=180, bg="#212120")
bottom_frame.pack(side=BOTTOM)

firstbox = PhotoImage(file="image/3.png")
secondbox = PhotoImage(file="image/2.png")
Label(bottom_frame, image=firstbox, bg="#212120").place(x=30, y=20)
Label(bottom_frame, image=secondbox, bg="#212120").place(x=300, y=30)
Label(bottom_frame, image=secondbox, bg="#212120").place(x=400, y=30)
Label(bottom_frame, image=secondbox, bg="#212120").place(x=500, y=30)
Label(bottom_frame, image=secondbox, bg="#212120").place(x=600, y=30)
Label(bottom_frame, image=secondbox, bg="#212120").place(x=700, y=30)
Label(bottom_frame, image=secondbox, bg="#212120").place(x=800, y=30)

# Clock to display time
clock = Label(root, font=("Helvetica", 30, 'bold'), fg="white", bg="#57adff")
clock.place(x=30, y=20)

# Timezone
timezone = Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
timezone.place(x=700, y=20)

long_lat = Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
long_lat.place(x=700, y=50)

# Continent Label
continent_label = Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
continent_label.place(x=700, y=80)

firstframe = Frame(root, width=230, height=132, bg="#282829")
firstframe.place(x=35, y=315)
day1 = Label(firstframe, font="arial 20", bg="#282829", fg="#fff")
day1.place(x=100, y=5)

firstimage=Label(firstframe,bg="#282829")
firstimage.place(x=1,y=15)



secondframe = Frame(root, width=70, height=115, bg="#282829")
secondframe.place(x=305, y=325)
day2 = Label(secondframe, bg="#282829", fg="#fff")
day2.place(x=10, y=5)

secondimage=Label(secondframe,bg="#282829")
secondimage.place(x=7,y=20)



thirdframe = Frame(root, width=70, height=115, bg="#282829")
thirdframe.place(x=405, y=325)
day3 = Label(thirdframe, bg="#282829", fg="#fff")
day3.place(x=10, y=5)

thirdimage=Label(thirdframe,bg="#282829")
thirdimage.place(x=7,y=20)

fourthframe = Frame(root, width=70, height=115, bg="#282829")
fourthframe.place(x=505, y=325)
day4 = Label(fourthframe, bg="#282829", fg="#fff")
day4.place(x=10, y=5)

fourthimage=Label(fourthframe,bg="#282829")
fourthimage.place(x=7,y=20)


fifthframe = Frame(root, width=70, height=115, bg="#282829")
fifthframe.place(x=605, y=325)
day5 = Label(fifthframe, bg="#282829", fg="#fff")
day5.place(x=10, y=5)

fifthimage=Label(fifthframe,bg="#282829")
fifthimage.place(x=7,y=20)


sixthframe = Frame(root, width=70, height=115, bg="#282829")
sixthframe.place(x=705, y=325)
day6 = Label(sixthframe, bg="#282829", fg="#fff")
day6.place(x=10, y=5)

sixthimage=Label(sixthframe,bg="#282829")
sixthimage.place(x=7,y=20)

sevenframe = Frame(root, width=70, height=115, bg="#282829")
sevenframe.place(x=805, y=325)
day7=Label(sevenframe, bg="#282829",fg="#fff")
day7.place(x=10,y=5 )
sevenimage=Label(sevenframe,bg="#282829")
sevenimage.place(x=7,y=20)





root.mainloop()