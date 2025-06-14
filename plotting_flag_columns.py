import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Excel file
file_path = r'C:\Users\rikin\Desktop\Trainity\Bank Loan Case Study (Project6)\New_Updated_Workbooks\application_data_forPython.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Checking the first few rows to understand the structure
print(df.head())


document_columns = [f'FLAG_DOCUMENT_{i}' for i in range(2, 22)]  # Identifying Columns

flag_columns = ['FLAG_MOBIL','FLAG_EMP_PHONE','FLAG_WORK_PHONE','FLAG_CONT_MOBILE','FLAG_PHONE','FLAG_EMAIL']
# Combining both columns
all_columns =  flag_columns + document_columns
target_column = 'TARGET'

# Define a color palette
palette = {0: 'blue', 1: 'red'}  # Blue for Repaid (0), Red for Defaulted (1)

# Analyze and plot data for all columns
for column in all_columns:
    if column in df.columns:  # Check if the column exists in the DataFrame
        # Grouping and counting using TARGET
        grouped = df.groupby([column, target_column]).size().reset_index(name='count')

        # Plotting the results
        plt.figure(figsize=(8, 6))
        sns.barplot(x=column, y='count', hue=target_column, data=grouped, palette=palette)

        # Setting plot labels and title
        plt.title(f'Counts of 0s and 1s in {column} by Loan Status (TARGET)')
        plt.xlabel(f'{column} (0: Not Provided, 1: Provided)')
        plt.ylabel('Count')


        handles = [plt.Rectangle((0,0),1,1, color=palette[0]),
                   plt.Rectangle((0,0),1,1, color=palette[1])]
        plt.legend(handles, ['Repaid (0)', 'Defaulted (1)'], title='TARGET', loc='upper right')


        plt.show()
    else:
        print(f'Column {column} not found in the DataFrame.')
