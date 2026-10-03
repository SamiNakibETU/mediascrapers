# Désinformation climatique en situation de crise : ce qu'il faut collecter pour détecter, et ce que mediascrapers permet aujourd'hui

**Rapport de cadrage pour l'étude Observatoire Défense & Climat / IRIS**
Version du 3 octobre 2026. Rédigé à partir de six revues documentaires (annexes 01 à 06, même dossier) et de la lecture intégrale de la note *Désinformation climatique et guerre informationnelle* (Jourde, Duffau, Guillaume, mai 2026).

> **Niveau de vérification des sources.** Le proxy réseau de l'environnement de rédaction bloquait presque tous les sites hors GitHub (sgdsn.gouv.fr, eeas.europa.eu, isdglobal.org, maldita.es, cnil.fr, arxiv.org, etc.). Chaque annexe indique donc, source par source, si le document a été **lu** (dépôts GitHub, page Microsoft, dépôt Nitter, tarifs X), seulement **retrouvé dans l'index d'un moteur de recherche** avec titre et extrait concordants, ou **non vérifié**. Dans ce rapport, les faits structurants (API X, Nitter, Zeeschuimer, twscrape, 4CAT, outils d'analyse) ont été vérifiés directement sur les dépôts. Les chiffres tirés de rapports PDF non ouverts sont à recontrôler avant toute citation dans une publication de l'Observatoire. La section 9 liste les vérifications restantes.

---

## 0. Résumé exécutif

1. **Le besoin est clairement identifié par la note de mai 2026 elle-même** : elle repose sur des bases secondaires déjà attribuées (EUvsDisinfo, NewsGuard, Media Matters, ECCO, New Climate Institute), ne mesure ni portée ni impact, et constate que les événements climatiques extrêmes sont sous-représentés parce qu'ils apparaissent « par pics » et exigent une « enquête de terrain ». L'étude à monter doit produire la **donnée primaire quantitative** qui manque, et la produire **pendant** la crise.
2. **La littérature converge sur un socle de données minimal** pour détecter la coordination et l'inauthenticité : identifiant de compte, identifiant de post, horodatage à la seconde, objet partagé (post reposté, URL, hashtag, mention, parent de réponse), texte, et hachage des médias. Le graphe d'abonnés **n'est pas requis** par les méthodes de coordination, ce qui est la bonne nouvelle de cette revue : ces méthodes sont les seules pleinement réalisables sur X en 2026 sans API.
3. **Les indicateurs utilisés en pratique** (VIGINUM, SEAE, Graphika, Check First, ISD, Antibot4Navalny, Recorded Future) se répartissent en six couches : compte, contenu, temporalité, réseau, média, infrastructure. Trois reviennent partout : persona inauthentique, co-publication synchrone du même objet, infrastructure partagée.
4. **Le paysage d'accès a changé en 2026** et condamne plusieurs hypothèses de la méthode de crise envisagée : l'API X est en paiement à l'usage sans offre gratuite ni piste académique ; Nitter a reçu une mise en demeure de X Corp le 24 août 2026 et son dépôt est archivé depuis le 11 septembre ; les outils à cookies (twscrape, twitter-cli derrière agent-reach) exposent les comptes et cassent à chaque rotation GraphQL. La capture navigateur par un humain (Zeeschuimer vers 4CAT) est aujourd'hui la voie la plus robuste et la plus défendable. Le DSA article 40(12) est la seule voie officielle gratuite, et la Commission a sanctionné X le 5 décembre 2025 précisément pour refus d'accès aux chercheurs.
5. **mediascrapers couvre environ un quart du besoin** : timelines récentes de comptes connus, compteurs d'engagement, structure RT/quote/reply, backfill historique, presse. Il manque la recherche par mots-clés, les fils de conversation, les profils (date de création, bio, abonnés), les snapshots d'engagement répétés, le hachage des médias, la provenance et l'archivage probant, et toute la couche d'analyse.
6. **Les commandes `climdef.crisis`, `discover`, `tweet-result` et `snowball` citées dans la méthode n'existent pas dans le dépôt.** Elles décrivent un plan, pas un outil. Le scénario Mayotte heure par heure doit être réécrit sur ce qui existe et sur ce qui est légalement tenable.
7. **Recommandation d'architecture** : activer **dès maintenant** une veille de fond légère et sans compte (watchlist syndication + presse + Telegram + Bluesky), et préparer un **mode crise** déclenché par la vigilance Météo-France, fondé sur Zeeschuimer avec des comptes institutionnels dédiés, twscrape seulement en appoint documenté, et une demande d'accès DSA 40(12) déposée en amont. La couche d'analyse (coordination, narratifs, superspreaders, archivage) se construit avec des briques existantes et vérifiées actives au 3 octobre 2026.

