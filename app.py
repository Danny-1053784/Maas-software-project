from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def index():
    # Read the CSV file
    with open('deMaas.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        data = [row for row in reader]
        

    # Render the template with the data
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)