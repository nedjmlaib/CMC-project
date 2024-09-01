# Excel File Processing Project

This project involves reading multiple Excel files from a specified folder, processing the data to compute the total duration per user and project, and exporting the results to a new Excel file. The script is written in Python and utilizes the pandas library for data manipulation.

## Overview

The purpose of this project is to automate the processing of time-tracking data stored in multiple Excel files. The script performs the following tasks:

1. Reads all Excel files from a specified input folder.
2. Groups the data by user and project.
3. Calculates the total duration in decimal hours and converts it to the number of workdays (assuming a 7-hour workday).
4. Exports the processed data to an output Excel file.

## Folder Structure

The project folder structure is as follows:

CMC-Project/excel_files/ 

  input/ # Folder containing input Excel files 

  output/ # Folder where the output Excel file will be saved 

  InnovLabReportScript.py # Python script for processing data

  README.md # Project documentation

## Requirements

- Python 3.x
- pandas library

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/CMC_Project.git
   cd CMC_Project
   
2. **Install the required Python packages:**
   
    You can install the required packages using pip:
     ```bash
     pip install pandas
     
## Usage

1. Place your Excel files in the excel_files/input folder.
2. Run the Python script to process the data:

  ```bash
  python script/process_data.py
  ```

3. Check the output in the excel_files/output folder. The result will be saved as Result.xlsx.
