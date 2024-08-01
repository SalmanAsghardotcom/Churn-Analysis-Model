
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Loading the datasets
file_20 = 'churn-bigml-20.csv'
file_80 = 'churn-bigml-80.csv'

data_20 = pd.read_csv(file_20)
data_80 = pd.read_csv(file_80)

# Merging both sets
data = pd.concat([data_20, data_80], axis=0)

# Checking for missing values
missing_values = data.isnull().sum()

# Encoding categorical features
label_encoder = LabelEncoder()
for column in data.select_dtypes(include=['object']).columns:
    if column != 'Churn':
        data[column] = label_encoder.fit_transform(data[column])

# Encoding the target variable
data['Churn'] = label_encoder.fit_transform(data['Churn'])

# Normalizing the numerical features
scaler = StandardScaler()
numerical_features = data.select_dtypes(include=['int64', 'float64']).columns
data[numerical_features] = scaler.fit_transform(data[numerical_features])

# Splitting the data into training and testing sets
X = data.drop('Churn', axis=1)
y = data['Churn'].astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predicting on the test set
y_pred = clf.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Saving the trained model
joblib.dump(clf, 'churn_model.pkl')

# Saving the processed dataset
data.to_csv('processed_telco_churn_data.csv', index=False)

# Outputting results
print("Missing values:", missing_values)
print("Model accuracy:", accuracy)
print("Classification report:\n", report)
