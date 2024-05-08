import tkinter as tk
from tkinter import ttk
import requests

def get_weather(event=None):
    city = entry.get().strip()
    if not city:
        weather_label.config(text="Please enter a city name.")
        return
    
    try:
        api_key = "bd5e378503939ddaee76f12ad7a97608"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        weather_data = response.json()
        
        if response.status_code == 200:
            description = weather_data["weather"][0]["description"].capitalize()
            temperature = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            wind_speed = weather_data["wind"]["speed"]
            weather_label.config(text=f"Weather: {description}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s")
        else:
            weather_label.config(text="City not found. Please try again.")
    except requests.exceptions.RequestException as e:
        weather_label.config(text="Error: Unable to connect to the server. Please check your internet connection.")

root = tk.Tk()
root.title("ClimaSearch")
root.geometry("400x200")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", font=("Helvetica", 12), background="#007bff", foreground="white", borderwidth=0)
style.map("TButton", background=[("active", "#0056b3")])
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TLabel", font=("Helvetica", 16, "bold"))

frame = ttk.Frame(root, padding="20")
frame.pack(expand=True)

label_title = ttk.Label(frame, text="ClimaSearch", style="TLabel")
label_title.grid(row=0, column=0, columnspan=2, pady=(0, 10))

entry = ttk.Entry(frame, style="TEntry", width=30)
entry.grid(row=1, column=0, padx=5, pady=5)
entry.bind("<Return>", get_weather)

button = ttk.Button(frame, text="Get Weather", command=get_weather, style="TButton")
button.grid(row=1, column=1, padx=5, pady=5)

weather_label = ttk.Label(frame, font=("Helvetica", 12), justify="left")
weather_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

root.mainloop()