---

## 1. Point de départ : la note de mai 2026 et ses limites déclarées

La note (81 pages) adopte la matrice FIMI du SEAE (quatre catégories de canaux : officiels, contrôlés, liés, alignés) et recense 161 cas entre janvier 2021 et mars 2026, dont 120 d'origine russe et 41 d'origine américaine. Trois « objets » structurent les narratifs : politiques énergétiques et climatiques (89 % des cas russes, 71 % des cas américains), sciences climatiques, événements climatiques extrêmes (4 % et 2 %).

Les limites que la note énonce elle-même (p. 16 et 19) définissent le cahier des charges de l'étude suivante :

| Limite déclarée dans la note | Ce que l'étude doit apporter |
|---|---|
| « Ces collectes de données ne visent pas l'exhaustivité » ; sources secondaires déjà attribuées | Collecte primaire, prospective, avec critères d'inclusion explicites |
| « Elles ne quantifient pas la portée et l'impact des cas recensés » ; chaque cas compte pour un | Métriques d'engagement et de diffusion par contenu, courbes de viralité, identification des hubs |
| Événements extrêmes sous-représentés car « par pics », repérés par « enquêtes de terrain » | Dispositif déclenchable en quelques heures, fenêtre J-2 à J+30 |
| « Barrières linguistiques » à l'échelle locale | Lexique multilingue incluant shimaoré, comorien, créole, et collecte des diasporas |
| Attribution difficile | Documentation d'incident au format SEAE (incident, canaux, observables, techniques DISARM) |

Les deux études de cas de la note (DANA Valence 2024, ouragan Helene 2024) et le scénario 3 (inondations Pas-de-Calais 2042 : faux FR-Alert, faux médias locaux, deepfake de la ministre, bilan gonflé, trolls saturant les canaux officiels) décrivent exactement les narratifs que la grille de collecte doit couvrir (section 4).

---

## 2. Ce que les détecteurs utilisent réellement : synthèse des rapports d'État et des enquêtes

### 2.1 Cadres de référence

- **VIGINUM** qualifie une ingérence numérique étrangère par quatre critères cumulatifs : atteinte aux intérêts fondamentaux, contenu manifestement trompeur, diffusion **artificielle ou automatisée**, implication d'un acteur étranger. Les rapports techniques (RRN 2023, Portal Kombat 2024, Matriochka 2024, JOP 2024, BIG 2024, Roumanie 2025, Storm-1516 2025, Rokh Solis 2026) documentent successivement contenu, inauthenticité et attribution. Aucun rapport VIGINUM dédié au climat ou à une catastrophe naturelle n'a été trouvé. La note de mai 2026 confirme que VIGINUM « n'intègre pas les changements climatiques dans son cadre d'analyse ».
- **SEAE** : unité d'analyse = l'*incident*, décomposé en *canaux* et *observables* ; 3e rapport (mars 2025) : 38 000 canaux, 25 plateformes, 68 000 observables ; 4e rapport (mars 2026) : 540 incidents, 10 500 canaux, 90 pays. Codage des techniques en **DISARM**, stockage en **STIX 2.1** (OpenCTI). Ces deux cadres sont vérifiés sur les dépôts GitHub de la DISARM Foundation.
- **Cadre ABCDE** (Actor, Behaviour, Content, Degree, Effect) : non vérifié dans cette session, mais c'est la grille implicite de tous les rapports lus.

### 2.2 Indicateurs mobilisés dans les rapports (par rapport source)

