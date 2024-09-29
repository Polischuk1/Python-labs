import pandas as pd 
import numpy as np
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


print(f"Number of men: {men_count}")
print(f"Number of women: {women_count}")

xlsx = pd.ExcelFile('employees_range.xlsx')
df1 = pd.read_excel(xlsx,'younger_18')
num_18 = df1.shape[0]
print(f'Number of people younger 18 is {num_18}')

df2 = pd.read_excel(xlsx,'18-45')
num_45 = df2.shape[0]
print(f'Number of people within range 18 - 45 is {num_45}')

df3 = pd.read_excel(xlsx,'45-70')
num_70 = df3.shape[0]
print(f'Number of people within range  45-70 is {num_70}')

df4 = pd.read_excel(xlsx,'Older_70')
num_older_70 = df4.shape[0]
print(f'Number of people who is older than 70 is {num_older_70}')


age_groups = ['<18','18-45','45-70','>70']
num_people =  [num_18, num_45, num_70, num_older_70]

plt.bar(age_groups,num_people,color=['blue','purple','darkblue','slateblue'])

plt.title('Number of people in each age group')
plt.xlabel('Age group')
plt.ylabel('Number of people')

plt.show()



men_count_18 = sum([1 for gender in df1['Стать'] if gender.lower() == 'ч'])
women_count_18 = sum([1 for gender in df1['Стать'] if gender.lower() == 'ж'])

print(f"Number of men younger 18: {men_count_18}")
print(f"Number of women younger 18: {women_count_18}")


men_count_45 = sum([1 for gender in df2['Стать'] if gender.lower()== 'ч'])
women_count_45 = sum([1 for gender in df2['Стать'] if gender.lower()== 'ж'])

print(f"Number of men 18-45: {men_count_45}")
print(f"Number of women 18-45: {women_count_45}")


men_count_70 = sum([1 for gender in df3['Стать'] if gender.lower()== 'ч'])
women_count_70 = sum([1 for gender in df3['Стать'] if gender.lower()== 'ж'])

print(f"Number of men 45-70: {men_count_70}")
print(f"Number of women 45-70: {women_count_70}")



men_count_older_70 = sum([1 for gender in df4['Стать'] if gender.lower()== 'ч'])
women_count_older_70 = sum([1 for gender in df4['Стать'] if gender.lower()== 'ж'])

print(f"Number of men older 70: {men_count_older_70}")
print(f"Number of women older 70: {women_count_older_70}")


men_counts = [men_count_18, men_count_45, men_count_70, men_count_older_70]
women_counts = [women_count_18, women_count_45, women_count_70, women_count_older_70]

age_groups = ['<18', '18-45', '45-70', '>70']


bar_width = 0.35 
index = np.arange(len(age_groups)) 

fig, ax = plt.subplots()

bar1 = ax.bar(index, men_counts, bar_width, label='Men', color='blue')
bar2 = ax.bar(index + bar_width, women_counts, bar_width, label='Women', color='purple')

# Add labels, title, and legend
ax.set_xlabel('Age Group')
ax.set_ylabel('Number of People')
ax.set_title('Comparison of Men and Women Across Age Groups')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(age_groups)
ax.legend()


plt.tight_layout()
plt.show()