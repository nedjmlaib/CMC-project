#read one excel file from a defiened folder path
#store in dataframe
#create a new dataframe with full duration column
#find the right formula 

import pandas as pd
import os

# Define the folder path containing Excel files
input_path = 'Downloads/CMC_Project/excel_files/input'
output_path = 'Downloads/CMC_Project/excel_files/output'

# List all files in the folder
files = os.listdir(input_path)

# Read Excel files 
for file in files:
    file_path = os.path.join(input_path, file)
    
    # Read the Excel file into a DataFrame
    input_df = pd.read_excel(file_path)
    
    #creating an empty dataFrame
    reportOutput = pd.DataFrame()
    
    grouped = input_df.groupby(['Utilisateur', 'Projet'], as_index=False)['Durée (décimal)'].sum()
    
    # Create new columns in the output DataFrame
    reportOutput['Utilisateur'] = grouped['Utilisateur']
    reportOutput['Projet'] = grouped['Projet']
    reportOutput['Durée total (décimal)'] = grouped['Durée (décimal)']
    reportOutput['Nombre de Jour (1j->7H)'] = reportOutput['Durée total (décimal)'] / 7
    
    
reportOutput.to_excel(os.path.join(output_path, 'Result.xlsx'), index=False)