| Indicateur | Données nécessaires | Qui l'utilise |
|---|---|---|
| Date de création du compte, créations en rafale | `account.created_at` | VIGINUM (Roumanie), ISD, Check First, SIO, CAAD Robo-COP29 |
| Motif de handle (prénom + 4 à 6 chiffres), incohérence langue/bio | `screen_name`, `bio`, `lang` | Antibot4Navalny, Graphika |
| Photo de profil générée ou volée | image de profil, hachage | Meta, OpenAI, Graphika, SIO |
| Texte identique ou quasi identique entre comptes | corpus texte | Graphika, Auswärtiges Amt, Check First, CAAD (464 comptes, 5 632 publications identiques en deux semaines) |
| Co-publication du même objet dans une fenêtre courte | horodatages, URL/vidéo partagée | Graphika, AA, Check First, Schoch et al. |
| Cadence non humaine ou calibrée, heures d'activité sur un fuseau étranger | horodatages | AA, Antibot4Navalny, SIO |
| Rôles seeders/quoters ou posters/followers | graphe de citations, réponses, reposts | VIGINUM (Matriochka), AA, Antibot4Navalny |
| Ratio impressions/engagement anormal, absence de traction hors du cluster | `views`, `likes`, `retweets` | Microsoft MTAC, Graphika, ISD, OpenAI (Breakout Scale) |
| Réutilisation de la même image/vidéo, artefacts IA, voix clonées, logos volés, QR codes | fichiers média, pHash/PDQ | MTAC (Maui), ISD, Check First, Graphika |
| Domaines : date d'enregistrement groupée, même IP, même CMS, TLD rares, redirecteurs | WHOIS/RDAP, DNS, empreinte web | VIGINUM (Portal Kombat, Rokh Solis), EU DisinfoLab, Recorded Future, MTAC |
| Cross-posting multi-plateformes, continuité des personas | identifiants et médias multi-plateformes | VIGINUM, Graphika, Check First |

**Enseignement transversal** : depuis 2023, l'IA générative banalise textes et personas ; les indicateurs les plus robustes deviennent comportementaux (synchronie, rôles) et infrastructurels (IP, registrar, CMS). Les plateformes publient des bilans sans signaux techniques ; ce sont les enquêteurs externes qui documentent les indicateurs observables.

### 2.3 Méthodes académiques et champs minimaux

Toutes les méthodes de détection de coordination (Pacheco et al. 2021, Nizzoli et al. 2021, Giglietto et al. 2020, CooRTweet 2025, Weber et Neumann 2021, Magelinski et al. 2022, Luceri et al. 2024, Schoch et al. 2022, Tardelli et al. 2024) suivent le même squelette : graphe biparti comptes/objets, projection sur les comptes, filtrage, détection de communautés. Le discriminant est la **fenêtre temporelle** : 10 s (CooRTweet par défaut), 60 s (QUT coordination-network-toolkit ; Schoch et al. : co-retweet en moins d'une minute, répété au moins 10 fois, retrouve 74 % des comptes des campagnes de l'archive Twitter Information Operations), 10 s à 15 min (Weber et Neumann).

| Famille | Champs minimaux | Réalisable sur X sans API en 2026 |
|---|---|---|
| Coordination (co-retweet, co-URL, co-hashtag, co-reply, co-texte) | `account_id`, `post_id`, `timestamp` (s), `retweeted_id`/`quoted_id`, `urls[]`, `hashtags[]`, `mentions[]`, `in_reply_to_id`, `text` | **Oui** |
| Similarité d'images | `media_url` + hachage perceptuel | Oui |
| Détection de bots (Botometer, BotBuster) | profil complet + 36 à 200 derniers posts par compte | Non à l'échelle ; Botometer-X figé avant mai 2023 ; critiques fortes (Rauchfleisch et Kaiser 2020, Gallwitz et Kreil 2022). Préférer les indicateurs de groupe |
| Cascades et viralité structurelle (Vosoughi et al. 2018, Goel et al. 2016) | arbre de repartage = graphe d'abonnés + horodatages | **Non** : X attribue tout retweet à la racine ; les réponses et citations exposent leur parent, donc arbres de conversation reconstructibles |
| Narratifs (BERTopic multilingue, CARDS, claim matching) | `text`, `lang`, `created_at`, `author_id` | Oui ; CARDS est anglophone, pas de version française validée identifiée |
| Superspreaders (Grinberg et al. 2019, DeVerna et al. 2024) | `author_id` par post, `retweeted_id`, profil | Oui pour la concentration ; non pour l'exposition réelle (panel ou DSA 40(4)) |

En France, le Climatoscope du CNRS (Chavalarias, Bouchaud, Chomel, Panahi, février 2023, HAL hal-03986798) reste la référence : graphe de retweets, communautés, scores d'inauthenticité ; environ 30 % des comptes traitant du climat nient l'origine humaine, communauté dénialiste avec davantage de comportements inauthentiques. Le Politoscope n'a plus d'accès API équivalent depuis 2023. Les outils du médialab (minet, twitwi, xan, ipysigma, graphology) ont pivoté vers Bluesky, Telegram, YouTube, TikTok.

---

## 3. Ce qu'il faut observer spécifiquement en crise climatique (annexe 04)

### 3.1 Enseignements des cas documentés

