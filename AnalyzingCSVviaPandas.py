from matplotlib import pyplot as plt
import csv
from collections import Counter
import pandas as pd

plt.style.use("seaborn")

language_counter = Counter()

csv_data = pd.read_csv("data.csv")
languagesResponses = csv_data["LanguagesWorkedWith"]

# print(languagesResponses)

for item in languagesResponses:
    language_counter.update(item.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

plt.barh(languages,popularity, color = "b")

plt.xlabel("Popularity")
plt.tight_layout()
plt.show()