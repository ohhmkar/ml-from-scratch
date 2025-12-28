ML Learning - Omkar Gajare

## Dataset

In Machine Learning, a dataset is just a collection of data that we use to train and test our models.
Think of it like an Excel sheet:

Rows → each row is one data point (called a sample).

Columns → each column contains information about that sample.
Features (Inputs)

Features are the independent variables — the input data we provide to the ML model.
They describe the properties of each sample.

Example:

- Age
- Salary
- Height
- Exam scores

**_Features are like the ingredients we give to a recipe._**

#### Labels (Outputs / Targets)

The label is what we want the model to predict.

It is also called the dependent variable or target.

Example:

- Will the student pass or fail? (Yes/No)
- Price of a house
- Disease diagnosis (Positive/Negative)

**_Labels are like the final dish that we expect after cooking with the ingredients._**

#### Example Dataset

| Age | Salary | Hours Studied | Passed |
| --- | ------ | ------------- | ------ |
| 20  | 30,000 | 5             | Yes    |
| 22  | 25,000 | 2             | No     |
| 19  | 40,000 | 6             | Yes    |
| 21  | 35,000 | 1             | No     |

#### Features →

- Age
- Salary
- Hours Studied

Label → Passed (Yes/No)

```py
# Step 1: Import pandas
import pandas as pd

# Step 2: Load the dataset (make sure students.csv is in the same folder as this script)
df = pd.read_csv("students.csv")

# Step 3: View the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Step 4: Separate features and label
features = df[["Age", "Salary", "Hours_Studied"]]
label = df["Passed"]

print("\nFeatures (X):")
print(features.head())

print("\nLabel (y):")
print(label.head())
```
