import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import os

def get_weather(city_name, Key):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "Key": 'api_key',
        "q": city_name,
        "aqi": "no"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        return {"error": f"Request error occurred: {req_err}"}
    except Exception as err:
        return {"error": f"Unexpected error: {err}"}

def display_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name!")
        return

    weather_data = get_weather(city, Key)
    if "error" in weather_data:
        messagebox.showerror("Error", weather_data["error"])
    elif "current" not in weather_data:
        messagebox.showerror("Error", "Unable to fetch weather data.")
    else:
        location = weather_data['location']['name']
        country = weather_data['location']['country']
        temp = weather_data['current']['temp_c']
        condition = weather_data['current']['condition']['text']

        print("Condition:", condition)

        location_label.config(text=f"{location}, {country}")
        temperature_label.config(text=f"{temp}°C")
        condition_label.config(text=condition)

        if condition.lower() == "sunny":
            icon_file = r"Icon Path"
        elif condition.lower() == "cloudy":
            icon_file = r"Icon Path"
        elif condition.lower() == "rainy":
            icon_file = r"Icon Path"
        elif condition.lower() == "thunderstorm":
            icon_file = r"Icon Path"
        else:
            icon_file = r"Icon Path"

        try:
            weather_icon = Image.open(icon_file).resize((100, 100), Image.Resampling.LANCZOS)
            weather_icon = ImageTk.PhotoImage(weather_icon)
            icon_label.config(image=weather_icon)
            icon_label.image = weather_icon
        except Exception as e:
            print(f"Error loading icon: {e}") 
            icon_label.config(image="", text="No icon available")

Key = "api_key"

root = tk.Tk()
root.title("Weather App")
root.geometry("500x500")
root.configure(bg="#87CEEB")

title_label = tk.Label(root, text="Weather App", font=("Helvetica", 24, "bold"), bg="#87CEEB", fg="white")
title_label.pack(pady=20)

city_label = tk.Label(root, text="Enter City Name:", font=("Helvetica", 14), bg="#87CEEB", fg="white")
city_label.pack(pady=5)

city_entry = tk.Entry(root, width=30, font=("Helvetica", 14))
city_entry.pack(pady=5)

submit_button = tk.Button(root, text="Get Weather", font=("Helvetica", 14), bg="#4682B4", fg="white", command=display_weather)
submit_button.pack(pady=10)

icon_label = tk.Label(root, bg="#87CEEB")
icon_label.pack(pady=10)

location_label = tk.Label(root, text="", font=("Helvetica", 18, "bold"), bg="#87CEEB", fg="white")
location_label.pack(pady=5)

temperature_label = tk.Label(root, text="", font=("Helvetica", 32, "bold"), bg="#87CEEB", fg="white")
temperature_label.pack(pady=5)

condition_label = tk.Label(root, text="", font=("Helvetica", 16), bg="#87CEEB", fg="white")
condition_label.pack(pady=5)

root.mainloop()
