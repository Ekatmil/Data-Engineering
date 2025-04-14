import pandas as pd       

def dinner (df): 
    dinner_map = {
            'pizza': 'pizza',

            'pasta': 'pasta',
            'spaghetti': 'pasta',
            'mac and cheese': 'pasta',
            'mac n cheese': 'pasta',
            'mac & cheese': 'pasta',
            'lasagna': 'pasta',
            'manicotti': 'pasta',
            'tortellini': 'pasta',

            'steak': 'meat',
            'beef': 'meat',
            'burgers': 'meat',
            'hamburgers': 'meat',
            'sloppy joe': 'meat',
            'roast beef': 'meat',
            'meatloaf': 'meat',

            'chicken': 'chicken',

            'fish': 'fish',
            'salmon': 'fish',
            'crab': 'fish',
            'shrimp': 'fish',
            'seafood': 'fish',
            'lobster': 'fish',
            'tuna': 'fish',

            'eggs': 'breakfast',
            'french toast': 'breakfast',
            'pancakes': 'breakfast',
            'waffles': 'breakfast',
            'cereal': 'breakfast',
            'breakfast': 'breakfast',

            'rice': 'carbs',
            'bread': 'carbs',
            'potato': 'carbs',
            'potatoes': 'carbs',

            'chocolate': 'sweet',
            'cookies': 'sweet',
            'ice cream': 'sweet',
            'pop tarts': 'sweet',
            'dessert': 'sweet',
            'pudding': 'sweet',

            'grilled cheese': 'sandwich',
            'sandwich': 'sandwich',
            'wrap': 'sandwich',
            'hot dog': 'sandwich',
            'panini': 'sandwich',

            'tacos': 'mexican',
            'burrito': 'mexican',
            'quesadillas': 'mexican',

            'pho': 'asian',
            'dumplings': 'asian',
            'noodles': 'asian',
            'chinese': 'asian',
            'korean': 'asian',
            'japanese': 'asian',
            'thai': 'asian',
            'vietnamese': 'asian',

            'vegetable': 'healthy',
            'salad': 'healthy',
            'asparagus': 'healthy',
            'broccoli': 'healthy',
            'edamame': 'healthy',

            'soup': 'soup',

            'unknown': 'unknown'
        }

    def categorize_dinner(text):
        if pd.isnull(text):
            return ['unknown']

        matched = []

        for keyword, category in dinner_map.items():
            if keyword in text:
                matched.append(category)

        return sorted(set(matched)) if matched else ['other']

    df['meals_dinner_friend'] = df['meals_dinner_friend'].apply(categorize_dinner).apply(lambda x: ', '.join(x))