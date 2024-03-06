from flask import Flask
import datetime as dt
import time

app=Flask(__name__)
x=dt.datetime.now()
finaldate= x.strftime("%x")
finalday= x.strftime("%A")

# print(finalday)

@app.route("/")
def home():
    time.sleep(5)
    return "Hello, to the home page: Following are the endpoints /date, /day, /currency, /gdp, /population, /car, /medals"

@app.route("/date")
def date():
    time.sleep(5)
    return finaldate

@app.route("/day")
def day():
    time.sleep(5)
    return finalday

@app.route("/currency")
def curr():
    time.sleep(5)
    return "1 US Dollars = 83 Indian rupees"

@app.route("/gdp")
def gdp():
    time.sleep(5)
    return "160.06 lakh crores as per GDP report from 31st May, 2023"

@app.route("/population")
def popu():
    time.sleep(5)
    return "1.42 Billion as per the report from 2023"

@app.route("/car")
def car():
    time.sleep(5)
    return "Koenigsegg Regera with the top speed of 251 MPH is the best car in the world. Period!!!" 

@app.route("/medals")
def medals():
    time.sleep(5)
    return "Indian shooters won 7 Gold medals at Hangzhou 2023 & a total of 111 medals at Asian para Games 2023."




if __name__=="__main__":
    app.run(debug=True)