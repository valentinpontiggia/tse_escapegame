# Escape-game



**Utilisation de Gitlab**

- Ne pas toucher à la branche main avant la version finale.
- Quand on veut coder, il faut créer une nouvelle branche portant le nom de la fonctionnalité qu'on veut implémenter. On code sur cette branche et dès qu'il est bon on le merge avec la branche develop.
- Bien penser à toujours tester le plus possible les branches les plus annexes (on les importe avec merge), avant de les mettre en commun quand ça fonctionne avec les branches centrales (on les rajoute avec merge request, qui se fait directement dans Gitlab).

**Qu'est ce qui correspond à quelle branche ?**

- Dans la branche `main` on ne met que les fichiers permettant de configurer ou de documenter le projet.

- Le codage se fait dans la branche `develop`. Plus précisément, vous créez une sous-branche à partir de cette branche, puis vous codez votre fonctionnalité dans votre branche nommée `features/<nom_de_la_fonctionnalite>` et quand vous avez fini vous faites une merge request de votre branche dans `develop`.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
