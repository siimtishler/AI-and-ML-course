import csv
import json
from collections import defaultdict

print('\nNAIVE BAYES\n')
article_count = 0                                           # Self explanatory
article_topic_count = defaultdict(int)                      # Cnt of 
topic_word_counts = defaultdict(lambda: defaultdict(int))   
topic_word_total = defaultdict(int)                         
unique_words = set()                                        


with open("Naive_Bayes\\bbc_train.csv", encoding="utf-8") as f:
    rd = csv.reader(f)
    for topic, text in rd:
        article_count += 1
        article_topic_count[topic] += 1  # Amount of the same topic
        # lowercase tokens longer than 3 chars
        words = [w.lower() for w in text.split() if len(w) > 3]

        for word in words:
            topic_word_counts[topic][word] += 1  # Word occurrence in the same topic
            topic_word_total[topic] += 1         # Word cnt in topic
            unique_words.add(word)               # Unique words in all topics

model_data = {
    "article_count": article_count,
    "article_topic_count": dict(article_topic_count),
    "topic_word_counts": {topic: dict(words) for topic, words in topic_word_counts.items()},
    "topic_word_total": dict(topic_word_total),
    "unique_words": len(unique_words)
}

# Save into JSON file
with open("Naive_Bayes\\naive_bayes_model.json", "w") as json_file:
    json.dump(model_data, json_file)