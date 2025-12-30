#### ML Learning - Omkar Gajare

## Handling Missing Values

In real-world datasets, missing values are very common. Machine learning models cannot work properly with missing values, so we need to handle them before training.

---

1. ## How to Identify Missing Values
   In Pandas, missing values are usually represented as:<br>NaN (Not a Number)<br>None<br>Empty cells.

#### Output:

| Name  | Age | Department | Salary |
| ----- | --- | ---------- | ------ |
| Rahul | 25  | IT         | 50000  |
| Priya | NaN | HR         | 45000  |
| Arjun | 28  | NaN        | 60000  |
| Sneha | 35  | IT         | NaN    |

2. ## Detect Missing Values

```py
# Check for missing values
print(df.isnull())

# Count missing values per column
print(df.isnull().sum())
```

3. ## Handling Missing Values : Removing Missing Values

```py
# Drop rows with missing values:
df_cleaned = df.dropna()
# Drop columns with too many missing values:
df_cleaned = df.dropna(axis=1)
```

4. ## Handling Missing Values : Filling Missing Values (Imputation)

```py
# Fill with a constant:
df['Age'] = df['Age'].fillna(0)  # Fill missing ages with 0
# Fill with mean/median/mode (common for numerical data):
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
# Fill categorical missing values with the most frequent value:
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])
```
