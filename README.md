# Loan Approval Prediction Model

## 📌 Project Overview
This project predicts whether a loan application will be approved based on applicant and loan details using **Machine Learning**.  
The dataset undergoes **data cleaning, exploratory data analysis (EDA)**, and **model training** with Logistic Regression, Decision Tree classifiers and Random Forest Classifier.  
The best performance was achieved using **Logistic Regression** with an **average cross-validation accuracy of 82%**.

---

## 📊 Dataset
- **Total Rows:** 614  
- **Features:** ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Gender, Education, Marital Status, Property Area, etc.
- **Target Variable:** Loan_Status (Approved = 1, Not Approved = 0)  

> The dataset contains both numerical and categorical features. Missing values were handled using median/mode imputation.

---

## 🛠 Data Preprocessing
1. **Handled Missing Values**  
   - Median for numerical columns  
   - Mode for categorical columns  
2. **Encoding**
   - Label encoding for Loan_Status
   - One-hot encoding for categorical variables using Pandas  
3. **Feature Scaling**  
   - StandardScaler used for Logistic Regression  
4. **Outlier Treatment**  
   - Statistical outliers reviewed manually; realistic values retained to preserve data diversity

---

## 📈 Exploratory Data Analysis (EDA)
Key insights:
- **Married applicants** have a higher loan approval rate than unmarried.
- **Semiurban areas** showed slightly higher approval rates.
- **Credit History** is the most significant factor in loan approval.

Example plots:
![EDA Example](images/eda_plot1.png)
![Correlation Heatmap](images/heatmap.png)

---

## 🤖 Model Building & Evaluation
Models used:
- **Logistic Regression**
- **Decision Tree Classifier**
- **Random Forest Classifier** (for comparison)

**Results:**
| Model                   | Accuracy | Cross-Validation Avg |
|-------------------------|----------|----------------------|
| Logistic Regression     | 75%      | **82%**              |
| Decision Tree           | 72%      | 74%                  |
| Random Forest           | 76%      | 78%                  |

**Best Model:** Logistic Regression (balanced performance + interpretability)

---

## 🚀 How to Run
1. Clone the repository:
```bash
git clone https://github.com/yourusername/Loan_Approval_Model.git
