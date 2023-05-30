<h1 align="center">Racke'TSE</h3>

  <p align="center">
    Notre projet de classification d'images, sous format d'Escape Game !
    <br />
    <br />
  </p>
</div>



<!-- Table des matières -->
<details>
  <summary><strong>Table des matières</strong></summary>
  <ol>
    <li>
      <a href="#about-the-project">A propos</a>
    </li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#utilisation">Utilisation</a></li>
   <li><a href="#classification">Classification</a>
    <li><a href="#contributors">Contributeurs</a></li>
     </ol>
</details>



<!-- ABOUT THE PROJECT -->
## A Propos


Cette application a été créée dans le but du projet de classification d'images de FISE2 de Télécom Saint-Etienne. Nous avons choisi de la créer sous format d'Escape Game afin d'ajouter un aspect ludique à la classification.


<!-- INSTALLATION -->
## Installation

Pour installer toutes les dépendances nécessaires à l'exécution de l'application, vous n'avez qu'à exécuter ces lignes dans votre terminal :

    pip install opencv-python
    pip install pillow
    pip install pygame
    pip install pandas
    pip install scikit-learn
    pip install scikit-image
    pip install seaborn
    pip install keyboard


<!-- UTILISATION -->
## Utilisation

Vous pouvez soit essayer de réaliser le scénario de l'Escape Game dans son entièreté, soit évaluer directement les résultats de la classification via l'onglet "Accuser".
Si vous souhaitez réaliser le scénario, vous pouvez enquêter et essayer de résoudre les énigmes ! Des indices sont disponibles dans le menu...
Attention, vous n'avez que 30 minutes !

<!-- CLASSIFICATION -->
## Classification

En ce qui concerne la classification, nous avons implémenté plusieurs classifieurs qui utilisent des algorithmes différents et des caractéristiques différentes. Voici comment choisir le classifieur désiré :

 1. Classification par comparaison d'histogramme à l'aide de la métrique de Smith : 
	 - Dans le fichier camera.py, à la ligne 50, utiliser la ligne "image_classifier = ImageClassifier2()"
	 
 2. Classification par méthode des k-plus-proches voisins :
	- Commentez la ligne 18 de classification.py "self.classifier = LinearSVC()"
	- Décommentez la ligne 21 : "self.classifier = KNeighborsClassifier(n_neighbors=2)"

 3. Classification SVM :
	 - Ne changez rien. (ou faites les étapes que vous venez de faire dans l'autre sens)

 4. Classification SVM avec histogramme de l'image séparée en 3 :
	 - Commentez la ligne 86 de classification.py  "features.append(self.extract_features(path))"
	 - Décommentez la ligne 87 : features.append(self.extract_features2(path))
	 - Décommentez la ligne 102 du même fichier pour regénérer un fichier CSV avec les nouvelles valeurs d'attributs : self.feature_extraction()

  
<!-- CONTRIBUTORS -->
## Contributeurs

Ce projet n'aurait pas pu exister sans ses principaux contributeurs qui sont listés ci-dessous. Un grand merci à eux tous !

 - Lilou Tisserand
 - Gaëlle Quillaud
 - Chloé Davoine
 - Elie Cormier
 - Valentin Pontiggia

Un grand merci à Anne-Claire Legrand pour ses précieux conseils tout au long du projet !