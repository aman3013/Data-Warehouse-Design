# Data-Warehouse-Design

Welcome to the Ethiopian Medical Business Data Warehouse project! This repository contains code for scraping, processing, and analyzing data related to Ethiopian medical businesses, along with object detection on images using YOLO, and exposing the data through a FastAPI application.


## Overview
The goal of this project is to build a comprehensive data warehouse that collects, processes, and stores data scraped from Ethiopian medical-related Telegram channels. The data is cleaned, transformed, and made available for analysis, including object detection on images using YOLOv5. The processed data is then exposed via a FastAPI-powered RESTful API for easy access.

## Features
- **Telegram Scraping**: Automatically scrape data (messages, images, metadata) from specific Telegram channels.
- **Data Processing**: Clean, standardize, and transform the scraped data using DBT.
- **Object Detection**: Detect objects in images using YOLOv5, with results saved to a PostgreSQL database.
- **REST API**: Access data via a FastAPI RESTful API for further analysis or integration with other systems.
- **PostgreSQL Data Warehouse**: Centralized storage for all scraped data and processing results.

## Technologies Used
- **Python**: Core language used for scripting and API development.
- **Telethon**: Library for scraping data from Telegram channels.
- **BeautifulSoup** & **Selenium**: Tools for web scraping and interacting with Telegram channels.
- **YOLOv5**: For object detection in scraped images.
- **PostgreSQL**: Relational database used as a data warehouse.
- **DBT**: For transforming raw data into a more usable format.
- **FastAPI**: Framework for building a RESTful API to serve the processed data.
- **Docker**: For containerizing the FastAPI application.

## Project Structure
```bash
.
├── data/               # Raw and processed data
├── yolov5/             # YOLOv5 model files
├── fastapi_app/        # FastAPI application code
├── dbt_project/        # DBT transformation scripts
├── scraping/           # Scripts for scraping Telegram data
├── object_detection/    # Object detection scripts using YOLOv5
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
## Technical Stack

- Python: For scripting and data processing
- Telegram API: For data extraction from Telegram channels
- YOLO: For object detection in images
- DBT: For data transformation
- PostgreSQL: As the relational DBMS for the data warehouse
- FastAPI: For exposing the collected data through an API

## Setup and Installation

1. Clone the repository:
git clone https://github.com/your-username/ethiopian-medical-data-warehouse.git
cd ethiopian-medical-data-warehouse
2. Install required packages:
pip install -r requirements.txt
3. Set up Telegram API credentials (instructions in `scraping/README.md`)

## Usage

### 1. Data Scraping and Collection

Run the scraping script:
python scraping/telegram_scraper.py

### 2. Data Cleaning and Transformation

Execute the DBT models:
cd dbt_project
dbt run
dbt test
dbt docs generate
dbt docs serve
### 3. Object Detection

Process images with YOLO:
python object_detection/yolo_processor.py
### 4. FastAPI Development

Start the FastAPI server:
uvicorn main:app --reload
## Data Sources

- Telegram Channels:
  - https://t.me/DoctorsET
  - Chemed Telegram Channel
  - https://t.me/lobelia4cosmetics
  - https://t.me/yetenaweg
  - https://t.me/EAHCI
  - Additional channels from https://et.tgstat.com/medicine


## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

