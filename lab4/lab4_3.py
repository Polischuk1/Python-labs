import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
try:
    df = pd.read_csv('employees.csv')
except:
    print('Impossible to open employees.csv')

gender_counts = df['Стать'].value_counts()

sns.barplot(x=gender_counts.index,y=gender_counts.values,palette='cubehelix')

plt.title('Comparison of Number of Men and Women')
plt.xlabel('Number of Persons')
plt.ylabel('Gender')
plt.show()


men_count = 0
women_count = 0


for index, row in df.iterrows():
  
    if row['Стать'].lower() == 'ч':  
        men_count += 1
    elif row['Стать'].lower() == 'ж':  
        women_count += 1

# Print out the results
print(f"Number of men: {men_count}")
print(f"Number of women: {women_count}")