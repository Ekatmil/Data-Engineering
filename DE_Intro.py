import pandas as pd


def info(df):
    df.info()
    df.dtypes.value_counts()

    missing_counts = df.isnull().sum()
    missing_df = pd.DataFrame({
        'missing_count': missing_counts,
        'dtype': df.dtypes
    })
    missing_df = missing_df[missing_df['missing_count'] > 0]
    print(missing_df)


    final_order = [
    
        'GPA', 'Gender', 'grade_level', 'income', 'marital_status', 'employment',
        'father_education', 'mother_education',
        'father_profession', 'mother_profession',

        'diet_current', 'ideal_diet', 'ideal_diet_coded',
        'comfort_food', 'comfort_food_categories', 'comfort_food_reasons', 'eating_changes',
        'meals_dinner_friend',  'fav_cuisine', 'fav_cuisine_coded', 
        'food_childhood', 'healthy_feeling', 'healthy_meal',

        'weight', 'self_perception_weight', 'exercise', 'sports', 'type_sports',

        'fruit_day', 'veggies_day', 'vitamins', 'soup', 'fries', 'coffee', 'drink',
        'calories_day', 'calories_chicken', 'calories_scone', 'waffle_calories', 'turkey_calories', 'tortilla_calories',

        'comfort_food_reasons_coded', 'comfort_food_reasons_coded.1',
        'diet_current_coded', 'eating_changes_coded', 'eating_changes_coded1',
        'ethnic_food', 'on_off_campus', 'parents_cook', 'cook', 'cuisine',
        'nutritional_check', 'pay_meal_out', 'breakfast', 'eating_out',

        'greek_food', 'indian_food', 'italian_food', 'persian_food', 'thai_food',

        'fav_food', 'life_rewarding'
    ]

    # Apply to DataFrame
    df = df[[col for col in final_order if col in df.columns] + [col for col in df.columns if col not in final_order]]

