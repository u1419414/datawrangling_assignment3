
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn2_circles, venn3, venn3_circles

# Load the dataset
df = pd.read_csv('DW3_set_exercise.csv')

# Convert 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Define the COVID and diabetes codes
covid_codes = ['U07.1', 'J12.82']
diabetes_codes = ['E08', 'E09', 'E10', 'E11', 'E13']

# Diabetes Set
print("Diabetes Set:")
diabetes_patients = df[df['Diagnosis Code'].isin(diabetes_codes)]
print(diabetes_patients['Patient ID'].tolist())

# Cardinality of the Diabetes set
print("\nCardinality of the Diabetes set:", len(diabetes_patients))

# COVID Set
print("\nCOVID Set:")
covid_patients = df[df['Diagnosis Code'].isin(covid_codes)]
print(covid_patients['Patient ID'].tolist())

# Cardinality of the COVID set
print("\nCardinality of the COVID set:", len(covid_patients))

# Intersection Set
print("\nIntersection Set:")
intersection_patients = df[df['Patient ID'].isin(diabetes_patients['Patient ID']) & df['Patient ID'].isin(covid_patients['Patient ID'])]
print(intersection_patients['Patient ID'].tolist())

# Cardinality of the Intersection set
print("\nCardinality of the Intersection set:", len(intersection_patients))

# Union Set
print("\nUnion Set:")
union_patients = pd.concat([diabetes_patients, covid_patients]).drop_duplicates()
print(union_patients['Patient ID'].tolist())

# Cardinality of the Union set
print("\nCardinality of the Union set:", len(union_patients))

print("========================================================")


diabetes_set = set(diabetes_patients['Patient ID'])
covid_set = set(covid_patients['Patient ID'])
intersection_set = diabetes_set.intersection(covid_set)
union_set = diabetes_set.union(covid_set)

# Create the Venn diagram
venn2(subsets=(len(diabetes_set), len(covid_set), len(intersection_set)),
      set_labels=('Diabetes', 'COVID'))

# Add labels
plt.text(0.3, 0.6, len(intersection_set), color='white')
plt.text(0.8, 0.6, len(covid_set) - len(intersection_set), color='white')
plt.text(0.05, 0.1, len(diabetes_set) - len(intersection_set), color='white')

# Add title
plt.title('Venn Diagram of Diabetes and COVID Sets')

# Display the Venn diagram
plt.show()


print("========================================================")


# Diabetes only after COVID Set
print("\nDiabetes only after COVID Set:")
covid_max_date = covid_patients['Date'].max()
diabetes_after_covid = df[(df['Diagnosis Code'].isin(diabetes_codes)) & (df['Date'] > covid_max_date)]
diabetes_only_after_covid = diabetes_after_covid[~diabetes_after_covid['Patient ID'].isin(covid_patients['Patient ID'])]
print(diabetes_only_after_covid['Patient ID'].tolist())

# Cardinality of the Diabetes only after COVID set
print("\nCardinality of the Diabetes only after COVID set:", len(diabetes_only_after_covid))

# Count breakdown for each diabetes code occurring only after COVID
print("\nCount breakdown for each diabetes code occurring only after COVID:")
count_breakdown = diabetes_only_after_covid['Diagnosis Code'].value_counts()
print(count_breakdown)

