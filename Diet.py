# print(df['diet_current'].dropna().unique())

import pandas as pd

def diet (df):
    diet_standard = {
        'vegan': 'vegan',
        'vegaan': 'vegan',

        'vegetarian': 'vegetarian',
        'vegitarian': 'vegetarian',
        'vegeterian': 'vegetarian',
        'no meat' : 'vegetarian',
    
        'pescatarian': 'pescatarian',
        'fish only': 'pescatarian',

        'gluten free': 'gluten free',

        'keto': 'low carb',
        'paleo': 'low carb',
        'low carb': 'low carb',
        'low in carbohydrates' : 'low carb',
        'avoid carbs': 'low carb',
        'less carbs': 'low carb',
        'low in carbs': 'low carb',

        'eat healthy': 'healthy',
        'good': 'healthy',
        'very healthy' : 'healthy',
        'fruits and vegetables': 'healthy',
        'balanced': 'healthy',
        'good carbs': 'healthy',
        'protein': 'healthy',
        'all food groups': 'healthy',
        'organic': 'healthy',
        'lean meat': 'healthy',
        'healthy' : 'healthy',
        'healthier' : 'healthy',
        'veggies' : 'healthy',

        'junk food': 'unhealthy',
        'unhealthy': 'unhealthy',
        'sweets': 'unhealthy',
        'terrible': 'unhealthy',
        'poor': 'unhealthy',

        'dining hall' : 'university diet',
        'college' : 'university diet',
        'cafeteria' : 'university diet',
        'campus': 'university diet',

        'no diet': 'no diet',
        'none': 'none',
        'anything': 'no diet',
        'not strict': 'no diet',
        'whatever': 'no diet',
        'everything': 'no diet',
        'ice cream' : 'no diet',
        'cookie': 'no diet',
        'candy': 'no diet',
        'sweet': 'no diet',

        'bread': 'high carbs',
        'rice': 'high carbs',
        'carbs': 'high carbs',
        'pizza': 'high carbs',
        'oatmeal': 'high carbs',

        'meat': 'high protein',
        'chicken': 'high protein',
        'egg': 'high protein',
        'fish': 'high protein',
        'turkey': 'high protein',
        'steak' : 'high protein'
    }

    def diet_categories(text):
        if pd.isnull(text):
            return ['other']
        
        matched = []
        for keyword, label in diet_standard.items():
            if keyword in text:
                matched.append(label)
                
        matched = sorted(set(matched))

        if 'no diet' in matched and len(matched) > 1:
            matched.remove('no diet')
        
        return matched if matched else ['other']

    df['diet_current'] = df['diet_current'].apply(diet_categories).apply(lambda x: ', '.join(x))
    df['ideal_diet'] = df['ideal_diet'].apply(diet_categories).apply(lambda x: ', '.join(x))

