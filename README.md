# Recipe Recommendation System

## Overview
This project implements a **Recipe Recommendation System** leveraging multiple datasets to provide personalized recipe recommendations. The system preprocesses data, applies content-based filtering, and incorporates user interactions and natural language processing (NLP) for insights and recommendations. Additionally, the system visualizes trends in user preferences, cuisine distributions, and ingredient popularity.

## Datasets Used
1. **[Recipe1M+ Dataset](https://www.kaggle.com/datasets/saldenisov/recipenlg/data):**
   - Contains recipe details, ingredients, and user reviews.
2. **[Food.com Recipes and User Interactions](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions):**
   - Includes recipes along with user interaction data (ratings and reviews).
3. **[What’s Cooking Dataset](https://www.kaggle.com/datasets/kaggle/recipe-ingredients-dataset):**
   - Provides over 40,000 recipes with ingredient lists and cuisine labels.

## Approach
### Data Preprocessing
1. **Loading and Cleaning:**
   - Imported datasets were loaded and cleaned by handling missing values and removing duplicates.
2. **Normalization:**
   - Text data (e.g., ingredients and titles) was normalized by converting to lowercase and removing punctuation.
3. **Feature Engineering:**
   - Added derived features, such as the count of ingredients for each recipe.
4. **Integration:**
   - Combined data from multiple datasets into a unified structure.

### Recommendation System
1. **Content-Based Filtering:**
   - Used TF-IDF vectorization to represent ingredients and calculated cosine similarity to recommend recipes based on user preferences.
2. **Hybrid Recommendation:**
   - Incorporated user interactions and content-based insights for a more robust recommendation.
3. **User Input:**
   - Collected user preferences such as dietary restrictions, cuisine preferences, available ingredients, and cooking time.

### Visualization and NLP
1. **NLP on Reviews:**
   - Extracted user preferences and ingredient popularity from reviews using the CountVectorizer.
2. **Visualization:**
   - Created charts and graphs to show trends in cuisines, popular ingredients, and user interactions over time.
   - Visualize top user preferences 
   - Most Common Ingredients in Recipes
   - Most Common Ingredients in Recipes 
   - Recipe Counts by Time to Cook  
   - Recipe Ratings Distribution 
   - Cuisine Distribution 
   - Visualize User Interactions Over Time  
   - Visualize Recipe Counts by Cuisine
   - Recipe Diversity Index 
   - Ingredient Frequency Over Time 
   - User interaction heatmap 

## Challenges and Solutions
1. **Data Volume and Consistency:**
   - **Challenge:** Managing large datasets and aligning different schemas.
   - **Solution:** Unified datasets using consistent feature extraction and normalization techniques.
2. **Sparse Data in User Reviews:**
   - **Challenge:** Insufficient or biased reviews for some recipes.
   - **Solution:** Augmented recommendations with content-based filtering to reduce dependence on user interactions.
3. **Ingredient Standardization:**
   - **Challenge:** Variability in ingredient naming (e.g., “tomato” vs. “tomatoes”).
   - **Solution:** Normalized ingredient text and removed duplicates.
4. **Visualization Scalability:**
   - **Challenge:** Displaying meaningful insights across large datasets.
   - **Solution:** Focused on key metrics such as most-requested cuisines and ingredients for concise visualizations.

## Key Features
1. **Personalized Recommendations:**
   - Recipes tailored to user preferences and available ingredients.
2. **Insights from Reviews:**
   - Extracted preferences and trends using NLP.
3. **Visualizations:**
   - Highlighted key insights like ingredient frequency, cuisine diversity, and user interactions.

## Ideas for Improvement
1. **Chatbot:**
   - Develop a voice-enabled chatbot and enhance personalization for more accurate user preferences.​
1. **Enhanced NLP Models:**
   - Use advanced NLP techniques like word embeddings (e.g. Word2Vec) or transformer-based models (e.g. BERT) for better analysis of reviews.
2. **Collaborative Filtering:**
   - Integrate collaborative filtering methods to enhance recommendations using user interaction data.
3. **Advanced Visualizations:**
   - Employ interactive dashboards (e.g. Plotly/Dash) for more user engagement.
4. **Real-Time Updates:**
   - Implement a real-time recommendation engine using APIs for dynamic user input and updates.

## How to Run
1. **Setup:**
   - Install required Python libraries:
     ```bash
     pip install pandas scikit-learn matplotlib seaborn nltk
     ```
2. **Generate Recommendations:**
   - Use `main.recommender.ipynb` for personalized recipe recommendations.
3. **Visualize Trends:**
   - Explore insights using `visualization_NLP.ipynb`.
4. **Recipe Recommender Flask WebApp:**
   - Run `preprocess_data.py` to clean and preprocess datasets.
   - Run `app.py` will se a web interface

## Results
1. Italian cuisine emerged as the most requested.
2. Ingredients like chicken, eggs, onion, and garlic were highly popular.
3. User reviews provided actionable insights for refining the recommendation engine.

## Screenshots 
![image](https://github.com/user-attachments/assets/b3bf6822-35c1-4296-91b8-287716ed2a66)

![image](https://github.com/user-attachments/assets/e93c6421-7793-451e-808f-cbe89115dfaa)

![image](https://github.com/user-attachments/assets/4e840583-90a2-434b-9815-cf0a9e080ee7)

![image](https://github.com/user-attachments/assets/e29e199c-32d0-4681-8568-25a1acf89934)

![image](https://github.com/user-attachments/assets/704622f1-8152-4f26-a68c-4a70c098a7a2)

![image](https://github.com/user-attachments/assets/4df31e5a-f1a8-4f47-b19b-2a8990d7ef1d)
