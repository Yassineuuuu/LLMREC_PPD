# Simulate simple feature encoding using TF-IDF or one-hot
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Dummy movie descriptions for TF-IDF
movies = ["Action Adventure Spy", "Drama Crime"]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(movies)
print(X.toarray())