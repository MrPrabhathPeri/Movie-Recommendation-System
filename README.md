# 🎬 Movie Recommendation System

This project is a **content-based movie recommender system** built using Python and machine learning. It leverages movie metadata from the TMDB 5000 dataset to recommend similar movies based on a selected title.

## 📁 Dataset Used

- **TMDB 5000 Movies Dataset**
- **TMDB 5000 Credits Dataset**
- Source: [Kaggle - TMDB Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
  
## 🚀 Features

- Content-based filtering using metadata like:
  - Movie overview
  - Genres
  - Keywords
  - Cast
  - Crew (Director & Writer)
- Text processing and vectorization using `CountVectorizer`
- Cosine similarity for recommending similar movies

## 🧠 Tech Stack

- **Python**
- **Pandas** – data processing
- **Scikit-learn** – machine learning (CountVectorizer, cosine similarity)
- **Numpy**

## 📌 How It Works

1. Merge `movies` and `credits` datasets on the movie title.
2. Extract relevant features and process:
   - Convert JSON-like strings to Python lists using `ast.literal_eval`
   - Extract top 4 cast members and filter crew for Directors and Writers
3. Combine processed features into a single **tags** column.
4. Vectorize the tags using `CountVectorizer`.
5. Compute cosine similarity between all movies.
6. Recommend top 10 similar movies based on cosine similarity score.

## 📈 Example

```python
recommend("Avengers: Age of Ultron")
```

**Output:**
```
Iron Man 3
Captain America: The Winter Soldier
The Avengers
Thor: The Dark World
X-Men: Days of Future Past
Fantastic Four
Man of Steel
Batman v Superman: Dawn of Justice
Ant-Man
The Amazing Spider-Man 2
```

## 🛠 How to Run

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install numpy pandas scikit-learn
   ```
3. Place `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` in the project directory.
4. Run the Python script or open it in a Jupyter/Colab environment.

## 📎 To-Do / Possible Improvements

- Add a simple web interface using Streamlit or Flask
- Use TF-IDF or advanced NLP techniques
- Include IMDb ratings or user reviews for hybrid recommendations

