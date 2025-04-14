import pandas as pd


def proffesion (df):
    proffesion_map = {
        'professor': 'education',
        'teacher': 'education',
        'school': 'education',
        'principal' : 'education',

        'doctor': 'healthcare',
        'dentist': 'healthcare',
        'optometrist': 'healthcare',
        'clinical': 'healthcare',
        'therapist': 'healthcare',
        'pharmaceutical': 'healthcare',
        'nurse': 'healthcare',
        'dental': 'healthcare',

        'engineer': 'engineering',
        'information systems architect': 'engineering',
        'engineering': 'engineering',
        'biohemical waste elimination': 'engineering',

        'lawyer': 'law',
        'contract negotiations': 'law',

        'police': 'public safety',
        'officer': 'public safety',
        'fireman': 'public safety',
        'commissioner of erie county': 'public safety',

        'military': 'military/civil service',
        'united nations': 'military/civil service',

        'ceo': 'management',
        'vp': 'management',
        'president': 'management',
        'cfo': 'management',
        'manager': 'management',
        'supervisor': 'management',
        'director': 'management',

        'self employed': 'business',
        'business': 'business',
        'owner': 'business',
        'trader': 'business',
        'realtor': 'business',
        'journalist': 'business',
        'sales': 'business',
        'salesman': 'business',
        'marketing': 'business',
        'real estate': 'business',
        'secretary' : 'business',

        'driver': 'transportation',
        'delivery': 'transportation',
        'transportation': 'transportation',
        'beacon light': 'transportation',

        'mechanic': 'manual labor',
        'assembler': 'manual labor',
        'welder': 'manual labor',
        'hvac': 'manual labor',
        'handyman': 'manual labor',
        'shirt designer': 'manual labor',
        'subcontractor': 'manual labor',
        'house appraiser': 'manual labor',
        'construction': 'manual labor',
        'construction': 'manual labor',
        'landscaping': 'manual labor',
        'cross-guard': 'manual labor',
        'service technition': 'manual labor',
        'plant employee': 'manual labor',

        'accountant': 'finance',
        'banker': 'finance',

        'politician': 'politics',

        'retired': 'retired',
        'retire': 'retired',
        'deceased': 'retired',
        
        'home marker': 'homemaker',
        'homemaker': 'homemaker',
        'stay at home': 'homemaker',
        'home': 'homemaker',
        'house': 'homemaker',

        'unemployed' : 'unemployed',
        'nothing': 'unemployed',
        'none': 'unemployed',

        'unknown': 'unknown',
        'idk': 'unknown',
        'not sure': 'unknown',
        'dead beat': 'unknown'

    }

    def prof_category(text):
        if pd.isnull(text):
            return ['other']
        
        text = str(text).strip()
        matched = []

        for keyword, label in proffesion_map.items():
            if keyword in text:
                matched.append(label)
        
        matched = sorted(set(matched))
        return matched if matched else ['other']

    df['father_profession'] = df['father_profession'].apply(prof_category).apply(lambda x: ', '.join(x))
    df['mother_profession'] = df['mother_profession'].apply(prof_category).apply(lambda x: ', '.join(x))
