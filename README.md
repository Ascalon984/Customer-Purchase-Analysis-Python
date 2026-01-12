<p align="center">
  <img src="https://github.com/user-attachments/assets/61bf11f0-7999-4716-a60e-4477fc20f47c" width="800">
</p>


Online Store Sales Analysis Pipeline

Transforming Transaction Data into Data-Based Business Strategy.

[![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-ffffff?style=for-the-badge&logo=matplotlib&logoColor=black)](https://matplotlib.org/)
[![Statsmodels](https://img.shields.io/badge/Statsmodels-Statistical%20Modeling-4B8BBE?style=for-the-badge&logo=scipy&logoColor=white)](https://www.statsmodels.org/)
[![Tabulate](https://img.shields.io/badge/Tabulate-Table%20Formatting-2C2C2C?style=for-the-badge&logo=readme&logoColor=white)](https://pypi.org/project/tabulate/)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)](#)

📖 Overview

This project is an automated customer purchase history data analysis pipeline (Online Store Orders) with Python. Workflows include rigorous data cleaning (regex, typo fixing), feature transformation, customer segmentation, to regression analysis and advanced visualization to support data-driven strategic decision making.

🚨 Business Impact:
– Identify products and categories with the highest revenue contribution
– Map customer shopping behavior and loyalty through meaningful segmentation
– Support marketing and inventory strategy recommendations based on real trends from transaction data.

📊 Highlights of Analysis Results
1. Revenue Contribution & Operational Health
The Printer & Chair category dominates revenue (15.5% each). However, the status Canceled (250 orders) was the highest frequency, indicating the need to evaluate the order fulfillment system.
<img width="350" alt="Revenue and Status" src="https://github.com/user-attachments/assets/2e69d553-acf9-4bdf-8296-05fd2c7c89a4" />

2. Distribution of Sales Performance
The majority of transactions (688 data) were classified into the Low Sales Performance category. This is a great opportunity for an upselling strategy to the Medium (190) or High (143) categories.
<img width="350" alt="Sales Performance" src="https://github.com/user-attachments/assets/3860011b-cc8c-4a34-a74e-09c379a05b1c" />

3. Market Acquisition (Referral)
The Instagram channel outperformed other platforms with a contribution of $275,285.45, proving the effectiveness of visual campaigns in attracting high-value customers.
<img width="350" alt="Top Referral" src="https://github.com/user-attachments/assets/40fc6750-070f-4ab1-90c4-68cf6b2cbbdf" />

4. Correlation of Goods Volume vs Total Price
Found a correlation of 0.39 (moderate positive). The scatter plot graph shows that an increase in the number of items in the basket tends to be followed by an increase in the total transaction price.
<img width="350" alt="Correlation Plot" src="https://github.com/user-attachments/assets/8dc00b21-4104-46d6-900a-f23e9d56aa22" />

5. Trends in Transaction Volume & Average Value
Most transactions contain 5-6 items. Strategically, the red line shows Average TotalPrice peaking at 10 item transactions (near 1,800 value).
<img width="350" alt="Transaction Volume" src="https://github.com/user-attachments/assets/71a539da-847e-460b-ae9b-13695ca53e5e" />

6. Sales Performance Summary
Emphasizing the dominance of the Low segment in terms of volume, but mapping the presence of the Very High segment (94 transactions) which provides the largest profitability margin for the business.
<img width="350" alt="Performance Distribution" src="https://github.com/user-attachments/assets/381106b5-fa74-4d7e-8b97-b04ce8250b58" />

💡 Key Findings (Executive Insights)
- Market Leader: Printer and Laptop products consistently lead revenue, indicating strong market demand and the need for tight inventory management in this category.

- Operational Leakage: The cancellation number (Cancelled: 250) that exceeds the Delivered or Shipped status is an operational risk that must be handled immediately to prevent potential profit loss.

- Optimal Basket Value: Even though most transactions contain 5-6 items, maximum profitability (highest average value) is in transactions of 10 items. The bundling strategy is highly recommended.

- Referral ROI: Instagram provides the highest ROI above the average of other channels, indicating that marketing budget allocation on the visual platform provides significant results.

- End-to-End Pipeline: This project includes data cleaning (regex & typo correction), statistical aggregation, custom customer segmentation, as well as Multiple Linear Regression modeling using Statsmodels for revenue prediction.

🚀 How to Run a Project

Clone this repository:
git clone https://github.com/Ascalon984/Customer-Purchase-Analysis-Python

Make sure the dataset (Online-Store-Orders.xlsx) is available in the project folder.

Install dependencies:
pip install pandas numpy matplotlib statsmodels tabulate openpyxl
4. Run the Python script in order of numbering.

---
Organized by **[Aditya Tri Prasetyo]** • 2026 | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/aditya-tri-prasetyo-7b3a0a396) [![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://instagram.com/aditya.trisetya)
