import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define the number of rows
num_rows = 10000

# Generate data
data = {
    'Lead ID': [f'LD{i}' for i in range(1, num_rows + 1)],
    'Location': np.random.choice(['Ahmedabad', 'Surat', 'Mumbai', 'Delhi', 'Bangalore'], num_rows),
    'College': np.random.choice(['XYZ University', 'ABC Institute', 'LMN College', 'PQR University'], num_rows),
    'Year of Study': np.random.choice(['1st', '2nd', '3rd', '4th'], num_rows),
    'Program Interest': np.random.choice(['Data Science', 'Robotics', 'AI', 'Electric Vehicle'], num_rows),
    'Lead Source': np.random.choice(['Instagram', 'LinkedIn', 'College Collaboration', 'Google Form', 'Mass-Mailing', 'Whatsapp'], num_rows)
}

# Create DataFrame
df = pd.DataFrame(data)

# Data Preprocessing
# Check for missing values
print("Missing values:\n", df.isnull().sum())

# Demographic Analysis
# Trends in lead sourcing based on location, college, and year of study
location_trends = df['Location'].value_counts()
college_trends = df['College'].value_counts()
year_trends = df['Year of Study'].value_counts()

# Program Analysis
# Interest levels for various e-learning programs
program_interest = df['Program Interest'].value_counts()

# Generate hypothetical conversion data
np.random.seed(42)  # For reproducibility
df['Converted'] = np.random.choice([0, 1], size=num_rows, p=[0.7, 0.3])  # 30% conversion rate

# Calculate conversion rates by location
conversion_by_location = df.groupby('Location')['Converted'].mean()

# Calculate conversion rates by college
conversion_by_college = df.groupby('College')['Converted'].mean()

# Calculate conversion rates by year of study
conversion_by_year = df.groupby('Year of Study')['Converted'].mean()

# Calculate conversion rates by program interest
conversion_by_program = df.groupby('Program Interest')['Converted'].mean()

# Calculate conversion rates by lead source
conversion_by_source = df.groupby('Lead Source')['Converted'].mean()

# Budget Allocation Strategy
# Define total marketing budget
total_budget = 100000  # Example budget in currency units

# Allocate budget based on conversion rates
budget_by_location = (conversion_by_location / conversion_by_location.sum()) * total_budget
budget_by_college = (conversion_by_college / conversion_by_college.sum()) * total_budget
budget_by_year = (conversion_by_year / conversion_by_year.sum()) * total_budget
budget_by_program = (conversion_by_program / conversion_by_program.sum()) * total_budget
budget_by_source = (conversion_by_source / conversion_by_source.sum()) * total_budget

# Plot lead distribution by location
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Location')
plt.title('Lead Distribution by Location')
plt.show()

# Plot lead distribution by college
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='College')
plt.title('Lead Distribution by College')
plt.show()

# Plot lead distribution by year of study
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Year of Study')
plt.title('Lead Distribution by Year of Study')
plt.show()

# Plot lead distribution by program interest
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Program Interest')
plt.title('Lead Distribution by Program Interest')
plt.show()

# Plot lead distribution by lead source
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Lead Source')
plt.title('Lead Distribution by Lead Source')
plt.show()

# Plot conversion rates by program interest
plt.figure(figsize=(10, 6))
conversion_by_program.plot(kind='bar', color='skyblue')
plt.title('Conversion Rates by Program Interest')
plt.xlabel('Program Interest')
plt.ylabel('Conversion Rate')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Print budget allocation
print("Budget Allocation by Location:\n", budget_by_location)
print("\nBudget Allocation by College:\n", budget_by_college)
print("\nBudget Allocation by Year of Study:\n", budget_by_year)
print("\nBudget Allocation by Program Interest:\n", budget_by_program)
print("\nBudget Allocation by Lead Source:\n", budget_by_source)

# Save the dataset to CSV
df.to_csv('leads_dataset.csv', index=False)
print("Dataset generated and saved as 'leads_dataset.csv'")
