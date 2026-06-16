import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("Employee.csv")

print("Dataset Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Encode categorical columns
label_encoder = LabelEncoder()

categorical_cols = [
    'Education',
    'City',
    'Gender',
    'EverBenched'
]

for col in categorical_cols:
    df[col] = label_encoder.fit_transform(df[col])

# Features and Target
X = df.drop('LeaveOrNot', axis=1)
y = df['LeaveOrNot']

# Save processed dataset
df.to_csv("processed_employee_data.csv", index=False)

print("\nFeatures Shape:", X.shape)
print("Target Shape:", y.shape)

print("\nPreprocessing Complete!")