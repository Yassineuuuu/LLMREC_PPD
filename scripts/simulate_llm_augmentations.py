# Simulate LLM-based augmentation of profiles and interactions
import json
import pandas as pd

profiles = json.load(open('data/synthetic/fake_profiles.json'))
interactions = pd.read_csv('data/synthetic/fake_interactions.csv')

print("Sample profiles:", profiles[:1])
print("Sample interactions:")
print(interactions.head())