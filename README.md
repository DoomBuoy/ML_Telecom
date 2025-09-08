# ML_Telecom




# Project Overview

## For Business Stakeholders

This project leverages advanced machine learning to help a telecom company better understand and predict customer satisfaction and churn risk. By analyzing customer address and satisfaction data, the solution identifies key customer segments—Promoters, Passives, and Detractors—enabling targeted engagement, improved retention, and data-driven business decisions. The model empowers the business to:

- **Increase Customer Advocacy:** Identify Promoters for referral and loyalty programs.
- **Enhance Retention:** Detect Passives early and convert them into Promoters.
- **Prevent Churn:** Accurately flag Detractors for timely intervention.

## For Technical Audiences

The project follows a robust data science pipeline:

- **Data Exploration & Cleaning:** Comprehensive EDA on customer address and satisfaction datasets, handling missing values, duplicates, and feature engineering (see EDA notebooks).
- **Feature Engineering:** Creation of meaningful features such as NPS category, CLTV percentiles, postcode binning, and neighborhood density to enrich the predictive power.
- **Modeling:**
    - The core model is a Random Forest Classifier trained to predict NPS categories (Promoter, Passive, Detractor).
    - Baseline performance is established using a Dummy Classifier.
    - Data imbalance is addressed with SMOTE to ensure fair representation of all classes.
    - Model evaluation uses cross-validation and classification reports, focusing on F1-score for Passives, recall for Promoters, and F1-score for Detractors.
- **Results:**
    - The Random Forest achieved ~69% cross-validation accuracy, with strong performance in detecting Detractors (F1 ~87), moderate recall for Promoters (~73%), but struggled with Passives (F1 ~29-32) due to class imbalance.
    - The model is valuable for churn detection but requires further refinement for engagement and advocacy strategies.

## Business Impact

- **Actionable Insights:** Enables targeted marketing, loyalty, and retention strategies.
- **Data-Driven Decisions:** Empowers teams to focus on high-value customers and reduce churn.
- **Scalable Framework:** The modular pipeline supports future enhancements and integration with business systems.

For more details, see the EDA and Classification notebooks, and the project report.

# Setup:
Run the SetYouUp.ipynb file to get started.

# Running the Project
0. Run `SetYouUp.ipynb`
1. Open the project folder in your terminal.
2. Start Jupyter Lab with `poetry run jupyter lab` or launch Visual Studio Code with `poetry run code .` (ensure VS Code is added to your system PATH to use the latter command).
3. If using VS Code, select the kernel that matches the project folder name.


# Data Cards

## customer_address.csv

| Column       | Description                                   |
|--------------|-----------------------------------------------|
| customer_id  | Unique identifier of customer                 |
| street       | Customer’s address street name                |
| type         | Customer’s address street type                |
| suburb       | Customer’s address suburb                     |
| postcode     | Customer’s address postcode                   |
| full_address | Customer’s full address                       |

## customer_satisfaction.csv

| Column      | Description                                                        |
|-------------|--------------------------------------------------------------------|
| customer_id | Unique identifier of customer                                      |
| nps         | Customer’s overall satisfaction rating (1=Very Unsatisfied, 5=Very Satisfied) |
| cltv        | Customer Lifetime Value. Higher value = more valuable customer      |
| reason      | Customer’s specific reason for leaving the company                 |




# Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         ml_telecom and configuration for tools like black
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── ml_telecom   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes ml_telecom a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    └──dataset.py              <- Scripts to download or generate data
   
```

--------

