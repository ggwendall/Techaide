![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

# TechAide - Charity Website

TechAide est une page de collecte de dons en ligne pour une association caritative. Cette page permet de présenter la cause défendue et de recueillir des promesses de dons via un formulaire en ligne. Le projet a été développé en utilisant les technologies suivantes : Python, Flask, MySQL, HTML/CSS.

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

## Fonctionnalités

- Une page d'accueil présentant l'association et la cause à financer.
- Un formulaire permettant de faire une promesse de don avec les champs suivants : nom, prénom, adresse, e-mail, somme promise, une case à cocher pour indiquer que le donneur a pris connaissance des conditions, etc.
- Une page affichant toutes les informations sur les promesses de don, telles que la liste des donateurs, les sommes promises et les e-mails à contacter, ainsi que le total récolté.
- Les informations du formulaire sont stockées dans une base de données MySQL.

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

## Structure du Projet

Le projet est organisé comme suit :

- `templates` : Dossier contenant les fichiers HTML utilisés pour les différentes pages du site.
    - `index.html` : Page d'accueil présentant l'association et la cause à financer.
    - `donate.html` : Formulaire de promesse de don.
- `static` : Dossier contenant les fichiers statiques tels que les fichiers CSS , SCSS , JS et les images.
- `database.sql` : Fichier contenant le code pour la gestion de la base de données MySQL.
- `app.py` : Fichier principal contenant le code Python pour l'application web.
- `requirements.txt` : Fichier listant les dépendances Python nécessaires pour le projet.

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

## Installation

1. Assurez-vous d'avoir Python et MySQL installés sur votre système.
2. Clonez ce dépôt Git sur votre machine locale.
3. Naviguez vers le répertoire du projet et installez les dépendances en exécutant la commande suivante :

```bash
pip install -r requirements.txt
```

4. Assurez-vous que le serveur MySQL est en cours d'exécution et configurez les informations de la base de données dans le fichier `database.py`.

5. Exécutez l'application en utilisant la commande suivante :

```bash
python app.py
```

6. Accédez à l'application dans votre navigateur en visitant l'URL `http://localhost:5000`.

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

## Crédits

Ce projet a été développé en utilisant les ressources suivantes :

- [Flask](https://flask.palletsprojects.com/) : Framework web Python
- [MySQL](https://www.mysql.com/) : Système de gestion de base de données
- [Bootstrap](https://getbootstrap.com/) : Framework CSS et SCSS
- [Font Awesome](https://fontawesome.com/) : Icônes SVG
- [jQuery](https://jquery.com/) : Bibliothèque JavaScript

## Auteur

Ce projet a été développé par Quenet Gwendal.

<div align=center>

<img src="https://media.giphy.com/media/VgCDAzcKvsR6OM0uWg/giphy.gif" width="50"> 

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

![Bottom](https://github.com/ggwendall/ggwendall/assets/48108275/1f58de6a-f411-45fd-86a6-e9aa673332e6)
