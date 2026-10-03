# 03 — Revue de littérature : méthodes académiques de détection de la coordination, des cascades et de la manipulation narrative, et données requises

*Rédigé le 2026-10-03. Statut de vérification : les URL/DOI marqués « ✔ » ont été retrouvés via moteur de recherche (titre + auteurs + venue concordants) ; ceux marqués « ✔✔ » ont en plus été ouverts directement (dépôts GitHub). Tout élément que je n'ai pas pu confirmer est marqué **[non vérifié]**. Contrainte technique de la session : l'accès direct à arxiv.org, nature.com, acm.org, tandfonline, springer, pnas.org, pmc, cran et aaai.org était bloqué par le proxy ; seuls github.com et les extraits des résultats de recherche ont pu être lus. Les paramètres numériques cités ci-dessous proviennent donc soit des extraits de recherche, soit des README des dépôts ; les autres sont signalés.*

---

## A. Tableau des sources

| # | Référence | Année / venue | URL / DOI | Statut |
|---|-----------|---------------|-----------|--------|
| 1 | Pacheco, Hui, Torres-Lugo, Truong, Flammini, Menczer — *Uncovering Coordinated Networks on Social Media: Methods and Case Studies* | ICWSM 2021, vol. 15, p. 455-466 | https://ojs.aaai.org/index.php/ICWSM/article/view/18075 ; arXiv:2001.05658 | ✔ |
| 2 | Nizzoli, Tardelli, Avvenuti, Cresci, Tesconi — *Coordinated Behavior on Social Media in 2019 UK General Election* | ICWSM 2021, vol. 15 | https://ojs.aaai.org/index.php/ICWSM/article/view/18074 ; données : https://zenodo.org/records/4647893 | ✔ |
| 3 | Giglietto, Righetti, Rossi, Marino — *It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections* | Information, Communication & Society, 2020, 23(6), p. 867-891 | DOI 10.1080/1369118X.2020.1739732 | ✔ |
| 3b | Giglietto, Righetti, Rossi, Marino — *Coordinated Link Sharing Behavior as a Signal to Surface Sources of Problematic Information on Facebook* | SMSociety 2020 (ACM) | DOI 10.1145/3400806.3400817 | ✔ |
| 3c | Giglietto, Marino, Mincigrucci, Stanziano — *A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election* | Social Media + Society, 2023 | DOI 10.1177/20563051231196866 | ✔ |
| 4 | Righetti, Balluff — *CooRTweet: A Generalized R Software for Coordinated Network Detection* | Computational Communication Research, 2025, 7(1) | DOI 10.5117/CCR2025.1.7.RIGH ; dépôt https://github.com/nicolarighetti/CooRTweet ; CRAN v2.1.2 | ✔✔ (dépôt) |
| 5 | Weber, Neumann — *Amplifying influence through coordinated behaviour in social networks* | Social Network Analysis and Mining, 2021, 11:111 | DOI 10.1007/s13278-021-00815-2 ; code https://github.com/weberdc/find_hccs | ✔✔ (dépôt) |
| 5b | Weber, Neumann — *A General Method to Find Highly Coordinating Communities in Social Media through Inferred Interaction Links* | arXiv 2021 | arXiv:2103.03409 | ✔ |
| 6 | Magelinski, Ng, Carley — *A Synchronized Action Framework for Detection of Coordination on Social Media* | Journal of Online Trust and Safety, 2022, 1(2) | https://tsjournal.org/index.php/jots/article/view/30 ; code https://github.com/CASOS-IDeaS-CMU/coordination-analysis | ✔✔ (dépôt) |
| 6b | Ng, Carley — *A combined synchronization index for evaluating collective action social media* | Applied Network Science, 2023 | DOI 10.1007/s41109-022-00526-3 | ✔ |
| 7 | Luceri, Pantè, Burghardt, Ferrara — *Unmasking the Web of Deceit: Uncovering Coordinated Activity to Expose Information Operations on Twitter* | WWW '24 (ACM Web Conference 2024), p. 2530-2541 | DOI 10.1145/3589334.3645529 ; arXiv:2310.09884 | ✔ |
| 7b | Luceri et al. — *Beyond Interaction Patterns: Assessing Claims of Coordinated Inter-State Information Operations on Twitter/X* | WWW '25 Companion | DOI 10.1145/3701716.3715575 ; arXiv:2502.17344 | ✔ |
| 8 | Cinelli, Cresci, Quattrociocchi, Tesconi, Zola — *Coordinated inauthentic behavior and information spreading on Twitter* | Decision Support Systems, 2022, vol. 160, 113819 | DOI 10.1016/j.dss.2022.113819 | ✔ |
| 9 | Vargas, Emami, Traynor — *On the Detection of Disinformation Campaign Activity with Network Analysis* | ACM CCSW 2020 (Cloud Computing Security Workshop) | DOI 10.1145/3411495.3421363 ; arXiv:2005.13466 | ✔ |
| 10 | Schoch, Keller, Stier, Yang — *Coordination patterns reveal online political astroturfing across the world* | Scientific Reports, 2022, 12:4572 | DOI 10.1038/s41598-022-08404-9 | ✔ |
| 11 | Keller, Schoch, Stier, Yang — *Political Astroturfing on Twitter: How to Coordinate a Disinformation Campaign* | Political Communication, 2020, 37(2), p. 256-280 | DOI 10.1080/10584609.2019.1661888 | ✔ |
| 12 | Tardelli, Nizzoli, Tesconi, Conti, Nakov, Da San Martino, Cresci — *Temporal dynamics of coordinated online behavior: Stability, archetypes, and influence* | PNAS, 2024, 121(20) | DOI 10.1073/pnas.2307038121 | ✔ |
| 12b | Tardelli et al. — *Detection and Characterization of Coordinated Online Behavior: A Survey* | arXiv 2024 | arXiv:2408.01257 | ✔ |
| 13 | Graham / QUT Digital Observatory — *Coordination Network Toolkit* | logiciel 2020 ; article J. Computational Social Science 2024 | DOI 10.25912/RDF_1632782596538 ; DOI article 10.1007/s42001-024-00260-z ; https://github.com/QUT-Digital-Observatory/coordination-network-toolkit | ✔✔ (dépôt) |
| 14 | Yang, Varol, Hui, Menczer — *Scalable and Generalizable Social Bot Detection through Data Selection* (BotometerLite) | AAAI 2020 | arXiv:1911.09179 | ✔ |
| 15 | Sayyadiharikandeh, Varol, Yang, Flammini, Menczer — *Detection of Novel Social Bots by Ensembles of Specialized Classifiers* (Botometer v4) | CIKM 2020 | DOI 10.1145/3340531.3412698 | ✔ |
| 15b | Yang, Ferrara, Menczer — *Botometer 101: social bot practicum for computational social scientists* | J. Computational Social Science, 2022 | DOI 10.1007/s42001-022-00177-5 | ✔ |
| 16 | Ng, Carley — *BotBuster: Multi-Platform Bot Detection Using a Mixture of Experts* | ICWSM 2023, 17(1), p. 686-697 | https://ojs.aaai.org/index.php/ICWSM/article/view/22179 ; https://github.com/quarbby/BotBuster-Universe | ✔✔ (dépôt) |
| 17 | Cresci — *A decade of social bot detection* | Communications of the ACM, 2020, 63(10), p. 72-83 | DOI 10.1145/3409116 | ✔ |
| 18 | Cresci, Di Pietro, Petrocchi, Spognardi, Tesconi — *DNA-inspired online behavioral modeling and its application to spambot detection* | IEEE Intelligent Systems, 2016, 31(5), p. 58-64 | arXiv:1602.00110 | ✔ |
| 19 | Rauchfleisch, Kaiser — *The False positive problem of automatic bot detection in social science research* | PLOS ONE, 2020 | DOI 10.1371/journal.pone.0241045 | ✔ |
| 20 | Gallwitz, Kreil — *Investigating the Validity of Botometer-based Social Bot Studies* | MISDOOM 2022 (Springer LNCS) | DOI 10.1007/978-3-031-18253-2_5 ; arXiv:2207.11474 | ✔ |
| 20b | Gallwitz, Kreil — *The Rise and Fall of 'Social Bot' Research* | SSRN 2021 | https://ssrn.com/abstract=3814191 | ✔ |
| 20c | Cresci, Yang, Spognardi, Di Pietro, Menczer, Petrocchi — *Demystifying Misconceptions in Social Bots Research* | Social Science Computer Review, 2025 | DOI 10.1177/08944393251376707 | ✔ |
| 21 | Vosoughi, Roy, Aral — *The spread of true and false news online* | Science, 2018, 359(6380), p. 1146-1151 | DOI 10.1126/science.aap9559 | ✔ |
| 22 | Goel, Anderson, Hofman, Watts — *The Structural Virality of Online Diffusion* | Management Science, 2016, 62(1), p. 180-196 | DOI 10.1287/mnsc.2015.2158 | ✔ |
| 23 | Juul, Ugander — *Comparing information diffusion mechanisms by matching on cascade size* | PNAS, 2021, 118(46) | DOI 10.1073/pnas.2100786118 | ✔ |
| 24 | Zhao, Zhao, Sano, Levy, Takayasu, Takayasu, Li, Wu, Havlin — *Fake news propagates differently from real news even at early stages of spreading* | EPJ Data Science, 2020, 9:7 | DOI 10.1140/epjds/s13688-020-00224-z | ✔ |
| 25 | Varol, Ferrara, Menczer, Flammini — *Early detection of promoted campaigns on social media* | EPJ Data Science, 2017, 6:13 | DOI 10.1140/epjds/s13688-017-0111-y | ✔ |
| 25b | Ferrara, Varol, Davis, Menczer, Flammini — *The rise of social bots* | Communications of the ACM, 2016, 59(7), p. 96-104 | DOI 10.1145/2818717 | ✔ |
| 26 | (auteurs non confirmés) — *How the cascade inference problem distorts information diffusion* | arXiv 2024 | arXiv:2410.21554 | ✔ (titre/ID) ; auteurs **[non vérifié]** |
| 27 | Grinberg, Joseph, Friedland, Swire-Thompson, Lazer — *Fake news on Twitter during the 2016 U.S. presidential election* | Science, 2019 | DOI 10.1126/science.aau2706 | ✔ |
| 28 | Baribi-Bartov, Swire-Thompson, Grinberg — *Supersharers of fake news on Twitter* | Science, 2024 (31 mai) | DOI 10.1126/science.adl4435 ; données Dryad DOI 10.5061/dryad.44j0zpcmq | ✔ |
| 29 | Nogara, Vishnuprasad, Cardoso, Ayoub, Luceri, Giordano — *The Disinformation Dozen: An Exploratory Analysis of Covid-19 Disinformation Proliferation on Twitter* | ACM WebSci 2022 | DOI **[non vérifié]** | ✔ (titre/venue) |
| 30 | DeVerna, Aiyappa, Pacheco, Bryden, Menczer — *Identifying and characterizing superspreaders of low-credibility content on Twitter* | PLOS ONE, 2024, 19(5) e0302201 | DOI 10.1371/journal.pone.0302201 | ✔ |
| 31 | Coan, Boussalis, Cook, Nanko — *Computer-assisted classification of contrarian claims about climate change* (CARDS) | Scientific Reports, 2021, 11:22320 | DOI 10.1038/s41598-021-01714-4 ; code https://github.com/traviscoan/cards | ✔✔ (dépôt) |
| 32 | Rojas, Algra-Maschio, Andrejevic, Coan, Cook, Li — *Augmented CARDS: A machine learning approach to identifying triggers of climate change misinformation on Twitter* | arXiv 2024 | arXiv:2404.15673 | ✔ |
| 32b | Zanartu et al. (auteurs **[non vérifié]**) — *A technocognitive approach to detecting fallacies in climate misinformation* | Scientific Reports, 2024 | https://www.nature.com/articles/s41598-024-76139-w ; arXiv:2405.08254 | ✔ (URL) |
| 33 | Grootendorst — *BERTopic: Neural topic modeling with a class-based TF-IDF procedure* | arXiv 2022 | arXiv:2203.05794 ; https://github.com/MaartenGr/BERTopic | ✔✔ (dépôt) |
| 34 | CLEF CheckThat! Lab (2026) — *Advancing Multilingual Fact-Checking* ; *Multilingual vs Crosslingual Retrieval of Fact-Checked Claims* | arXiv 2025-2026 | arXiv:2602.09516 ; arXiv:2505.22118 | ✔ (IDs) |
| 35 | Chavalarias, Bouchaud, Chomel, Panahi — *Les nouveaux fronts du dénialisme et du climato-scepticisme : deux années d'échanges Twitter passées aux macroscopes* | Rapport CNRS / ISC-PIF, 13 févr. 2023 | https://hal.science/hal-03986798 ; https://iscpif.fr/climatoscope/ | ✔ |
| 36 | Gaumont, Panahi, Chavalarias — *Reconstruction of the socio-semantic dynamics of political activist Twitter networks* (Politoscope 2017) | PLOS ONE, 19 sept. 2018 | DOI **[non vérifié]** (PMC6145593) | ✔ (titre/venue) |
| 37 | Chavalarias — *Toxic Data : comment les réseaux manipulent nos opinions* | Flammarion, mars 2022 | ISBN 9782080274946 | ✔ |
| 38 | Bouchaud, Ramaciotti, Chavalarias — *Crowdsourced audit of Twitter's recommender systems* | Scientific Reports, 2023 | PubMed 37798318 ; DOI **[non vérifié]** | ✔ (titre/venue) |
| 39 | Chavalarias (JASSS 2024) — *Can a Single Line of Code Change Society? …* | JASSS, 2024, 27(1) 9 | https://www.jasss.org/27/1/9.html | ✔ |
| 40 | médialab Sciences Po — outils gazouilloire, minet, twitwi, xan, ipysigma, graphology | logiciels | https://github.com/medialab ; graphology DOI 10.5281/zenodo.5681257 | ✔✔ |
| 41 | CERES (Sorbonne Université, UFR Lettres ; dir. V. Julliard, GRIPIC/CELSA) | centre de méthodes numériques | https://ceres.sorbonne-universite.fr/ | ✔ |
| 42 | Blakey — *The Day Data Transparency Died: How Twitter/X Cut Off Access for Social Research* | Contexts/SAGE 2024 | DOI 10.1177/15365042241252125 | ✔ |
| 42b | *RIP Twitter API: A eulogy to its vast research contributions* | arXiv 2024 | arXiv:2404.07340 | ✔ |
| 42c | *Finally, Access: How Article 40 DSA Changes Platform Research in Practice* | Political Communication, 2026 | DOI 10.1080/10584609.2026.2664157 | ✔ |
| — | Mazières et al. | — | **non retrouvé** : aucune publication identifiable sous ce nom dans le périmètre (coordination / Twitter FR) ; à préciser par le demandeur | **[non vérifié]** |

