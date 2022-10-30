import pandas as pd
from flask import Flask, render_template, request
import requests 
from flask_restful import Api, Resource
 
sheet_id = '1k6u2hOpVJ1__BGJnHbOR4ybQZHt-tBfJSF3yo5zgHFc'
df = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv')
# print (df) #print data table
records = df.to_dict(orient='records') 
# print(records) #print coverted data as a dictionary 

# instantiate new Flask Application Object
app = Flask(__name__)

# Top three channels in views in the USA
headings = ('Channel', 'Channel Type', 'Total Views(Till End Of The Week)')
data = (('Cocomelon - Nursery Rhymes', 'Education', '138,918,281,415'),
       ('MrBeast', 'Entertainment', '17,341,761,178'),
        ('Kids Diana Show', 'Entertainment', '81,460,839,462'))

#initialize API object for the Flask Application
api = Api(app)

#Routes - Search Pages
@app.route('/')
def home():
    return render_template('home.html')

#Routes - Region
@app.route('/region')
def region():
    return render_template('region.html', headings=headings, data=data)

#Routes - Content
@app.route('/content') 
def content():
    with open('textfile.txt', 'r') as f:
        return render_template('content.html', text=f.read()) 

# Routes - Testing Google Script API Call
# @app.route('/index')
# def index():
#     return render_template('Index.html')

#API Request
class All(Resource):
    def get(self):
        return records
    
class Channel(Resource):
    def get(self,value):
        return [obj for obj in records if obj['Channel'].lower().startswith(value.lower())]
    
class Country(Resource):
    def get(self,value):
        return [obj for obj in records if obj['Country'].lower().startswith(value.lower())]
    
class Channel_Type(Resource):
    def get(self,value):
        return next([obj for obj in records if obj['Channel Type'].lower().startswith(value.lower())])
    
#Register API Resources
#Uses the serach character to find the values from the google sheet 
api.add_resource(All,'/api/')
api.add_resource(Channel, '/api/channel/<string:value>')
api.add_resource(Country, '/api/country/<string:value>')
api.add_resource(Channel_Type, '/api/channeltype/<string:value>')

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)