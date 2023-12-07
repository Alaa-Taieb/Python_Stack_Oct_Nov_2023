from flask import Flask , render_template , request, redirect , session
import requests

app = Flask(__name__)

app.secret_key = "ASDKJDHKJSdfn"

@app.route('/')
def index():

    request = requests.get("https://restcountries.com/v3.1/all?fields=name,flags")
    data = request.json()


    return render_template("index.html" , data = data)

@app.route('/get_flag' , methods = ['POST'])
def get_flag():
    data = request.form
    # {"country" : URL}
    session['image_url'] = data['country']
    return redirect("/display_flag")

@app.route('/display_flag')
def display_flag():
    
    return render_template("display_flag.html", url = session['image_url'])

@app.route('/site_2')
def site_2():
    request = requests.get("http://127.0.0.1:5000/")
    data = request.text

    return data

if __name__ == "__main__":
    app.run(debug=True , port = 5001)