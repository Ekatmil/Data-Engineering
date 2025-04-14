
import pandas as pd

def comfort_food (df):


    # step 1: check what are the entries 

    df['comfort_food_list'] = df['comfort_food'].dropna().apply(lambda x: [i.strip() for i in x.split(',')])
    # all_foods = list(chain.from_iterable(df['comfort_food_list'].dropna()))
    # food_counts = Counter(all_foods)
    # food_df = pd.DataFrame.from_dict(food_counts, orient='index', columns=['count'])
    # food_df = food_df.sort_values(by='count', ascending=False)
    # print(food_df.head(100))
    # print (food_counts)

    # step 2: normalization 
    normalized = {
    'ice crea': 'ice cream',
    'icecream': 'ice cream',
    'ice-cream': 'ice cream',
    'ice crea': 'ice cream',
    'ice cream.': 'ice cream',

    'chinese': 'asian food',
    "grandma's chinese": 'asian food',
    'korean food' : 'asian food',
    'chinese food' : 'asian food',
    'indian': 'asian food',
    'sushi': 'asian food',

    'mac n cheese': 'mac and cheese',
    'macaroni': 'mac and cheese',
    'mac-n-cheese': 'mac and cheese',
    'mac in cheese': 'mac and cheese',
    'mac & cheese': 'mac and cheese',

    'peanut butter' : 'sweets',
    'frozen yogurt': 'sweets',
    'banana sandwich' : 'sweets',
    'peanut butter sandwich' : 'sweets',
    'dessets' : 'sweets',
    'nutella' : 'sweets',
    'peanut butter n chocolate ice cream' : 'sweets',
    'truffles' : 'sweets',
    'macaroons' : 'sweets',
    'candy': 'sweets',
    'sponge candy': 'sweets',
    'pancakes' : 'sweets',

    'quinoa' : 'cereal',

    'omelet' : 'egg',

    'fries': 'french fries',
    '& fries': 'french fries',
    'french fires' : 'french fries',

    'doughnuts': 'donuts',
    
    'mozzarella sticks': 'cheese',

    'spaghetti': 'pasta',
    'noodle ( any kinds of noodle)': 'pasta',
    'spaghetti squash': 'pasta',
    'pasta dishes' : 'pasta',

    'fried chicken': 'chicken',
    'wings': 'chicken',
    'chicken curry': 'chicken',
    'chicken tikka masala': 'chicken',
    'chicken fingers': 'chicken',
    'chicken wings': 'chicken',
    'grilled chicken' : 'chicken',

    'butter naan': 'bread', 
    'cornbread': 'bread',
    'garlic bread': 'bread',
    'toast': 'bread',

    'tuna sandwich' : 'sandwich',
    'deli sandwhich' : 'sandwich',
    'subs': 'sandwich',
    'meatball sub': 'sandwich',

    'chicken nuggets': 'fast food',
    'mcdonalds': 'fast food',
    'chicken nuggs': 'fast food',
    "moe's" : 'fast food',
    "moes": 'fast food',
    'burritos': 'fast food',

    'pierogies' : 'ethnic',
    'peruvian food from back home' : 'ethnic',
    'chipotle': 'ethnic',

    'salty snacks': 'snacks',
    'little debbie snacks': 'snacks',
    'chex mix': 'snacks',
    'chex-mix': 'snacks',
    'cheez-its': 'snacks',
    'slim jims' : 'snacks',
    'beef jerky' : 'snacks',
    'microwaveable foods' : 'snacks',

    'potato chips' : 'chips',
    'terra chips' : 'chips',
    'doritos' : 'chips',
    'plantain chips': 'chips',
    'chips.': 'chips',
    'salt and vinegar chips': 'chips',
    'chips sweets popcorn': 'chips',

    'dark chocolate': 'chocolate',
    'hot chocolate': 'chocolate',
    'chocolates': 'chocolate',

    'ritz': 'chocolate bar',
    'protein bars': 'chocolate bar',
    "reese's cups(dark chocolate)": 'chocolate bar',
    'pop': 'chocolate bar',
    'candy bars': 'chocolate bar',
    'kit kat': 'chocolate bar',
    'twizzlers': 'chocolate bar',

    'fruit snacks': 'fruit',
    'fritos': 'fruit',
    'watermelon' : 'fruit',
    'grapes': 'fruit',

    'pretzals': 'pretzels',
    'pretzels.': 'pretzels',

    'chicken noodle soup': 'soup',
    'chilli' : 'soup',
    'seaweed soup': 'soup',
    'tomato soup' : 'soup',
    'potato soup' : 'soup',

    'cookies': 'cookie',
    'cookie dough': 'cookie',
    'wegmans cookies' : 'cookie',
    'chocolate brownie': 'cookie',
    'crackers with cottage cheese' : 'cookie',
    'frosted brownies': 'cookie',
    'brownies': 'cookie',

    'grandma homemade chocolate cake anything homemade' : 'cake',
    'cheesecake' : 'cake',
    'pot pie': 'cake',
    
    'burgers': 'burger',
    'cheeseburgers': 'burger',
    'hamburgers': 'burger',

    'soda.' : 'soda',
    'pepper': 'soda',
    'pepsi': 'soda',

    'mashed potatoes' : 'potatoes',
    'potato' : 'potatoes',

    'stuffed peppers': 'vegetables',
    'cucumber': 'vegetables',
    'broccoli' : 'vegetables',
    'carrots' : 'vegetables',

    'homemade lasagne': 'lasagna',

    'pizza cookies steak' : 'pizza',
    'pizza chocolate chips bagels ice capps' : 'pizza', 

    'milkshakes' : 'milkshake', 

    'salsa' : 'dip', 
    'ranch' : 'dip',

    'saltfish': 'fish',

    '' : 'nan',
    'none': 'nan'
}

    def normalize_food_list(food_list):
        if not isinstance(food_list, list):
            return []
    
        cleaned = [
            normalized.get(item.strip().strip('.'), item.strip().strip('.'))
            for item in food_list
        ]
        return [i for i in cleaned if i and i != 'dr']

    df['comfort_food_list'] = df['comfort_food_list'].apply(normalize_food_list).apply(lambda x: sorted(x) if isinstance(x, list) else x)


    #step 3: categorize 
    categorier = {
        'ice cream': 'sweet',
        'chocolate': 'sweet',
        'cookie': 'sweet',
        'cake': 'sweet',
        'sweets': 'sweet',
        'donuts': 'sweet',
        'milkshake': 'sweet',
        'chocolate bar': 'sweet',

        'pizza': 'fast food',
        'burger': 'fast food',
        'french fries': 'fast food',
        'fast food': 'fast food',

        'mac and cheese': 'carbs',
        'pasta': 'carbs',
        'bread': 'carbs',
        'potatoes': 'carbs',
        'lasagna': 'carbs',
        'rice': 'carbs',
        'cereal': 'carbs',

        'chicken': 'protein',
        'fish': 'protein',

        'snack': 'snack',
        'snacks': 'snack',
        'chips': 'snack',
        'popcorn' : 'snack',
        'pretzels': 'snack',
        'dip': 'snack',
        'cheese': 'snack',

        'fruit': 'healthy',
        'vegetables': 'healthy',
        'sandwich': 'healthy',
        'soup': 'healthy',
        'egg': 'healthy',

        'ethnic': 'ethnic',
        'asian food': 'ethnic',

        'soda': 'drink',
        'coffee': 'drink',
        'wine': 'drink'
    }

    def categorize_foods(food_list):
        if not isinstance(food_list, list):
            return []

        categories = [categorier[item] for item in food_list if item in categorier]

        return sorted(set(categories)) if categories else ['unknown']

    df['comfort_food_categories'] = df['comfort_food_list'].apply(categorize_foods).apply(lambda x: ', '.join(x))
    df['comfort_food'] = df['comfort_food_list'].apply(lambda x: ', '.join(x))
    df.drop(columns=['comfort_food_list'], inplace=True)