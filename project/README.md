# BRFSS 2023 Risk Modeling Project

## Overview
This project uses the 2023 Behavioral Risk Factor Surveillance System (BRFSS) dataset to model the risk of co-occurring heart disease and kidney disease conditions using logistic regression, PCA-based logistic regression, random forest classification and decision tree classification approaches.

## Data
- Source: [CDC BRFSS 2023](https://www.cdc.gov/brfss/annual_data/annual_2023.html)
- Download the SAS Transport Format (.XPT) file (https://www.cdc.gov/brfss/annual_data/2023/files/LLCP2023XPT.zip)
- Unzip the LLCP2023XPT.zip file into your local drive
- Download 2023 Codebook to use as a data dictionary mapping (https://www.cdc.gov/brfss/annual_data/2023/zip/codebook23_llcp.zip)
- Unzip the codebook23_llcp-v2-508.zip file into your local drive
- Convert codebook23_llcp.pdf into excel codebook23_llcp.xlsx
- Convert codebook23_llcp.xlsx into 2023_Mapping_Dictionary.csv with Value, and Value_Label columns from the codebook and a new column called Variable_Name sourced from the SAS Variable Name from the codebook.


## How to Run
- Open Convert_BRFSS_2023_XPT_to_CSV.ipynb
- Update the local file path in the code before running
- Run all cells in order (recommended in Jupyter Notebook or Jupyter Lab).
- The notebook will:
   - Convert the XPT file to CSV

- After converting the XPT file to CSV for easier analysis, open Risk_profiling_for_heart_and_kidney_disease_using_BRFSS_data.ipynb
- Update the local file path in the code before running
- Run all cells in order (recommended in Jupyter Notebook or Jupyter Lab).
   - Clean and preprocess data
   - Train and evaluate models
   - Perform hyperparameter tuning
   - Interpret results with feature importance

## Output
- Evaluation metrics: Accuracy, Precision, Recall, F1 Score, AUC
- Visualizations: Various graphs, Confusion matrices, ROC curves, Feature importances
