import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# --- 1. Synthetic Data Generation ---
np.random.seed(42) # for reproducibility
# Define A/B test variations
subject_lines = ['Subject Line A', 'Subject Line B']
calls_to_action = ['Call to Action A', 'Call to Action B']
# Generate synthetic data
data = {
    'Subject Line': np.random.choice(subject_lines, size=1000),
    'Call to Action': np.random.choice(calls_to_action, size=1000),
    'Clicks': np.random.binomial(1, 0.1, size=1000), # 10% click-through rate on average
    'Conversions': np.random.binomial(1, 0.05, size=1000) # 5% conversion rate on average
}
df = pd.DataFrame(data)
# --- 2. Data Cleaning and Preparation ---
# (In a real-world scenario, this section would involve handling missing values, 
# outliers, and data type conversions)
# --- 3. Analysis ---
# Calculate click-through rates and conversion rates for each combination
result = df.groupby(['Subject Line', 'Call to Action']).agg({'Clicks': 'sum', 'Conversions': 'sum'}).reset_index()
total_emails = df.groupby(['Subject Line', 'Call to Action']).size().reset_index(name='Total Emails')
result = pd.merge(result, total_emails, on=['Subject Line', 'Call to Action'])
result['Click-Through Rate'] = (result['Clicks'] / result['Total Emails']) * 100
result['Conversion Rate'] = (result['Conversions'] / result['Total Emails']) * 100
print("\n--- A/B Test Results ---")
print(result)
# Find the best performing combination
best_combination = result.loc[result['Conversion Rate'].idxmax()]
print(f"\nBest Performing Combination:\n{best_combination}")
# --- 4. Visualization ---
plt.figure(figsize=(12, 6))
# Click-Through Rate Bar Plot
plt.subplot(1, 2, 1)
sns.barplot(x='Subject Line', y='Click-Through Rate', hue='Call to Action', data=result)
plt.title('Click-Through Rate by Subject Line and Call to Action')
plt.ylabel('Click-Through Rate (%)')
# Conversion Rate Bar Plot
plt.subplot(1, 2, 2)
sns.barplot(x='Subject Line', y='Conversion Rate', hue='Call to Action', data=result)
plt.title('Conversion Rate by Subject Line and Call to Action')
plt.ylabel('Conversion Rate (%)')
plt.tight_layout()
# Save the plot to a file
output_filename = 'ab_test_results.png'
plt.savefig(output_filename)
print(f"\nPlot saved to {output_filename}")