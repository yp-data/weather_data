Weather Data Dashboard

Project Overview
----------------
This project fetches weather data from the OpenWeather API, stores it in a PostgreSQL database, and visualizes it using Power BI. The data retrieval is automated using a Python scheduler that runs every 5 minutes.

Features
--------
- Fetches current weather and 5-day forecast data for multiple cities.
- Stores data in a PostgreSQL database.
- Automates data retrieval using a Python scheduler.
- Provides data visualization in Power BI.
- Implements error handling for API requests.

Project Structure
-----------------
- OpenWeatherAPI.py  -> Fetches and stores weather data in PostgreSQL
- weather_analysis.py -> Processes and visualizes the data
- weather_dashboard.pbix -> Power BI dashboard
- sql_scripts/
  - create_db.sql -> Initializes the database
  - create_table.sql -> Creates required tables
- README.txt -> Project documentation

Setup Instructions
------------------
Prerequisites:
- Python 3.x
- PostgreSQL
- Power BI
- Required Python libraries:
  pip install requests pandas psycopg2 matplotlib seaborn

Database Setup:
1. Initialize the PostgreSQL database:
   psql -U postgres -f sql_scripts/create_db.sql
2. Create the required table:
   psql -U postgres -d weather_db -f sql_scripts/create_table.sql

API Key Configuration:
- Replace `API_KEY` in `OpenWeatherAPI.py` with your OpenWeather API key.

Running the Scripts
-------------------
Fetch Weather Data (manual mode):
  python OpenWeatherAPI.py manual

Automate Data Retrieval (scheduler mode):
  python OpenWeatherAPI.py

The script will continuously run every 5 minutes using Python's `time.sleep(300)` function.

Analyze Weather Data:
  python weather_analysis.py

Power BI Integration
--------------------
Connecting Power BI to PostgreSQL:
1. Open Power BI Desktop.
2. Click 'Get Data' -> 'PostgreSQL Database'.
3. Enter Server: `localhost`, Database: `weather_db`.
4. Click 'Load' to import the data.

Power BI Dashboard Visualizations:
- Current weather and 5-day forecast.
- Temperature and humidity trends.
- Forecast accuracy analysis.

Note: Due to API restrictions, only forecast data is available without a paid subscription.

Expected Output
---------------
- **Weather Data in PostgreSQL**: The database should contain current and forecasted weather data for multiple cities.
- **Power BI Dashboard**: A dynamic and interactive visualization displaying trends and insights from the fetched weather data.
- **Generated Charts**: Temperature trends for different cities saved in the designated output folder.

Troubleshooting
---------------
1. **Database Connection Issues**:
   - Ensure PostgreSQL is running.
   - Verify database credentials in `OpenWeatherAPI.py`.
   
2. **API Request Errors**:
   - Check if the API key is valid and has the necessary access.
   - Ensure internet connectivity.
   
3. **Scheduler Not Running**:
   - Confirm the script is being executed and running in a loop.
   - Run `python OpenWeatherAPI.py manual` to check for immediate errors.

Design Approach
---------------
- **Data Accuracy**: Uses a database to store historical data for trend analysis.
- **Automation**: Uses a Python scheduler for continuous data updates.
- **Error Handling**: Handles network failures and invalid API responses.
- **Scalability**: Can fetch weather data for additional cities.

Future Improvements
-------------------
- Add support for historical weather data.
- Implement a web interface for real-time data visualization.
- Optimize database queries for better performance.

Need Help?
----------
For questions or issues, feel free to reach out!