| Cas | Narratifs dominants | Ce que les analystes ont mesuré |
|---|---|---|
| Helene et Milton (États-Unis, 2024) | HAARP, « ils contrôlent le temps », FEMA détourne l'aide vers migrants ou Ukraine, lithium, menaces contre météorologues ; évacuation d'équipes FEMA sur rumeur de milice | Logically : 76 000 posts, 5 % des comptes = 40 % des posts trompeurs, X 52 %, TikTok 27 % ; CCDH : 221 M de vues, Meta sans fact-check sur 98 % des posts ; DiMattina et al. 2026 : 586 189 messages de 116 canaux Telegram, part substantielle de coordination |
| DANA Valence (Espagne, 2024) | corps cachés au parking Bonaire, barrages démolis, HAARP, « l'UME ne se déploie pas », faux numéro 112, faux SMS AEMET, dons jetés | Maldita : 133 bulos ; 185 fact-checks en deux semaines ; comptes « mutants » changeant d'identité ; TikTok 4,4 M de vues sur une vidéo ; Community Notes inopérantes |
| Lahaina (Maui, 2023) | « arme météo » américaine | Microsoft : Spamouflage, images IA, 31 langues, 85 comptes et blogs au contenu identique |
| Feux du Canada (2023) | armes à énergie dirigée, incendies d'État | CAAD/McGill « Flame Wars » : cartographie de réseau X |
| Feux de Grèce (2023) | migrants incendiaires | milices citoyennes séquestrant des demandeurs d'asile |
| Feux de Los Angeles (2025) | DEI, Ukraine, deepfake Grok relayé par Sputnik, Lavrov | GMF Hamilton 2.0 ; Alex Jones 408 M de vues sur X |
| Texas (2025) | ensemencement Rainmaker | menaces de mort contre le PDG |
| Mayotte, cyclone Chido (déc. 2024) | « 60 000 morts », « charniers », abandon, rapatriements discriminatoires, migrants comoriens | **aucune étude de désinformation dédiée identifiée** malgré 1 100 à 1 200 militaires déployés |
| Pas-de-Calais (2023-24), tempête Alex (2020) | wateringues, rumeur de brèche au barrage du Boréon | aucune étude dédiée |

Trois constats opérationnels : le narratif apparaît **dans les heures** suivant l'événement, donc la collecte doit démarrer avant (vigilance orange/rouge) ; la diffusion est **concentrée** sur quelques hubs monétisés ou vérifiés ; la grammaire est **répétitive** (bilan caché, infrastructure sabotée, catastrophe provoquée, secours incompétents ou malveillants, bouc émissaire, aide détournée), ce qui autorise un codage pré-établi. Le volet FIMI est souvent secondaire en volume mais stratégique en ciblage (défiance envers l'État, OTAN, Ukraine).

**Mayotte-Chido est le pilote outre-mer naturel** : tous les ingrédients étaient réunis et personne ne l'a étudié.

### 3.2 Grille narrative pour le codage (à transformer en lexique de requêtes)

- Bilan : chiffres cachés, morts non comptés, charniers, parking, morgue pleine.
- Causalité : HAARP, chemtrails, ensemencement, géo-ingénierie, arme climatique, laser, barrage ouvert ou lâché, wateringues sabotées, canicule fabriquée, Météo-France ment.
- Politique climatique : dictature climatique, pass climat, Great Reset, ZFE, arnaque verte, éoliennes responsables.
- Anti-État et anti-secours : abandon, État failli, l'armée ne fait rien ou fait de la figuration, militaires pour mater la population, réquisition, rapatriement des métropolitains.
- Boucs émissaires : migrants, ONG, écologistes, OTAN ou Ukraine, Maroc ou Algérie.
- Aide : dons jetés, aide détournée, préférence aux étrangers.

Le lexique doit exister en français, anglais, russe, et dans les langues locales du territoire concerné.

---

## 4. Schéma de données cible

C'est le livrable central de cette revue : la liste des champs qu'une collecte doit produire pour que les analyses de la section 2 soient possibles. Les champs marqués ★ sont ceux sans lesquels la détection de coordination est impossible.

**Post** (toutes plateformes, colonne `platform`)
★ `post_id`, ★ `author_id`, ★ `created_at` (seconde, UTC), ★ `text` intégral, `lang`, ★ `retweeted_post_id`, ★ `quoted_post_id`, ★ `in_reply_to_post_id`, `conversation_id`, ★ `urls[]` (résolues, domaine extrait), ★ `hashtags[]`, ★ `mentions[]`, `media[]` (URL, type, hachage pHash et PDQ, fichier archivé), `metrics{likes, reposts, replies, quotes, views}` **horodatés** (plusieurs snapshots : t0, +1 h, +6 h, +24 h, +7 j), `raw` JSON intégral, `source_tool`, `captured_at`, `captured_by`, `query_or_list` (provenance).

