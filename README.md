# Escape-game



**Utilisation de Gitlab**

- Ne pas toucher à la branche main avant la version finale.
- Quand on veut coder, il faut créer une nouvelle branche portant le nom de la fonctionnalité qu'on veut implémenter. On code sur cette branche et dès qu'il est bon on le merge avec la branche develop.
- Bien penser à toujours tester le plus possible les branches les plus annexes (on les importe avec merge), avant de les mettre en commun quand ça fonctionne avec les branches centrales (on les rajoute avec merge request, qui se fait directement dans Gitlab).

**Qu'est ce qui correspond à quelle branche ?**

- Dans la branche `main` on ne met que les fichiers permettant de configurer ou de documenter le projet.

- Le codage se fait dans la branche `develop`. Plus précisément, vous créez une sous-branche à partir de cette branche, puis vous codez votre fonctionnalité dans votre branche nommée `features/<nom_de_la_fonctionnalite>` et quand vous avez fini vous faites une merge request de votre branche dans `develop`.
