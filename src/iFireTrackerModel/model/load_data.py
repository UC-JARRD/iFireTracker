import logging
import pandas as pd

LOG_PATH = './logs/main_execution.log'
INPUT_WEATHER_STATIONS_PATH = './data/input/canterbury_weather_stations.csv'
INPUT_FIRE_RISK_PATH = './data/input/fire_risk.csv'
MERGED_LAND_USE_STATIONS_PATH = './data/input/merged/land_use_areas_per_station.csv'

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(LOG_PATH)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)


def load_data():
    logging.info("[load_data.py] Loading weather station data...")
    # Load weather station data
    try:
        weather_stations_coords = pd.read_csv(INPUT_WEATHER_STATIONS_PATH) # coordinates of each station
        fire_risk = pd.read_csv(INPUT_FIRE_RISK_PATH) # fire risk at each station (will come from database eventually)
        logging.info("[load_data.py] Weather station data loaded successfully.")
    except FileNotFoundError:
        logging.error("[load_data.py] Failed to load weather station data. File not found.")
        raise

    logging.info("[load_data.py] Merging weather station data...")
    # Merge the datasets on the 'station_name' column
    try:
        station_fire_risk = pd.merge(weather_stations_coords, fire_risk, on='station_name')
        logging.info("[load_data.py] Datasets merged successfully.")
    except Exception as e:
        logging.error(f"[load_data.py] Failed to merge datasets: {str(e)}")
        raise

    logging.info("[load_data.py] Loading land use data...")
    # Load land_use_data
    try:
        land_use_data = pd.read_csv(MERGED_LAND_USE_STATIONS_PATH)
        logging.info("[load_data.py] Land use data loaded successfully.")
    except FileNotFoundError:
        logging.error("[load_data.py] Failed to load land use data. File not found.")
        raise

    return station_fire_risk, land_use_data