**Compte**
`account_id`, `handle`, `display_name`, **`created_at`**, `bio`, `location`, `profile_image` (hachage), `followers_count`, `following_count`, `statuses_count`, `verified_type` (payant, organisation), série temporelle des compteurs (une ligne par capture), `first_seen_in_corpus`, `grade` (A validé, B probable, C candidat), `role` (seeder, amplificateur, relais authentique), langue dominante observée, heures d'activité observées.

**Arêtes** : `(source, cible, type ∈ {repost, quote, reply, mention}, post_id, timestamp)`.

**Média** : hachage, premier et dernier compte à l'avoir publié, nombre de comptes distincts, verdict IA ou montage (manuel), fichier archivé.

**Domaine** (pour les URL partagées) : domaine, date d'enregistrement, registrar, IP, CMS, premier post citant, nombre de comptes citant.

**Incident** (format SEAE) : début, fin, territoire, narratif(s) codés selon la grille 3.2, acteur présumé, plateformes, liste de canaux, liste d'observables, techniques DISARM, impact estimé, niveau de confiance, TLP.

**Preuve** : SHA-256 du brut, horodatage RFC 3161 ou OpenTimestamps, capture WACZ ou SingleFile, journal (qui, quand, outil, version, compte).

---

## 5. État de l'accès aux données en octobre 2026 (faits vérifiés)

| Voie | État vérifié | Conséquence |
|---|---|---|
| API X officielle | Paiement à l'usage par défaut depuis le 6 février 2026 (environ 0,005 $ par post lu), Basic migré d'office après le 1er juin, Pro après le 1er septembre, pas de piste académique (sources : annonce X Developers « Legacy Basic plans moving to PPU », blogs techniques) | Hors budget. 1 M de posts lus ≈ 5 000 $ |
| DSA article 40(12) | Règlement délégué 2025/2050 en vigueur depuis le 29 octobre 2025 ; décision de la Commission contre X le 5 décembre 2025 (120 M€) citant le refus d'accès des chercheurs aux données publiques et l'interdiction contractuelle du scraping ; décision du tribunal de Berlin du 17 février 2026 ordonnant à X d'ouvrir son API à Democracy Reporting International (sources secondaires, non lues) | **Déposer une demande maintenant**, au nom de l'IRIS, pour X, Meta, TikTok. Même refusée, elle fonde la position juridique |
| Nitter | Mise en demeure X Corp 24 août 2026 ; dépôt archivé 11 septembre 2026 ; README « the project will continue » (lu sur GitHub) ; auto-hébergement exige des sessions de vrais comptes | **Ne pas en faire un socle.** Répond à la question « pourquoi pas self-host un Nitter » |
| Zeeschuimer + 4CAT | Commits du 9 septembre et du 1er octobre 2026 ; capture `SearchTimeline`, `TweetDetail` (fils), `UserTweets`, `UserReplies`, listes, Explore ; champs auteur, bio, followers, métriques, médias, entités | **Voie principale pour la recherche par mots-clés et les conversations.** Volume : quelques milliers de posts par heure humaine |
| twscrape | Commit du 22 septembre 2026, v0.20.1 après casse GraphQL de mai 2026 ; recherche, réponses, fils, retweeters, followers, timelines plafonnées à 3 200 ; cookies de vrais comptes ; détection de challenge Cloudflare dans les derniers commits | Appoint pour automatiser des requêtes définies, avec comptes dédiés, risque de suspension assumé et documenté |
| agent-reach / twitter-cli | Commit du 15 septembre 2026 ; cookies de navigateur, GraphQL interne, empreinte TLS via curl_cffi, conseil d'utiliser un proxy | **Même couche de risque que twscrape**, sans valeur ajoutée pour la recherche. Confirme votre analyse |
| Syndication `timeline-profile` (mediascrapers) | En production dans ED Mediawatch depuis août 2026 (README du dépôt) ; `robots.txt` en Disallow ; une issue tierce signale un arrêt de `tweet-result` depuis avril 2026 | Fonctionne mais fragile et non supporté. Prévoir un mode dégradé et sonder depuis le VPS (section 8) |
| fxtwitter / vxtwitter | Actifs (commit 1er octobre 2026), sans clé, usage unitaire | Hydratation d'URL citées, jamais en masse |
| Bluesky Jetstream | Flux complet public sans clé | Seule plateforme où followers, réponses et reposts sont exhaustifs |
| Telegram (Telethon, telegram-tracker, tg-archive, minet) | Actifs ; Telethon a quitté GitHub le 21 février 2026 | Source primaire des campagnes (Matriochka, Storm-1516 partent de Telegram) |
| TikTok Research API | Gratuite, 1 000 requêtes/jour, éligibilité institutionnelle | À demander ; TikTok pèse 27 % des posts trompeurs en crise |
| Meta Content Library | Candidature via Research Tools Manager depuis décembre 2025 | À demander |

