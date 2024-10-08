# Facebook Ads Analysis with Python, SQL and Power Bi

This project is designed to extract, clean, and analyze Facebook Ads data for Acala Skin, one of my e-commerce brands. The process includes extracting data from the Facebook Marketing API, cleaning the data in a Jupyter Notebook, exporting it to a PostgreSQL database, and creating a Power BI report that updates daily with the new data.

![image](https://github.com/user-attachments/assets/4394c829-f22e-45a9-acae-fe53ea4818f1)



## Link to the Power Bi Dashboard
https://app.powerbi.com/view?r=eyJrIjoiZDhkNGYwNWMtMWQyOS00NzIwLWI2ZTgtOTFkMjYzNjhmYjk1IiwidCI6IjMxZDdlMmE1LWJkZDgtNDE0ZS05ZTk3LWJlYTk5OGViZGZlMSIsImMiOjN9

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Data Pipeline](#data-pipeline)
- [Power BI Report](#power-bi-report)
- [Contact](#contact)

## Overview

This project aims to provide a comprehensive analysis of Facebook Ads performance by leveraging various tools and technologies. The data is extracted using Python, cleaned in a Jupyter Notebook, stored in a PostgreSQL database, and visualized in a Power BI report that updates daily.

## Features

- **Data Extraction:** Extracts Facebook Ads data using the Facebook Marketing API.
- **Data Cleaning:** Cleans and processes the data in a Jupyter Notebook.
- **Data Storage:** Stores the cleaned data in a PostgreSQL database.
- **Data Visualization:** Creates a Power BI report that updates daily with the latest data.
- **Automation:** Automates the data extraction and cleaning process using Windows Task Manager.

## Installation

### Prerequisites

- Python 3.7 or higher
- PostgreSQL
- pgAdmin 4
- Visual Studio Code
- Jupyter Notebook
- Power BI Desktop
- Windows Task Manager (for scheduling tasks)

### Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/facebook-ads-analysis.git
    cd facebook-ads-analysis
    ```

3. **Set up the PostgreSQL database:**
    - Create a new PostgreSQL database using pgAdmin.

4. **Configure the Facebook Marketing API:**
    - Obtain your access token from the Facebook Developer portal.
    - Update the API credentials in `facebook_api_config.py`.

## Usage

1. **Run the data extraction, cleaning, and export script:**
    ```sh
    python runscript.py
    ```

2. **Open the Power BI report:**
    - Ensure the Power BI report is connected to your PostgreSQL database.
    - Refresh the report to load the latest data.

3. **Automate the process:**
    - Schedule the `runscript.bat` file to run daily using Windows Task Manager.

## Project Structure

```plaintext
facebook-ads-analysis/
│
├── data/
│   ├── facebook_ads_data.csv/
│   ├── facebook_ads_data_clean/
│
├── notebooks/
│   ├── Facebook_Ads_Data.ipynb
│
├── scripts/
│   ├── runscript.py
│   ├── runscript.bat
│
├── power_bi/
│   ├── report.pbix
│
└── README.md
```
## Data Pipeline

1. **Data Extraction and Cleaning:**
    - The `Facebook_Ads_Data.ipynb` notebook extracts data from the Facebook Marketing API and cleans it.

2. **Data Export:**
    - The notebook exports the cleaned data to the PostgreSQL database.

3. **Automation:**
    - The `runscript.py` script runs the notebook, and `runscript.bat` is used to automate this process with Windows Task Manager.

4. **Data Visualization:**
    - The Power BI report (`report.pbix`) connects to the PostgreSQL database and visualizes the data.

## Power BI Report

The Power BI report provides various insights into the performance of Facebook Ads, including metrics such as impressions, clicks, conversions, and ROAS (Return on Ad Spend). The report is designed to update daily with the latest data from the PostgreSQL database.

## Contact

For any questions or inquiries, please contact:

- **Name:** Eduardo Geovany Rodríguez González
- **Linkedin:** https://www.linkedin.com/in/geovany-rodriguez/
- **Email:** gio_rdz.27@hotmail.com
- **GitHub:** https://github.com/geovanyrdz

