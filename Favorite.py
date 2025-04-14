import pandas as pd

def favorite_dish (df):
    dish_map = {
        'italian': 'italian',
        'italia': 'italian',
        'pasta': 'italian',
        'pizza': 'italian',

        'mexican': 'mexican',
        'mex': 'mexican',
        'tacos': 'mexican',

        'indian': 'indian',
        'curry': 'indian',

        'chinese': 'asian',
        'asian': 'asian',
        'japanese': 'asian',
        'korean': 'asian',
        'thai': 'asian',
        'sushi': 'asian',
        'chow mani noodles' : 'asian',

        'home cooked': 'home cooked',
        'homemade': 'home cooked',

        'american': 'american',
        'burgers': 'american',
        'bbq': 'american',
        'mac and cheese' : 'american',

        'hispanic cuisine': 'hispanic',
        'jamaican': 'hispanic',
        'colombian':'hispanic',

        'mediterranean': 'mediterranean',
        'greek': 'mediterranean',
        'middle eastern': 'mediterranean',
        'arabic cuisine': 'mediterranean',
        'turkish' : 'mediterranean',

        'vegan': 'healthy',
        'salads': 'healthy',
        'healthy': 'healthy',
        'lean': 'healthy',

        'no preference': 'none',
        'none': 'none',
        'idk': 'none',
        'any': 'none'
    }

    def fav_category(text):
        if pd.isnull(text):
            return ['other']

        text = str(text).strip()
        matched = []

        for keyword, label in dish_map.items():
            if keyword in text:
                matched.append(label)
        
        if 'none' in matched and len(matched) > 1:
            matched.remove('none')

        matched = sorted(set(matched))
        return matched if matched else ['other']

    df['fav_cuisine'] = df['fav_cuisine'].apply(fav_category).apply(lambda x: ', '.join(x))