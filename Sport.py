import pandas as pd     

def sport(df):
    sport_map = {
        'basketball': 'basketball',
        'soccer': 'football',
        'fotball': 'football',
        'football': 'football',

        'baseball': 'baseball',
        'softball': 'baseball',

        'volleyball': 'volleyball',
        'tennis': 'tennis',
        'hockey': 'hockey',
        'wrestling': 'wrestling',

        'rowing': 'rowing',
        'crew': 'rowing',

        'swimming': 'swimming',
        'water polo': 'swimming',

        'skiing': 'winter sport',
        'snowboarding': 'winter sport',

        'track': 'track and field',
        'running': 'track and field',
        'cycling': 'track and field',

        'gym': 'fitness',
        'working out': 'fitness',

        'dance': 'dance',
        'dancing': 'dance',
        'danced': 'dance',
        'marching band': 'dance',

        'horse back riding': 'equestrian',
        'equestrian team': 'equestrian',

        'car racing': 'motor sport',

        'pool': 'recreational',
        'darts': 'recreational',

        'none': 'none',
        'none.': 'none',
        'no' : 'none'
    }

    def sports_caregory(text):
        if pd.isnull(text):
            return ['unknown']

        matched = []

        for keyword, category in sport_map.items():
            if keyword in text:
                matched.append(category)

        return sorted(set(matched)) if matched else ['other']

    df['type_sports'] = df['type_sports'].apply(sports_caregory).apply(lambda x: ', '.join(x))