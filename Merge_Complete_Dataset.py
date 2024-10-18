import pandas as pd
import glob
import os

# Directory containing the individual CSV files
input_dir = r'C:/Users/mutem/Downloads/Grapevine_Annotated_Dataset/Segmented_Cleaned_Data'
output_file = r'C:/Users/mutem/Downloads/Grapevine_Annotated_Dataset/Merged_Dataset.csv'

# List to store DataFrames
dataframes = []

# Define common columns to merge on
common_columns = [
    'Leaf_ID', 'Image_Name', 'Leaf_Condition', 'Z_order', 'Width', 'Height', 
    'Source', 'Occluded'
]

# Use glob to read all CSV files in the specified directory
csv_files = glob.glob(os.path.join(input_dir, '*.csv'))

# Process each file
for file_path in csv_files:
    try:
        # Read CSV file into DataFrame
        df = pd.read_csv(file_path)

        # Standardize the 'Occluded' column by merging columns containing "Occlude"
        occlude_cols = df.filter(regex='Occlude').columns
        if len(occlude_cols) > 0:
            df['Occluded'] = df[occlude_cols].bfill(axis=1).iloc[:, 0]
            df.drop(columns=occlude_cols, inplace=True)
        else:
            df['Occluded'] = ""  # Add the column if not present

        # Add missing common columns as blanks to ensure alignment during merge
        for col in common_columns:
            if col not in df.columns:
                df[col] = ""

        # Add the 'LeafAnnotated_points' column last if it's missing
        if 'LeafAnnotated_points' not in df.columns:
            df['LeafAnnotated_points'] = ""

        # Reorder columns so common columns come first, and 'LeafAnnotated_points' is last
        remaining_cols = [col for col in df.columns if col not in common_columns and col != 'LeafAnnotated_points']
        df = df[common_columns + remaining_cols + ['LeafAnnotated_points']]

        # Append DataFrame to the list
        dataframes.append(df)
        
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

# Concatenate all DataFrames and fill missing values with 'N/A'
merged_df = pd.concat(dataframes, ignore_index=True, sort=False).fillna('N/A')

# Reorder columns, common columns first, followed by unique columns, with 'LeafAnnotated_points' at the end
unique_cols = [col for col in merged_df.columns if col not in common_columns and col != 'LeafAnnotated_points']
merged_df = merged_df[common_columns + unique_cols + ['LeafAnnotated_points']]

# Save the final merged DataFrame to CSV
merged_df.to_csv(output_file, index=False)
print(f"Merged dataset saved to {output_file}")
