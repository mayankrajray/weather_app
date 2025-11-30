# weather_app 🌤️

A simple web application to fetch and display weather information for any location worldwide.

## 🔎 Overview  
This project allows users to enter a city name (or use geolocation) and retrieves current weather data (and optionally forecast) using a weather API.  
The UI is built with HTML, CSS and JavaScript.  

## ✅ Features  
- Search weather by city name  
- Option to use browser geolocation (if you give permission)  
- Displays key weather information: temperature, humidity, wind, etc.  
- Clean and responsive UI — works on desktop and mobile  

*(You can expand this list depending on what your app actually supports — e.g. forecast view, error-handling, history search, etc.)*

## 🛠️ Technologies Used  
- HTML5  
- CSS3  
- JavaScript (ES6)  
- Weather API: (e.g. OpenWeatherMap or whichever API you used)  

## 🚀 Getting Started  

### Prerequisites  
- A modern web browser (Chrome, Firefox, Edge, Safari)  
- (Optional) An API key from your weather data provider  

### Installation & Usage  
1. Clone the repository:  
   ```bash
   git clone https://github.com/mayankrajray/weather_app.git
    ```

2. Navigate to the project folder:
```bash
cd weather_app
```
- Open index.html (or appropriate main file) in your browser.

- Enter a city name (or allow geolocation) and enjoy the weather information.

## 📁 Project Structure
```bash
/weather_app
  ├── index.html         ← Main HTML file  
  ├── style.css          ← Stylesheet  
  ├── script.js          ← JavaScript logic to fetch & display weather data  
  └── README.md          ← This file  
```

(Modify paths/names to match your actual project structure — I used generic names.)

## 🔑 API Key Setup

If your weather API requires an API key:

Get a key from your API provider (e.g. OpenWeatherMap)

Insert the key in your JavaScript (e.g. const apiKey = "YOUR_KEY_HERE")

Save changes and reload the app

## 📄 License

- This project is open-source. Use it, modify it, and redistribute as you like.

## 🙏 Credits

- Inspired by many weather-app templates and projects using vanilla JS + weather APIs.