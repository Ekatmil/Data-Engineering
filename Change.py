import pandas as pd

def eating_change (df):
    eat_change_map = {

        'healthier': 'healthier',
        'eat better': 'healthier',
        'self control': 'healthier',
        'more fruits': 'healthier',
        'more vegetables': 'healthier',
        'more veggies': 'healthier',
        'more salads': 'healthier',
        'clean': 'healthier',
        'avoid junk': 'healthier',

        'unhealthy': 'unhealthier',
        'junk food': 'unhealthier',
        'fried': 'unhealthier',
        'greasy': 'unhealthier',
        'sweets': 'unhealthier',
        'bad on the weekends': 'unhealthier',
        'worse': 'unhealthier',
        'poor': 'unhealthier',

        'eat more': 'more food',
        'bigger meals': 'more food',
        'more often': 'more food',
        'snack more': 'more food',
        'more food': 'more food',
        'unlimited swipes': 'more food',
        'eat too often': 'more food',

        'eat less': 'less food',
        'less food': 'less food',
        'smaller portions': 'less food',
        'skip meals': 'less food',
        'snack less': 'less food',
        'rarely eat': 'less food',
        "don't eat as much": 'less food',

        'dining hall': 'less healthy options',
        'cafe': 'less healthy options',
        'less options': 'less healthy options',
        'money': 'less healthy options',
        'expensive': 'less healthy options',
        'not as healthy': 'less healthy options',

        "don't cook": 'cook less',
        'not make': 'cook less',
        'quick meals': 'cook less',
        'hard to cook': 'cook less',
        'on the go foods': 'cook less',

        'prepare my own meals': 'cook more',
        'cook': 'cook more',
        'pack my lunch': 'cook more',

        'no change': 'no change',
        'none': 'no change',
        'same': 'no change',
        "hasn't changed": 'no change',
        'nun': 'no change'
    }

    def eating_change(text):
        if pd.isnull(text):
            return ['other']
        
        matched = []
        for keyword, label in eat_change_map.items():
            if keyword in text:
                matched.append(label)

        matched = sorted(set(matched))
        
        return matched if matched else ['other']

    df['eating_changes'] = df['eating_changes'].apply(eating_change).apply(lambda x: ', '.join(x))