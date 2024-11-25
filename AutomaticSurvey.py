# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the survey data
# Replace 'survey_data.csv' with the path to your survey dataset
data = pd.read_csv('survey_data.csv')

# Display basic information about the dataset
print("Dataset Overview:")
print(data.info())
print("\nFirst 5 rows of the dataset:")
print(data.head())

# Clean the data
# Handling missing values
print("\nHandling Missing Values:")
missing_values = data.isnull().sum()
print(missing_values)
data.fillna(data.median(numeric_only=True), inplace=True)  # Fill numeric missing values with median

# Analyze survey responses
# Example: Satisfaction Ratings Analysis
print("\nStatistical Analysis of Satisfaction Ratings:")
if 'Satisfaction' in data.columns:
    satisfaction_stats = data['Satisfaction'].describe()
    print(satisfaction_stats)
else:
    print("No 'Satisfaction' column in the dataset.")

# Automated insights
# Calculate proportions of categorical responses
if 'Preferred_Feature' in data.columns:
    feature_distribution = data['Preferred_Feature'].value_counts(normalize=True) * 100
    print("\nFeature Preference Distribution:")
    print(feature_distribution)

# Correlation Analysis
print("\nCorrelation Analysis:")
correlation_matrix = data.corr()
print(correlation_matrix)

# Visualization
# Histogram of satisfaction ratings
if 'Satisfaction' in data.columns:
    plt.figure(figsize=(8, 6))
    plt.hist(data['Satisfaction'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Distribution of Satisfaction Ratings')
    plt.xlabel('Satisfaction Rating')
    plt.ylabel('Frequency')
    plt.savefig('satisfaction_distribution.png')  # Save the plot as an image
    plt.show()

# Generate automated insights report
with open('survey_analysis_report.txt', 'w') as report:
    report.write("Survey Analysis Report\n")
    report.write("======================\n\n")
    report.write("Dataset Overview:\n")
    report.write(data.info(buf=None, verbose=True).__str__() + "\n\n")
    report.write("Missing Values:\n")
    report.write(missing_values.to_string() + "\n\n")
    if 'Satisfaction' in data.columns:
        report.write("Satisfaction Ratings Statistics:\n")
        report.write(satisfaction_stats.to_string() + "\n\n")
    if 'Preferred_Feature' in data.columns:
        report.write("Preferred Feature Distribution:\n")
        report.write(feature_distribution.to_string() + "\n\n")
    report.write("Correlation Matrix:\n")
    report.write(correlation_matrix.to_string() + "\n\n")
    report.write("Generated Insights: Visualization saved as 'satisfaction_distribution.png'.\n")
