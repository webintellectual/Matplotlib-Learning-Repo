from matplotlib import pyplot as plt
import csv
from collections import Counter

plt.style.use("seaborn")

with open("data.csv") as csv_file: 
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

# print(language_counter.most_common(15))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()
plt.barh(languages,popularity, color = "b")

plt.xlabel("Popularity")
plt.tight_layout()
plt.show()