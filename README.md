# TodoList: exemple de projet réalisé en Test Driven Developpement (TDD)
Les informations ci-dessous sont les notes prises suite à la présentation de ce projet 
par **@Rachidj**, les 19 et 26 septembre 2024 sur le serveur Discord "Docstring".
La présentation de @Rachidj est enregistrée ici :
- [partie 1: codage du coeur de l'application en TDD](https://drive.google.com/file/d/1epaTxwzPjRYpcCxEX0EU2BEoqUZbOR7w/view)
- [partie 2: exemple d'implémentation avec FastAPI](https://drive.google.com/file/d/1y2IrHHuf3DTmexayeNMUBXaWrM1Wczmg/view)


## L'esprit du TDD
- On commence par écrire un test, puis on écrit le code nécessaire à la réussite du test 
(et pas une ligne de plus que nécessaire pour que le test passe).
- Quand c'est bon, on écrit le test suivant, puis le code minimal pour le faire réussir.
- Et ainsi de suite...


## Architecture du projet
- On s'occupe d'abord du cœur du projet, qui sera le même quelle que soit l'implémentation 
(ligne de commande, GUI, web...) → c'est ce qui est dans le dossier **todolist**. 
C'est pour ce coder cœur qu'on utilise l'approche TDD. 
- On code ensuite dans le dossier **infrastructure** l'implémentation retenue

## Focus sur le dossier todolist, cœur du projet
- Dans le fichier `todo_repository_protocol.py`, on a écrit un protocole de répertoire
de todo-listes, grâce à la classe `Protocol` du module `typing`. 
**Protocole** = uniquement les signatures des fontions nécessaires, ainsi que les noms et types 
des attributs. Les implémentations devront obligatoirement reprendre ce protocole.
- Dans le fichier `todo_usecase.py`, on a écrit les classes des cas d'utilisations,
qui sont utilisés dans les tests. Pour chacun, on a implémenté la méthode __call__ 
permettant de rendre les instances appelables dans les tests.
- Le modèle de base de todo list est créé dans le fichier `todo_entity.py`. On utilise le module `pydantic` 
pour faciliter le typage.
- Pour simuler l'accès à une base de données, on a créé ce qui s'appelle un **in-memory** 
→ voir le fichier `in_memory_todo_repository.py`, qui simule un CRUD.
