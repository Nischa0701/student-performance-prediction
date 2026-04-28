import pandas as pd
import matplotlib.pyplot as plt
import  seaborn as sns


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import joblib

# Load dataset
df = pd.read_csv("students.csv")

print("First 5 rows:")
print(df.head())

print("\nSummary:")
print(df.describe())

# Visualization
sns.scatterplot(x="hours_studied", y="score", data=df)
plt.title("Hours Studied vs Score")
plt.show()

sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Matrix")
plt.show()

# Features & target
X = df[["hours_studied", "sleep_hours", "attendance"]]
y = df["score"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

print("\nPredictions:", predictions)
print("Actual:", list(y_test))

# Error
error = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", error)

# Test new input
new_data = [[5, 7, 80]]
predicted_score = model.predict(new_data)
print("\nPredicted score for new student:", predicted_score)

# Save model
import joblib

joblib.dump(model, "model.pkl")
print("Model saved successfully!")