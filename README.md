# Agritech Leaf Disease Analysis Project

## Project Overview
This project focuses on analyzing leaf disease patterns in agricultural crops using a dataset of 99 leaf images with various characteristics and disease indicators. The analysis includes comprehensive data exploration, preprocessing, and preparation for machine learning applications.

## Dataset Description
- **Size**: 99 samples
- **Format**: CSV file (Complete_Dataset - Merged_Dataset.csv.csv)
- **Features**: 25 columns including:
  - Image metadata
  - Leaf characteristics
  - Disease indicators
  - Annotation data

### Key Features
1. **Core Metadata**
   - Leaf_ID
   - Image_Name
   - Width/Height
   - Source information

2. **Disease Indicators**
   - Leaf_Condition
   - Spot characteristics
   - Fungal growth presence
   - Leaf area affected

3. **Physical Characteristics**
   - Leaf color and texture
   - Leaf shape
   - Vein characteristics

## Project Structure
```
├── data/
│   ├── raw/                   # Original dataset
│   ├── processed/             # Cleaned and processed data
│   └── splits/                # Train/validation/test splits
├── notebooks/
│   ├── 1_data_exploration.ipynb
│   ├── 2_data_preprocessing.ipynb
│   └── 3_feature_analysis.ipynb
├── visualizations/
│   ├── distribution_plots/
│   ├── correlation_matrices/
│   └── missing_value_charts/
└── README.md
```

## Data Analysis Summary

### Data Quality
- Complete core features (100% data availability)
- Partial feature completion:
  - Leaf Area Affected: 49.5% complete
  - Most categorical features: ~25% complete
  - Significant missing data in detailed characteristics

### Key Insights
1. Image Characteristics
   - Consistent dimension format
   - All images include annotation points
2. Disease Patterns
   - Multiple leaf conditions documented
   - Varying degrees of area affected
3. Feature Relationships
   - Correlations between physical characteristics and disease indicators

## Setup and Installation

### Prerequisites
```python
# Required Python packages
pandas==1.5.3
numpy==1.24.3
matplotlib==3.7.1
seaborn==0.12.2
scikit-learn==1.2.2
```

### Installation Steps
1. Clone the repository:
```bash
git clone [repository-url]
cd agritech-project
```

2. Create and activate virtual environment:
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
# or
env\Scripts\activate  # Windows
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Data Exploration
```python
# Load and explore the dataset
import pandas as pd

# Read the dataset
df = pd.read_csv('data/raw/Complete_Dataset - Merged_Dataset.csv.csv')

# Basic information
print(df.info())
```

### Running the Analysis
1. Open Jupyter Notebook:
```bash
jupyter notebook
```

2. Navigate to notebooks/
3. Run notebooks in sequence:
   - 1_data_exploration.ipynb
   - 2_data_preprocessing.ipynb
   - 3_feature_analysis.ipynb

## Results and Visualizations
The analysis produces various visualizations and insights:
- Distribution of leaf conditions
- Missing value patterns
- Feature correlations
- Disease indicator relationships

## Contributing
1. Fork the repository
2. Create your feature branch:
```bash
git checkout -b feature/YourFeature
```
3. Commit your changes:
```bash
git commit -m 'Add some feature'
```
4. Push to the branch:
```bash
git push origin feature/YourFeature
```
5. Open a Pull Request

## Contact
[Your Name/Organization]
[Contact Information]

## License
This project is licensed under the [License Name] - see the LICENSE.md file for details

## Acknowledgments
- Data source attribution
- Collaborators and contributors
- Supporting institutions/organizations
