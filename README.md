
# Churn Prediction Model

This project details the development and evaluation of a churn prediction model for a telecommunications company. The primary objective of this model is to predict whether a customer will churn (i.e., leave the service) based on their demographic, account, and usage data.

## Dataset

The dataset used for this model is the Telco Customer Churn dataset obtained from Kaggle. It contains various features related to customer demographics, account information, and usage patterns. The dataset was split into two parts: one containing 20% of the data and the other containing 80% of the data. The combined dataset includes the following features:
- State: The state in which the customer resides
- Account length: The duration of the customer's account
- Area code: The area code of the customer's phone number
- International plan: Whether the customer has an international plan
- Voice mail plan: Whether the customer has a voicemail plan
- Number of voicemail messages: Number of voicemail messages
- Total day minutes: Total minutes of calls during the day
- Total day calls: Total number of calls during the day
- Total day charge: Total charges for calls during the day
- Total evening minutes: Total minutes of calls during the evening
- Total evening calls: Total number of calls during the evening
- Total evening charge: Total charges for calls during the evening
- Total night minutes: Total minutes of calls during the night
- Total night calls: Total number of calls during the night
- Total night charge: Total charges for calls during the night
- Total international minutes: Total minutes of international calls
- Total international calls: Total number of international calls
- Total international charge: Total charges for international calls
- Customer service calls: Number of calls to customer service
- Churn: Whether the customer churned (target variable)

## Data Preprocessing

Data preprocessing is a crucial step to prepare the raw data for model training. The following steps were performed:
- Combined the two datasets into one.
- Checked for missing values and found none.
- Encoded categorical features using Label Encoding.
- Normalized numerical features using Standard Scaler.
- Split the data into training (80%) and testing (20%) sets.

## Model Building

A Random Forest classifier was used to build the churn prediction model. Random Forest is a robust and widely used algorithm for classification tasks. The model was trained using the training dataset and evaluated on the test dataset. The training process involved fitting the model to the training data and tuning hyperparameters to achieve the best performance.

## Model Evaluation

The model achieved an accuracy of approximately 95%. The detailed classification report is as follows:
```
              precision    recall  f1-score   support

           0       0.96      0.99      0.97       571
           2       0.91      0.73      0.81        96

    accuracy                           0.95       667
   macro avg       0.93      0.86      0.89       667
weighted avg       0.95      0.95      0.95       667
```

## Business Analysis Perspective

From a business perspective, the churn prediction model provides valuable insights that can help the telecommunications company in several ways:
1. **Customer Retention**: By identifying customers who are at risk of churning, the company can proactively reach out to these customers with targeted offers, discounts, or personalized services to retain them.
2. **Resource Allocation**: The model helps in allocating resources more effectively by focusing on high-risk customers. This ensures that retention efforts are directed towards customers who are most likely to churn, maximizing the return on investment.
3. **Customer Satisfaction**: Understanding the factors that contribute to churn allows the company to address common issues and improve overall customer satisfaction. For instance, if customers with high service call rates are more likely to churn, the company can work on improving customer service quality.
4. **Revenue Growth**: Reducing churn directly impacts the company's revenue growth. Retaining existing customers is often more cost-effective than acquiring new ones. By lowering churn rates, the company can achieve steady revenue growth.
5. **Competitive Advantage**: Having a robust churn prediction model gives the company a competitive edge. It enables the company to stay ahead of competitors by maintaining a loyal customer base and minimizing churn rates.

## Conclusion

The churn prediction model developed in this project demonstrates high accuracy and robust performance in predicting customer churn. With an accuracy of 95%, it can be effectively used by the telecommunications company to identify customers at risk of churning and implement targeted retention strategies. The model not only helps in reducing churn rates but also provides valuable business insights that can drive customer satisfaction and revenue growth.

Future work can focus on enhancing the model by incorporating additional features, using advanced machine learning algorithms, and performing hyperparameter tuning. Continuous monitoring and updating of the model are also essential to ensure its relevance and accuracy over time.

## Files

- `churn_prediction_model.py`: Python script containing the code for data preprocessing, model building, and evaluation.
- `churn_model.pkl`: Trained Random Forest model.
- `processed_telco_churn_data.csv`: Processed dataset used for model training and evaluation.
- `Churn_Prediction_Model_Report_Detailed.docx`: Detailed report of the project.

