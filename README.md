# Google-API-Sheet

Simple Python Flask API with Google Sheets

Summarizes

Calling from google sheets api to refference the available data in a spreasheet.  

Prerequisites

Have a google sheet created and available to share
1. Click on the share button
2. Click on shareable link 

Create your virutal enviroment

Open Anaconda
1. Click on the enviroments
2. Create a new enviroment
3. Name this new enviroment: "GoogleSheetsFlaskAPI"

Create a folder under the same name as the new enviroment
Open the folder in the Jupyer Lab

Type this in the terminal to activate the enviroment: 
- Type: conda activate GoogleSheetsFlaskAPI 

Installation

- Pip install pandas
- Pip install Flask
- Pip install Flask-RESTful

Import Google Sheet, Convert to a List of Objects

1. Go to the sheet and copy the share link
2. Create a new python file
- naming after FlaskApi Server.py
3. import pandas as pd
- Place "sheet_id" = 'Spreadsheet_ID'
- df= pd.read_csv(f'GooglesheetURL{sheet_id}/export?formart=csv")
4. Print statement 
5. Run the python script 
- Now you are able to see the table within the terminal
  

