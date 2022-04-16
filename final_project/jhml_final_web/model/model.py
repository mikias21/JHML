# Imports 
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTE
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.base import TransformerMixin, BaseEstimator 
from sklearn.preprocessing import StandardScaler, OneHotEncoder


# Load dataset
stroke_dataset = pd.read_csv('./dataset/healthcare-dataset-stroke-data.csv')
stroke_dataset.head()

# Clean 'other' value from gender column
stroke_dataset = stroke_dataset[stroke_dataset.gender != 'Other']

# Get X and Y values 
X = stroke_dataset.iloc[:, :-1]
y = stroke_dataset.iloc[:, -1]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Remove the ID column
for set_ in (X_train, X_test):
    set_.drop("id", axis=1, inplace=True)

# Create custom transformer to add attributes 
age_index, avg_glucose_index, bmi_index = 0, 3, 4

class CombinedAttributeAdder(TransformerMixin, BaseEstimator):
    def fit(self, X, y=None):
        return self 
    def transform(self, X, y=None):
        age_per_bmi = X[:, age_index] / X[:, bmi_index]
        age_per_avg_glucose= X[:, age_index] / X[:, avg_glucose_index]
        return np.c_[X, age_per_bmi, age_per_avg_glucose]


# Preprocess data 
x_numeric_attributes = X_train.drop(['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status'], axis=1)
numeric_attributes = list(x_numeric_attributes)
categorical_attributes = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']

# Create Pipelines and transform data 
num_pipeline = Pipeline(
    [
        ('imputer', SimpleImputer(strategy='median')),
        ('attribute_adder', CombinedAttributeAdder()),
        ('std_scaler', StandardScaler())
    ]
)

full_pipeline = ColumnTransformer(
    [
        ('num', num_pipeline, numeric_attributes),
        ('cat', OneHotEncoder(), categorical_attributes)
    ]
)

X_train_processed = full_pipeline.fit_transform(X_train)

# Transform testing data
X_test = full_pipeline.transform(X_test)

# # Use SMOTE to solve the class imbalance problem 
smote = SMOTE()
x_resample, y_resample = smote.fit_resample(X_train_processed, y_train.ravel())


def make_prediction(data):
    rf_classifier = RandomForestClassifier(random_state=42)
    rf_classifier.fit(x_resample, y_resample)
    prediction = rf_classifier.predict(X_test)
    data_prediction = rf_classifier.predict(full_pipeline.transform(data))
    accuracy = (round(accuracy_score(y_test, prediction), 2)) * 100 
    f1score = (round(f1_score(y_test, prediction), 2)) * 100
    print('Accuracy ', accuracy)
    print('F1-Score ', f1score)
    return data_prediction 