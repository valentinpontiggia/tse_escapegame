import cv2
import numpy as np
import pandas as pd
import glob
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.svm import LinearSVC


from skimage import feature

def swain_ballard_histogram(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv_image], [0, 1, 2], None, [8, 8, 8], [0, 180, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    return hist

def aspect_ratio(image):
    height, width = image.shape[:2]
    return float(width) / float(height)

def local_binary_pattern(image, num_points=24, radius=8):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    lbp = feature.local_binary_pattern(gray_image, num_points, radius, method="uniform")
    hist, _ = np.histogram(lbp.ravel(), bins=np.arange(0, num_points + 3), range=(0, num_points + 2))
    hist = hist.astype("float")
    hist /= (hist.sum() + 1e-7)
    return hist

def extract_features(image_path):
    image = cv2.imread(image_path)
    sb_hist = swain_ballard_histogram(image)
    ar = aspect_ratio(image)
    lbp_hist = local_binary_pattern(image)
    return np.concatenate(([ar], sb_hist, lbp_hist))

def smith_distance(hist1, hist2):
    return np.sum(np.sqrt(np.multiply(hist1, hist2)))

def feature_extraction ():
    image_paths = glob.glob("apprentissage/*.*")
    labels = [os.path.basename(path).split("_")[0] for path in image_paths]

    features = []
    for path in image_paths:
        features.append(extract_features(path))

    df = pd.DataFrame(features)
    df.insert(0, "label", labels)
    df.to_csv("features.csv", index=False)

#feature_extraction()
data = pd.read_csv("features.csv")
X = data.drop("label", axis=1)
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

classifier = LinearSVC()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