**Cadre juridique à retenir** (annexe 05, section C) : RGPD base « intérêt légitime » ou « mission d'intérêt public » avec article 89 ; recommandations CNIL de juin 2024 sur la réutilisation de données publiées et fiches de juin 2025 sur le moissonnage (pseudonymiser à la collecte, durée de conservation, information publique, respecter l'opposition de l'éditeur) ; article 323-3 du Code pénal en cas de contournement de protections techniques, ce qui plaide **contre** proxys tournants, empreintes simulées et imitation de comportement ; CGU de X acceptées par tout compte connecté, donc risque contractuel sur le compte utilisé. Conséquences pratiques : jamais de compte personnel pour une collecte automatisée ; comptes institutionnels dédiés et documentés ; comité d'éthique et AIPD ; corpus bruts non redistribués.

---

## 6. Diagnostic de mediascrapers par rapport au besoin

| Besoin (section 4) | État dans le dépôt | Écart |
|---|---|---|
| Timeline récente d'un compte connu, texte, date, type, compteurs | `SyndicationClient` : 20 à 100 derniers tweets, `Post` avec likes, RT, réponses, citations, vues | Couvert. Pas de pagination : un compte très actif en crise dépasse 100 posts par jour |
| Historique d'un compte | `Backfill` Wayback CDX + fxtwitter | Couvert, couverture inégale |
| Presse (RSS, texte intégral, paywall) | `mediascrapers.press` | Couvert |
| Recherche par mots-clés et hashtags | absent | **Écart majeur**. Zeeschuimer (humain) ou twscrape (comptes dédiés) |
| Fils de conversation, réponses, citations d'un post | absent (`reply_to_url` et `quoted_url` sont capturés, pas suivis) | **Écart majeur**. `TweetDetail` via Zeeschuimer ; `tweet_replies` via twscrape |
| Profil : date de création, bio, image, abonnés, série temporelle | `Profile` : `followers`, `statuses`, `protected` seulement | Écart. Ajouter `created_at`, `bio`, `location`, image hachée, `verified_type`, et historiser |
| Snapshots d'engagement répétés | une valeur par collecte, pas de clé temporelle | Écart. Stocker chaque capture avec `captured_at` |
| Hachage des médias et archivage | `media_url` seulement | Écart. imagehash/PDQ, téléchargement immédiat (les URL expirent) |
| Provenance et preuve | `collected_via` | Écart. SHA-256, horodatage, journal de collecte |
| Multi-plateforme | X et presse | Écart. Telegram, Bluesky, TikTok |
| Couche d'analyse (coordination, communautés, narratifs, superspreaders) | absente par conception (« storage is the caller's business ») | Écart, à construire avec des briques existantes |
| Stockage | aucun (dataclasses) | Écart. Postgres JSONB + Parquet |

La bibliothèque est propre, testée et bien délimitée ; son rôle naturel est **le collecteur de watchlist sans compte**. Il ne faut pas lui demander d'être le moteur de recherche de crise.

---

## 7. Avis sur la méthodologie de crise proposée

Le découpage de principe est juste : **mots-clés** pour découvrir, **comptes** pour suivre. Les corrections portent sur les outils et sur le cadre.

**Ce qui tient**
- Un VPS qui ne fait que du sans-compte (syndication, presse, Telegram, Bluesky, archives) : aucun compte à bannir, exposition nulle, c'est la base de fond à activer dès maintenant.
- Refus du VPN de dissimulation, des agents « imitant le comportement humain » et des empreintes simulées : la revue juridique le confirme (article 323-3 CP, CNIL sur le contournement des oppositions), et la revue technique montre que c'est précisément ce que la détection de X cible le mieux (commits twscrape de septembre 2026 sur les challenges Cloudflare).
- Zeeschuimer comme « comportement humain » : c'est aujourd'hui l'outil de référence de l'équipe DMI d'Amsterdam et la voie la plus défendable, parce qu'il n'automatise rien.
- Bursts rares et courts avec des comptes dédiés : cohérent avec ce que font les équipes qui utilisent encore twscrape.

