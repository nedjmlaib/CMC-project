#read one excel file from a defiened folder path
#store in dataframe
#create a new dataframe with full duration column
#find the right formula 

import pandas as pd
import os

# Define the folder path containing Excel files
folder_path = 'Downloads\CMC_Project\excel_files\input'

# List all files in the folder
files = os.listdir(folder_path)

# Read Excel files 
for file in files:
    file_path = os.path.join(folder_path, file)
    
    # Read the Excel file into a DataFrame
    input = pd.read_excel(file_path)
    
    #creating an empty dataFrame
    reportOutput = pd.DataFrame()
    
    reportOutput['Durée total (décimal)'] = input.groupby(['Utilisateur', 'Projet'])['Durée (décimal)'].sum()
    reportOutput['Nombre de Jour (1j->7H)'] = reportOutput['Durée total (décimal)'] / 7
    
    
reportOutput.to_excel('Downloads/CMC_Project/excel_files/output/Result.xlsx')