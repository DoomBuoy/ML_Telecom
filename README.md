# ML_Telecom



Description

# Setup:
Run the SetYouUp.ipynb file to get started.

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

