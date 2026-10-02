# Dispositif de veille « désinformation climatique » pour l'Observatoire Défense & Climat

Étude de faisabilité : état du collecteur `mediascrapers`, écarts avec le besoin, architecture
cible et plan de travail.

Version du 2 octobre 2026. Rédigée pour l'équipe de l'Observatoire (IRIS / DGRIS) à partir de la
note *Désinformation climatique et guerre informationnelle* (mai 2026) et du code du dépôt.

---

## 1. Ce que l'Observatoire demande, traduit en besoins de données

La note de mai 2026 pose trois constats méthodologiques qui dictent le cahier des charges :

1. **Le recensement actuel compte des cas, pas des audiences.** Les 161 cas (120 russes, 41
   états-uniens) viennent d'EUvsDisinfo, NewsGuard, Media Matters, ECCO et New Climate, et la
   note reconnaît qu'elle « ne quantifie pas la portée et l'impact » (p. 16). La valeur ajoutée
   d'un collecteur maison est précisément de mesurer la **diffusion** : qui relaie, combien, à
   quelle vitesse, vers quelles communautés.
2. **Les événements climatiques extrêmes sont sous-représentés** (4 % des cas russes) parce que
   la désinformation y arrive « par pics » que les bases de données annuelles ratent (p. 19).
   La DANA de Valence (une centaine de contenus en quelques jours, Maldita) et l'ouragan Helene
   sont les deux études de cas de la Partie 3. Le scénario 3 (Pas-de-Calais 2042) décrit
   exactement ce qu'il faut pouvoir observer : faux comptes « France Alert », faux médias locaux,
   faux bilans, deepfakes, saturation des canaux officiels. **D'où l'architecture à deux
   régimes : veille de fond permanente, et activation en crise.**
3. **La grille d'analyse existe déjà** : la matrice FIMI du SEAE (canaux A/B/C/D, assumé /
   dissimulé, attribué / non attribué) et le tableau « objets × narratifs » (p. 18 : science
   climatique, événements extrêmes, politique énergétique ; ancien déni / nouveau déni). Il
   faut la transformer en **codebook d'annotation** appliqué aux contenus collectés.

Ce que cela implique, en termes de données :

| Besoin analytique | Données nécessaires | Granularité |
|---|---|---|
| Qui porte un narratif, dans quelle case FIMI | comptes : bio, date de création, localisation, site, vérification, abonnés, abonnements | profil complet |
| Comment il se diffuse | tweets : texte intégral, type (original / RT / citation / réponse), identifiants de la cible (`quoted`, `reply_to`), `conversation_id`, horodatage précis | tweet + arêtes |
| À quelle échelle | compteurs : RT, likes, réponses, citations, vues | tweet, répété dans le temps |
| Les cascades (réponses sous un démenti officiel, sous un faux bilan) | arbre de conversation complet, pas seulement les tweets des comptes suivis | conversation |
| Les communautés et la coordination | réseau RT / mention / citation ; co-partage d'URL ; co-RT dans une fenêtre courte ; `source` (client) | graphe |
| Ce qui circule hors des comptes suivis | **recherche par mots-clés / hashtags** sur toute la plateforme | requête |
| Qui suit qui (structure latente) | listes d'abonnés / abonnements | optionnel, coûteux |

## 2. Audit du collecteur actuel

### 2.1 Ce que `mediascrapers` sait faire aujourd'hui

Le paquet est petit (environ 1 500 lignes hors tests), propre, testé (28 tests), sans compte X
ni proxy. Trois voies :

