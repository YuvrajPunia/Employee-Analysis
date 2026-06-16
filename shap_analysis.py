import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt

# Load model
model = joblib.load("attrition_model.pkl")

# Load processed dataset
df = pd.read_csv("processed_employee_data.csv")

# Features
X = df.drop("LeaveOrNot", axis=1)

# Create SHAP explainer
explainer = shap.TreeExplainer(model)

# Calculate SHAP values
shap_values = explainer.shap_values(X)

# SHAP Summary Plot
shap.summary_plot(
    shap_values,
    X,
    show=False
)

plt.tight_layout()
plt.savefig("shap_summary.png", dpi=300)

print("SHAP Analysis Complete!")
print("Saved: shap_summary.png")