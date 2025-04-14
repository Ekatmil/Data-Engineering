import pandas as pd

def apply_labels (text):
    if pd.isnull(text):
        return 'unknown'
    
    reasons = []
    text = str(text)

    if 'boredom' in text or 'bored' in text:
        reasons.append('boredom')
    if 'sad' in text:
        reasons.append('sadness')
    if 'stress' in text or 'stres' in text:
        reasons.append('stress')
    if 'hungry' in text or 'hunger' in text:
        reasons.append('hunger')
    if 'happy' in text or 'happiness' in text:
        reasons.append('happiness')
    if 'angry' in text or 'anger' in text:
        reasons.append('anger')
    if not reasons and ('dont' in text or 'not' in text or 'none' in text):
        reasons.append('nan')

    return ', '.join(reasons) if reasons else 'other'

def comfort_reasons (df):
    df['comfort_food_reasons'] = df['comfort_food_reasons'].apply(apply_labels)