import pandas as pd  

def healthy (df):
    healthy_map = {
        'chicken': 'protein',
        'meat': 'protein',
        'steak': 'protein',
        'fish': 'protein',
        'salmon': 'protein',
        'protein': 'protein',
        'egg': 'protein',

        'vegetable': 'vegetables',
        'veggie': 'vegetables',
        'greens': 'vegetables',
        'salad': 'vegetables',
        'broccoli': 'vegetables',
        'asparagus': 'vegetables',
        'zucchini': 'vegetables',
        'tomatoes': 'vegetables',

        'fruit': 'fruits',
        'berries': 'fruits',

        'rice': 'carbs',
        'pasta': 'carbs',
        'quinoa': 'carbs',
        'bread': 'carbs',
        'potato': 'carbs',
        'starch': 'carbs',
        'carb': 'carbs',

        'lean': 'lean/prep',
        'grilled': 'lean/prep',
        'cooked yourself': 'lean/prep',
        'nonprocessed': 'lean/prep',
        'homemade': 'lean/prep',

        'balanced': 'balanced',
        'all food groups': 'balanced',
        'food pyramid': 'balanced',
        'every food group': 'balanced',

        'color': 'color/variety',
        'variety': 'color/variety',
        'rainbow': 'color/variety',

        'low fat': 'low fat/sugar',
        'low carbs': 'low fat/sugar',
        'low calories': 'low fat/sugar',
        'low sugar': 'low fat/sugar',

        'water': 'drink',
        'milk': 'drink',
        'soda': 'drink'
    }


    def categorize_healthy(text):
        if pd.isnull(text):
            return ['unknown']

        matched = []

        for keyword, category in healthy_map.items():
            if keyword in text:
                matched.append(category)

        return sorted(set(matched)) if matched else ['other']

    df['healthy_meal'] = df['healthy_meal'].apply(categorize_healthy).apply(lambda x: ', '.join(x))


