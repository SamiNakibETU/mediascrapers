# ed-mediawatch-x

Copie du collecteur X tel qu'il tourne dans ED Mediawatch, avec ses dépendances au projet
(`src.config`, `src.database`, modèles SQLAlchemy). Ce code ne s'importe pas tel quel : il sert
de référence pour comparer avec `src/mediascrapers/x`.

Différences avec le paquet :

- repli Nitter (`nitter_client.py`, `x_html_parser.py`) quand la syndication échoue ;
- orchestration et écriture en base dans `x_collector.py` ;
- scripts de diagnostic et de rattrapage dans `scripts/`.

Ordre de collecte dans `x_collector.run_collection` : syndication, puis backfill Wayback si la
timeline revient vide sur un compte actif, puis Nitter (HTML, puis RSS) si une instance répond.
Les tweets tronqués à 280 caractères sont complétés à la fin du passage.
