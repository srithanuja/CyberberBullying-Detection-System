import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import pickle

class RF2:

    def detecting(stmt):
    	stmt=[stmt]
    	filename = 'd2_rf_model.model'
    	train = pickle.load(open(filename, 'rb'))
    	predicted_class = train.predict(stmt)
    	return predicted_class[0]

if __name__ == "__main__":
    print(NN2.detecting("chinky you "))