| Voie | Entrée | Sortie | Limites structurelles |
|---|---|---|---|
| `x.SyndicationClient` (endpoint des widgets embarqués) | un handle | 20 à 100 derniers tweets, texte, type, cible RT/citation, compteurs RT/like/réponses/citations, profil | **pas de pagination, pas de recherche, pas de réponses d'autrui, pas de vues** ; tweets longs coupés à 280 ; un passage sur 110 comptes = 6 min |
| `x.Backfill` (Wayback CDX + fxtwitter) | un handle, une année | tweets historiques (ceux qu'un tiers a archivés), vues incluses | échantillon biaisé vers ce qui a été archivé ; dépend d'un service tiers (fxtwitter) |
| `press.*` | liste RSS (60 titres FR, bloc MENA) | articles en texte intégral, détection paywall | rien à redire pour la presse |

Le dossier `ed-mediawatch-x/` contient en plus un client Nitter (RSS + HTML avec pagination par
curseur et compteurs d'engagement) et un parseur HTML éprouvé. Il est désactivé en production
« depuis la mise en demeure contre Nitter » : les instances publiques sont mortes, seul un
auto-hébergement le ferait revivre.

### 2.2 Ce qui a été ajouté dans cette révision

Sans nouvelle dépendance réseau, le modèle de données a été aligné sur l'analyse de réseaux.
Chaque `Post` porte désormais `tweet_id`, `conversation_id`, `author_id`, `reply_to_user_id`,
`quoted_user_id`, `mentions`, `hashtags`, `urls` (développées) et `source` (client de
publication, utile pour repérer l'automatisation). Chaque `Profile` porte la bio, la
localisation, le site, la date de création, les drapeaux de vérification, abonnements, listes,
médias. La page de syndication contient les profils des comptes relayés : `parse_profiles` et
`SyndicationClient.last_profiles` les exposent, et la commande `mediascrapers x profile --neighbours`
les émet. C'est le point de départ d'un *snowball* sur les amplificateurs : un passage sur la
liste de comptes de l'équipe donne gratuitement leur premier cercle avec bios.

Ce qui n'a pas pu être fait ici : vérifier en direct que l'endpoint de syndication répond
toujours au même format. Le bac à sable de cette session n'a pas de sortie réseau vers
`syndication.twitter.com`, `api.fxtwitter.com`, `web.archive.org` ni les instances Nitter. Les
tests sont des tests de parseur sur des fixtures. **À faire depuis une machine de l'IRIS avant
toute décision : `mediascrapers x timeline J_Bardella | head -1` et `mediascrapers x profile
--neighbours MeteoFrance`.**

### 2.3 Matrice des écarts

| Besoin | État | Verdict |
|---|---|---|
| Tweets récents des comptes suivis | syndication | couvert, cadence 2 à 6 min par passage |
| Texte intégral | syndication + fxtwitter | couvert |
| Bio et métadonnées de compte | ajouté dans cette révision | couvert pour les comptes suivis et leur premier cercle |
| Compteurs d'engagement | syndication (sans vues), fxtwitter (avec vues) | couvert ; **pas de série temporelle** sauf à repasser et stocker chaque mesure |
| Historique profond d'un compte | Wayback + fxtwitter | partiel, biaisé, lent (1 requête par tweet) |
| **Réponses sous un tweet (cascades)** | aucune voie | **non couvert** |
| **Recherche par mots-clés / hashtag** | aucune voie | **non couvert** |
| Abonnés / abonnements | aucune voie | non couvert |
| Stockage, reprise, déduplication | « storage is the caller's business » | à construire (était dans ED Mediawatch) |
| Orchestration, cadence, mode crise | absent | à construire |
| Annotation narrative, graphe, clustering | absent | à construire |

Les deux lignes en gras sont bloquantes pour l'étude telle que décrite : sans cascades ni
recherche, on observe des émetteurs connus, pas une campagne. Elles ne se résolvent pas en
améliorant le code existant ; elles exigent une **nouvelle voie d'accès aux données**.

## 3. Voies d'accès aux données X en 2026

Les faits ci-dessous sont établis à la date de rédaction et sont à revérifier avant chaque
démarrage : cet écosystème bouge tous les trimestres.

### 3.1 Comparatif

| Voie | Recherche | Cascades | Profils / bios | Abonnés | Coût | Risque | Verdict |
|---|---|---|---|---|---|---|---|
| **A. Syndication + fxtwitter + Wayback** (actuel) | non | non | oui (1er cercle) | non | 0 | faible, mais endpoint non documenté, peut fermer sans préavis | socle de la veille de fond |
| **B. Nitter auto-hébergé** | oui (recherche Nitter) | oui (page de statut avec réponses, pagination) | oui | oui (pages followers) | serveur + **jetons de session de comptes X réels** | moyen : les comptes prêteurs peuvent être suspendus ; dépend de la maintenance de Nitter ; zone grise CGU | **meilleur rapport capacités / coût pour le mode crise** |
| **C. Bibliothèques GraphQL avec pool de comptes** (twscrape, twikit) | oui | oui (`tweet_details` / réponses) | oui | oui | comptes X + proxies résidentiels | élevé : suspensions, cassures de l'API interne, CGU | utile en complément de B, même mécanique de comptes |
| **D. API officielle X** | Basic : recherche 7 jours, 10 à 15 k tweets / mois ; Pro : recherche complète, `conversation_id`, 1 M tweets / mois | oui via `conversation_id` | oui | Pro | Basic ≈ 200 $/mois ; Pro ≈ 5 000 $/mois | nul juridiquement | Basic insuffisant pour une crise (quota épuisé en une journée) ; Pro hors budget d'une note mais **finançable sur un mois de crise** |
| **E. Accès chercheur DSA (art. 40)** | oui | oui | oui | oui | 0 | dossier auprès du coordinateur national (ARCOM) et de la plateforme ; délais de plusieurs mois ; X conteste les demandes | **à lancer dès maintenant** pour la version 2027 de l'étude, pas pour une crise cet hiver |
| **F. Capture navigateur** (Zeeschuimer + 4CAT, DMI Amsterdam) | oui (ce que l'analyste fait défiler) | oui | oui | non | 0 | faible ; manuel ; volume limité à ce qu'on fait défiler | **complément immédiat pour une cellule de 2 à 3 personnes en crise** : chacun ouvre X, scrolle les recherches, 4CAT agrège |
| G. Revendeurs de données (Bright Data, Apify, etc.) | oui | oui | oui | oui | à l'usage | juridiquement bancal pour une étude publiée ; traçabilité faible | à éviter dans un livrable DGRIS |

### 3.2 Pourquoi « des plateformes comme Nitter y arrivent et pas nous »

Elles n'y arrivent plus gratuitement. Depuis février 2024, X a fermé les comptes invités ; une
instance Nitter ne fonctionne qu'alimentée par les jetons de session de **vrais comptes X**
(script `get_session.py` du projet, un compte peut servir des centaines de requêtes par
quart d'heure avant limitation). Les instances publiques ont été fermées l'une après l'autre
par mise en demeure. En revanche, **une instance privée, non indexée, alimentée par trois à
cinq comptes dédiés, tourne de manière stable** chez de nombreux chercheurs. C'est la voie B.
Le client et le parseur Nitter existent déjà dans `ed-mediawatch-x/` : il faut les remonter
dans le paquet, ajouter la recherche et la page de conversation, et les tester contre
l'instance privée.

Le point dur n'est pas technique, il est **organisationnel** : qui fournit les comptes X, sur
quels numéros de téléphone, avec quelle traçabilité, et qui assume que ces comptes peuvent être
suspendus. Il faut une décision de l'IRIS sur ce point avant d'écrire une ligne de la voie B.

### 3.3 Autres plateformes à ne pas oublier

La note montre que, dans les crises DANA et Helene, la circulation est partie de Telegram et de
sites miroirs (Pravda / Portal Kombat), puis a été relayée sur X, Facebook et TikTok. Un
dispositif centré sur X seul rate l'amont.

| Plateforme | Voie | Faisabilité |
|---|---|---|
| **Telegram** | API officielle (Telethon / Pyrogram) sur canaux publics : messages, vues, transferts, horodatages | **élevée, gratuite, stable** ; brique prioritaire n° 2 après X |
| Sites Pravda / Portal Kombat, médias d'État | `mediascrapers.press` (RSS + extraction) avec une liste de sources dédiée | élevée, déjà outillé ; la liste de domaines est à construire avec VIGINUM / EUvsDisinfo |
| TikTok | Research API (ouverte aux chercheurs européens sous DSA) | moyenne : dossier d'accès, données agrégées |
| Facebook / Instagram | Meta Content Library | moyenne : dossier d'accès via ICPSR, lecture sans export brut |
| Bluesky | Jetstream / firehose public | élevée, mais audience française faible |
| YouTube | Data API (quota gratuit) | élevée pour les commentaires et métadonnées |

## 4. Architecture cible : veille froide, activation chaude

### 4.1 Principe

Deux régimes sur la même base, le second n'étant qu'un changement de cadence et de périmètre.

**Régime froid (permanent, dès maintenant).**
Objectif : constituer la ligne de base sans laquelle une crise n'est pas lisible (qui parle de
climat en temps normal, à quel volume, dans quelles communautés).

- Liste de comptes fournie par l'équipe Climat (émetteurs FIMI A/B/C/D connus, relais français,
  influenceurs climatosceptiques, comptes officiels : Météo-France, VIGICRUES, préfectures,
  sécurité civile, ministère des Armées, FrenchResponse).
- Passage syndication toutes les 2 h ; profils et premier cercle une fois par jour ;
  `press` toutes les heures sur la liste de sources dédiée ; Telegram en continu.
- Stockage de **chaque mesure** d'engagement (table `post_metrics(tweet_id, observed_at, likes,
  rts, …)`) : la vitesse de diffusion se lit sur les différences, pas sur un instantané.
- Classification narrative hebdomadaire par modèle de langage, contre le codebook de la note.

**Régime chaud (activation en crise).**
Déclencheur : vigilance rouge Météo-France ou VIGICRUES, feu majeur, événement en outre-mer, ou
décision de l'équipe. Durée : 7 à 21 jours.

- Cadence syndication 15 min sur la liste élargie.
- **Recherche par mots-clés** (toponymes, hashtags, « bilan », « morts », « HAARP », « géo-ingénierie »,
  « 112 », « France Alert », noms des ministres) toutes les 15 min via la voie B ou D.
- **Cascades** : pour tout tweet dépassant un seuil (par ex. 200 RT) ou émis par un compte
  officiel, récupération de l'arbre de réponses et de citations, re-visité à J+1 et J+3.
- **Snowball** : les comptes qui apparaissent plus de N fois comme amplificateurs entrent dans
  la liste suivie pour la durée de la crise ; leur profil est capturé immédiatement (les comptes
  jetables sont supprimés vite).
- Capture navigateur Zeeschuimer par les analystes en parallèle, agrégée dans 4CAT, comme filet
  de sécurité si la voie automatique casse.
- Archivage Wayback (`archive.wayback`) de chaque URL externe partagée au-dessus du seuil : les
  faux sites disparaissent.

### 4.2 Chaîne technique

```
  listes (comptes, mots-clés, sources, canaux)        ← équipe Climat, fichiers YAML versionnés
          │
  ┌───────┴────────────────────────────────────────────────────────┐
  │ collecteurs (mediascrapers)                                    │
  │  x.syndication  x.backfill  x.nitter*  x.search*  x.thread*    │
  │  press.feed+extract        telegram*          archive.wayback  │
  └───────┬────────────────────────────────────────────────────────┘
          │  Post / Profile / Article / Message (dataclasses, JSONL)
  ┌───────┴──────────────┐
  │ entrepôt             │  SQLite en local, PostgreSQL si équipe ; tables : posts, profiles,
  │ (storage*)           │  post_metrics (séries), edges (rt / quote / reply / mention / url),
  └───────┬──────────────┘  conversations, articles, telegram_messages, annotations
          │
  ┌───────┴──────────────────────────────────────────────────────┐
  │ analyse (analysis*)                                          │
  │  graphe : networkx / igraph → Louvain-Leiden, PageRank, k-core│
  │  coordination : co-RT < 60 s, co-URL, co-hashtag (CooRnet)   │
  │  temporel : séries, détection de pics, demi-vie des rumeurs  │
  │  texte : codebook FIMI × narratifs par LLM, embeddings, BERTopic
  │  export : GEXF pour Gephi, parquet, tableaux pour la note     │
  └───────┬──────────────────────────────────────────────────────┘
          │
  orchestration* : `mediascrapers watch --mode cold|hot --config climdef.yaml`
  (boucle asynchrone, journal, reprise sur incident, alerte sur seuils)

  * = à écrire
```

### 4.3 Modèle de graphe

Nœuds : comptes (clé `user_id`, pas le handle, qui change), tweets, URL / domaines, hashtags.
Arêtes datées :

| Arête | Source déjà disponible | Ce qu'elle mesure |
|---|---|---|
| compte → compte, `retweet` | `quoted_user_id` sur un `retweet` | amplification brute, c'est le réseau classique des communautés |
| compte → compte, `quote` | `quoted_user_id` sur un `quote` | commentaire, souvent conflictuel : sépare les camps |
| compte → compte, `reply` | `reply_to_user_id` | cascades, harcèlement des comptes officiels |
| compte → compte, `mention` | `mentions` | sollicitation, appels à relais |
| compte → URL / domaine | `urls` | co-partage, détection des sites Pravda et faux médias |
| compte → hashtag | `hashtags` | campagnes de hashtag |

Avec la voie A seule, le graphe est **égocentré** sur les comptes suivis (on voit qui ils
relaient, pas qui les relaie). La voie B ou D le rend **complet** sur une requête.

### 4.4 Analyses livrables pour l'Observatoire

1. **Cartographie des communautés** par narratif (tableau p. 18) : partition Leiden sur le
   réseau RT, étiquetage des communautés par leurs hashtags, domaines et bios dominantes,
   projection des 161 cas déjà recensés pour relier cas et communautés.
2. **Chronologie d'une crise** : volume horaire par narratif, délai entre premier post et pic,
   délai entre démenti officiel et décrue, part des comptes créés depuis moins de 30 jours.
3. **Indicateurs de coordination** : groupes de comptes qui co-retweetent en moins de 60 s,
   partagent les mêmes URL dans l'heure, ont le même `source`, la même date de création ; score
   par groupe, pas étiquette « bot » par compte (la littérature a abandonné Botometer).
4. **Classement FIMI des relais** : pour chaque compte au-dessus d'un seuil d'amplification,
   case A/B/C/D proposée par le modèle à partir de la bio, du site et des domaines partagés,
   validée par un analyste.
5. **Flux transplateformes** : première apparition d'une URL ou d'une affirmation sur Telegram,
   presse d'État, X, presse française ; mesure du « saut » vers le grand public.

## 5. Cadre juridique et éthique

- **RGPD** : les tweets publics de personnalités publiques et de comptes de diffusion sont
  traitables au titre de l'intérêt légitime et de la recherche ; les comptes de particuliers
  pris dans les cascades doivent être **pseudonymisés dans tout livrable** (identifiants
  hachés, pas de citation nominative sous un seuil d'audience). Tenir un registre de traitement
  IRIS et une durée de conservation (proposition : 3 ans, données brutes chiffrées).
- **Conditions d'utilisation de X** : la voie A s'appuie sur un endpoint public non documenté,
  la voie B/C sur des comptes contre les CGU. Le risque est la suspension des comptes et, en
  théorie, une action civile ; aucune n'a visé un institut de recherche européen à ce jour, mais
  l'IRIS doit l'accepter explicitement. La voie D et E suppriment ce risque.
- **DSA article 40** : la demande d'accès « chercheur agréé » doit être déposée auprès de l'ARCOM
  (coordinateur français des services numériques) avec un protocole de recherche. L'IRIS, en
  tant qu'organisme de recherche à but non lucratif, est éligible. Le délai est long, mais c'est
  la seule voie durable pour une **étude pluriannuelle** sous contrat DGRIS.
- **Attribution** : le dispositif mesure la diffusion et la coordination ; il n'attribue pas à
  un État. Les livrables doivent conserver la distinction de la note (attribué / non attribué)
  et renvoyer à VIGINUM pour l'attribution.

## 6. Plan de travail

| Phase | Durée | Contenu | Prérequis |
|---|---|---|---|
| **0. Décisions** | 1 semaine | choix de la voie crise (B ou D), fourniture des comptes ou du budget, dépôt du dossier DSA, liste initiale de comptes / mots-clés / canaux par l'équipe Climat | réunion IRIS |
| **1. Socle froid** | 2 semaines | module `storage` (SQLite, migrations, séries de métriques), `watch --mode cold`, listes YAML, Telegram, liste de sources presse « État + relais », export GEXF, tableau de bord minimal | aucun |
| **2. Voie crise** | 3 semaines | si B : remontée du client Nitter dans le paquet, instance privée, `x.search`, `x.thread` (réponses + citations paginées), rotation de jetons ; si D : client API v2 (`search/recent`, `conversation_id`), gestion des quotas | comptes ou clés |
| **3. Analyse** | 3 semaines | construction du graphe, Leiden, indicateurs de coordination, codebook FIMI × narratifs en prompt, validation inter-annotateurs sur 200 contenus, gabarits de figures pour la note | données de la phase 1 |
| **4. Exercice à blanc** | 1 semaine | rejouer la DANA 2024 ou un épisode cévenol récent à partir des archives (Wayback + fxtwitter) pour calibrer seuils et cadences ; procédure d'activation écrite (qui déclenche, qui scrolle, qui archive) | phases 1 à 3 |

Charge totale estimée : 10 semaines d'une personne, en parallèle du travail de l'équipe
Climat sur les listes et le codebook. Le régime froid peut tourner dès la fin de la phase 1 :
chaque semaine de ligne de base acquise avant la première crise a de la valeur.

## 7. Verdict

- **Faisable en l'état pour la veille de fond** sur une liste de comptes, avec bios et premier
  cercle, dès que le stockage et la boucle de collecte sont écrits (phase 1).
- **Pas faisable en l'état pour une crise** : il manque la recherche et les cascades, qui
  dépendent d'une décision d'accès aux données (comptes pour Nitter privé, ou budget API Pro
  le temps de la crise), pas d'un développement.
- **Le bon investissement immédiat** : lancer la phase 0 (décisions, dossier DSA, listes) et la
  phase 1 (socle froid) sans attendre, et brancher Telegram et la presse d'État, qui couvrent
  l'amont des campagnes observées dans la note.
- **Garde-fous** : pseudonymisation, registre RGPD, séparation stricte entre mesure de
  diffusion et attribution.
