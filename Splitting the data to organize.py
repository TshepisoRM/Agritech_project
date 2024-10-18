import pandas as pd
import os

# Load the CSV file
input_csv_path = 'C:/Users/mutem/Downloads/Grapevine_Annotated_Dataset/annotations.csv'  # Replace with your file path
output_directory = 'C:/Users/mutem/Downloads/Grapevine_Annotated_Dataset/Cleaned_Individual'  # Replace with desired output directory

# Create output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Read the CSV file
df = pd.read_csv(input_csv_path)

# Check if "polygon/_label" column exists
if "polygon/_label" not in df.columns:
    raise ValueError("The 'polygon/_label' column is not found in the CSV file.")

# Group the DataFrame by the 'polygon/_label' column
grouped = df.groupby("polygon/_label")

# Loop through each group and save it as a separate CSV file
for label, group in grouped:
    # Replace invalid filename characters with an underscore
    file_label = str(label).replace('/', '_').replace('\\', '_')
    output_csv_path = os.path.join(output_directory, f"{file_label}.csv")
    
    # Save the group as a separate CSV
    group.to_csv(output_csv_path, index=False)
    print(f"Created CSV file for label '{label}': {output_csv_path}")

print("CSV files for each group have been created successfully!")
