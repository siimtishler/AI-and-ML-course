import csv
from collections import defaultdict

print('\nNAIVE BAYES\n')
article_count = 0 
article_topic_count = defaultdict(int)

topic_word_counts = defaultdict(lambda: defaultdict(int))

topic_word_total = defaultdict(int)

unique_words = set()


with open("Naive_Bayes\\bbc_test_small.csv", encoding="utf-8") as f:
    rd = csv.reader(f)
    for topic, text in rd:
        article_count += 1
        article_topic_count[topic] +=1 # Amount of the same articles
        # lowercase tokens longer than 3 chars
        words = [w.lower() for w in text.split() if len(w) > 3]

        for word in words:
            topic_word_counts[topic][word] += 1 # Word occurence in the same article
            topic_word_total[topic] += 1        # All words in topic
            unique_words.add(word)              # Unique words

        # store topic and words somewhere

# P(c)
def topicProbaility(topic):
    print(f"P({topic}) = {article_topic_count[topic]}/{article_count} = {article_topic_count[topic]/article_count:.3}\n")
    return article_topic_count[topic]/article_count

def wordOccurrenceInTopic(topic, word):
    print(f"'{word}' Occurs {topic_word_counts[topic][word]} times in {topic}\n")
    return topic_word_counts[topic][word]

def uniqueWords():
    print(f"Unique words count: {len(unique_words)}\n")
    return len(unique_words)

def wordsInTopic(topic):
    print(f"Words in {topic}: {topic_word_total[topic]}\n")
    return topic_word_total[topic]

# P (w1|c)
def probabilityInTopic(topic, word): 
    wo = wordOccurrenceInTopic(topic, word) + 1
    nw = wordsInTopic(topic)
    unq = uniqueWords()

    prob = wo / (nw + unq)
    print(f"Probability of {word} in {topic} is {prob}")
    return prob


topicProbaility('tech')


# 1) find the total number of articles and how many belongs to each class, you will get the probabilities P(c)
# 2) count the word occurrences in each topic (tech, politics, ...)
# 3) find total number of words in each topic (including repetitions)
# 4) count the unique words in training data (|V|)