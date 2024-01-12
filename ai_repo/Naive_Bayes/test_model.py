import csv
import json
import math
from collections import defaultdict

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

DEBUG = True
debug = lambda x: print(x) if DEBUG else None

def print_green(text):
    debug("\033[32m" + text + "\033[0m")  # \033[32m sets the text color to green, \033[0m resets the color

def print_red(text):
    debug("\033[91m" + text + "\033[0m")

def load_model(model_file):
    # Load the model data from the JSON file
    with open(model_file, "r") as json_file:
        loaded_model_data = json.load(json_file)
    return loaded_model_data

def classify_article(article, model_data):
    log_probabilities = defaultdict(float)

    for topic, word_probs in model_data["topic_word_counts"].items():
        # Initialize with log(P(c))
        # print(topic)
        log_probabilities[topic] = math.log(model_data["article_topic_count"][topic] / model_data["article_count"])
        for word in article:
            # If the word is not in the training data for this topic, use the default probability
            word_occurrences = word_probs.get(word, 0)
            # print(f"({topic})  \t {word}: {word_occurrences}")
            total_words_in_topic = model_data["topic_word_total"][topic]
            unique_words = model_data["unique_words"]
            word_probability = (word_occurrences + 1) / (total_words_in_topic + unique_words)

            # Add log(P(w|c))
            log_probabilities[topic] += math.log(word_probability)

    # Find the topic with the highest log probability
    predicted_topic = max(log_probabilities, key=log_probabilities.get)
    return predicted_topic

def evaluate_accuracy(test_file, model_data):
    correct_predictions = 0
    total_articles = 0
    true_labels = []
    predicted_labels = []

    with open(test_file, encoding="utf-8") as f:
        rd = csv.reader(f)
        for topic, text in rd:
            total_articles += 1
            true_labels.append(topic)
            # lowercase tokens longer than 3 chars
            words = [w.lower() for w in text.split() if len(w) > 3]
            predicted_topic = classify_article(words, model_data)
            predicted_labels.append(predicted_topic)
            
            if predicted_topic == topic:
                print_green(f"Real: {topic}\t| Pred: {predicted_topic}")
                correct_predictions += 1
            else:
                print_red(f"Real: {topic}\t| Pred: {predicted_topic}")

    accuracy = (correct_predictions / total_articles) * 100
    debug(f"Accuracy: {accuracy:.2f}%")

    # Create confusion matrix
    conf_matrix = confusion_matrix(list(true_labels), list(predicted_labels), labels=list(model_data["article_topic_count"].keys()))


    # Display confusion matrix using seaborn heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues",
                xticklabels=model_data["article_topic_count"].keys(),
                yticklabels=model_data["article_topic_count"].keys())
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.title("Confusion Matrix")
    plt.show()



if __name__ == "__main__":
    # Load the pre-trained model
    model_data = load_model("Naive_Bayes\\naive_bayes_model.json")

    # Evaluate accuracy on the test data
    evaluate_accuracy("Naive_Bayes\\bbc_test.csv", model_data)

