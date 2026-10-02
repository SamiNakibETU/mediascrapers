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
« depuis la mise en demeure contre Nitter » : les instances publiques sont mortes et, depuis
l'archivage du projet en septembre 2026 (section 3.1), ce code n'a plus de source à interroger.
Il reste utile comme référence de parseur et de pagination par curseur.

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

Les faits ci-dessous ont été vérifiés le 2 octobre 2026 à partir des dépôts de code, des
communiqués de la Commission européenne et de la presse spécialisée (références en annexe).
Cet écosystème bouge tous les trimestres : à revérifier avant chaque démarrage.

### 3.1 Trois événements récents qui changent la donne

1. **Nitter est juridiquement mort.** Le 24 août 2026, X Corp a adressé des mises en demeure
   au projet et aux instances ; le dépôt `zedeus/nitter` a été archivé en lecture seule le
   11 septembre 2026 ; les instances publiques sont murées. Le client Nitter de
   `ed-mediawatch-x/` est à considérer comme du code d'archive. **Il ne faut pas bâtir le mode
   crise dessus.**
2. **L'API officielle n'a plus de paliers.** Le palier Free est fermé aux nouveaux comptes
   depuis février 2026, Basic a été migré de force vers le paiement à l'usage le 1er juin 2026,
   Pro est en cours de suppression. Le modèle est désormais : environ 0,005 $ par tweet lu,
   0,010 $ par profil lu, recherche limitée aux 7 derniers jours, `conversation_id` utilisable
   comme opérateur de recherche, pas d'archive complète hors Enterprise. Ordre de grandeur :
   100 000 tweets ≈ 500 $, un million ≈ 5 000 $. **Pour une crise de deux semaines, c'est
   finançable et juridiquement propre.**
