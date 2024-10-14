import os
import sys
import logging

# Configure logging
logging.basicConfig(
    filename='dbt_process.log',  # Log file name
    level=logging.INFO,           # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

# Example of logging messages
def main():
    logging.info("Starting the DBT process...")
    
    try:
        # Your DBT commands
        logging.info("Running DBT models...")
        os.system('dbt run')

        logging.info("Running DBT tests...")
        os.system('dbt test')

        logging.info("Generating DBT documentation...")
        os.system('dbt docs generate')

        logging.info("Serving DBT documentation...")
        os.system('dbt docs serve')
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    logging.info("DBT process completed.")

if __name__ == "__main__":
    main()
