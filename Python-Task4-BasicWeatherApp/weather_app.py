
import tkinter as tk
from tkinter import messagebox
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    if not API_KEY:
        messagebox.showerror("API Error", "API key not found in .env file.")
        return

    result_label.config(text="Fetching weather...", fg="#2563EB")
    root.update_idletasks()

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            BASE_URL, params=params, timeout=10
        )

        if response.status_code == 404:
            messagebox.showerror("Error", "City not found.")
            result_label.config(text="")
            return

        if response.status_code == 401:
            messagebox.showerror(
                "API Error",
                "API key is not active yet. Please try later."
            )
            result_label.config(text="")
            return

        response.raise_for_status()
        data = response.json()

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"].title()
        wind_speed = data["wind"]["speed"]
        city_name = data["name"]

        result_label.config(
            text=(
                f"{city_name}\n"
                f"{temperature:.1f} °C\n"
                f"{condition}\n\n"
                f"Feels Like: {feels_like:.1f} °C\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s"
            ),
            fg="#FFFFFF"
        )

    except requests.exceptions.Timeout:
        messagebox.showerror("Error", "Request timed out.")

    except requests.exceptions.ConnectionError:
        messagebox.showerror("Error", "Check your internet connection.")

    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Unable to fetch weather data.")

    except (KeyError, IndexError, ValueError):
        messagebox.showerror("Error", "Unexpected weather data received.")


# Main Window
root = tk.Tk()
root.title("Basic Weather App")
root.geometry("420x520")
root.resizable(False, False)
root.configure(bg="#14243B")

title = tk.Label(
    root,
    text="WEATHER APP",
    font=("Arial", 23, "bold"),
    bg="#14243B",
    fg="white"
)
title.pack(pady=(35, 8))

subtitle = tk.Label(
    root,
    text="Check current weather of any city",
    font=("Arial", 10),
    bg="#14243B",
    fg="#CBD5E1"
)
subtitle.pack(pady=5)

city_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center",
    width=25
)
city_entry.pack(pady=25, ipady=9)
city_entry.insert(0, "Enter city name")

search_button = tk.Button(
    root,
    text="GET WEATHER",
    font=("Arial", 12, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    cursor="hand2",
    command=get_weather
)
search_button.pack(ipadx=25, ipady=9)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 13),
    bg="#14243B",
    fg="white",
    justify="center"
)
result_label.pack(pady=35)

footer = tk.Label(
    root,
    text="Powered by OpenWeatherMap API",
    font=("Arial", 9),
    bg="#14243B",
    fg="#94A3B8"
)
footer.pack(side="bottom", pady=15)

root.mainloop()
