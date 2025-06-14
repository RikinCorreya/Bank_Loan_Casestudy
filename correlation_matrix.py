import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'C:/Users/rikin/Desktop/Trainity/Bank Loan Case Study (Project6)/New_Updated_Workbooks/application_data_CLEANED_DATA_ANALYSIS.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1', header=2)

# Filtering the DataFrame to include only rows where TARGET is 0 (repaid)
df_repaid = df[df['TARGET'] == 1]

columns_to_analyze = [
    'AMT_INCOME_TOTAL',
    'AMT_CREDIT',
    'AMT_ANNUITY',
    'AMT_GOODS_PRICE',
    'AGE',
    'YEARS_EMPLOYED',
    'YEARS_REGISTRATION',
    'YEARS_ID_PUBLISH',
    'CNT_FAM_MEMBERS',
    'REGION_RATING_CLIENT',
    'REGION_POPULATION_RELATIVE',
    'HOUR_APPR_PROCESS_START',
    'EXT_SOURCE_2',
    'EXT_SOURCE_3',
    'OBS_30_CNT_SOCIAL_CIRCLE',
    'DEF_30_CNT_SOCIAL_CIRCLE',
    'OBS_60_CNT_SOCIAL_CIRCLE',
    'DEF_60_CNT_SOCIAL_CIRCLE',
    'YEARS_LAST_PHONE_Change',
    'AMT_REQ_CREDIT_BUREAU_HOUR',
    'AMT_REQ_CREDIT_BUREAU_DAY',
    'AMT_REQ_CREDIT_BUREAU_WEEK'
]
df_selected = df_repaid[columns_to_analyze]


correlation_matrix = df_selected.corr()

plt.figure(figsize=(12, 10))  # Adjusted for better visibility with more columns

# Create the heatmap using seaborn
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, fmt='.2f', cbar=True)

plt.title('Correlation Heatmap of All Columns (Defaulters Only)')
plt.show()
