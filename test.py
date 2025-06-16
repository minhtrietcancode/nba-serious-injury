# Load the dataset 
import pandas as pd 
df = pd.read_csv('PlayerStats.csv')

# now display the unique features here 
print(df.columns.unique())
