from flask import Flask, render_template, request
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import json
from joblib import load

app = Flask(__name__)
print("Loading preprocessed data...")
try:
    combined_recipes = load('datasets/preprocessed_recipes.joblib')
    print("Preprocessed data loaded successfully.")
except Exception as e:
    print(f"Error loading preprocessed data: {e}")

# Content-Based Filtering
def content_based_recommendation(df, user_preferences):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df['ingredients'])
    user_tfidf = vectorizer.transform([', '.join(user_preferences['available_ingredients'])])
    cosine_sim = cosine_similarity(user_tfidf, tfidf_matrix).flatten()
    recommended_indices = cosine_sim.argsort()[-5:][::-1]
    return df.iloc[recommended_indices]

def hybrid_recommendation(user_preferences, recipes_df):
    content_recommendations = content_based_recommendation(recipes_df, user_preferences)
    return content_recommendations.head(5)

@app.route('/', methods=['GET', 'POST'])
def index():
    print("Received request at /")
    if request.method == 'POST':
        print("Processing POST request")
        dietary_restrictions = request.form['dietary_restrictions'].split(',')
        cuisine_preferences = request.form['cuisine_preferences'].split(',')
        available_ingredients = request.form['available_ingredients'].split(',')
        time_to_cook = int(request.form['time_to_cook'])

        user_preferences = {
            'dietary_restrictions': dietary_restrictions,
            'cuisine_preferences': cuisine_preferences,
            'available_ingredients': available_ingredients,
            'time_to_cook': time_to_cook
        }

        print("User Preferences:", user_preferences)

        recommendations = hybrid_recommendation(user_preferences, combined_recipes)

        return render_template('index.html', recommendations=recommendations.to_dict('records'))

    return render_template('index.html', recommendations=None)

if __name__ == '__main__':
    app.run(debug=True)