# Student Performance Analysis & Prediction

## 📌 Overview
This project analyzes how different student habits such as study time, sleep, and attendance affect exam performance.  
A machine learning model is built to predict student scores based on these factors.

---

## 🎯 Objective
To understand the relationship between study behavior and academic results, and to build a predictive model for student performance.

---

## 🗂 Dataset
The dataset used in this project is a simple structured dataset with the following features:

- **hours_studied** → Number of hours a student studies  
- **sleep_hours** → Average sleep duration  
- **attendance** → Attendance percentage  
- **score** → Final exam score  

---

## 📊 Exploratory Data Analysis (EDA)
- Scatter plots were used to analyze the relationship between study hours and scores  
- A correlation heatmap was used to identify relationships between variables  
- Results show a strong positive correlation between study hours and exam scores  

---

## 🤖 Machine Learning Model
- **Algorithm Used:** Linear Regression  
- **Train-Test Split:** 80% training, 20% testing  
- **Evaluation Metric:** Mean Absolute Error (MAE)  

The model learns patterns from student behavior and predicts expected exam scores.

---

## 📈 Results & Insights
- Study hours have the highest impact on student performance  
- Attendance also significantly influences results  
- Sleep shows moderate impact  
- The model provides reasonably accurate predictions for unseen data  

---

## 🔍 Example Prediction
Input:
- Hours Studied: 5  
- Sleep Hours: 7  
- Attendance: 80%  

Predicted Score: ~75  

---

##  Tools & Technologies
- Python  
- pandas  
- matplotlib  
- seaborn  
- scikit-learn  
