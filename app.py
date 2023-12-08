from flask import Flask, render_template, request
import csv
from datetime import datetime 

app = Flask(__name__)

@app.route('/')
def index():
    # Read the CSV file
    with open('deMaas.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        data = [row for row in reader]

    # Get the page number from the request query parameters
    page = int(request.args.get('page', 1))
    items_per_page = 200
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page

    # Get the data for the current page
    current_data = data[start_index:end_index]

    # Calculate the total number of pages
    total_pages = (len(data) + items_per_page - 1) // items_per_page

    # Render the template with the data and pagination information
    return render_template('index.html', data=current_data, page=page, total_pages=total_pages)



def search(data): 
    query_date = request.form.get('WAARNEMINGSDATUM')
    formatted_date = datetime.strptime(query_date, "%Y-%m-%d").date() if query_date else None

    results = [date_data for date_data in data if
               not formatted_date or datetime.strptime(date_data["date"], "%Y-%m-%d").date() == formatted_date]

    return render_template('index.html', data=results, query_date=query_date)


if __name__ == '__main__':
    app.run(debug=True)