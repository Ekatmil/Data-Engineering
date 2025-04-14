    
import pandas as pd

import duckdb

def SQL_Run_Queries (df):
    duckdb.register('df', df)
    print(df.columns.tolist())

    #AVERAGE GPA PER GENDER
    query_gpa_and_gender = """
    SELECT 
        Gender,
        ROUND(AVG(GPA), 2) AS avg_gpa
    FROM df
    GROUP BY Gender
    ORDER BY Gender;
    """

    print ("Average GPA per Gender")
    print(duckdb.query(query_gpa_and_gender).to_df())


    # CHECK WHAT ARE 10 MOST COMMON COMFORT FOOD 
    query_comfort_food = """
    SELECT 
        TRIM(food) AS comfort_food_item,
        COUNT(*) AS count
    FROM (
        SELECT UNNEST(STRING_SPLIT(comfort_food, ',')) AS food
        FROM df
    )
    GROUP BY comfort_food_item
    ORDER BY count DESC
    LIMIT 10
    """
    print ("THE MOST COMMON COMFORT FOOD")
    print(duckdb.query(query_comfort_food).to_df())


    # CHECK WHAT ARE 10 MOST COMMON COMFORT FOOD REASON
    query_comfort_food_reason = """
    SELECT 
        TRIM(reason) AS comfort_reason,
        COUNT(*) AS count
    FROM (
        SELECT UNNEST(STRING_SPLIT(comfort_food_reasons, ',')) AS reason
        FROM df
    )
    GROUP BY comfort_reason
    ORDER BY count DESC
    LIMIT 10
    """
    print ("THE MOST COMMON COMFORT FOOD REASON")
    print(duckdb.query(query_comfort_food_reason).to_df())


    # COMBINE 5 MOST COMMON COMFORT FOOD AND THE MOST COMMON REASONS FOR THEM
    query_combined = """
    WITH preparation AS (
        SELECT 
            TRIM(food) AS food_item,
            TRIM(reason) AS reason
        FROM (
            SELECT 
                UNNEST(STRING_SPLIT(comfort_food, ',')) AS food,
                UNNEST(STRING_SPLIT(comfort_food_reasons, ',')) AS reason
            FROM df
        )
    ),
    common_foods AS (
        SELECT food_item, COUNT(*) AS food_count
        FROM preparation
        GROUP BY food_item
        ORDER BY food_count DESC
        LIMIT 5
    ),
    reasons_for_food AS (
        SELECT 
            cf.food_item,
            p.reason,
            COUNT(*) AS reason_count,
            ROW_NUMBER() OVER (PARTITION BY cf.food_item ORDER BY COUNT(*) DESC) AS rn
        FROM common_foods cf
        JOIN preparation p ON p.food_item = cf.food_item
        WHERE LOWER(p.reason) NOT IN ('none', 'nan', 'other')
        GROUP BY cf.food_item, p.reason
    )
    SELECT food_item, reason AS most_common_reason, reason_count
    FROM reasons_for_food
    WHERE rn = 1
    ORDER BY reason_count DESC;
    """

    print ("MOST COMMON REASON FOR THE MOST COMMON COMFORT FOOD")
    print(duckdb.query(query_combined).to_df())



    # CONNECTION BETWEEN CURRENT DIETS AND PARENT'S PROFESSION
    query_diet_and_professions = """
    WITH preparation AS (
        SELECT 
            UNNEST(STRING_SPLIT(diet_current, ',')) AS diet_current,
            TRIM(father_profession) AS father_prof,
            TRIM(mother_profession) AS mother_prof
        FROM df
        WHERE father_profession IS NOT NULL AND mother_profession IS NOT NULL
    ),
    cleaned AS (
        SELECT 
            TRIM(LOWER(diet_current)) AS diet,
            LOWER(father_prof) AS father_prof,
            LOWER(mother_prof) AS mother_prof
        FROM preparation
        WHERE diet IS NOT NULL AND diet <> 'other'
    ),
    father_ranked AS (
        SELECT 
            diet,
            father_prof,
            COUNT(*) AS count,
            ROW_NUMBER() OVER (PARTITION BY diet ORDER BY COUNT(*) DESC) AS rn
        FROM cleaned
        GROUP BY diet, father_prof
    ),
    mother_ranked AS (
        SELECT 
            diet,
            mother_prof,
            COUNT(*) AS count,
            ROW_NUMBER() OVER (PARTITION BY diet ORDER BY COUNT(*) DESC) AS rn
        FROM cleaned
        GROUP BY diet, mother_prof
    )
    SELECT 
        f.diet,
        f.father_prof AS most_common_father_profession,
        f.count AS father_count,
        m.mother_prof AS most_common_mother_profession,
        m.count AS mother_count
    FROM father_ranked f
    JOIN mother_ranked m ON f.diet = m.diet AND f.rn = 1 AND m.rn = 1
    ORDER BY f.diet;
    """

    print ("DIET IN RELATION WITH PARENTS' PROFESSION")
    print(duckdb.query(query_diet_and_professions).to_df())
