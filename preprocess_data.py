import pandas as pd
import json
from joblib import dump

def load_and_preprocess_data():
    
    print("Loading datasets...")
    try:
        recipe1m = pd.read_csv('datasets/full_dataset.csv')
        pp_recipes = pd.read_csv('datasets/PP_recipes.csv')
        pp_users = pd.read_csv('datasets/PP_users.csv')
        raw_interactions = pd.read_csv('datasets/RAW_interactions.csv')
        raw_recipes = pd.read_csv('datasets/RAW_recipes.csv')
        with open('datasets/train.json') as f:
            whats_cooking_train = json.load(f)
        whats_cooking_train = pd.DataFrame(whats_cooking_train)
        with open('datasets/test.json') as f:
            whats_cooking_test = json.load(f)
        whats_cooking_test = pd.DataFrame(whats_cooking_test)
    except Exception as e:
        print(f"Error loading datasets: {e}")

    recipe1m.dropna(inplace=True)
    raw_interactions.dropna(inplace=True)
    raw_recipes.dropna(inplace=True)
    whats_cooking_train.dropna(inplace=True)

    whats_cooking_train['ingredients'] = whats_cooking_train['ingredients'].apply(lambda x: ','.join(x) if isinstance(x, list) else x)

    recipe1m.drop_duplicates(inplace=True)
    raw_interactions.drop_duplicates(inplace=True)
    raw_recipes.drop_duplicates(inplace=True)
    whats_cooking_train.drop_duplicates(inplace=True)

    def normalize_text(df, column):
        df[column] = df[column].str.lower().str.replace(r'[^\w\s]', '')
        return df

    recipe1m = normalize_text(recipe1m, 'ingredients')
    recipe1m = normalize_text(recipe1m, 'title')
    raw_recipes = normalize_text(raw_recipes, 'ingredients')
    raw_recipes = normalize_text(raw_recipes, 'name')
    raw_recipes = raw_recipes.rename(columns={'name': 'title', 'steps': 'directions'})
    whats_cooking_train = normalize_text(whats_cooking_train, 'ingredients')
    whats_cooking_train = whats_cooking_train.rename(columns={'id': 'title', 'cuisine': 'directions'})

    # Feature Engineering 
    def extract_features(df):
        df['ingredient_count'] = df['ingredients'].apply(lambda x: len(x.split(',')))
        return df

    recipe1m = extract_features(recipe1m)
    raw_recipes = extract_features(raw_recipes)
    whats_cooking_train = extract_features(whats_cooking_train)

    # Combined recipes 
    combined_recipes = pd.concat([recipe1m[['title', 'ingredients', 'directions']],
                                  raw_recipes[['title', 'ingredients', 'directions']],
                                  whats_cooking_train[['title', 'ingredients', 'directions']]], ignore_index=True)
    combined_recipes.drop_duplicates(inplace=True)

    # Save preprocessed data
    dump(combined_recipes, 'datasets/preprocessed_recipes.joblib')
    print("Data preprocessed and saved successfully.")

if __name__ == "__main__":
    load_and_preprocess_data()
