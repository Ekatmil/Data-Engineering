import pandas as pd

from DE_Intro import info
from Comfort_Reason import comfort_reasons
from Comfort_Food import comfort_food
from Diet import diet
from Change import eating_change
from Prof import proffesion
from Favorite import favorite_dish
from Childhood import childhood
from Dinner import dinner
from Sport import sport
from Healthy_Meal import healthy 

#Read file 
df = pd.read_csv('food_coded.csv')

#Step 1: Getting Info (types, missing data) + Formating Order 
info(df)

# Step 2: Cleaning 

#2.1 -- Fix non-numeric columns

#2.1.1. -- GPA fix from object to numeric
df['GPA'] = pd.to_numeric(df['GPA'], errors='coerce')

#2.1.2 -- Weight fix from object to numeric
df['weight'].unique()

def only_digits(val):
    if pd.isnull(val):
        return None
    digits = ''.join(filter(str.isdigit, str(val)))
    return float(digits) if digits else None

df['weight'] = df['weight'].apply(only_digits)

#2.2 -- All objects to lowercase and change all "and", "/", ". " to "," 

# Special Cases (do not change "and")
protected = {
    "mac and cheese": "mac_and_cheese",
    "salt and vinegar": "salt_and_vinegar"
}

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.lower().str.strip()
    
    for phrase, placeholder in protected.items():
        df[col] = df[col].str.replace(phrase, placeholder, regex=False)
    
    df[col] = (
        df[col]
        .str.replace(", and ", ", ", regex=False)
        .str.replace(" and ", ", ", regex=False)
        .str.replace("/", ", ", regex=False)
        .str.replace("\r", ", ", regex=False)
        .str.replace(". ", ", ", regex=False)
    )
    for phrase, placeholder in protected.items():
        df[col] = df[col].str.replace(placeholder, phrase, regex=False)

#2.3 -- Filling missing values for numeric columns
df.fillna(df.median(numeric_only=True), inplace=True)

#2.4 -- Dealing with columns with objects

#2.4.1 -- Comfort Food Reason - > labels 
comfort_reasons(df)

#2.4.2 -- Comfort Food -> put all into standart form and add column with categorization
comfort_food(df)

#2.4.3 -- Diet_current and Ideal Diet -> put all reasons into standart (category)
# print(df['diet_current'].dropna().unique())
# print(df['ideal_diet'].dropna().unique())
diet(df)

#2.4.4 -- Eating Changes -> Categorize everything 
# print(df['eating_changes'].dropna().unique())
eating_change(df)

#2.4.5 -- Father Profession and Mother Profession -> Categorized
# print(df['father_profession'].dropna().unique())
# print(df['mother_profession'].dropna().unique())
proffesion(df)

#2.4.6 -- Fav Cuisine -> everything into standart
# print(df['fav_cuisine'].dropna().unique())
favorite_dish (df)

#2.4.7 -- Food Childhood -> Categorized
#print(df['food_childhood'].dropna().unique())
childhood (df)

#2.4.8 -- Meals Dinner Friend -> Categorized
# print(df['meals_dinner_friend'].dropna().unique())
dinner (df)

#2.4.9 -- Type Sport -> Put into Standard
# print(df['type_sports'].dropna().unique())
sport (df)

#2.4.10 -- Healthy Meal -> Categorize
# print(df['healthy_meal'].dropna().unique())
healthy (df)


#STEP 3 -- Save data into a new file (print summary)

df.to_csv("food_coded_cleaned.csv", index=False)

print ("New CSV File is Created")

summary = pd.DataFrame({
    'Column': df.columns,
    'Missing': df.isnull().sum().values,
    'Unique': df.nunique().values,
    'Type': df.dtypes.values
})
print(summary)

print(df.describe(include='all'))
