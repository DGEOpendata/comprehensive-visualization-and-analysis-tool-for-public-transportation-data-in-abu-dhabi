python
import pandas as pd
import folium
from flask import Flask, render_template

# Load the dataset
df = pd.read_csv('Abu_Dhabi_Public_Transportation_Usage.csv')

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    # Create a map centered around Abu Dhabi
    abu_dhabi_map = folium.Map(location=[24.4539, 54.3773], zoom_start=12)

    # Add bus stops to the map
    for index, row in df.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"Stop: {row['stop_name']}<br>Route: {row['route']}",
            tooltip=row['stop_name']
        ).add_to(abu_dhabi_map)

    # Save the map as an HTML file
    abu_dhabi_map.save('templates/map.html')
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)