**Ce qui ne tient pas**
- **Les commandes citées n'existent pas.** `climdef.crisis`, `discover`, `tweet-result`, `snowball`, `search_local.py` sont à écrire. Le rapport « 30 minutes après » n'existe pas non plus.
- **« Sans aucun compte, 15 requêtes sur les moteurs de recherche donnent les ids de tweets indexés »** : les moteurs généralistes indexent peu et tard les posts X, surtout les premières heures d'une crise ; aucune équipe recensée ne s'appuie sur cette voie. Elle vaut pour retrouver des posts cités par la presse, pas pour découvrir.
- **`tweet-result` (syndication unitaire)** : signalé en arrêt depuis avril 2026 par au moins un projet tiers ; à sonder depuis le VPS avant de bâtir dessus. fxtwitter est l'alternative unitaire.
- **Utiliser le compte personnel du chercheur** pour Zeeschuimer est acceptable pour une navigation humaine, mais **pas « tes deux comptes » pour des requêtes automatisées twscrape** : il faut des comptes institutionnels dédiés, créés avec l'identité de l'institut, inscrits au registre de traitement, et dont la suspension est un coût accepté.
- **Nitter self-hébergé** : à écarter comme socle (mise en demeure, dépôt archivé, sessions de vrais comptes requises).
- **Le scénario « 100 à 300 comptes syndication chaque nuit = 2 000 à 5 000 tweets/jour »** est réaliste en volume (une passe de 110 comptes prend six minutes d'après le README), mais la syndication ne renvoie que 20 à 100 posts par compte : en crise, un hub qui publie 300 fois par jour sera tronqué. Il faut passer plusieurs fois par jour sur les comptes de grade A.
- **La mesure de la viralité** réclame des snapshots d'engagement horodatés ; aucun composant actuel ne les stocke.

**Ce qui manque et que personne ne remplace**
- La demande d'accès **DSA 40(12)** à X, Meta, TikTok : c'est la seule voie officielle et gratuite, et c'est le seul argument juridique opposable si X conteste une collecte. Elle prend des mois ; elle doit partir avant la première crise.
- La **cellule de validation humaine** (grade C vers B vers A) et le **journal de crise** : prévus dans la méthode, ils sont la partie la plus coûteuse en temps et la seule qui produise de la vérité terrain (toutes les méthodes de coordination sont non supervisées).

---

## 8. Architecture recommandée et plan de travail

### 8.1 Deux régimes

**Régime de fond (dès maintenant, sans compte, VPS)**
- Watchlist initiale fournie par l'équipe Climdef, enrichie des acteurs recensés dans la note (canaux de la matrice FIMI, influenceurs, médias d'opinion identifiés par l'Observatoire des médias sur l'écologie, écosystèmes pro-russes francophones déjà suivis par VIGINUM, comptes locaux ultramarins et diasporas).
- mediascrapers `x timeline` deux fois par jour sur la watchlist, `press collect` sur press_fr, canaux Telegram via telegram-tracker ou minet, flux Bluesky filtré par lexique, archivage quotidien.
- Stockage Postgres (JSONB brut + colonnes normalisées, schéma de la section 4), exports Parquet.
- Baseline de deux à trois mois : volumes, hubs, lexique vivant. Sans baseline, aucune anomalie n'est mesurable en crise.

**Régime de crise (déclenché par vigilance Météo-France orange ou rouge, ORSEC, activation de moyens militaires)**
- H+0 à H+2 : fiche d'événement (type, lieu, fenêtre, lexique multilingue), ouverture du journal de crise, passage de la watchlist à quatre passes par jour.
- H+2 à H+6 : deux à trois chercheurs sur Zeeschuimer, sessions de 30 min, recherches « Latest » par bloc de lexique, déroulé systématique des fils des posts les plus engagés, export ndjson vers 4CAT ou vers la base.
- H+6 : décision du référent sur l'usage de twscrape (comptes dédiés, 10 requêtes espacées de 8 s par bloc de lexique, journalisées).
- H+6 à J+2 : snowball manuel à partir des interacteurs (citeurs, répondeurs, mentionneurs), grade C vers B, entrée en watchlist, snapshots d'engagement t0, +1 h, +6 h, +24 h, +7 j sur les posts viraux.
- J+2 à J+30 : rythme quotidien ; fin de crise : backfill Wayback et fxtwitter des comptes découverts, pipeline d'analyse, note pour l'Observatoire.

### 8.2 Chaîne d'analyse (briques vérifiées actives au 3 octobre 2026)

