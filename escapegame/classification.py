import cv2
import numpy as np
import pandas as pd
import glob
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.svm import LinearSVC
from skimage import feature

class ImageClassifier:
    def __init__(self):
        self.scaler = StandardScaler()
        self.classifier = LinearSVC()
        # Si vous voulez utiliser le classifieur des K plus proches voisins, décommentez
        # la ligne ci-dessous.
        #self.classifier = KNeighborsClassifier(n_neighbors=2)


# Cette fonction extrait le histogramme de couleur dans l'espace HSV 
# (Hue, Saturation, Value) d'une image.
    def swain_ballard_histogram(self, image):
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([hsv_image], [0, 1, 2], None, [8, 8, 8], [0, 180, 0, 256, 0, 256])
        hist = cv2.normalize(hist, hist).flatten()
        return hist

# Cette fonction calcule le ratio largeur/hauteur d'une image.
    def aspect_ratio(self, image):
        height, width = image.shape[:2]
        return float(width) / float(height)

# Cette fonction extrait le Local Binary Pattern (LBP) d'une image grâce à la bibliothèque skimage
    def local_binary_pattern(self, image, num_points=24, radius=8):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        lbp = feature.local_binary_pattern(gray_image, num_points, radius, method="uniform")
        hist, _ = np.histogram(lbp.ravel(), bins=np.arange(0, num_points + 3), range=(0, num_points + 2))
        hist = hist.astype("float")
        hist /= (hist.sum() + 1e-7)
        return hist

# Cette fonction combine toutes les méthodes ci-dessus pour extraire un ensemble 
# complet de caractéristiques pour une image.
    def extract_features(self, image_path):
        image = cv2.imread(image_path)
        sb_hist = self.swain_ballard_histogram(image)
        ar = self.aspect_ratio(image)
        lbp_hist = self.local_binary_pattern(image)
        return np.concatenate(([ar], sb_hist, lbp_hist))

# Cette fonction est une variante de la précédente, où l'image est d'abord 
# divisée en trois parties, et un histogramme Swain-Ballard est extrait pour chaque partie.
    def extract_features2(self, image_path):
        image = cv2.imread(image_path)
        height, width, channels = image.shape

        # Diviser la largeur de l'image en 3 parties égales
        sub_image_width = width // 3

        # Créer les trois sous-images
        sub_image1 = image[:, 0:sub_image_width]
        sub_image2 = image[:, sub_image_width:2*sub_image_width]
        sub_image3 = image[:, 2*sub_image_width:width]
        sb_hist1 = self.swain_ballard_histogram(sub_image1)
        sb_hist2 = self.swain_ballard_histogram(sub_image2)
        sb_hist3 = self.swain_ballard_histogram(sub_image3)
        ar = self.aspect_ratio(image)
        lbp_hist = self.local_binary_pattern(image)
        return np.concatenate(([ar], sb_hist1, sb_hist2, sb_hist3, lbp_hist))

# Cette fonction est conçue pour appliquer la fonction d'extraction des caractéristiques 
# à un ensemble d'images et enregistrer les résultats dans un fichier CSV.
    def feature_extraction(self):
        image_paths = glob.glob("apprentissage/*.*")
        labels = [os.path.basename(path).split("_")[0] for path in image_paths]

        features = []
        for path in image_paths:
            # Si vous voulez utiliser les caractéristiques 
            # (rapport largeur/hauteur, LBP, histogrammes en 3 parties),
            # utilisez la fonction extract_features2.
            features.append(self.extract_features(path))
            # features.append(self.extract_features2(path))

        df = pd.DataFrame(features)
        df.insert(0, "label", labels)
        df.to_csv("features.csv", index=False)


# Cette méthode effectue la phase d'apprentissage du modèle. Elle charge les données
# à partir du fichier CSV généré précédemment, les divise en ensembles de test et d'apprentissage,
# normalise les données, entraîne le modèle et enfin évalue le modèle sur l'ensemble de test. 
# Elle affiche également une matrice de confusion pour visualiser les performances du modèle.
    def train(self):
        # Si vous n'avez pas encore extrait les caractéristiques ou que vous avez changé de
        # caractéristiques (si vous passez à un histogramme Swain-Ballard qui est extrait 
        # pour chaque sous-partie horizontale de l'image), décommentez la ligne suivante.
        #self.feature_extraction()
        data = pd.read_csv("features.csv")
        X = data.drop("label", axis=1)
        y = data["label"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        self.scaler.fit(X_train)
        X_train = self.scaler.transform(X_train)
        X_test = self.scaler.transform(X_test)

        self.classifier.fit(X_train, y_train)
        y_pred = self.classifier.predict(X_test)
        cf_matrix = confusion_matrix(y_test, y_pred)
        print("Confusion matrix : ")
        print(cf_matrix)
        plt.figure(figsize=(8, 6))
        sns.heatmap(cf_matrix/np.sum(cf_matrix), annot=True, fmt='.2%', cmap='Oranges')
        plt.show()
        print("Classication report : ")
        print(classification_report(y_test, y_pred))
        print("Accuracy score : ")
        print(accuracy_score(y_test, y_pred))

# Cette méthode permet de prédire la classe d'une seule image. Elle est utilisée pour la fin
# de l'escape game.
    def predict_single_image(self, image_path):
        self.train()
        features = self.extract_features(image_path)
        features = np.array([features])
        features = self.scaler.transform(features)
        predicted_class = self.classifier.predict(features)
        print(f"Classe prédite pour l'image {image_path}: {predicted_class[0]}")
        return predicted_class[0]
