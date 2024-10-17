# AgriTech Image Annotation Project: Plant Health Assessment

## Project Overview
This project is a collaboration between VineTech Innovations and Groot Constantia, South Africa's oldest wine-producing estate, aimed at developing an image annotation solution for detecting plant diseases, particularly grapevine leafroll disease. The solution utilizes drone imagery and AI-powered computer vision to monitor vineyard health across Groot Constantia's 165-hectare estate.

### Key Objectives
- Develop an image annotation solution for plant disease detection
- Create a trained machine learning model for early disease detection
- Enable efficient monitoring of vineyard health
- Facilitate early intervention in disease management

## Dataset Information
- **Source**: Plant Village Dataset (Kaggle)
- **Size**: 99 annotated samples
- **Features**: 25 characteristics including:
  - Leaf condition classifications
  - Disease indicators
  - Physical measurements
  - Image metadata

## Solution Components

### 1. Data Exploration
- Analysis of healthy vs. diseased plant characteristics
- Identification of key disease indicators
- Statistical analysis of dataset composition

### 2. Image Analysis Features
- Individual plant identification
- Health status classification:
  - Healthy
  - Early-stage infection
  - Advanced infection
- Detection of missing or dead plants

### 3. Technical Implementation
```
project/
├── data/
│   ├── raw/                # Original Plant Village dataset
│   ├── processed/          # Cleaned and annotated data
│   └── metadata/           # Dataset statistics and information
├── notebooks/
│   ├── exploration/        # Data analysis notebooks
│   ├── preprocessing/      # Data cleaning and preparation
│   └── modeling/          # Model development notebooks
├── src/
│   ├── data/              # Data processing scripts
│   ├── features/          # Feature engineering code
│   └── visualization/     # Visualization utilities
├── tests/                 # Unit tests
├── docs/                  # Documentation
└── requirements.txt       # Project dependencies
```

## Installation and Setup

### Prerequisites
```python
# Required packages
pandas>=1.5.3
numpy>=1.24.3
matplotlib>=3.7.1
seaborn>=0.12.2
scikit-learn>=1.2.2
opencv-python>=4.7.0
```

### Getting Started
1. Clone the repository:
```bash
git clone [repository-url]
cd agritech-project
```

2. Create virtual environment:
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
# or
env\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage Guide

### Data Processing
```python
# Example of basic data loading and processing
from src.data import process_data

# Load and process dataset
processed_data = process_data.load_dataset('path/to/data')
```

### Running Analysis
1. Navigate to notebooks directory
2. Execute notebooks in sequence:
   - 1_data_exploration.ipynb
   - 2_preprocessing.ipynb
   - 3_feature_analysis.ipynb

## Key Features
- Automated image preprocessing
- Disease detection algorithms
- Statistical analysis tools
- Visualization capabilities
- Annotation guidelines

## Project Status
- [x] Data collection and organization
- [x] Initial exploratory analysis
- [x] Feature engineering
- [x] Base model development
- [ ] Advanced model optimization
- [ ] Deployment preparation

## Ethical Considerations
- Data privacy protection
- Bias mitigation strategies
- Impact assessment on agricultural labor
- Responsible AI implementation

## Contributing
1. Fork the repository
2. Create feature branch:
```bash
git checkout -b feature/YourFeature
```
3. Commit changes:
```bash
git commit -m 'Add some feature'
```
4. Push to branch:
```bash
git push origin feature/YourFeature
```
5. Submit a Pull Request

## Team
- Matimu Nghonyama - Data Scientist/ ML Engineer
- Edzani Bruce Mutemula - Data Scientist
- Matome Seshoka - Researcher
- Tsepiso Moeketsi - Project Manager/ Data Analyst
- Earl Tlhagane - Researcher
- Nico Zwane - Researcher
- Kefilwe - Researcher

## Acknowledgments
- VineTech Innovations
- Groot Constantia Estate
- Plant Village Dataset contributors



## Contact
For any queries regarding this project:
- Email: nghonyamamatimu@gmail.com

