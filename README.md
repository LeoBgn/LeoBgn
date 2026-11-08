![Léo Bugyan · Data science et développement Python](./assets/profile.svg)

**[Explorer mes projets](#projets) · [Jouer au défi SQL](#défi-sql) · [Voir le serpent](#contributions) · [LinkedIn](https://www.linkedin.com/in/l%C3%A9o-bugyan-278158357/) · [M’écrire](mailto:bugyan.leo@gmail.com)**

Étudiant en data science, je développe des outils Python pour nettoyer des données, en tirer des indicateurs et les rendre accessibles dans des applications métier.

## Projets

<details>
<summary><strong>01 · CRM et applications métier</strong> &nbsp;·&nbsp; Django, SQL, JavaScript</summary>

Je travaille sur des applications qui centralisent des données dispersées dans des tableurs. J’y combine modélisation relationnelle, contrôles à l’import et interfaces pour retrouver et suivre l’information.

</details>

<details>
<summary><strong>02 · Analyse et automatisation</strong> &nbsp;·&nbsp; Python, pandas, NumPy</summary>

Je développe des scripts pour nettoyer et rapprocher des données de plusieurs sources, puis produire des fichiers structurés, des statistiques descriptives et des graphiques.

</details>

<details>
<summary><strong>03 · Machine learning et vision par ordinateur</strong> &nbsp;·&nbsp; Python</summary>

J’ai travaillé sur l’extraction d’indicateurs à partir de vidéos. Pour comparer des modèles, je prépare un jeu de données commun, je vérifie les doublons et j’évalue les modèles sur le même ensemble.

</details>

## Défi SQL

**En novembre, quel canal compte le plus de clients distincts ayant payé une commande ?** Le tableau utilise des données fictives. Déplie la réponse de ton choix.

| Date | Canal | Client | Statut |
| --- | --- | --- | --- |
| 03/11 | E-mail | A | Payée |
| 05/11 | Web | B | Payée |
| 08/11 | E-mail | A | Payée |
| 14/11 | Web | C | Payée |
| 19/11 | E-mail | D | Annulée |
| 02/12 | Web | D | Payée |

<details>
<summary><strong>A.</strong> Égalité, deux clients par canal</summary>

Les deux commandes payées par e-mail viennent du même client. Il ne compte qu’une fois.

</details>

<details>
<summary><strong>B.</strong> Web, deux clients</summary>

Exact. En novembre, B et C ont payé via le Web, et A a payé par e-mail.

![Résultat du défi SQL. Web, deux clients. E-mail, un client.](./assets/sql-result.svg)

</details>

<details>
<summary><strong>C.</strong> Web, trois clients</summary>

Le client D a payé via le Web en décembre. Sa commande sort de la période étudiée.

</details>

<details>
<summary>Voir la requête SQL</summary>

```sql
SELECT canal, COUNT(DISTINCT client_id) AS clients
FROM commandes
WHERE statut = 'payee'
  AND date_commande >= '2026-11-01'
  AND date_commande <  '2026-12-01'
GROUP BY canal
ORDER BY clients DESC;
```

</details>

## Stack

![Python](https://img.shields.io/badge/Python-325B86?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-405B7A?style=for-the-badge)
![pandas](https://img.shields.io/badge/pandas-473877?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-355786?style=for-the-badge&logo=numpy&logoColor=white)

![Django](https://img.shields.io/badge/Django-135946?style=for-the-badge&logo=django&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F4D74E?style=for-the-badge&logo=javascript&logoColor=252017)
![HTML5](https://img.shields.io/badge/HTML5-B6432B?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-663399?style=for-the-badge&logo=css&logoColor=white)
![Git](https://img.shields.io/badge/Git-A2382B?style=for-the-badge&logo=git&logoColor=white)

## Contributions

![Serpent animé qui mange les cases colorées du calendrier de contributions visible sur mon profil GitHub.](./assets/contribution-snake.svg)
