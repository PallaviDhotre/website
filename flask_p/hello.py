from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello():
    return "<h1 style='text-align:center;'>Hi, Adi! <br>This is a REST service :) <br> I used Flask to do this. <br> Thank you so much for everything! :)</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)

