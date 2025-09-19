# Optimizing Email Campaign Engagement: A/B Test Analysis of Subject Line and Call-to-Action Variations

## Overview

This project analyzes the results of an A/B test conducted on an email marketing campaign.  The analysis focuses on determining the optimal combination of email subject lines and call-to-actions (CTAs) that yield the highest click-through rates (CTR) and conversion rates.  The analysis involves data cleaning, statistical analysis, and data visualization to identify statistically significant differences between the various A/B test variations.

## Technologies Used

* Python 3
* Pandas
* Matplotlib
* Seaborn

## How to Run

1. **Install Dependencies:**  Ensure you have Python 3 installed.  Then, install the required Python libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Analysis:** Execute the main script:

   ```bash
   python main.py
   ```

## Example Output

The script will print a summary of the A/B test results to the console, including key statistics such as CTR and conversion rates for each variation.  Additionally, the script generates several visualizations (saved as PNG files in the `output` directory):

* **Subject Line Performance:** A bar chart comparing the click-through rates of different subject lines.
* **CTA Performance:** A bar chart comparing the conversion rates of different call-to-actions.
* **Combined Performance:** A heatmap visualizing the interaction effect between subject lines and CTAs on conversion rates.

These visualizations provide a comprehensive overview of the A/B test results and aid in identifying the most effective email subject line and CTA combination.  The specific file names of the generated plots might vary slightly.