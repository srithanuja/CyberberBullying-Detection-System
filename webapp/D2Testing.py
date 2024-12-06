import matplotlib.pyplot as plt;
import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import pickle
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score

class D2Testing:

    def detecting(test_file, model):

        #train_news = pd.read_csv(train_file)
        test_ = pd.read_csv(test_file)
        
        testdata=test_['Class']
        
        train = pickle.load(open(model, 'rb'))
        predicted_class = train.predict(test_['Word'])
        print('start')

        r=D2Testing.model_assessment(testdata,predicted_class)

        print(r)

        return r

    def model_assessment(y_test, predicted_class):
        l=[]
        
        #Accuracy = (TP + TN) / ALL
        accuracy=((accuracy_score(y_test, predicted_class)))
        # Precision = TP / (TP + FP) (Where TP = True Positive, TN = True Negative, FP = False Positive, FN = False Negative).
        precision=(precision_score(y_test, predicted_class, pos_label='Sexual',average='weighted'))
        #Recall = TP / (TP + FN)
        recall=(recall_score(y_test, predicted_class, pos_label='Sexual',average='weighted'))
        #F - scores are a statistical method for determining accuracy accounting for both precision and recall.
        fscore=(f1_score(y_test, predicted_class, pos_label='Sexual',average='micro'))


        accuracy=accuracy*100
        accuracy=round(float(accuracy),2)

        precision=precision*100
        precision=round(float(precision),2)

        recall=recall*100
        recall=round(float(recall),2)                

        fscore=fscore*100
        fscore=round(float(fscore),2)



        l=[accuracy,precision,recall,fscore]
        
        return l



    def main():
        nb=D2Testing.detecting('D2Testing.csv','d2_nb_model.model')
        rf=D2Testing.detecting('D2Testing.csv','d2_rf_model.model')
        svm=D2Testing.detecting('D2Testing.csv','d2_svm_model.model')
        nn=D2Testing.detecting('D2Testing.csv','d2_nn_model.model')
        algos = ['Naive Bayees',"SVM","Neural Network","Random Forest"]
        d={}
        d[algos[0]]=nb
        d[algos[1]]=svm
        d[algos[2]]=nn
        d[algos[3]]=rf
        from .DBConnection import DBConnection
        mydb = DBConnection.getConnection()
        cursor = mydb.cursor()
        query = "delete from webapp_performance where dataset='Dataset 2'"
        cursor.execute(query)
        mydb.commit()
        query = "insert into webapp_performance(dataset, algo, acc, prec,recall, f1)  values(%s,%s,%s,%s,%s,%s)"
        values=('Dataset 2', 'Naive Bayees', str(nb[0]), str(nb[1]), str(nb[2]), str(nb[3]))
        cursor.execute(query, values)


        query = "insert into webapp_performance(dataset, algo, acc, prec,recall, f1)  values(%s,%s,%s,%s,%s,%s)"
        values=('Dataset 2', 'SVM', str(svm[0]), str(svm[1]), str(svm[2]), str(svm[3]))
        cursor.execute(query, values)

        query = "insert into webapp_performance(dataset, algo, acc, prec,recall, f1)  values(%s,%s,%s,%s,%s,%s)"
        values=('Dataset 2', 'Neural Network', str(nn[0]), str(nn[1]), str(nn[2]), str(nn[3]))
        cursor.execute(query, values)
        mydb.commit()


        query = "insert into webapp_performance(dataset, algo, acc, prec,recall, f1)  values(%s,%s,%s,%s,%s,%s)"
        values=('Dataset 2', 'Random Forest', str(rf[0]), str(rf[1]), str(rf[2]), str(rf[3]))
        cursor.execute(query, values)
        mydb.commit()

        from .bargraph import bargraph
        bargraph.view(d,'g2.jpg')
          
    
if __name__ == '__main__':
    D2Testing.main()

	


