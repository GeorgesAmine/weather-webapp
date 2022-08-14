import requests
import config
from flask import Flask, request, render_template

app = Flask(__name__)



@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
        city = request.form.to_dict()['city']
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={config.API_KEY}'
        response = requests.get(url=api_url, params={'units':'metric'}).json()
        return render_template('index.html',response=response)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)

