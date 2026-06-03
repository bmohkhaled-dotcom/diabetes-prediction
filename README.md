# Diabetes Readmission Prediction Using Machine Learning

## Introduction
Diabetes readmission refers to the repeated hospitalization of patients who have previously been treated for diabetes-related conditions. It is a major concern in healthcare systems because it indicates poor disease management, complications, or ineffective treatment after discharge. Predicting readmission risk is important as it helps hospitals and healthcare providers identify high-risk patients early, improve post-discharge care, and reduce healthcare costs. With the help of machine learning, patterns in patient history, medications, lab results, and hospital visits can be analyzed to predict whether a diabetic patient is likely to be readmitted, enabling better decision-making and improved patient outcomes.

## Project Description
This project focuses on predicting diabetes-related hospital readmission using the diabetic_data.csv dataset, which contains 101,766 patient records and 50 medical features collected from hospital encounters. The dataset includes demographic information (such as age, gender, and race), clinical details (lab procedures, diagnoses, and number of medications), and hospital utilization features (time in hospital, number of emergency visits, and inpatient visits).

The dataset is not fully clean, as it contains missing values represented by “?” and requires preprocessing, including handling missing data by mode, encoding categorical variables, and removing duplicates  remove non essential features such as weight. After data cleaning, exploratory data analysis was performed to understand relationships between variables and readmission outcomes.Both univariate and multivariate plots were performed for univerate we used Gender distrubution, age and Readmission distrubution.On the otherhand, for multivariate we used readmission against medication, Readmission against age, time spent in hospital and correlation heatmap for the features Feature engineering was applied to create new variables such as total patient visits and encode categorial variables

Multiple machine learning models, including Logistic Regression, Random Forest, and Decision Tree, were trained and compared using evaluation metrics such as accuracy, precision, recall, and F1-score. The best-performing model was selected which is random forest, after hyperparameter tuning using GridSearchCV. Finally, the trained model was deployed using a Streamlit web application to provide real-time predictions of whether a diabetic patient is likely to be readmitted.
## Data set source
https://www.kaggle.com/datasets/brandao/diabetes?select=diabetic_data.csv
## Live Demo
https://machine-project-git-htqeua4nvzmhs39ppo39ck.streamlit.app/
## Libaries
- pandas
- numpy
- matplotlib
- seaborn
- joblib
- streamlit
  ## Results
  ## Accuracy,precision,F1score and Recall
  	-       Logestic Regression	Decision Tree	Random Forest
  	- Accuracy	     0.569	      0.474	        0.580
  	- Precision	    0.534       	0.476	        0.550
  	- Recall	       0.569	      0.474	        0.580
  	- F1 score      0.498         0.475	        0.533
  


 ## Video
https://drive.google.com/file/d/1Z-TamGQQtk1r7GpVa0CtocqxpvTnKe9d/view?usp=sharing
## Team
Basel Mohamed