3. **L'accès chercheur DSA devient réel.** Après l'amende de 120 M€ du 5 décembre 2025 (dont
   40 M€ pour obstruction à l'accès des chercheurs) et la décision du tribunal de Berlin du
   17 février 2026, la Commission a accepté le 15 juillet 2026 le plan d'action de X : accès
   **gratuit** aux chercheurs éligibles au titre de l'article 40(12), filtrage des candidatures
   revu, et **levée de l'interdiction contractuelle de collecte des données publiques pour les
   chercheurs éligibles**, avec six mois de mise en œuvre (horizon janvier 2027) et audit
   indépendant. En parallèle, l'acte délégué 2025/2050 (en vigueur depuis le 29 octobre 2025)
   ouvre la voie 40(4) via le portail européen d'accès aux données, instruite en France par
   l'Arcom. Les organismes de recherche sans but lucratif et indépendants d'intérêts
   commerciaux sont éligibles : l'IRIS l'est sur le papier. Les premiers retours (DSA
   Observatory, mars 2026) décrivent un processus lent, de type dossier de subvention, avec des
   refus.

### 3.2 Comparatif

| Voie | Recherche | Cascades | Profils / bios | Abonnés | Coût | Risque | Verdict |
|---|---|---|---|---|---|---|---|
| **A. Syndication + fxtwitter + Wayback** (actuel) | non | non | oui (1er cercle) | non | 0 | endpoint non documenté, signalé instable par des tiers depuis 2025 et sans nouveau contenu chez certains depuis avril 2026 ; fonctionnait en production ED Mediawatch en août-septembre 2026 ; peut fermer sans préavis | socle de la veille de fond **tant qu'il répond** ; à sonder chaque jour |
| **B. Pool de comptes X + twscrape** (ce que Nitter faisait en interne : API GraphQL de X avec les cookies d'un compte) | oui | oui (`tweet_replies`, `retweeters`) | oui | oui | 0 hors comptes ; 5 à 20 comptes créés par l'équipe, un proxy résidentiel par compte (quelques dizaines d'euros par mois, ou des IP de box) | suspensions de comptes à prévoir et à remplacer ; bug de pagination de la recherche depuis mars 2026 (recouper par plusieurs requêtes) ; contre les CGU, mais l'IRIS est éligible à la levée d'interdiction DSA de juillet 2026 | **voie crise n° 1** : la seule gratuite qui donne recherche, cascades, retweeteurs et abonnés en volume |
| **C. Zeeschuimer + 4CAT** (capture navigateur, DMI Amsterdam) | oui (ce que l'analyste fait défiler) | oui (fils de réponses) | oui | non | 0 ; temps humain | le plus faible : on collecte ce qu'un compte connecté voit | **voie crise n° 2**, filet de sécurité manuel des analystes si le pool tombe |
| D. API X à l'usage (`search/recent`, `conversation_id`) | oui, 7 jours glissants | oui | oui | payant | ≈ 0,005 $/tweet | nul juridiquement ; pas de rétrospectif | **non retenue** : l'équipe ne veut pas de budget API ; à garder en tête seulement si le pool de comptes devenait intenable |
| **E. Accès chercheur DSA** 40(12) via X, 40(4) via Arcom | oui | oui | oui | oui | 0 | délai de 3 à 9 mois, issue incertaine | **à déposer dès maintenant** pour la version 2027 de l'étude |
| F. Nitter auto-hébergé | oui | oui | oui | oui | serveur + jetons de comptes | projet archivé le 11 septembre 2026, mises en demeure | **écarté** |
| G. Revendeurs de données (Bright Data, Apify…) | oui | oui | oui | oui | à l'usage | traçabilité et licéité faibles pour un livrable DGRIS | écarté |

Deux précisions sur l'existant :

- **fxtwitter** (`api.fxtwitter.com`) fonctionne toujours sans clé et renvoie likes, RT,
  réponses et vues. Il sert à **réhydrater** des tweets connus par leur URL (métriques dans le
  temps, texte intégral), pas à en découvrir.
- **minet** (médialab Sciences Po), auquel on pense naturellement, a sa commande X cassée
  depuis mai 2025 (ticket ouvert par le mainteneur, non résolu) ; gazouilloire est inactif.
  Le médialab a réorienté ses connecteurs vers Bluesky, YouTube, Reddit et Telegram, et ces
  connecteurs-là restent utiles.

### 3.3 Pourquoi « des plateformes comme Nitter y arrivent et pas nous »

Le logiciel Nitter est mort, mais **le mécanisme est reproductible et gratuit hors comptes**.
Depuis février 2024, Nitter ne faisait plus qu'une chose : appeler l'API GraphQL interne de X
avec les cookies de vrais comptes. La bibliothèque Python `twscrape` fait exactement cela,
est maintenue (commits d'août 2026) et expose ce qui manque au dépôt : recherche, tweets et
réponses d'un utilisateur, détail d'un tweet, réponses sous un tweet, retweeteurs, abonnés,
abonnements, profils. Elle gère un pool de comptes et bascule quand l'un est limité. Les
quotas internes sont par compte et par quart d'heure (quelques dizaines de requêtes de
recherche, une vingtaine de tweets chacune) : dix comptes suffisent à une veille mots-clés
toutes les quinze minutes. Ce que cela demande : des comptes créés avec des numéros et des
mails distincts et vieillis quelques semaines, un proxy résidentiel ou une IP de box par
compte, et l'acceptation que certains comptes soient suspendus et remplacés. Le point dur
n'est donc pas technique : il est **organisationnel** (qui crée et porte les comptes) et se
couvre juridiquement par le dossier DSA, puisque le plan d'action de juillet 2026 oblige X à
lever l'interdiction de collecte pour les chercheurs éligibles.

### 3.4 Autres plateformes à ne pas oublier

La note montre que, dans les crises DANA et Helene, la circulation est partie de Telegram et de
sites miroirs (Pravda / Portal Kombat), puis a été relayée sur X, Facebook et TikTok. Un
dispositif centré sur X seul rate l'amont.

| Plateforme | Voie | Faisabilité |
|---|---|---|
| **Telegram** | API officielle (Telethon, tegracli du Leibniz-HBI) sur canaux publics : historique complet, vues, transferts, réactions, commentaires | **élevée, gratuite, stable** ; brique prioritaire n° 2 après X ; limites de débit (environ 200 résolutions de noms par jour et par compte) |
| Sites Pravda / Portal Kombat, médias d'État | `mediascrapers.press` (RSS + extraction) avec une liste de sources dédiée | élevée, déjà outillé ; la liste de domaines est à construire avec VIGINUM / EUvsDisinfo |
| TikTok | Research API, ouverte depuis septembre 2026 aux organismes sans but lucratif enregistrés dans l'UE | moyenne : environ quatre semaines d'instruction ; 1 000 requêtes et 100 000 enregistrements par jour ; vidéos, commentaires, profils |
| Facebook / Instagram | Meta Content Library, ouverte aux organismes sans but lucratif à mission de recherche ; instruction par le CASD pour l'UE | moyenne : quatre à huit semaines ; travail dans une enclave sécurisée facturée, pas d'export brut |
| Bluesky | Jetstream / firehose public | élevée, mais audience française faible |
| YouTube | Data API (quota de base gratuit ; quota étendu réservé aux établissements d'enseignement supérieur) | élevée pour les commentaires et métadonnées, recherche incomplète |

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
  « 112 », « France Alert », noms des ministres) toutes les 15 min via le pool de comptes
  (voie B), doublée par la capture navigateur des analystes (voie C).
- **Cascades** : pour tout tweet dépassant un seuil (par ex. 200 RT) ou émis par un compte
  officiel, récupération de l'arbre de réponses et de citations, re-visité à J+1 et J+3.
- **Snowball** : les comptes qui apparaissent plus de N fois comme amplificateurs entrent dans
  la liste suivie pour la durée de la crise ; leur profil est capturé immédiatement (les comptes
  jetables sont supprimés vite).
- Capture navigateur Zeeschuimer par les analystes en parallèle, agrégée dans 4CAT : c'est la
  voie la plus défendable juridiquement et le filet de sécurité si la voie automatique casse.
- Archivage Wayback (`archive.wayback`) de chaque URL externe partagée au-dessus du seuil : les
  faux sites disparaissent.

### 4.2 Chaîne technique

```
  listes (comptes, mots-clés, sources, canaux)        ← équipe Climat, fichiers YAML versionnés
          │
  ┌───────┴────────────────────────────────────────────────────────┐
  │ collecteurs (mediascrapers)                                    │
  │  x.syndication  x.backfill  x.graphql* (pool)  zeeschuimer_in* │
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
relaient, pas qui les relaie). Les voies B, C ou D le rendent **complet** sur une requête.

### 4.4 Analyses livrables pour l'Observatoire

1. **Cartographie des communautés** par narratif (tableau p. 18) : partition Leiden sur le
   réseau RT, étiquetage des communautés par leurs hashtags, domaines et bios dominantes,
   projection des 161 cas déjà recensés pour relier cas et communautés.
2. **Chronologie d'une crise** : volume horaire par narratif, délai entre premier post et pic,
   délai entre démenti officiel et décrue, part des comptes créés depuis moins de 30 jours.
3. **Indicateurs de coordination** : groupes de comptes qui co-retweetent en moins de 60 s,
   partagent les mêmes URL dans l'heure, ont le même `source`, la même date de création ; score
   par groupe, pas étiquette « bot » par compte : Botometer ferme le 2 novembre 2026 et ne
   notait plus que des comptes d'avant juin 2023 ; les outils vivants sont le Coordination
   Network Toolkit (QUT) et CooRTweet (R), tous deux hors ligne sur des exports CSV.
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
  la voie B sur un pool de comptes. Le risque est la suspension des comptes et, en théorie,
  une action civile ; les mises en demeure d'août 2026 ont visé Nitter, pas des instituts de
  recherche, et le plan d'action DSA de juillet 2026 lève l'interdiction de collecte pour les
  chercheurs éligibles. L'IRIS doit néanmoins l'accepter explicitement. Les voies C et E
  suppriment ce risque.
- **DSA article 40** : deux dossiers à déposer en parallèle, le formulaire « DSA vetted
  researchers » de X (article 40(12), données publiques, gratuit) et une demande 40(4) sur le
  portail européen d'accès aux données, instruite par l'Arcom, avec un protocole de recherche
  et la déclaration du financement DGRIS. L'IRIS, organisme de recherche sans but lucratif, est
  éligible. Le délai est long et les refus existent, mais c'est la seule voie durable pour une
  **étude pluriannuelle**.
- **Attribution** : le dispositif mesure la diffusion et la coordination ; il n'attribue pas à
  un État. Les livrables doivent conserver la distinction de la note (attribué / non attribué)
  et renvoyer à VIGINUM pour l'attribution.

## 6. Plan de travail

| Phase | Durée | Contenu | Prérequis |
|---|---|---|---|
| **0. Décisions** | 1 semaine | qui crée et porte les 5 à 20 comptes X du pool et sur quelles IP ; dépôt des deux dossiers DSA ; liste initiale de comptes / mots-clés / canaux par l'équipe Climat ; sonde quotidienne de l'endpoint de syndication | réunion IRIS |
| **1. Socle froid** | 2 semaines | module `storage` (SQLite, migrations, séries de métriques), `watch --mode cold`, listes YAML, Telegram, liste de sources presse « État + relais », export GEXF, tableau de bord minimal | aucun |
| **2. Voie crise** | 3 semaines | module `x.graphql` adossé à twscrape (recherche, réponses, retweeteurs, abonnés, profils) normalisé dans `Post` / `Profile` ; gestionnaire de pool (ajout par cookies, santé, rotation, remplacement) ; recoupement des recherches pour contrer le bug de pagination ; importateur des exports Zeeschuimer / 4CAT | 2 à 3 comptes pour valider, puis le pool |
| **3. Analyse** | 3 semaines | construction du graphe, Leiden, indicateurs de coordination, codebook FIMI × narratifs en prompt, validation inter-annotateurs sur 200 contenus, gabarits de figures pour la note | données de la phase 1 |
| **4. Exercice à blanc** | 1 semaine | rejouer la DANA 2024 ou un épisode cévenol récent à partir des archives (Wayback + fxtwitter) pour calibrer seuils et cadences ; procédure d'activation écrite (qui déclenche, qui scrolle, qui archive) | phases 1 à 3 |

Charge totale estimée : 10 semaines d'une personne, en parallèle du travail de l'équipe
Climat sur les listes et le codebook. Le régime froid peut tourner dès la fin de la phase 1 :
chaque semaine de ligne de base acquise avant la première crise a de la valeur.

## 7. Verdict

- **Faisable en l'état pour la veille de fond** sur une liste de comptes, avec bios et premier
  cercle, dès que le stockage et la boucle de collecte sont écrits (phase 1).
- **Pas faisable en l'état pour une crise** : il manque la recherche et les cascades. Le
  logiciel Nitter n'est plus une option, mais son mécanisme l'est : un **pool de comptes X
  créés par l'équipe** derrière twscrape, sans budget API, avec la **capture navigateur des
  analystes** en filet de sécurité et le dépôt immédiat des **dossiers DSA** comme couverture.
- **Le bon investissement immédiat** : lancer la phase 0 (décisions, dossier DSA, listes) et la
  phase 1 (socle froid) sans attendre, et brancher Telegram et la presse d'État, qui couvrent
  l'amont des campagnes observées dans la note.
- **Garde-fous** : pseudonymisation, registre RGPD, séparation stricte entre mesure de
  diffusion et attribution.

## Annexe : sources de la section 3 (consultées le 2 octobre 2026)

- Nitter : dépôt `zedeus/nitter` (archivé le 11 septembre 2026), tickets #1301 et #1442 ; The Register, 15 septembre 2026, sur les mises en demeure visant xcancel.
- twscrape : dépôt `vladkens/twscrape` (commits d'août 2026), tickets #295, #298, #315 ; twikit : fork `unclecode/twikit`, ticket d60/twikit #298.
- API X : docs.x.com (inaccessible depuis l'environnement de rédaction), recoupé par quatre billets de revendeurs concordants (Elfsight, Blotato, PostProxy, SocialCrawl) ; chiffres à confirmer sur la console développeur avant tout engagement.
- DSA : Commission européenne, « Commission accepts X's action plan to comply with the Digital Services Act », juillet 2026 ; TechPolicy.Press, juillet 2026 ; Verfassungsblog sur l'amende du 5 décembre 2025 ; GFF sur Democracy Reporting International c. X (Berlin, 17 février 2026) ; help.x.com « DSA vetted researchers » ; Arcom, procédure d'agrément des chercheurs (article 40 du RSN) ; DSA Observatory, 12 mars 2026, sur un refus ; FAQ Coimisiún na Meán, décembre 2025.
- Syndication : discussions Hacker News (2023), billets samwize (août 2025) et shkspr.mobi (avril 2025), ticket tiers de juillet 2026 constatant l'arrêt d'ingestion ; à mettre en regard du fonctionnement observé en production ED Mediawatch en août-septembre 2026.
- fxtwitter : wiki FxEmbed « Status Fetch API ».
- médialab : minet, ticket #1009 (14 mai 2025, ouvert) ; gazouilloire (inactif) ; 4CAT, « Available data sources » ; Zeeschuimer.
- Plateformes : tegracli (Leibniz-HBI) ; TikTok Research API et « Vetted researcher data access » ; Bluesky Jetstream ; research.youtube ; Meta Content Library ; Bellingcat toolkit.
- Corpus et méthodes climat : Climatoscope / ISC-PIF (Chavalarias, arXiv 2406.17135) ; CARDS augmenté (arXiv 2404.15673, Nature Communications Earth & Environment 2024) ; QuotaClimat × Data For Good × Science Feedback (octobre 2025) ; EDMO ; CAAD, ISD ; DeSmog.
- Coordination : Botometer (arrêt le 2 novembre 2026) ; OSoMeNet ; Coordination Network Toolkit (QUT) ; CooRTweet ; CooRnet (archivé le 2 septembre 2024).