---

## B. Familles de méthodes

### B1. Détection de coordination par réseaux de similarité comportementale

#### Principe commun
Toutes les approches ci-dessous partagent un squelette (formalisé par Pacheco et al. 2021, repris par Nizzoli 2021, Luceri 2024, CooRTweet 2025, Tardelli 2024 survey) :
1. choisir une **trace comportementale** (objet partagé : tweet retweeté, URL, hashtag, séquence de hashtags, image, texte, compte mentionné, fil de réponse, horodatage) ;
2. construire un **graphe biparti** comptes ↔ objets ;
3. **projeter** sur les comptes (arête pondérée = nombre d'objets communs, ou similarité cosinus de vecteurs TF-IDF) ;
4. **filtrer** (seuil fixe, percentile, backbone multi-échelle) ;
5. **détecter des communautés** (Louvain, composantes connexes, FSA_V…) et les caractériser.

La contrainte temporelle est le discriminant principal : un partage commun dans une fenêtre très courte (secondes à minutes) est beaucoup plus improbable spontanément qu'un partage commun non contraint dans le temps.

#### B1.1 Pacheco et al. (ICWSM 2021) — cadre général, 5 études de cas
- **Traces** : (i) partage de *handle* (changements de pseudo coordonnés, détecté via logs Botometer) ; (ii) **similarité d'images** (profil/médias) ; (iii) **séquences de hashtags** (5-grammes identiques) ; (iv) **co-retweet** ; (v) **synchronisation temporelle** (activité dans les mêmes intervalles).
- **Paramètres** (extraits) : pour le co-retweet, exclusion des auto-retweets et des comptes ayant **< 10 retweets** ; pondération **TF-IDF** des tweets retweetés (pénalise les tweets très populaires) ; similarité **cosinus** entre vecteurs de comptes. Seuils de filtrage des arêtes dépendants du cas ; valeurs exactes **[non vérifié]**.
- **Données minimales** : `user_id`, `tweet_id`, `retweeted_status.id` (ou `referenced_tweets` v2), `created_at`, `entities.hashtags`, `entities.urls`, `user.screen_name` (historique), URLs des médias (pour images).
- **Outil** : `osome-iu/coordination-detection` (Python) — 4 méthodes implémentées (handles, séquences de hashtags, co-retweet, co-temporalité) ; la similarité d'images n'est **pas** implémentée. https://github.com/osome-iu/coordination-detection ✔✔
- **Limites** : non supervisé → pas de vérité terrain ; les seuils sont ad hoc ; sensible aux comptes très actifs ; nécessite un volume de tweets important par compte.

#### B1.2 Nizzoli et al. (ICWSM 2021) — UK GE 2019, « degré de coordination »
- **Trace** : co-retweet. Biparti comptes ↔ tweets retweetés, **TF-IDF**, **cosinus**, puis filtrage par **backbone multi-échelle** (Serrano et al.), communautés **Louvain**, estimation d'un degré de coordination continu (non binaire).
- **Données** : ~11 M tweets, 12 nov. – 12 déc. 2019, publiés sur Zenodo (ids). Champs : `user_id`, `retweeted_status.id`, `created_at`.
- **Limite** : étude uniquement sur co-retweet ; suite dans Tardelli et al. PNAS 2024 (réseau **multiplexe temporel** + détection dynamique de communautés : communautés instables, archétypes).

#### B1.3 Giglietto et al. (ICS 2020 ; SMSociety 2020 ; SM+S 2023) — Coordinated Link Sharing Behavior (CLSB) & CooRnet
- **Trace** : co-partage d'**URL** (articles) par des entités Facebook/Instagram (pages, groupes, profils vérifiés) dans un **intervalle de coordination** court.
- **Paramètres** (README/doc CooRnet, extraits) : `coordination_interval` en secondes, soit fixé manuellement, soit **estimé** par `estimate_coord_interval()` à partir de la distribution des délais entre premier partage et partages suivants (principe : identifier les partages « anormalement rapides » par rapport à l'ensemble du jeu). La valeur exacte des quantiles par défaut (q, p) **[non vérifié]**. `percentile_edge_weight` **= 0,90 par défaut** (on ne garde que les paires ayant coordonné plus que 90 % des paires).
- **Données minimales** : liste d'URL + date de publication ; puis, via CrowdTangle, pour chaque partage : `account.id/name/platform`, `date` (horodatage du post), `expandedLinks`, métriques d'engagement. **CrowdTangle a fermé en août 2024 → le dépôt CooRnet est archivé (2 sept. 2024)** et renvoie vers CooRTweet (R) et coordination-network-toolkit (Python). ✔✔
- **Extensions** : `CooRnet_ImgTxt` (images avec texte identique) ; workflow longitudinal 2022 (SM+S 2023).
- **Limites** : dépendance totale à CrowdTangle (désormais Meta Content Library, accès restreint) ; la coordination de pages d'un même média est « légitime » → besoin de qualification manuelle (cadre A-B-C : Actors, Behavior, Content).

#### B1.4 Righetti & Balluff — CooRTweet (CCR 2025, CRAN 2.1.2)
- **Principe** : définition minimale et abstraite de la coordination : « des comptes partageant le **même objet** dans la **même fenêtre temporelle**, de façon **répétée** ». Multi-plateforme et multi-modal (URL, hashtags, texte, images, retweets, « co-posting »…).
- **Format d'entrée (champs exacts)** : `object_id` (identifiant de l'objet partagé), `account_id`, `content_id` (identifiant du post), `timestamp_share` (epoch). `prep_data()` convertit le JSON Academic API v2.
- **Paramètres** : `time_window` **= 10 s par défaut** ; `min_participation` (activité minimale d'un compte) ; `edge_weight` / `percentile` (filtrage des arêtes) ; `generate_coordinated_network()` produit le graphe igraph.
- **Limites** : fenêtre très courte par défaut (orientée automatisation) ; comme toute méthode biparti, pas de vérité terrain intégrée.

#### B1.5 Weber & Neumann (SNAM 2021 ; arXiv 2021) — Latent Coordination Networks (LCN) / Highly Coordinating Communities (HCC)
- **Traces (critères d'inférence de liens)** : co-retweet, co-mention, co-hashtag, co-URL, co-reply (même fil de réponses) ; variante « retweet rapide » non implémentée dans le dépôt.
- **Fenêtres** : fenêtres discrètes (`find_behaviour_via_windows.py`) ; fenêtres **décroissantes** expérimentales (facteur alpha). Les expériences de temps d'exécution couvrent des fenêtres de **10 s à 15 min** ; pas de défaut unique.
- **Extraction HCC** : **FSA_V** (variante de Focal Structures Analysis), kNN (k = ln|U|), seuil sur poids d'arêtes.
- **Données** : tweets JSON bruts → CSV d'interactions (`user_id`, `interaction_type`, `target`, `timestamp`).
- **Outil** : https://github.com/weberdc/find_hccs ✔✔

#### B1.6 Magelinski, Ng, Carley (JOTS 2022) — Synchronized Action Framework ; Ng & Carley (ANS 2023) — indice de synchronisation combiné
- **Principe** : réseau **multi-vues** (une vue par type d'action : hashtag, URL, mention ; 3 vues) où deux comptes sont liés selon la force de leur synchronisation dans des fenêtres étroites ; détection d'anomalies sur les comptes.
- **Fenêtre** : « fenêtre glissante » paramétrable dans le code ; la valeur de 5 min souvent citée **[non vérifié]**.
- **Données** : JSON Twitter v1/v2 (`created_at`, `entities.hashtags/urls/user_mentions`, `user.id`).
- **Outil** : https://github.com/CASOS-IDeaS-CMU/coordination-analysis ✔✔ (sortie : CSV de paires d'acteurs ayant effectué la même action dans des intervalles chevauchants).
- **Extension 2023** : indice combinant tous les types d'actions au lieu d'une dimension à la fois.

#### B1.7 Luceri, Pantè, Burghardt, Ferrara (WWW 2024) — fusion multi-indicateurs
- **Indicateurs** : **co-retweet**, **co-URL**, **retweet rapide** (fast retweet), **hashtags partagés** (séquences), **similarité textuelle** (embeddings). Pour chaque indicateur : réseau de similarité comptes, arêtes pondérées par **cosinus** entre vecteurs de comptes ; puis **fusion** en un réseau unique ; détection des « key players » via centralité / structure.
- **Données** : jeux Twitter *Information Operations* (comptes étatiques divulgués par Twitter) + comptes contrôle. Champs : `user_id`, `retweeted_status.id`, `created_at` (delta pour fast retweet), `entities.urls`, `entities.hashtags`, `text`.
- **Suite 2025** (*Beyond Interaction Patterns*) : montre que des « similarités d'interaction » entre opérations étatiques différentes peuvent être des **faux positifs** structurels → appel à aller au-delà des patterns d'interaction.
- **Limites** : vérité terrain = divulgations plateformes (biais de sélection) ; seuils de fusion non universels.

#### B1.8 Vargas, Emami, Traynor (ACM CCSW 2020) — classification supervisée sur séries de réseaux
- **Principe** : réseaux de coordination **quotidiens** (co-retweet, co-hashtag, co-URL, co-mention… **[liste exacte non vérifiée]**) → features statistiques de graphe → classifieur binaire campagne/légitime.
- **Résultats** : F1 = 0,98 en distribution ; **F1 = 0,71 hors distribution** (hausse des faux positifs).
- **Données** : archives Twitter Information Operations + échantillons légitimes ; champs d'interaction + `created_at`.

#### B1.9 Keller, Schoch, Stier, Yang (Pol. Comm. 2020) ; Schoch et al. (Sci Rep 2022) — astroturfing et traces de la relation principal-agent
- **Principe** : les agents rémunérés d'une campagne produisent des patterns détectables (**co-tweet** : même texte original au même moment ; **co-retweet** : même tweet retweeté au même moment), sous-produits de l'organisation du travail (horaires de bureau, consignes).
- **Paramètres (Sci Rep 2022, extrait)** : lien de co-retweet si deux comptes retweetent le même message dans une fenêtre d'**1 minute**, **au moins 10 fois** ; même logique pour le co-tweet. Résultat : en moyenne **74 %** des comptes de chaque campagne de l'archive Twitter IO présentent du co-tweeting/co-retweeting.
- **Vérité terrain** : 2020 — dossiers judiciaires de la campagne du NIS sud-coréen (2012) ; 2022 — archive Twitter Information Operations (toutes campagnes).
- **Données** : `user_id`, `text`, `retweeted_status.id`, `created_at` à la seconde.
- **Limites** : fenêtre 1 min + ≥10 répétitions = très conservateur (bonne précision, rappel limité) ; dépend de la granularité des horodatages.

#### B1.10 Cinelli, Cresci, Quattrociocchi, Tesconi, Zola (DSS 2022)
- **Principe** : CIB = mélange de comptes authentiques, faux et dupliqués ; étude de l'effet de la coordination sur la **diffusion** (cascades), en combinant détection de coordination (co-retweet) et métriques de propagation.
- **Données** : tweets + arbres de retweets ; champs standards de retweet + horodatage. Détails de seuils **[non vérifié]**.

#### B1.11 Coordination Network Toolkit (QUT, Graham 2020 ; JCSS 2024)
- **Types** : co-retweet, co-tweet (texte verbatim), co-link (URL), co-reply, co-similarity (Jaccard sur texte), co-post.
- **Fenêtre par défaut : 60 s** pour tous les types.
- **CSV d'entrée (ordre imposé)** : `message_id, user_id, username, repost_id, reply_id, message_text, timestamp (secondes), urls (séparées par espace)`. Sortie GraphML (Gephi). Licence MIT. ✔✔

**Synthèse B1 — champs minimaux communs à toute détection de coordination** : `account_id`, `post_id`, `timestamp` (seconde), et au moins un **objet** : `retweeted_post_id` / `quoted_id`, `urls[]` (normalisées), `hashtags[]`, `mentions[]`, `in_reply_to_id` / `conversation_id`, `text`, `media_url` (hash perceptuel). Le **graphe de followers n'est pas requis**. Les métriques d'engagement ne sont pas requises pour la détection, seulement pour la caractérisation.

---

### B2. Détection de bots

#### Principe
Classification supervisée compte par compte à partir de features de profil, de contenu, de réseau et de temporalité ; ou modélisation comportementale non supervisée (séquences d'actions).

#### Outils et features
- **Botometer v4** (Sayyadiharikandeh et al., CIKM 2020) : > **1 000 features** en 6 catégories (métadonnées utilisateur, réseaux de retweet et de mention, temporalité, contenu, sentiment) ; nécessite les **200 derniers tweets** du compte ; architecture *Ensemble of Specialized Classifiers* (un classifieur par type de bot, règle du max) ; +56 % de F1 sur comptes inédits. **Dépendant de l'API Twitter v1.1 → non opérationnel depuis 2023** (Botometer 101, JCSS 2022, documente l'usage).
- **BotometerLite** (Yang, Varol, Hui, Menczer, AAAI 2020) : métadonnées minimales du profil uniquement (âge du compte, nombre de followers/friends, statuses_count, favourites_count, présence d'une description, de photo, longueur du nom, ratio followers/friends, cadence = statuses/âge…), permettant le passage à l'échelle sur le flux complet. Le dépôt `osome-iu/BotometerLite` renvoie 404 au 2026-10-03.
- **BotBuster** (Ng & Carley, ICWSM 2023) : *mixture of experts*, chaque expert traite une portion d'information (**username, screen name, description, posts, métadonnées**) → robuste aux données incomplètes ; multi-plateforme (Twitter/X, Reddit, Instagram, Telegram) ; F1 moyen 73,5 vs 45,1 pour les baselines sur 10 jeux Twitter ; **36 posts suffisent** à une classification stable. Dépôt : https://github.com/quarbby/BotBuster-Universe ✔✔ (+ BotSorter, BotBias).
- **DNA numérique** (Cresci et al., IEEE IS 2016) : encoder la séquence d'actions d'un compte (tweet, retweet, réponse…) en chaîne de caractères ; détecter les groupes partageant une **longue sous-chaîne commune** (LCS) → détection de *groupes* de spambots, non de comptes isolés. Requiert : timeline ordonnée de chaque compte avec type d'action.
- **Cresci 2020 (CACM)** : revue de la décennie ; passage de la détection individuelle à la **détection de groupes** et aux approches adversariales.

#### Champs requis (profil X/Twitter)
`created_at` (âge du compte), `followers_count`, `following_count` (friends), `statuses_count` (tweet_count), `listed_count`, `favourites_count`, `verified`, `description` (longueur, URLs, emojis), `profile_image_url` (défaut ou non), `screen_name` (entropie, chiffres), `name`, `location`, `url` ; pour les modèles complets : les N derniers posts avec `created_at` (cadence, entropie inter-arrivées), `source` (client), proportions retweet/réponse/original, mentions/hashtags/URLs par tweet, langue.

#### Critiques
- **Rauchfleisch & Kaiser (PLOS ONE 2020)** : 5 jeux (n = 4 134), anglais/allemand, 3 mois : scores Botometer instables dans le temps, mauvais en allemand, seuils arbitraires → nombreux faux positifs *et* faux négatifs ; la plupart des études en sciences sociales comptent des humains comme bots.
- **Gallwitz & Kreil (MISDOOM 2022 ; SSRN 2021)** : inspection manuelle de centaines de comptes étiquetés « bots » dans des études évaluées par les pairs → **aucun** bot social trouvé ; conclusion : ces études ont mesuré des artefacts.
- **Réponse** : Cresci et al. 2025 (SSCR) *Demystifying Misconceptions in Social Bots Research*.
- **Conséquence méthodologique** : préférer des indicateurs comportementaux de **groupe** (coordination) et une **validation manuelle** ; traiter le score bot comme une variable continue, jamais comme un seuil dichotomique ; la fermeture de l'API rend de toute façon Botometer inopérant sur X.

---

### B3. Cascades et diffusion

#### Principe
Reconstruire l'arbre de propagation d'un contenu (qui a repartagé qui, quand), puis mesurer : taille, profondeur, largeur maximale, **viralité structurelle** (Goel et al. 2016 : indice de Wiener = distance moyenne entre toutes les paires de nœuds de l'arbre ; faible = diffusion « broadcast », élevé = diffusion « virale » de pair à pair), vitesse (temps pour atteindre k nœuds).

#### Résultats clés
- **Vosoughi, Roy, Aral (Science 2018)** : ~126 000 cascades de rumeurs (2006-2017), ~3 M personnes ; le faux diffuse plus loin, plus vite, plus profond, plus largement ; le top 1 % des fausses cascades atteint 1 000-100 000 personnes, le vrai rarement > 1 000 ; le vrai met 6× plus de temps à atteindre 1 500 personnes ; +70 % de probabilité de retweet pour le faux.
- **Juul & Ugander (PNAS 2021)** : en **appariant sur la taille des cascades**, les différences structurelles vrai/faux de Vosoughi disparaissent (elles tiennent à la distribution des tailles) ; les différences images/vidéos/news/pétitions persistent → toute comparaison structurelle doit contrôler la taille.
- **Zhao et al. (EPJ DS 2020)** : Weibo + Twitter (Japon) : signaux topologiques distinctifs du faux dès **5 h** après les premiers repartages, sans contenu ni infos utilisateurs.
- **Varol, Ferrara, Menczer, Flammini (EPJ DS 2017)** : détection précoce des campagnes promues (memes/trending) à partir de features de réseau, de temporalité, de contenu et d'utilisateurs ; Ferrara et al. 2016 (CACM) pour le cadre « rise of social bots ».

#### Données requises et problème structurel de X/Twitter
- Idéal : pour chaque repartage, `(repartageur, source immédiate, timestamp)`. **Or l'API Twitter/X attribue tout retweet à l'auteur original** (`retweeted_status` pointe toujours vers la racine ; un « retweet de retweet » n'est pas exposé) → la cascade brute est une **étoile**.
- Méthode standard de reconstruction : **Time-Inferred Diffusion** (popularisée par Vosoughi et al.) : pour chaque retweeteur, le parent est le compte qu'il **suit** ayant retweeté le plus récemment avant lui → requiert le **graphe de followers** des participants (coûteux ; endpoint followers quasi inaccessible aujourd'hui sur X) + horodatages exacts. Sans graphe de followers, approximation par ordre temporel + popularité, avec biais documentés (arXiv:2410.21554, *cascade inference problem*).
- Les **réponses** et **citations** (quotes) exposent, elles, leur parent direct (`in_reply_to_status_id`, `conversation_id`, `quoted_status_id`) → arbres de conversation reconstructibles sans graphe social.
- Champs minimaux : `post_id`, `author_id`, `created_at` (ms si possible), `retweeted_id`/`quoted_id`/`in_reply_to_id`, `conversation_id`, `author.followers_count` ; optionnel : liste de followers des diffuseurs.
- **Limites** : impossible de distinguer broadcast et viral sans reconstruction ; les métriques `retweet_count` agrégées ne suffisent pas ; depuis 2023, la collecte exhaustive d'une cascade sur X est pratiquement impossible sans accès DSA art. 40.

---

### B4. Analyse narrative

#### B4.1 Topic modelling neuronal — BERTopic (Grootendorst 2022)
- Pipeline modulaire : embeddings sentence-transformers → **UMAP** → **HDBSCAN** → tokenisation → **c-TF-IDF** par cluster → représentation (mots-clés, ou étiquetage **LLM**). Modèle multilingue (`language="multilingual"`, 50+ langues). Variantes : topics dynamiques (par fenêtre temporelle), guidés, hiérarchiques.
- **Données** : `text` nettoyé (retrait URL/mentions), `created_at` pour les topics dynamiques, `author_id` pour mesurer la concentration d'auteurs par topic. Paramètres typiques : `min_cluster_size` 15-100 selon volume ; `n_neighbors` UMAP 15 ; `nr_topics` auto.
- **Limites** : tweets courts → bruit ; instabilité de l'UMAP (fixer `random_state`) ; les clusters ne sont pas des « narratifs » (une narration = acteurs + événement + cadrage), d'où la nécessité d'une couche d'extraction de claims.

#### B4.2 Taxonomie CARDS et Augmented CARDS (climat)
- **CARDS** (Coan, Boussalis, Cook, Nanko, Sci Rep 2021) : taxonomie hiérarchique des claims contrariens en **5 super-catégories** (1 : le réchauffement n'a pas lieu ; 2 : pas causé par l'humain ; 3 : les impacts ne sont pas graves ; 4 : les solutions ne marchent pas ; 5 : science/mouvement climatique non fiables) et sous-claims ; classifieur **RoBERTa + régression logistique** (ensemble), entraîné sur think tanks conservateurs et blogs contrariens (~20 ans). Dépôt : https://github.com/traviscoan/cards (Apache-2.0, poids 3,5 Go, notebooks). ✔✔
- **Augmented CARDS** (Rojas et al., arXiv 2024) : modèle **hiérarchique en deux étapes** adapté aux tweets ; appliqué à **5 M tweets climat sur 6 mois de 2022** ; > 50 % des claims contrariens sont des **attaques contre les acteurs climatiques** (cat. 5) ; pics déclenchés par 4 stimuli (événements politiques, événements naturels, influenceurs contrariens, influenceurs convaincus).
- **Fallacies** (Sci Rep 2024, arXiv:2405.08254) : détection des **sophismes** (approche « technocognitive ») complémentaire à CARDS.
- **Données** : `text` (anglais ; une traduction ou un modèle FR est nécessaire pour un corpus français — point ouvert), `created_at` (séries temporelles), `author_id` (influenceurs).
- **Limites** : taxonomie anglo-centrée ; performances dégradées sur sous-claims rares ; pas de version française validée identifiée **[non vérifié]**.

#### B4.3 Stance detection, clustering d'embeddings multilingues, claim matching par LLM
- **Stance** : classification pour/contre/neutre vis-à-vis d'une cible ; modèles encodeurs fine-tunés ou LLM zero-shot ; données : `text` + cible explicite ; limites : dépendance au domaine, sarcasme, FR sous-doté. (Références de surveys non vérifiables dans cette session → **[non vérifié]**.)
- **Clustering multilingue** : embeddings multilingues (LaBSE, multilingual-e5, paraphrase-multilingual) + HDBSCAN/BERTopic pour regrouper des posts de langues différentes véhiculant la même claim ; données : `text`, `lang`.
- **Claim matching / fact-checked claim retrieval** (CLEF CheckThat!, éditions 2021-2026 ; arXiv:2505.22118 compare approches multilingues vs cross-lingues ; CheckThat! 2026 inclut EN/DE/FR) : apparier un post à une base de fact-checks (ClaimReview) par similarité d'embeddings puis **re-ranking LLM** ; données : `text` du post + base de claims vérifiées (titre, claim, verdict, langue). Limites : biais de langue et de récupération documentés (arXiv:2509.25138), hallucination des LLM en génération.
- **Champs minimaux B4** : `post_id`, `text`, `lang`, `created_at`, `author_id` ; optionnel : `urls[]` (pour relier aux domaines/fact-checks), `media` (OCR pour images-texte).

---

### B5. Écosystème français

#### B5.1 Sciences Po médialab (https://github.com/medialab) ✔✔
- **gazouilloire** : collecte longue durée de tweets (API v1.1 *search* + *filter*, comblement automatique des trous) ; export CSV avec champs normalisés (id, texte, auteur, horodatages, hashtags, liens, médias, géo, infos de retweet, fil de conversation). Clés API créées après le 29 avr. 2022 : *search* seulement. **De fait inopérant depuis la fermeture de l'API gratuite (2023)**, mais toujours maintenu pour les corpus existants.
- **twitwi** : normalisation des payloads Twitter v1.1/v2 **et Bluesky** en lignes plates (`TWEET_FIELDS`), anonymisation, extraction de timestamp depuis l'ID.
- **minet** : CLI/lib Python de webmining ; collecte par API (Bluesky, MediaCloud, TikTok, Twitter, Wikipedia, YouTube) et **scraping** (Instagram, Reddit, Telegram, TikTok, Twitter) ; `minet fetch/extract/scrape/crawl/url-parse` ; `minet twitter scrape` (fragile face aux contre-mesures de X — statut à vérifier au cas par cas).
- **xan** (ex-xsv, Rust) : manipulation CSV massive (filtres, agrégations, jointures, expressions, visualisation terminal).
- **ipysigma** (widget Jupyter sigma.js) + **graphology** (JS ; Louvain, métriques, ForceAtlas2 ; DOI 10.5281/zenodo.5681257) : visualisation/analyse de graphes de retweets, de co-URL, etc.
- **Travaux 2024-2026 sur X après fermeture de l'API** : non vérifiables dans cette session ; ce que l'on peut affirmer : (i) le médialab (J.-P. Cointet) utilisait massivement l'API pour la polarisation et la désinformation (CJR 2023) ; (ii) la boîte à outils a pivoté vers **Bluesky, TikTok, Telegram, YouTube** (minet, twitwi) ; (iii) le cadre légal de remplacement est le **DSA art. 40** (40(12) données publiques ; 40(4) données non publiques via les coordinateurs nationaux ; acte délégué en vigueur depuis le **29 oct. 2025**) — cf. Political Communication 2026, DOI 10.1080/10584609.2026.2664157. Les projets spécifiques du médialab sous art. 40 : **[non vérifié]**.

#### B5.2 ISC-PIF / CNRS — David Chavalarias
- **Politoscope** (2016-) : collecte en continu (~3 000 élus/cadres suivis ; 0,5-2 M tweets/jour) ; cartes politiques par **graphe de retweets** (lien = A a retweeté B), communautés et dynamique socio-sémantique. Présidentielle 2017 : 60 M tweets, 2,4 M comptes ; fake news (Décodex) = 0,1 % du contenu, 73 % diffusées par deux communautés (Gaumont, Panahi, Chavalarias, PLOS ONE 2018).
- **Toxic Data** (Flammarion, 2022) : synthèse grand public des méthodes (macroscopes, ingérences, astroturfing).
- **Climatoscope** — rapport **« Les nouveaux fronts du dénialisme et du climato-scepticisme »** (Chavalarias, Bouchaud, Chomel, Panahi, 13 févr. 2023, HAL hal-03986798) : deux ans d'échanges Twitter (FR + monde) ; ~30 % de comptes dénialistes parmi les comptes traitant du climat ; **hausse nette des comportements inauthentiques depuis 2019** (astroturfing possible) ; intensification en France depuis juillet 2022. Méthode : graphe de retweets, détection de communautés, scores d'inauthenticité, analyse sémantique (Gargantext). Détails des seuils d'inauthenticité **[non vérifié]** (rapport non ouvert).
- **Audit du système de recommandation de Twitter** (Bouchaud, Ramaciotti, Chavalarias, Sci Rep 2023) : collecte **crowdsourcée** (extension navigateur) des timelines ; amplification des amis de même communauté, des contenus toxiques/émotionnels, asymétrie politique. Illustre la mesure **exposition réelle vs abonnements**.
- **JASSS 2024** (Chavalarias et al.) : modélisation des risques systémiques des recommandeurs optimisant l'engagement.
- Dépôts GitHub ISC-PIF : `tweetoscope`, `python-gargantext`, `OpenPortability` (migration hors X). ✔✔
- **Données requises par ces travaux** : flux complet de tweets avec `retweeted_status`, `user`, `text`, `created_at` ; profils (`created_at`, compteurs) pour les scores d'inauthenticité. **Depuis 2023, le Politoscope n'a plus d'accès API équivalent** (statut précis **[non vérifié]**).

#### B5.3 CERES (Sorbonne Université) / GRIPIC-CELSA
- Centre d'expérimentation en méthodes numériques pour les SHS (Faculté des Lettres), dirigé par Virginie Julliard (GRIPIC/CELSA). Outil **Restweet** (collecte Twitter) **inutilisable pour de nouvelles collectes depuis la fermeture de l'API** ; ateliers CrowdTangle ; travaux sur la modération (invisibilisation de contenus LGBT/TDS). Orientation : analyse sémiotique et discursive plus que détection algorithmique.

#### B5.4 Mazières et al.
- Référence **non identifiée** avec certitude (homonymes possibles) ; aucune publication ne pouvant être rattachée sans ambiguïté aux méthodes ci-dessus. **[non vérifié]** — à préciser.

---

### B6. Exposition vs amplification : viralité organique vs inauthentique

#### Principe
Distinguer (a) **l'exposition** (combien de personnes ont vu), (b) **l'engagement** (likes, repartages), (c) **l'amplification** (part de l'engagement produite par un petit nombre de comptes ou par des comptes coordonnés/automatisés).

#### Résultats de référence
- **Grinberg et al. (Science 2019)** : panel d'électeurs US sur Twitter (2016) ; **1 % des utilisateurs reçoivent 80 % de l'exposition** aux fake news ; **0,1 % en partagent 80 %** ; fake news ≈ 6 % de la consommation d'actualités. Méthode : panel apparié registres électoraux ↔ comptes, timelines reconstruites via la liste des **followees** (exposition potentielle).
- **Baribi-Bartov, Swire-Thompson, Grinberg (Science 2024)** : 2 107 « supersharers » (sur 664 391 électeurs) produisent 80 % des fake news ; atteignent 5,2 % des électeurs présents ; fournissent ~¼ des fake news reçues par leurs followers ; volume **manuel** (retweets persistants), pas automatisé ; surreprésentation femmes, âgés, républicains.
- **DeVerna et al. (PLOS ONE 2024)** et **Nogara et al. (WebSci 2022)** : « superspreaders » de contenus peu crédibles ; 10 comptes (0,003 %) à l'origine de 34 % du contenu peu crédible sur 8 mois ; 0,25 % des comptes → > 70 % ; métriques simples (volume de partage pondéré par les retweets reçus) prédisent les futurs superspreaders ; profils = pundits, médias peu crédibles et leurs comptes affiliés, influenceurs politiques, langage plus toxique.
- **Bouchaud et al. (Sci Rep 2023)** : exposition algorithmique mesurée côté utilisateur (timelines réelles) ≠ abonnements.

#### Indicateurs opérationnels et données
| Indicateur | Formule / principe | Champs requis | Statut source |
|---|---|---|---|
| Concentration des diffuseurs | courbe de Lorenz / Gini des partages par compte ; part des top 0,1 % | `author_id` par post, `retweeted_id` | Grinberg 2019, Baribi-Bartov 2024 ✔ |
| Engagement normalisé par audience | `retweets / followers_count` de l'auteur ; z-score par rapport à l'historique du compte | `public_metrics`, `author.followers_count` | pratique courante ; pas de source canonique identifiée **[non vérifié]** |
| Ratio likes/vues (X) | `like_count / impression_count` ; valeurs anormalement hautes ou basses signalent achat d'engagement ou amplification artificielle | `impression_count` (vues publiques X, disponibles depuis fin 2022 **[non vérifié]**), `like_count` | heuristique sans validation académique identifiée **[non vérifié]** |
| Part des retweets issus de comptes coordonnés | proportion de l'engagement d'un post provenant de communautés détectées en B1 | sortie B1 + `retweeted_id` | Cinelli 2022 ; Tardelli 2024 ✔ |
| Vitesse initiale | nombre de repartages dans les 5/10/60 premières minutes vs. courbe médiane | `created_at` des repartages | Zhao 2020 ; Schoch 2022 (fenêtre 1 min) ✔ |
| Audience atteinte (reach) | somme des followers uniques des repartageurs (borne haute) | listes de followers | Grinberg 2019 ✔ ; quasi inaccessible sur X depuis 2023 |

**Limites** : `impression_count` n'est pas exposé pour les posts d'autrui via l'API v2 gratuite/basic (uniquement vues publiques affichées) ; les followers ne sont plus récupérables à l'échelle ; les métriques sont instantanées (nécessité de **re-collecter** à t+1 h, t+24 h, t+7 j pour des courbes). L'exposition réelle n'est mesurable que par panels (Grinberg), extensions navigateur (Bouchaud) ou accès **DSA art. 40(4)** (logs d'exposition).

---

## C. Matrice de synthèse « méthode × données requises »

Légende : ● requis ; ○ utile/optionnel ; — non requis. « Followers » = graphe/listes d'abonnés ; « Profil » = métadonnées de compte (`created_at`, compteurs, bio, image) ; « Métriques » = `like/retweet/reply/quote/impression_count`.

| Méthode (source) | account_id + post_id | timestamp (s) | retweeted_id / quoted_id | in_reply_to / conversation_id | urls[] | hashtags[] | mentions[] | text | media (hash) | Profil | Followers | Métriques | Timeline complète du compte | Vérité terrain |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Co-retweet TF-IDF/cosinus (Pacheco 2021 ; Nizzoli 2021) | ● | ○ | ● | — | — | — | — | — | — | — | — | — | ○ (≥10 RT) | — |
| Séquences de hashtags (Pacheco 2021) | ● | ○ | — | — | — | ● | — | — | — | — | — | — | ● | — |
| Similarité d'images (Pacheco 2021) | ● | — | — | — | — | — | — | — | ● | ○ | — | — | — | — |
| Synchronisation temporelle (Pacheco 2021) | ● | ● | — | — | — | — | — | — | — | — | — | — | ● | — |
| CLSB / CooRnet (Giglietto 2020) | ● | ● | — | — | ● | — | — | — | — | ○ | — | ○ | — | — |
| CooRTweet (Righetti & Balluff 2025) — objet générique | ● | ● (10 s) | ○ | ○ | ○ | ○ | ○ | ○ | ○ | — | — | — | — | — |
| LCN/HCC (Weber & Neumann 2021) | ● | ● (10 s-15 min) | ● | ● | ● | ● | ● | — | — | — | — | — | — | — |
| Synchronized Action (Magelinski 2022) | ● | ● | — | — | ● | ● | ● | — | — | — | — | — | — | — |
| Fusion multi-indicateurs (Luceri 2024) | ● | ● | ● | — | ● | ● | — | ● | — | — | — | — | — | ● (Twitter IO) |
| Classif. séries de réseaux (Vargas 2020) | ● | ● (jour) | ● | — | ● | ● | ● | — | — | — | — | — | — | ● (Twitter IO) |
| Co-tweet/co-retweet 1 min ×10 (Schoch 2022 ; Keller 2020) | ● | ● | ● | — | — | — | — | ● | — | — | — | — | — | ● (archives IO / justice) |
| Coordination Network Toolkit (QUT) | ● | ● (60 s) | ● | ● | ● | — | — | ● | — | — | — | — | — | — |
| Réseau multiplexe temporel (Tardelli 2024) | ● | ● | ● | ○ | ○ | ○ | ○ | — | — | — | — | ○ | — | — |
| Botometer v4 (2020) | ● | ● | ● | ● | ● | ● | ● | ● | — | ● | ○ | — | ● (200 tweets) | ● (jeux annotés) |
| BotometerLite (2020) | ● | — | — | — | — | — | — | — | ○ | ● | — | — | — | ● |
| BotBuster (2023) | ● | ○ | — | — | — | — | — | ● | — | ● | — | — | ○ (36 posts) | ● |
| DNA numérique (Cresci 2016) | ● | ● | ● | ● | — | — | — | — | — | — | — | — | ● | — |
| Cascades / viralité structurelle (Goel 2016 ; Vosoughi 2018 ; Juul 2021) | ● | ● | ● | ○ | — | — | — | — | — | ○ | ● (TID) | ○ | — | ○ (fact-checks) |
| Détection précoce (Zhao 2020 ; Varol 2017) | ● | ● (5 h) | ● | — | — | — | — | ○ | — | ○ | ○ | ○ | — | ● |
| BERTopic / clustering multilingue | ● | ○ | — | — | ○ | — | — | ● | — | — | — | — | — | — |
| CARDS / Augmented CARDS | ● | ○ | — | — | ○ | — | — | ● | — | ○ | — | — | — | ● (corpus annoté) |
| Stance / claim matching LLM | ● | — | — | — | ○ | — | — | ● | ○ (OCR) | — | — | — | — | ● (fact-checks) |
| Politoscope / Climatoscope (ISC-PIF) | ● | ● | ● | — | — | ● | — | ● | — | ● | — | — | — | — |
| Superspreaders / supersharers (Grinberg 2019 ; DeVerna 2024 ; Baribi-Bartov 2024) | ● | ● | ● | — | ● (domaines) | — | — | — | — | ● | ● (exposition) | ○ | — | ● (listes de domaines) |
| Engagement normalisé / ratio vues (B6) | ● | ● (re-collecte) | ● | — | — | — | — | — | — | ● | — | ● | — | — |

### Lecture transversale
1. **Socle minimal universel** (couvre B1 presque entièrement) : `account_id`, `post_id`, `timestamp` à la seconde, `retweeted_id`, `urls[]`, `hashtags[]`, `mentions[]`, `in_reply_to_id`, `text`. Ce sont des champs **publics**, présents dans toute collecte par scraping ou API basique.
2. **Ce qui n'est plus réaliste sur X depuis 2023** : graphe de followers (cascades TID, exposition), timelines de 200 tweets par compte à l'échelle (Botometer), flux exhaustif (Politoscope). Les méthodes de coordination **n'en ont pas besoin**, d'où leur place centrale dans les travaux 2024-2026.
3. **Vérité terrain** : seules les archives Twitter *Information Operations* (jusqu'en 2022) et les décisions de justice (NIS Corée) fournissent une validation externe ; toute étude actuelle sur X doit prévoir une **annotation manuelle** (cadre A-B-C) et traiter les faux positifs (Luceri 2025 ; Gallwitz & Kreil 2022).
4. **Paramètres de fenêtre documentés** : 10 s (CooRTweet défaut), 60 s (QUT toolkit, Schoch 2022 co-retweet ×10), 10 s-15 min (Weber & Neumann), intervalle estimé sur la distribution des délais (CooRnet), 1 jour (Vargas), 5 h (Zhao, détection précoce).
5. **Pour un corpus francophone** : BERTopic multilingue et claim matching fonctionnent ; CARDS exige adaptation (anglais) ; les outils médialab (minet/twitwi/xan/graphology) fournissent la chaîne collecte → normalisation → graphe sans dépendre de l'API X ; le DSA art. 40 est la seule voie légale vers les données non publiques (exposition, modération).
