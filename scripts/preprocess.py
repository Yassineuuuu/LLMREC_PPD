# Load and clean raw MovieLens data
import pandas as pd

def load_data():
    df = pd.read_csv('data/movielens_100k/ratings.csv')
    return df[df['rating'] >= 4]  # implicit feedback

if __name__ == '__main__':
    df = load_data()
    print(df.head())