# Diabetes Readmission Prediction Using Machine Learning

## Introduction
Diabetes readmission refers to the repeated hospitalization of patients who have previously been treated for diabetes-related conditions. It is a major concern in healthcare systems because it indicates poor disease management, complications, or ineffective treatment after discharge. Predicting readmission risk is important as it helps hospitals and healthcare providers identify high-risk patients early, improve post-discharge care, and reduce healthcare costs. With the help of machine learning, patterns in patient history, medications, lab results, and hospital visits can be analyzed to predict whether a diabetic patient is likely to be readmitted, enabling better decision-making and improved patient outcomes.

## Project Description
This project focuses on predicting diabetes-related hospital readmission using the diabetic_data.csv dataset, which contains 101,766 patient records and 50 medical features collected from hospital encounters. The dataset includes demographic information (such as age, gender, and race), clinical details (lab procedures, diagnoses, and number of medications), and hospital utilization features (time in hospital, number of emergency visits, and inpatient visits).

The dataset is not fully clean, as it contains missing values represented by “?” and requires preprocessing, including handling missing data by mode, encoding categorical variables, and removing duplicates  remove non essential features such as weight. After data cleaning, exploratory data analysis was performed to understand relationships between variables and readmission outcomes.Both univerate and multiverate plots were performed for univerate we used Gender distrubution, age and Redmesion distruvution.On the otherhand, for multiverate we used readmission against medication, Readmission against age, time spent in hospital and corrolation heatmap for the features Feature engineering was applied to create new variables such as total patient visits and encode categorial variables

Multiple machine learning models, including Logistic Regression, Random Forest, and Decision Tree, were trained and compared using evaluation metrics such as accuracy, precision, recall, and F1-score. The best-performing model was selected which is random forest, after hyperparameter tuning using GridSearchCV. Finally, the trained model was deployed using a Streamlit web application to provide real-time predictions of whether a diabetic patient is likely to be readmitted.
## Data set source
https://www.kaggle.com/datasets/brandao/diabetes?select=diabetic_data.csv
## Live Demo
https://machine-project-git-htqeua4nvzmhs39ppo39ck.streamlit.app/
## Liberies
 pandas
 numpy
 matplotlib.pyplot
 joblib
 streamlit
 ## Video
 https://export-download.canva.com/79ff84c2-aaca-4b32-ab63-585cf0d86d2e/0-4811475551354273725.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUH5AO7UJ26%2F20260602%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260602T213304Z&X-Amz-Expires=63994&X-Amz-Signature=778e77e24e95fdd17e73e56ffd79690df99766cc448ae2397b8a60af4377a9ca&X-Amz-SignedHeaders=host&response-content-disposition=attachment%3B%20filename%2A%3DUTF-8%27%27Diabetes%2520Readmission%2520Prediction.mp4&response-expires=Wed%2C%2003%20Jun%202026%2015%3A19%3A38%20GMT
 
## Team
Basel Mohamed