```
COLLECTE                        STOCKAGE                ANALYSE                          PREUVE / ANNOTATION
mediascrapers (watchlist, presse)  Postgres + JSONB     coordination-network-toolkit     browsertrix-crawler (WACZ)
Zeeschuimer -> 4CAT / ndjson       + pgvector           ou CooRTweet (co-RT, co-URL,     auto-archiver (SHA-256, RFC 3161,
twscrape (appoint, comptes dédiés) Parquet / DuckDB     co-reply, co-texte, 60 s)        PDQ, Wayback)
telegram-tracker, minet bsky       Meilisearch          igraph + Leiden, Gephi Lite      Label Studio (grille 3.2 + DISARM)
                                                        BERTopic + e5/bge-m3, CARDS      schéma incident SEAE en base
                                                        imagehash + PDQ, faster-whisper  Metabase (tableaux de bord)
```

OpenCTI et son connecteur DISARM ne se justifient que si des incidents sont partagés en STIX avec des tiers (VIGINUM, SEAE) ; sinon un schéma « incident » en base suffit et évite 16 Go de RAM.

### 8.3 Ordre de travail proposé

1. **Semaine 1** : sonder depuis le VPS les endpoints syndication (`timeline-profile`, `tweet-result`), oEmbed et fxtwitter ; déposer les demandes DSA 40(12) (X, Meta) et TikTok Research API ; créer deux comptes X institutionnels ; rédiger la politique de collecte (finalité, durée, pseudonymisation, information publique) et saisir le comité d'éthique.
2. **Semaines 2 à 3** : étendre mediascrapers (profil complet, snapshots horodatés, hachage des médias, provenance), écrire le mapper d'unification Zeeschuimer/twscrape/Telegram/Bluesky vers le schéma de la section 4, monter Postgres et le premier tableau de bord.
3. **Semaines 3 à 5** : baseline de fond sur la watchlist Climdef ; brancher coordination-network-toolkit, BERTopic, superspreaders ; premier rapport de baseline.
4. **Semaine 6** : **dry-run** sur un événement passé ou sur la prochaine vigilance orange : chronométrer H+0 à H+6, mesurer ce que Zeeschuimer rapporte en 30 min, tester le snowball et la validation ; rédiger la fiche réflexe.
5. **Étude rétrospective Mayotte-Chido** (Wayback, fxtwitter, Telegram, TikTok, presse locale) comme pilote outre-mer et démonstrateur pour l'Observatoire.

---

## 9. Limites de cette revue et vérifications restantes

- Aucun PDF de VIGINUM, du SEAE, de l'ISD, de CAAD, de Maldita ni de la CNIL n'a pu être ouvert ; leurs contenus proviennent d'extraits indexés et de sources secondaires. Les chiffres de la section 3 sont à recontrôler à la source.
- Non vérifiés : premier et deuxième rapports SEAE, FIMI Toolbox, cadre ABCDE, rapports GEC, FCDO/RUSI, BfV, Doublethink Lab ; détails du règlement délégué 2025/2050 et de la page « DSA Vetted Researchers » de X ; issues 2026 des contentieux X contre CCDH, Media Matters et Bright Data ; statut actuel de Junkipedia, Communalytic, SMAT, Meta Content Library ; modèles CARDS 2 et classifieurs climat sur Hugging Face ; nouvelle forge de Telethon.
- Pas trouvés : rapport VIGINUM sur Chido, Moldavie ou pays baltes ; étude de désinformation dédiée à Chido, au Pas-de-Calais ou à la tempête Alex ; référence « Mazières et al. ».
- Les affirmations sur les endpoints X non documentés (syndication, oEmbed) n'ont pas pu être testées en direct depuis cet environnement.

Les six annexes détaillent, source par source, le statut de vérification, les URL et les passages cités.

---

## Annexes (même dossier)

- `annexes/01_etats_viginum_eeas.md` : rapports VIGINUM, SEAE, DISARM, autres États ; champs à collecter en six couches.
- `annexes/02_industrie_ong_methodes.md` : Meta, Microsoft, OpenAI, Google, TikTok, Graphika, EU DisinfoLab, Check First, ISD, Alliance4Europe, Clemson, Recorded Future, Antibot4Navalny, SIO, DFRLab, Maldita ; catalogue d'indicateurs.
- `annexes/03_academique_methodes.md` : coordination, bots, cascades, narratifs, écosystème français ; matrice méthode × données.
- `annexes/04_desinfo_climat_cas.md` : observatoires climat, typologie de 17 narratifs, douze fiches de cas, grille de collecte en crise.
- `annexes/05_acces_donnees_outils_2026.md` : outils d'accès, programmes officiels, cadre juridique et éthique, stack à coût nul.
- `annexes/06_briques_open_source.md` : briques open source vérifiées, architecture de référence, lacunes de X et contournements.
