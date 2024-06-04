import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
titanic = pd.read_csv('titanic.csv')

# Handle missing values
titanic['age'] = titanic['age'].fillna(titanic['age'].median())
titanic['embarked'] = titanic['embarked'].fillna('S')
titanic['embark_town'] = titanic['embark_town'].fillna('Southampton')
titanic['deck'] = titanic['deck'].fillna('C')

# Print the missing values count after filling
print(titanic.isnull().sum())

# Visualizations
# Pie charts for survival rate by gender
f, ax = plt.subplots(1, 2, figsize=(10, 5))  # Create subplots
titanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(
    explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True
)
titanic['survived'][titanic['sex'] == 'female'].value_counts().plot.pie(
    explode=[0, 0.1], autopct='%1.1f%%', ax=ax[1], shadow=True
)
ax[0].set_title('Survived (Male)')
ax[1].set_title('Survived (Female)')
plt.show()

# Count plot for class vs survived
titanic['pclass'].astype(str)  # Ensure pclass is a string for better plot labels
titanic.groupby(['pclass', 'survived']).size().unstack().plot(kind='bar', stacked=True)
plt.title('Pclass vs Survived')
plt.xlabel('Pclass')
plt.ylabel('Count')
plt.show()

# Calculate the correlation matrix for numeric columns only
numeric_cols = titanic.select_dtypes(include=['float64', 'int64']).columns
titanic_corr = titanic[numeric_cols].corr(method='pearson')

print(titanic_corr)
