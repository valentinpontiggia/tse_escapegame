import cv2
import numpy as np
import pandas as pd
import glob
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
from skimage import feature
from scipy.spatial.distance import euclidean


class ImageClassifier2:
    
    def __init__(self):
        self.scaler = StandardScaler()
    #récupération d'un attribut: le lbp
    def local_binary_pattern(self, image_path, num_points=24, radius=8):
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        lbp = feature.local_binary_pattern(gray_image, num_points, radius, method="uniform")
        hist, _ = np.histogram(lbp.ravel(), bins=np.arange(0, num_points + 3), range=(0, num_points + 2))
        hist = hist.astype("float")
        hist /= (hist.sum() + 1e-7)
        return hist
    
    def feature_extraction(self):
        #endroit ou se trouve notre base d'images
        image_paths = glob.glob("apprentissage/*.*")
        labels = [os.path.basename(path).split("_")[0] for path in image_paths]
    
        lbp=[]
        # pour chaque image calcul du lbp
        for i, path in enumerate(image_paths):
            lbp.append(self.local_binary_pattern(path))
        #insertion des données récupérées pour chaque image dans un csv    
        df1 = pd.DataFrame(lbp)
        df1.insert(0, "label", labels)
        df1.to_csv("features1.csv", index=False)
    # calcul de la smiliarité de smith entre 2 séries
    def smith_similarity(self, series1, series2):
        # Si les séries ont la même longueur
        if len(series1) != len(series2):
            raise ValueError("Les séries doivent avoir la même longueur.")
    
        n = len(series1)
        similarity = 0.0
    
        # Calcul la moyenne des séries
        mean1 = np.mean(series1)
        mean2 = np.mean(series2)
    
        for i in range(n-1):
            for j in range(i+1, n):
                # Calcul des différences entre les valeurs des séries
                diff1 = series1[i] - series1[j]
                diff2 = series2[i] - series2[j]
    
                # Calcul de la distance euclidienne entre les différences
                distance = euclidean([diff1, mean1], [diff2, mean2])
    
                # Mise à jour la similarité de Smith
                similarity += 1.0 / (1.0 + distance)
    
        # Normaliser la similarité
        similarity /= (n * (n-1) / 2)
    
        return similarity
    
    def train(self, data):
        # features_extraction est une étape longue qu'on laisse commenée puisque
        # notre base de données d'image restera la même donc les données seront
        # les mêmes
        #self.feature_extraction()
        # Nous avons récupéré dans un csv des séries de données pour chaque image
        # et non les histogrammes car calculer chaque histogramme pour chaque 
        # image est très long comme on peut le voir en lancant la fonction features_extraction
        X = data.drop("label", axis=1)
        y = data["label"]
        # on créer une base train et une base test de notre base d'images
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        self.scaler.fit(X_train)
        X_train = self.scaler.transform(X_train)
        X_test = self.scaler.transform(X_test)

        # Récupération des index
        indexes = y_test.index
        # Création d'un pandas Series
        y_pred = pd.Series(np.nan, index=indexes)
        # On va comparer chaque élément de X_test avec chaque élément de X_train
        # pour trouver la plus petite distance qu'il aura avec un élement de X_train
        # et on attribuera la classe y_train à y_test correspondant à cet élément
        for j, x_test in enumerate(X_test):
            min_distance = float('inf')  # Initialisation de la plus petite distance à une valeur infinie
            predicted_class = None  # Classe prédite correspondant à la plus petite distance
            
            # Parcourir chaque élément de X_train
            for i, x_train in enumerate(X_train):
                distance = self.smith_similarity(x_test, x_train)
                if distance < min_distance:
                    min_distance = distance
                    predicted_class = y_train.iloc[i]  # Attribuer la classe correspondante de y_train
                
            y_pred.iloc[j] = predicted_class
        # On récupère toutes les données pour avoir une base complète
        X_combined = np.concatenate((X_train, X_test), axis=0)
        y_combined = pd.concat((y_train, y_pred), axis=0)
        
        cf_matrix = confusion_matrix(y_test, y_pred)
        print("Confusion matrix : ")
        print(cf_matrix)
        plt.figure(figsize=(8, 6))
        sns.heatmap(cf_matrix/np.sum(cf_matrix), annot=True, fmt='.2%', cmap='Blues')
        plt.show()
        print("Classication report : ")
        print(classification_report(y_test, y_pred))
        print("Accuracy score : ")
        print(accuracy_score(y_test, y_pred))
                        
        return X_combined, y_combined
    # Calcul de la classe d'une seule image
    def predict_single_image(self, image_path):
        # On reprends le meme algorithme que précédemment mais pour une seule image
        data1 = pd.read_csv("features1.csv")
        X, y = self.train(data1)
        features = self.local_binary_pattern(image_path)
        features = np.array(features)
        min_distance = float('inf')  # Initialiser la plus petite distance à une valeur infinie
        predicted_class = None  # Classe prédite correspondant à la plus petite distance
        
        # Parcourir chaque élément de X_train
        for i, x in enumerate(X):
            distance = self.smith_similarity(features, x)  # Calculer la distance de Smith
            
            if distance < min_distance:
                min_distance = distance
                predicted_class = y.iloc[i]  # Attribuer la classe correspondante de y_train
       
        print("Classe prédite :", predicted_class)
