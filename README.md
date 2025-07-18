# 🎓 Student Score Prediction

This project predicts the **math exam score** of students based on attributes such as gender, ethnicity, parental education level, lunch type, test preparation course, and other academic scores. The application is powered by a machine learning model (**Ridge Regression**) and deployed using **Flask**.

---

## 🚀 Features

- ✅ Predict student's **math score** based on interactive form inputs  
- ✅ Interactive **Flask web application** for real-time predictions  
- ✅ Data preprocessing using `ColumnTransformer`  
- ✅ Benchmarking with multiple regression models  
- ✅ **Randomized Search CV** used for hyperparameter tuning  
- ✅ **MLflow** integrated for:
  - Experiment tracking  
  - Metric logging  
  - Model comparison and versioning  

---

## 🔍 Models Used

- ✅ **Ridge Regression** (final selected model after tuning)  
- Benchmark models evaluated:
  - Linear Regression  
  - Lasso  
  - K-Nearest Neighbors Regressor  
  - Decision Tree Regressor  
  - Random Forest Regressor  
  - XGBoost Regressor  
  - CatBoost Regressor  
  - AdaBoost Regressor  

---

## 🛠️ Technologies Used

- Python (Pandas, NumPy, Scikit-learn)
- Ridge Regression (and other regressors)
- Flask (Web App Deployment)
- MLflow (Tracking)
- Matplotlib & Seaborn (Visualization)

--- 

## ✅ Next Steps

- Improve feature engineering (e.g., interaction terms)
- Try target encoding for tree-based models
- Explore ensemble and stacking models
