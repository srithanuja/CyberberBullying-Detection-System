import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import metrics

from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
import pickle
import sys
def model():
    try:
        train_data = pd.read_csv("D2dataset.csv")
        print(train_data)
        tfidf = TfidfVectorizer(stop_words='english', use_idf=True, smooth_idf=True,ngram_range=(1, 1))  # TF-IDF

        print("Start Building Model NN Classifier")
        clf_nn = Pipeline([('NNTF_IDF', tfidf), ('nn_clf',  RandomForestClassifier())])
        clf_nn.fit(train_data['Word'], train_data['Class'])
        with open('d2_nn_model.model', 'wb') as f:
            print("+++++=")
            pickle.dump(clf_nn, f)
            print("model created")

    except Exception as e:
        print("Error=" + e)

if __name__ == '__main__':
    model()
