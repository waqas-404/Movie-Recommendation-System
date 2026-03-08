# 🎬 Movie Recommender System

A **Movie Recommendation Web Application** built with **Python and Streamlit** that suggests movies using two different recommendation approaches:

* **Popularity-Based Recommendation**
* **Content-Based Recommendation**

The system analyzes movie metadata such as genres, keywords, cast, director, and overview to recommend similar movies.

---

## 📌 Project Overview

Recommendation systems are widely used by platforms such as **Netflix, Amazon Prime, and Spotify** to personalize user experiences.

This project implements two common recommendation techniques:

1. **Popularity-Based Filtering**
2. **Content-Based Filtering**

The application allows users to select a movie and instantly receive similar movie recommendations along with their posters.

---

## ⚙️ Features

* Interactive **Streamlit web interface**
* Two recommendation strategies:

  * Popularity-based
  * Content-based
* Movie poster retrieval using **TMDB API**
* Fast similarity computation using **Cosine Similarity**
* Clean and simple UI for easy interaction
* Top **50 popular movies displayed on the homepage**

---

## 🧠 Recommendation Approaches

### 1️⃣ Popularity-Based Recommendation

Popularity-based recommendation suggests movies that are **globally popular** among users.

In this project, the popularity score from the dataset is used to identify the **top 50 most popular movies**.

#### Steps

1. Sort the dataset by the **popularity column** in descending order.
2. Select the **top 50 movies**.
3. Display them on the homepage.

Example logic:

```python
popular_movies = movies.sort_values('popularity', ascending=False).head(50)
```

This method works well for **new users with no interaction history**, but it does not personalize recommendations.

---

### 2️⃣ Content-Based Recommendation

Content-based recommendation suggests movies **similar to the one selected by the user** based on movie features.

Instead of user behavior, the system analyzes the **content of movies**.

#### Features Used

The following movie attributes are combined into a single feature called **tags**:

* Overview
* Genres
* Keywords
* Cast
* Director

Example of tag creation:

```python
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']
```

---

## 🔍 Vectorization

To compare movies, textual features must be converted into numerical vectors.

This is done using **CountVectorizer** from Scikit-Learn.

```python
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()
```

This converts movie descriptions into a **vector space representation**.

---

## 📏 Similarity Calculation

To determine how similar two movies are, the project uses **Cosine Similarity**.

Cosine similarity measures the angle between two vectors.

```python
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vectors)
```

Movies with the **highest similarity scores** are recommended.

---

## 🎥 Poster Retrieval

Movie posters are fetched dynamically using the **TMDB API**.

Example API request:

```
https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY
```

Poster images are then displayed in the Streamlit interface.

---

## 🖥️ Application Workflow

1. Load processed movie dataset.
2. Load precomputed similarity matrix.
3. Display **Top 50 Popular Movies** on the homepage.
4. User selects a movie from the dropdown.
5. The system calculates the most similar movies using cosine similarity.
6. Recommended movies and posters are displayed.

---

## 📂 Project Structure

```
Movie-Recommender-System
│
├── app.py                 # Streamlit application
├── new_movies.csv         # Processed movie dataset
├── pop_movies.csv         # Top 50 popular movies
├── similarity.joblib      # Precomputed similarity matrix
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

The application will open in your browser:

```
http://localhost:8501
```

---

## 🧰 Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-Learn
* Joblib
* TMDB API
* Requests

---

## 📊 Dataset

The project uses the **TMDB Movie Dataset**, which contains metadata such as:

* Movie titles
* Genres
* Keywords
* Cast
* Crew
* Overview
* Popularity score

---

## 📈 Future Improvements

Possible enhancements for this project include:

* Hybrid recommendation systems
* Collaborative filtering
* User ratings integration
* Movie search with NLP
* Improved UI with movie cards
* Deployment on cloud platforms

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

Developed as a machine learning project to demonstrate practical implementation of recommendation systems using **Python and Streamlit**.
