
import pandas as pd     
def childhood (df):   
    childhood_map = {
        'tacos': 'ethnic',
        'quesadillas' : 'ethnic',
        'casserole' : 'ethnic',
        'adobo': 'ethnic',
        'biryani': 'ethnic',
        'jollof': 'ethnic',
        'isombe': 'ethnic',
        'plantains': 'ethnic',
        'ugali': 'ethnic',
        'curry': 'ethnic',
        'stromboli': 'ethnic',

        'chicken': 'protein',
        'beef': 'protein',
        'fish' : 'protein',

        'pizza': 'fast food',
        'fries' : 'fast food',
        'hamburgers' : 'fast food',
        'hot dogs' : 'fast food',
        'sloppy joes': 'fast food',
        'hot pockets': 'fast food',

        'rice' : 'carbs',
        'beans' :'carbs',
        'mac and cheese' : 'carbs',
        'pasta': 'carbs',
        'macaroni': 'carbs',
        'spaghetti': 'carbs',
        'lasagna': 'carbs',
        'tortellini': 'carbs',
        'manicotti': 'carbs',
        'noodle': 'carbs',
        'bread': 'carbs',
        'rolls': 'carbs',
        'potatoes': 'carbs',
        'potato': 'carbs',
        'rice': 'carbs',
        'dumplings': 'carbs',

        'biscuits' : 'sweet',
        'chocolate': 'sweet',
        'cookies': 'sweet',
        'pop tarts': 'sweet',
        'tiramisu': 'sweet', 
        'waffles': 'sweet',
        'salad': 'healthy',
        'soup': 'healthy'
    }

    def food_childhood_helper(text):
        if pd.isnull(text):
            return ['other']
        
        matched = []
        for keyword, label in childhood_map.items():
            if keyword in text:
                matched.append(label)

        matched = sorted(set(matched))

        return matched if matched else ['other']

    df['food_childhood'] = df['food_childhood'].apply(food_childhood_helper).apply(lambda x: ', '.join(x))