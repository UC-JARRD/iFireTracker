import logging
import load_data
import process_data
import create_map

# Configure logging
logging.basicConfig(filename='./logs/main_execution.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    logging.info("Starting main function...")

    try:
        # Load the data
        logging.info("Loading data...")
        station_fire_risk, land_use_data = load_data.load_data()
        logging.info('Data loaded successfully.')
        print('Data loaded successfully.')

        # Process the data
        logging.info("Processing data...")
        fire_risk_per_land_use_area = process_data.process_data(station_fire_risk, land_use_data)
        logging.info('Data processed successfully.')
        print('Data processed successfully.')

        # Save fire_risk_per_polygon DataFrame to CSV
        logging.info("Saving data...")
        fire_risk_per_land_use_area.to_csv('./data/output/csv/fire_risk_per_land_use_area.csv', index=False)
        logging.info('Data saved to "./data/output/csv/fire_risk_per_land_use_area.csv" successfully.')
        print('Data saved to "./data/output/csv/fire_risk_per_land_use_area.csv" successfully.')

        # Create the map
        logging.info("Creating map...")
        create_map.create_map(fire_risk_per_land_use_area)
        logging.info('Map created successfully.')
        print('Map created successfully.')

    except Exception as e:
        logging.error(f"Error in main function: {str(e)}")
        raise

if __name__ == "__main__":
    main()