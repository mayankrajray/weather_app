from flask import Flask, render_template, request, flash
import requests # pip install requests
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Bharat123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Config
class WeatherData(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    city = db.Column(db.String(50),nullable=False)
    max_temp = db.Column(db.Integer, nullable=False)
    min_temp = db.Column(db.Integer,nullable=False)
    weather = db.Column(db.Text, nullable=False)

    num = 0

    def __init__(self, c, min_temp, max_temp, w):
        self.num = 1+ WeatherData.num
        self.city = c
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.weather = w
    


with app.app_context():
    db.create_all()


@app.route('/', methods = ['GET', 'POST'])
def weather_details():
    if request.method == 'POST':
        city_name = request.form['name']

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=4743c03fb0f316a1c4df85ad570f3f0d'
        try:
            response = requests.get(url.format(city_name)).json()
            temp = response['main']['temp']
            weather = response['weather'][0]['description']
            min_temp = response['main']['temp_min']
            max_temp = response['main']['temp_max']+2
            icon = response['weather'][0]['icon']
            new_weather = WeatherData(city_name, max_temp, min_temp, weather)
            db.session.add(new_weather)
            db.session.commit()
            finalresponse = True
            return render_template('Home.html',temp=temp,weather=weather,min_temp=min_temp,max_temp=max_temp,icon=icon, city_name = city_name, finalresponse=finalresponse)
        except:
            flash('Enter a valid city', 'error')
            return render_template('Home.html')

        
    else:
        return render_template('Home.html')

@app.route('/About')
def about():
    return render_template('About.html')


if __name__ == '__main__':
    app.run(debug=True)