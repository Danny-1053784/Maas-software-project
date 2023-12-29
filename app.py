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

    # Get the search query from the request query parameters
    query = request.args.get("query")

    if query:
        # Filter the data based on the search query
        filtered_data = []
        for row in data:
            if query.lower() in row["WAARNEMINGDATUM"].lower():
                filtered_data.append(row)
        
        # Update the total number of pages based on the filtered data
        total_pages = (len(filtered_data) + items_per_page - 1) // items_per_page
        
        # Get the data for the current page
        current_data = filtered_data[start_index:end_index]
    else:
        # Calculate the total number of pages
        total_pages = (len(data) + items_per_page - 1) // items_per_page
        
        # Get the data for the current page
        current_data = data[start_index:end_index]


    # Render the template with the data and pagination information
    return render_template('index.html', data=current_data, page=page, total_pages=total_pages, query=query)




if __name__ == '__main__':
    app.run(debug=True)