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

---

## 🛠️ Module Navigation
Access the technical documentation and complete source code for each stage through the modules below:

| 🧹 01. Data Cleaning & Preprocessing | 🧬 02. Statistical Modeling | 📈 03. Insight Visualization |
| :--- | :--- | :--- |
| Regex cleaning, handling nulls, & data type conversion. | Multiple Linear Regression (Statsmodels) & Customer Segmentation (NumPy). | Advanced plotting (Matplotlib) & Automated Reporting (Tabulate). |

---

📊 Highlights of Analysis Results
1. Revenue Contribution & Operational Health
The Printer & Chair category dominates revenue (15.5% each). However, the status Canceled (250 orders) was the highest frequency, indicating the need to evaluate the order fulfillment system.
<table border="0">
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/be2b5b20-d8dc-427b-8910-b98943c785ee" width="400" alt="Revenue Analysis">
    </td>
    <td>
      <img src="https://github.com/user-attachments/assets/791a34c6-0409-457c-8886-5342209b5b02" width="400" alt="Order Status">
    </td>
  </tr>
</table>

3. Distribution of Sales Performance
The majority of transactions (688 data) were classified into the Low Sales Performance category. This is a great opportunity for an upselling strategy to the Medium (190) or High (143) categories.
<table border="0">
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/422b6ba3-2c91-4e31-837e-6d99891edd98" width="400" alt="Sales Performance Distribution">
      <br><em>Sales Performance Distribution</em>
    </td>
  </tr>
</table>

4. Market Acquisition (Referral)
The Instagram channel outperformed other platforms with a contribution of $275,285.45, proving the effectiveness of visual campaigns in attracting high-value customers.
<table border="0">
  <tr>
    <td align="center" width="800">
      <img src="https://github.com/user-attachments/assets/40fc6750-070f-4ab1-90c4-68cf6b2cbbdf" width="600" alt="Top Referral">
      <br>
      <small><em>Market Acquisition by Referral Source</em></small>
    </td>
  </tr>
</table>

6. Correlation of Goods Volume vs Total Price
Found a correlation of 0.39 (moderate positive). The scatter plot graph shows that an increase in the number of items in the basket tends to be followed by an increase in the total transaction price.
<table border="0">
  <tr>
    <td align="center" width="800">
      <img src="https://github.com/user-attachments/assets/1b5a79d4-ef13-4295-ad2f-044f21b0ba78" width="600" alt="Correlation Plot">
      <br>
      <small><em>Correlation of Goods Volume vs Total Price</em></small>
    </td>
  </tr>
</table>

8. Trends in Transaction Volume & Average Value
Most transactions contain 5-6 items. Strategically, the red line shows Average TotalPrice peaking at 10 item transactions (near 1,800 value).
<table border="0">
  <tr>
    <td align="center" width="800">
      <img src="https://github.com/user-attachments/assets/8dc00b21-4104-46d6-900a-f23e9d56aa22" width="700" alt="Transaction Volume Trend">
      <br>
      <small><em>Relationship Between Item Count per Transaction and Average Order Value</em></small>
    </td>
  </tr>
</table>

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
