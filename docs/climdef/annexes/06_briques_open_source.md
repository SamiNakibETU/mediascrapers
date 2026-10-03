# 06 — Briques open source pour un pipeline de veille / analyse de désinformation (collecte → stockage → analyse → archivage → annotation)

Date de revue : 2026-10-03. Méthode : chaque dépôt GitHub a été ouvert (page `/commits`) pour relever la date du dernier commit réellement affichée. Les sites hors GitHub (junkipedia.org, communalytic.org, smat-app.com, pullpush.io, botometer.osome.iu.edu, huggingface.co, iscpif.fr, etc.) étaient inaccessibles depuis cet environnement (proxy) : les éléments correspondants sont marqués **[non vérifié]** et reposent sur des connaissances antérieures ou sur des résultats de recherche web secondaires. Budget de recherche web épuisé après 3 requêtes utiles (Nitter, Botometer, tarification API X) ; tout le reste est issu de fetchs GitHub directs.

Légende « pertinence X 2026 » : ●●● = voie réaliste de collecte X sans API payante ; ●●○ = utile en aval ou partiellement ; ●○○ = sans rapport avec X / X cassé ; ✖ = mort pour X.

---

## A. Tableau de synthèse

| Brique | Rôle | État vérifié (2026-10-03) | Licence | Pertinence X 2026 | URL |
|---|---|---|---|---|---|
| **4CAT** (DMI) | Plateforme web capture + analyse (processeurs réseaux, co-mots, etc.) | Dernier commit **2026-10-01** ; dernière *release* taguée v1.57 (2024-09-10), développement continu sur master ; 416★ ; Postgres | MPL-2.0 | ●●● (import X via Zeeschuimer, datasource `twitter-import` + `twitterv2`) | github.com/digitalmethodsinitiative/4cat |
| **Zeeschuimer** | Extension Firefox qui capture le trafic JSON pendant la navigation (X, TikTok, Instagram, Threads, Truth, Gab, Pinterest, 9gag, Imgur, Douyin, RedNote) → ndjson/CSV/4CAT | Dernier commit **2026-09-09** (ajout eslint & CI) | MPL-2.0 | ●●● (collecte X « navigateur-assistée », légale côté chercheur, sans compte-bot) | github.com/digitalmethodsinitiative/zeeschuimer |
| **twscrape** | Lib/CLI Python asynchrone, API GraphQL non officielle de X, rotation multi-comptes | Dernier commit **2026-09-22** ; release v0.20.1 (2026-08-25) ; 2,8k★ ; commits récents : détection « CF challenge shell », auto-réparation des features GQL manquantes | MIT | ●●● (mais comptes X requis, ToS violées, bannissements) | github.com/vladkens/twscrape |
| **Nitter** | Front-end alternatif X, utilisable comme proxy RSS/HTML | Dépôt **archivé le 2026-09-11** après mise en demeure X Corp (2026-08-24) ; README du 2026-09-07 : « Following legal advice, the Nitter project will continue » ; 14,5k★ ; nécessite `sessions.jsonl` (sessions de vrais comptes) | AGPL-3.0 | ●●○ (fragile juridiquement et techniquement) | github.com/zedeus/nitter |
| **minet** (médialab) | CLI/lib de web-mining multi-plateforme (X, Bluesky, YouTube, Telegram, Instagram, TikTok, Reddit, Mediacloud…) | Dernier commit **2026-09-08** ; v4.1.0 (2025-12-02) ; 3 188 commits | GPL-3.0 | ●●○ (sous-commandes `twitter` dépendent de l'API v2 payante ou d'un `scrape` fragile ; très bon pour Bluesky/YouTube/Telegram) | github.com/medialab/minet |
| **gazouilloire** | Collecte longue durée X (search + stream) → Elasticsearch | Dernier commit **2026-04-10** (README) ; dernier code 2023-07 ; dépend de clés API Twitter v1.1/v2 | GPL-3.0 | ✖ (API payante) ; modèle de données ES réutilisable | github.com/medialab/gazouilloire |
| **DMI-TCAT** | Capture/analyse Twitter historique | **Archivé 2025-01-09** | Apache-2.0 | ✖ | github.com/digitalmethodsinitiative/dmi-tcat |
| **Facepager** | GUI de collecte API/scraping générique (YouTube, etc.) → SQLite | Dernier commit **2026-05-17** | MIT | ●○○ | github.com/strohne/Facepager |
| **Hoaxy** (OSoMe) | Diffusion de claims/fact-checks sur Twitter | Backend **archivé 2022-11-10** (« no longer maintained ») | [non vérifié : fichier LICENSE présent] | ✖ | github.com/IUNetSci/hoaxy-backend |
| **Botometer / Botometer-X** | Score de « botness » | botometer-python : dernier commit 2024-06-26. Botometer-X en **mode archive** : scores précalculés sur données < 2023-05-31 ; endpoints v4/Lite coupés le **2026-11-02** (source : résultats web, [non vérifié directement]) | MIT (client) | ✖ pour comptes récents | github.com/IUNetSci/botometer-python |
| **BotAmp** (OSoMe) | Mesure d'amplification par bots | URL github.com/osome-iu/BotAmp → **404** ; **[non vérifié]** | — | ✖ | — |
| **twint** | Scraper Twitter sans API | **Archivé 2023-03-30** ; forks non maintenus | MIT | ✖ | github.com/twintproject/twint |
| **Redlib** | Front-end Reddit (type Nitter) | Dernier commit **2026-04-24** | AGPL-3.0 [non vérifié licence] | ●○○ (Reddit) | github.com/redlib-org/redlib |
| **Telethon** | Client MTProto Python (base de tous les collecteurs Telegram) | Dernier commit **2026-02-21** (« Migrate off GitHub » : dév. déplacé hors GitHub, branche v1) | MIT [non vérifié] | ●○○ (Telegram) | github.com/LonamiWebs/Telethon |
| **telegram-tracker** | Collecte canaux Telegram (messages, forwards, réseau GEXF) | Dernier commit **2026-04-20** (README) ; code 2024-08 | Apache-2.0 | ●○○ (Telegram) | github.com/estebanpdl/telegram-tracker |
| **tg-archive** | Archive statique de groupes/canaux Telegram → SQLite + HTML | Dernier commit **2026-03-01** ; mainteneur « plus actif, PR relues » | MIT | ●○○ | github.com/knadh/tg-archive |
| **TeleScrape** | Scraper Telegram | **[non vérifié]** (non fetché) | — | — | — |
| **pyktok** | Scraper TikTok (JSON embarqué, cookies navigateur) | Dernier commit **2025-10-04** ; v0.0.31 (2025-02) ; casse fréquente | BSD-3 | ●○○ (TikTok) | github.com/dfreelon/pyktok |
| **TikTok Research API wrapper** (officiel) | Wrapper R/Python de l'API Recherche TikTok | 8 commits ; accès réservé aux chercheurs éligibles (UE/US) | MIT | ●○○ | github.com/tiktok/tiktok-research-api-wrapper |
| **4CAT datasources TikTok/Bluesky/Telegram** | Collecte native dans 4CAT | dossiers `bsky`, `telegram`, `tiktok`, `tiktok_comments`, `tiktok_urls` présents (2026-10) | MPL-2.0 | — | (voir 4CAT) |
| **atproto (MarshalX)** | SDK Python Bluesky (firehose, search, graph) | Dernier commit **2026-10-02** ; v0.0.72 | MIT [non vérifié] | ●○○ (Bluesky, API ouverte et gratuite) | github.com/MarshalX/atproto |
| **yt-dlp** | Téléchargement vidéos + métadonnées + commentaires YouTube/… (et X vidéo) | Dernier commit **2026-09-27** | Unlicense [non vérifié] | ●●○ (récupère médias X via URL) | github.com/yt-dlp/yt-dlp |
| **youtube-comment-downloader** | Commentaires YouTube sans API | Dernier commit **2026-07-29** | MIT [non vérifié] | ●○○ | github.com/egbertbouman/youtube-comment-downloader |
| **Mastodon.py** | Client API Mastodon | Dernier commit **2026-08-03** ; v2.2.2 | MIT [non vérifié] | ●○○ | github.com/halcy/Mastodon.py |
| **PullPush** (Reddit) | Index de rechange Pushshift | **[non vérifié]** (domaine bloqué) | — | — | pullpush.io |
| **Meta Content Library** | Seul accès légal FB/IG (pas open source, candidature ICPSR) | **[non vérifié]** | propriétaire | — | — |
| **Junkipedia** (ATI/NCoC) | Plateforme fermée multi-plateforme pour chercheurs | **[non vérifié]** (domaine bloqué) ; pas de code public connu | propriétaire | — | junkipedia.org |
| **Communalytic** | SaaS académique (Reddit, Telegram, YouTube, Bluesky…) | **[non vérifié]** | propriétaire/gratuit académique | — | communalytic.org |
| **SMAT** | Moteur de recherche multi-plateformes alt-tech (Telegram, Gab, 4chan, Truth…) avec API | **[non vérifié]** (domaine bloqué) | — | — | smat-app.com |
| **Verification plugin (InVID-WeVerify, AFP Medialab)** | Extension navigateur de vérification images/vidéos ; financée InVID→WeVerify→**vera.ai** (GA 101070093) | Dernier commit **2026-10-02** | MIT | ●●○ (analyse de médias X) | github.com/AFP-Medialab/verification-plugin |
| **Truly Media / AI4TRUST / vera.ai autres livrables** | Plateformes collaboratives EDMO | **[non vérifié]** ; Truly Media est propriétaire (ATC/Deutsche Welle) d'après connaissance antérieure | — | — | — |
| **OpenCTI** (Filigran) | Plateforme CTI STIX 2.1, utilisée pour le suivi d'incidents FIMI (SEEAS/EEAS, FIMI-ISAC) | Dernier commit **2026-10-03** ; versions 7.x ; 10,1k★ ; stack ES + Redis + RabbitMQ + MinIO | Apache-2.0 (CE) | ●●○ (couche « incidents », pas collecte) | github.com/OpenCTI-Platform/opencti |
| **Connecteur OpenCTI DISARM** | Importe DISARM (STIX) comme attack-patterns + kill-chain | « Filigran Verified », requiert OpenCTI ≥ 6.0 ; lit `DISARM_STIX/DISARM.json` | Apache-2.0 | ●●○ | github.com/OpenCTI-Platform/connectors (external-import/disarm-framework) |
| **MISP** | Partage d'indicateurs, galaxie DISARM intégrée | Dernier commit **2026-09-29** ; branche 2.5 | AGPL-3.0 | ●●○ | github.com/MISP/MISP ; misp-galaxy `clusters/disarm-techniques.json` |
| **DISARM frameworks** | Taxonomie TTP désinfo (Red/Blue), export STIX | Dernier commit **2025-02-10** | CC-BY-SA-4.0 | ●●○ (vocabulaire d'annotation) | github.com/DISARMFoundation/DISARMframeworks |
| **CooRnet** (R) | Détection de partage coordonné de liens (CrowdTangle) | **Archivé 2024-09-02** (fin CrowdTangle) ; renvoie vers CooRTweet / coordination-network-toolkit | [non vérifié] | ✖ | github.com/fabiogiglietto/CooRnet |
| **CooRTweet** (R, CRAN) | Détection de comportement coordonné, agnostique plateforme | Dernier commit **2025-07-10** ; sur CRAN | [non vérifié : fichier LICENSE] | ●●● (fonctionne sur tout export X : id, user, objet partagé, timestamp) | github.com/nicolarighetti/CooRTweet |
| **coordination-network-toolkit** (QUT DMRC, T. Graham) | CLI Python : co-retweet, co-tweet, co-similarity, co-link, co-reply, co-post ; SQLite | Dernier commit **2022-11-08** (stable mais dormant) | MIT | ●●● (CSV générique : message_id, user_id, repost_id, reply_id, urls, timestamp) | github.com/QUT-Digital-Observatory/coordination-network-toolkit |
| **Gephi** | Analyse/visualisation de graphes (bureau) | Dernier commit **2026-10-02** ; v0.11.3 (2026-09-06) | GPL-3/CDDL | ●●○ | github.com/gephi/gephi |
| **Gephi Lite** | Gephi dans le navigateur (sigma.js + graphology) | Dernier commit **2026-10-02** | GPL-3.0 | ●●○ | github.com/gephi/gephi-lite |
| **sigma.js** / **ipysigma** | Rendu WebGL de graphes / widget Jupyter | sigma.js v4, dernier commit 2026-04-30 ; ipysigma 0.24.6 (2025-11-25) | MIT | ●●○ | github.com/jacomyal/sigma.js ; github.com/medialab/ipysigma |
| **python-igraph** | Graphes, Leiden/Louvain intégrés | Dernier commit **2026-05-14** | GPL-2+ | ●●○ | github.com/igraph/python-igraph |
| **leidenalg** | Communautés Leiden | Dernier commit **2026-08-11** | GPL-3 | ●●○ | github.com/vtraag/leidenalg |
| **python-louvain** | Louvain (networkx) | Dernier commit **2024-03-16** (stable, peu actif ; préférer Leiden) | BSD | ●●○ | github.com/taynaud/python-louvain |
| **graph-tool** | Graphes C++/Python (SBM, inférence) | Hébergé sur git.skewed.de — **[non vérifié]** | LGPL-3 | ●●○ | git.skewed.de/count0/graph-tool |
| **BERTopic** | Topic modeling par embeddings | Dernier commit **2026-08-27** (Python 3.14) ; v0.17.4 (2025-12-03) | MIT | ●●● (narratifs) | github.com/MaartenGr/BERTopic |
| **sentence-transformers** | Embeddings (multilingual-e5, bge-m3, LaBSE…) | Dernier commit **2026-09-21** | Apache-2.0 | ●●● | github.com/UKPLab/sentence-transformers |
| **open_clip** | CLIP (clustering de mèmes, image↔texte) | Dernier commit **2026-09-30** | MIT [non vérifié] | ●●○ | github.com/mlfoundations/open_clip |
| **imagehash** | pHash/dHash/aHash/wHash | Dernier commit **2026-09-26** | BSD-2 | ●●○ | github.com/JohannesBuchner/imagehash |
| **PDQ / vPDQ** (Meta ThreatExchange) | Hash perceptuel robuste image (+ vidéo vPDQ) ; HMA 1.2.0 | Dernier commit dépôt **2026-10-02** (« Release HMA 1.2.0 ») ; impl. C++/PHP/Python/Java/WASM | BSD-style [non vérifié sur pdq/] | ●●○ | github.com/facebook/ThreatExchange (pdq/, vpdq/) |
| **Whisper / faster-whisper** | Transcription audio/vidéo | whisper : 2026-08-31 ; faster-whisper : **2026-10-01** | MIT | ●●○ | github.com/openai/whisper ; github.com/SYSTRAN/faster-whisper |
| **CARDS** (Coan, Boussalis, Cook, Nanko) | Classifieur de claims contrariens climat (RoBERTa + logit) | Dernier commit **2026-01-21** (README) ; poids 3,5 Go et données sur Google Drive ; « CARDS 2 » / modèles HF **[non vérifié]** | Apache-2.0 | ●●○ (classif. de textes X) | github.com/traviscoan/cards |
| **BotBuster** | Détection de bots multi-plateforme | URL testée → **404** ; **[non vérifié]** | — | — | — |
| **PostgreSQL + TimescaleDB** | Stockage relationnel + séries temporelles | TimescaleDB dernier commit **2026-10-02** ; 2.30.2 | Apache-2 / TSL | — | github.com/timescale/timescaledb |
| **DuckDB / Parquet** | Analytique colonne locale | Dernier commit **2026-10-02** ; v2.0 | MIT | — | github.com/duckdb/duckdb |
| **OpenSearch (+ Dashboards)** | Recherche plein texte + dashboards (fork libre d'ES/Kibana) | Dernier commit **2026-10-02** ; 3.9.1 | Apache-2.0 | — | github.com/opensearch-project/OpenSearch |
| **Meilisearch** | Recherche plein texte légère | Dernier commit **2026-09-29** ; v1.54.2 | MIT | — | github.com/meilisearch/meilisearch |
| **Metabase** | BI simple | Dernier commit **2026-10-03** | AGPL-3 (OSS) | — | github.com/metabase/metabase |
| **Apache Superset** | BI avancée | Dernier commit **2026-10-03** | Apache-2.0 | — | github.com/apache/superset |
| **Grafana** | Tableaux de bord séries temporelles | Dernier commit **2026-10-03** | AGPL-3 | — | github.com/grafana/grafana |
| **Label Studio** | Annotation manuelle (texte, image, multi-label) | Dernier commit **2026-10-02** ; 2.36.3 | Apache-2.0 | ●●● (annotation narratifs/DISARM) | github.com/HumanSignal/label-studio |
| **Argilla** | Annotation orientée NLP/LLM | Dernier commit **2025-08-05** (ralentissement net depuis rachat HF) | Apache-2.0 | ●●○ | github.com/argilla-io/argilla |
| **ArchiveBox** | Archivage multi-format (WARC, SingleFile, PDF, screenshot, soumission Wayback) | Dernier commit **2026-10-02** ; 0.9.72rc20 (branche dev, pré-release) | MIT | ●●○ (pages X nécessitent cookies/JS) | github.com/ArchiveBox/ArchiveBox |
| **browsertrix-crawler** | Crawl navigateur haute fidélité → WARC/WACZ (profils connectés) | Dernier commit **2026-10-02** ; 1.15.0-beta.1 | AGPL-3.0 | ●●● (seul outil capturant X rendu avec profil connecté) | github.com/webrecorder/browsertrix-crawler |
| **Browsertrix (app)** | Orchestrateur de crawls (k8s) | Nécessite Kubernetes ; AGPL-3 | AGPL-3.0 | ●●○ | github.com/webrecorder/browsertrix |
| **SingleFile** | Page unique HTML autonome (extension + CLI) | Dernier commit **2026-10-03** | AGPL-3.0 | ●●○ | github.com/gildas-lormeau/SingleFile |
| **auto-archiver** (Bellingcat) | Archivage automatisé + preuve : hash, OpenTimestamps, PDQ, Wayback, Ghostarchive, Whisper, WACZ | Dernier commit **2026-09-01** ; v1.2.9 | MIT | ●●○ (`twitter_api_extractor` = API payante ; sinon générique yt-dlp/antibot) | github.com/bellingcat/auto-archiver |
| **Wayback Save Page Now API** / **archive.today** / **Hunchly** | Archivage tiers / payant | **[non vérifié]** (domaines non testés) ; Hunchly propriétaire payant | — | ●●○ | — |
| **Media Cloud** | Recherche presse en ligne (API v4, client Python) | web-search : **2026-10-01** ; story-indexer : 2026-08-28 ; api-client Apache-2.0 | Apache-2.0 / AGPL | ●○○ (presse, pas X) | github.com/mediacloud |
| **GDELT / JRC EMM / Politoscope / Check First / ISD Beam / DFRLab / Alliance4Europe / Internet Archive Twitter** | Architectures de référence | **[non vérifié]** dans cette session (sites inaccessibles) ; voir § B.5 pour ce qui est documenté publiquement de mémoire | — | — | — |

---

## B. Notes par bloc

### B.1 Collecte / orchestration

**Situation X en 2026 (contexte vérifié par recherche web, 2026-10)** : l'API X est passée au *pay-per-use* par défaut le 2026-02-06 (≈ 0,005 $/post lu, plafond 3 M lectures/mois avant Enterprise ; Basic 200 $/mois migré de force après le 2026-06-01, Pro 5 000 $/mois déprécié après le 2026-09-01, Enterprise ≥ 42 000 $/mois). Pas de piste académique depuis 2023. En conséquence, « zéro budget » = collecte sans API, par trois voies : (a) **capture navigateur** (Zeeschuimer → 4CAT), (b) **API GraphQL interne avec comptes** (twscrape), (c) **proxys front-end** (Nitter, juridiquement sous pression depuis la mise en demeure du 2026-08-24).

- **4CAT + Zeeschuimer** (DMI, Amsterdam) : la combinaison la plus robuste et la plus « défendable » éthiquement. Zeeschuimer n'automatise rien : le chercheur navigue (recherche, profils, fils) et l'extension récupère les objets JSON que X envoie au navigateur (donc le schéma complet : tweet, auteur, métriques, médias, `conversation_id`, `in_reply_to`). Export ndjson/CSV ou push vers 4CAT, qui stocke en Postgres et propose des processeurs (réseaux de co-hashtags/mentions, co-mots, séries temporelles, exports GEXF, téléchargement médias, transcription audio). Commits 4CAT 2026-10-01 (un correctif « missing source field in tweet data » montre que le mapping X est maintenu) ; Zeeschuimer 2026-09-09. Limites : volume = ce qu'un humain fait défiler (quelques milliers de posts/heure), pas de collecte continue, pas d'historique au-delà de ce que la recherche X affiche.
- **twscrape** : la seule brique Python *active* (2026-09-22) couvrant search, `tweet_details`, `tweet_replies`, `tweet_thread`, `retweeters`, `followers`/`following`, `user_tweets` (plafond 3 200), listes, communautés, trends, modes `_raw`. Auth par cookies (`auth_token`, `ct0`) recommandée ; rotation de comptes ; proxies ; backend `curl-cffi` pour l'empreinte TLS ; les derniers commits détectent le « Cloudflare challenge shell » et auto-réparent les *features* GraphQL → signe d'une course aux armements. Risques : comptes bannis, violation des ToS, données partielles (la recherche X ne renvoie qu'un échantillon non reproductible).
- **Nitter** : archivé le 2026-09-11 par GitHub après la mise en demeure X Corp (2026-08-24), mais le README (2026-09-07) annonce la poursuite « following legal advice » ; xcancel est revenu en ligne (The Register / TNW, 2026-09). Fonctionne avec `sessions.jsonl` (sessions de vrais comptes X). À considérer uniquement comme source RSS d'appoint ; ne pas bâtir le pipeline dessus.
- **minet** : excellent socle CLI (fetch massif, extraction, résolution d'URL, `bsky`, `yt`, `tl channel-messages`, `insta`, `tk`). Les sous-commandes `twitter` (search, followers, retweeters…) reposent sur l'API v2 (payante) ; `twitter scrape` existe mais est fragile. Utiliser minet pour Bluesky/YouTube/Telegram et pour le *fetch* + extraction des liens partagés.
- **gazouilloire / DMI-TCAT / twint / Hoaxy / Botometer / BotAmp** : morts pour X (API ou archivage). Gazouilloire reste une référence de **modèle de données** (mapping ES, 1 Go/M tweets) ; DMI-TCAT pour la liste des analyses attendues.
- **Telegram** : Telethon (mais le projet a quitté GitHub le 2026-02-21, suivre sa nouvelle forge) ; telegram-tracker (channels → JSON/CSV + GEXF des forwards) ; tg-archive (SQLite + site statique) ; 4CAT a aussi une datasource Telegram native. Telegram reste la plateforme la plus « ouverte » techniquement.
- **TikTok** : pyktok (cookies, casse fréquente, dernier commit 2025-10-04) ; Zeeschuimer (posts + commentaires) ; API Recherche TikTok (wrapper officiel MIT, éligibilité UE/US académique).
- **Bluesky** : API AT Protocol ouverte et gratuite (firehose, search, graph) ; SDK `atproto` (2026-10-02) et `minet bsky`. 4CAT a une datasource `bsky`. C'est la seule grande plateforme où followers/replies/reposts sont intégralement récupérables sans compte.
- **YouTube** : yt-dlp (métadonnées + commentaires + sous-titres) et youtube-comment-downloader (2026-07-29) ; API Data v3 gratuite avec quota.
- **Facebook/Instagram** : seule voie légale = Meta Content Library (candidature, pas de code libre) [non vérifié cette session]. CooRnet (CrowdTangle) est archivé.
- **Reddit / Mastodon** : Redlib (2026-04-24) ; Mastodon.py (2026-08-03) ; PullPush [non vérifié].
- **Plateformes fermées pour chercheurs** : Junkipedia, Communalytic, SMAT [non vérifiés] — pas d'auto-hébergement possible, à mentionner comme compléments gratuits mais non souverains.
- **Écosystème EU / FIMI** : le plugin de vérification InVID-WeVerify (AFP Medialab) est bien vivant (commit 2026-10-02) et financé par **vera.ai** (GA 101070093) ; MIT. Truly Media, AI4TRUST : [non vérifiés], Truly Media est propriétaire. **OpenCTI** (7.x, commit 2026-10-03) + **connecteur DISARM** (Filigran Verified, importe `DISARM.json` STIX en attack-patterns/kill-chain) + **MISP** (2.5, 2026-09-29, galaxie `disarm-techniques`) forment la couche « gestion d'incidents FIMI » standard (STIX 2.1), celle utilisée par l'EEAS et le FIMI-ISAC [usage EEAS non re-vérifié ici]. Attention au coût d'exploitation : OpenCTI = ES + Redis + RabbitMQ + MinIO (≥ 16 Go RAM).

### B.2 Analyse

- **Coordination** : CooRnet archivé (2024-09-02). Deux remplaçants plateforme-agnostiques : **CooRTweet** (R, CRAN, 2025-07-10 ; entrée = `object_id`, `account_id`, `content_id`, `timestamp_share`) et **coordination-network-toolkit** (Python, MIT ; stable depuis 2022-11 ; CSV `message_id,user_id,username,repost_id,reply_id,message,timestamp,urls` → SQLite → graphes co-retweet / co-tweet / co-similarity (Jaccard) / co-link / co-reply / co-post, fenêtre 60 s par défaut). Les deux fonctionnent sur des exports Zeeschuimer/twscrape après un simple remappage.
- **Graphes** : python-igraph (Leiden intégré, 2026-05-14), leidenalg (2026-08-11), Gephi 0.11.3 (2026-10-02), Gephi Lite (web, GPL-3, 2026-10-02) et ipysigma pour l'exploration en notebook. Louvain (python-louvain) dormant → préférer Leiden. graph-tool [non vérifié] pour SBM.
- **Bots** : Botometer-X = archive figée (< 2023-05-31) ; BotBuster introuvable à l'URL testée. Recommandation : abandonner le « score de bot » et passer à des indicateurs comportementaux (coordination temporelle, âge du compte, ratio replies/posts, similarité textuelle) calculés localement.
- **Narratifs / NLP** : BERTopic 0.17.4 (2026-08-27) + sentence-transformers (2026-09-21) avec `multilingual-e5-large` ou `bge-m3` [disponibilité HF non vérifiée cette session] ; claim-matching par embeddings + reranking LLM local (Ollama). **CARDS** (Apache-2.0, RoBERTa, taxonomie contrarienne climat, poids 3,5 Go sur Drive ; README mis à jour 2026-01-21) reste réutilisable ; « CARDS 2 » (Rojas, Coan et al.) et les classifieurs HF [non vérifiés].
- **Médias** : imagehash (2026-09-26) pour pHash rapide ; **PDQ/vPDQ** (Meta ThreatExchange, HMA 1.2.0, 2026-10-02) pour un hash robuste image/vidéo standardisé (même algorithme que les plateformes) ; open_clip (2026-09-30) pour le clustering de mèmes ; faster-whisper (2026-10-01) pour transcrire vidéos X/TikTok/Telegram avant NLP.

### B.3 Stockage / dashboards

- **Postgres (+ TimescaleDB 2.30.2)** comme source de vérité : tables `posts` (JSONB brut + colonnes normalisées), `accounts`, `edges` (retweet/quote/reply/mention), `media` (hash PDQ, pHash, CLIP vector via `pgvector`), `collections` (provenance : outil, compte, horodatage). 4CAT fournit déjà un Postgres si on l'adopte.
- **DuckDB/Parquet** (v2.0) pour les exports analytiques et les notebooks ; coût nul, zéro serveur.
- **Recherche plein texte** : OpenSearch 3.9.1 + Dashboards (Apache-2.0, préférer à Elasticsearch/Kibana pour la licence) si > 10 M posts ; sinon **Meilisearch 1.54** (léger) ou simplement `tsvector`/`pg_trgm`.
- **Dashboards** : Metabase (AGPL, le plus simple pour non-dév), Superset (plus puissant), Grafana (séries temporelles / monitoring des collecteurs). Tous actifs au 2026-10-03.

### B.4 Archivage / preuve

- **browsertrix-crawler 1.15** (AGPL) : seul outil libre capturant X *rendu*, avec un **profil de navigateur connecté** (`--profile`), en WARC/WACZ signé ; c'est la base de preuve recommandée. Browsertrix (app) demande Kubernetes : trop lourd pour une petite équipe, lancer le crawler en Docker.
- **ArchiveBox 0.9.x** (MIT, pré-release) : multi-format (WARC, SingleFile, PDF, PNG, soumission Wayback) ; bon pour les URL externes (articles partagés), moins pour X (login).
- **SingleFile** (2026-10-03) : capture unitaire HTML autonome, extension + CLI.
- **auto-archiver 1.2.9** (Bellingcat, MIT) : pipeline « feeder → extractor → enricher → storage → database » avec `hash_enricher` (SHA-256), `timestamping_enricher` (RFC 3161), `opentimestamps_enricher` (ancrage Bitcoin), `pdq_hash_enricher`, `wayback_extractor_enricher`, `ghostarchive_enricher`, `whisper_enricher`, `wacz_extractor_enricher`, `ssl_enricher` ; feeders CSV/Google Sheets/CLI ; stockage local/S3/GDrive. Le `twitter_api_extractor` suppose l'API payante ; pour X sans API, passer par `generic_extractor` (yt-dlp) + `antibot_extractor_enricher` + `wacz`.
- **Chaîne de custodie** (Berkeley Protocol 2020/2022, guides Bellingcat — [non re-vérifiés ici]) : hash SHA-256 à la capture, horodatage indépendant (RFC 3161 et/ou OpenTimestamps), journal de capture (qui, quand, outil, version, URL, compte utilisé), conservation du brut (ndjson/WARC) séparée des dérivés, stockage WORM (bucket en mode *object lock* ou disque chiffré hors ligne). Wayback SPN / archive.today : [non vérifiés], utiles comme tiers de confiance mais X bloque souvent le rendu non connecté.

### B.5 Architectures de référence (ce qui est vérifié vs. de mémoire)

- **Vérifié** : Media Cloud (web-search 2026-10-01, story-indexer, API v4 client Apache-2.0) = presse, pas réseaux sociaux ; Hoaxy archivé 2022 ; 4CAT comme référence « collecte navigateur + Postgres + processeurs » ; auto-archiver comme référence « archivage probant » ; OpenCTI + DISARM + MISP comme référence « incidents FIMI ».
- **[non vérifiés cette session]** : Politoscope (ISC-PIF ; historiquement API Twitter → analyse de communautés), Junkipedia (ATI), SMAT (API publique, Elasticsearch), Check First « Matriochka » (documentation de stack non trouvée), DFRLab, ISD Beam (propriétaire), Alliance4Europe, Internet Archive « Twitter Stream » (arrêtée après 2023), GDELT (gratuit, presse/TV), JRC EMM (fermé, presse). À traiter comme sources d'inspiration, non comme briques.

---

## C. Synthèse : architecture de référence à coût nul

### C.1 Chaîne proposée

```
COLLECTE                      STOCKAGE                 ANALYSE                     ARCHIVAGE / PREUVE        ANNOTATION / INCIDENTS
Zeeschuimer (X, TikTok, IG,   Postgres 16 + Timescale  coordination-network-       browsertrix-crawler       Label Studio
Threads, Truth, Gab) ──┐      + pgvector + JSONB brut   toolkit / CooRTweet         (profil connecté, WACZ)   (taxonomie DISARM +
twscrape (X, comptes   ├─▶   ──▶ Parquet/DuckDB   ──▶ igraph/Leiden → Gephi Lite  auto-archiver (SHA-256,   narratifs maison)
dédiés, replies/threads)│      (exports analytiques)    BERTopic + e5/bge-m3        RFC3161/OTS, PDQ, Wayback)      │
minet bsky / yt / tl   ├─▶   Meilisearch ou OpenSearch  CARDS (climat)              SingleFile (unitaire)     OpenCTI + connecteur
Telethon / telegram-   │      (plein texte)              imagehash + PDQ + CLIP      ArchiveBox (URLs externes) DISARM (STIX 2.1,
tracker, atproto       ┘                                faster-whisper              stockage WORM             partage MISP/ISAC)
                                     │
                              Metabase / Grafana (dashboards), notebooks (ipysigma)
```

### C.2 Réutiliser vs. construire

**Réutiliser tel quel**
- 4CAT (Docker) comme console d'équipe : il apporte Postgres, l'import Zeeschuimer, les processeurs réseau et les exports GEXF/CSV sans code. Commits 2026-10.
- twscrape comme lib (pas comme service) dans un collecteur maison, avec 2-3 comptes X dédiés + proxies ; stocker la réponse `_raw` intégrale.
- coordination-network-toolkit (ou CooRTweet si l'équipe est sous R) sans modification : écrire seulement le *mapper* vers son CSV.
- BERTopic + sentence-transformers, imagehash + PDQ, faster-whisper : bibliothèques, pas de fork.
- browsertrix-crawler en Docker, auto-archiver en Docker : pipeline de preuve prêt à l'emploi.
- Label Studio pour l'annotation ; OpenCTI seulement si l'équipe partage des incidents en STIX avec des tiers (sinon, un schéma « incident » maison dans Postgres aligné sur DISARM suffit et évite 16 Go de RAM).
- Metabase pour les tableaux de bord, Gephi Lite pour l'exploration de graphes.

**Construire (petit, Python)**
1. **Mapper d'unification** X : ndjson Zeeschuimer / JSON twscrape → schéma commun (`post_id, author_id, created_at, text, lang, conversation_id, in_reply_to_post_id, quoted_post_id, retweeted_post_id, urls[], media[], metrics{}, raw JSONB, source_tool, captured_at, captured_by`). Même schéma pour Bluesky/Telegram/TikTok avec `platform`.
2. **Orchestrateur de collecte** (cron ou Prefect/Airflow minimal) : requêtes twscrape planifiées, déduplication, journal de provenance, alertes Grafana quand un compte est verrouillé.
3. **Résolveur d'URL** (minet `url-join`/`resolve` + extraction de domaine) pour les analyses de co-link et le croisement avec la presse (Media Cloud API).
4. **Service de hachage/horodatage** à l'ingestion (SHA-256 du brut + horodatage RFC 3161 ; auto-archiver le fait déjà pour les URL, il faut l'étendre aux objets JSON collectés).
5. **Dictionnaire d'annotation** : narratifs + techniques DISARM (import du JSON STIX) comme choix dans Label Studio, puis export vers Postgres pour les dashboards.

### C.3 Lacunes connues de la collecte X sans API, et contournements par outil

| Lacune | Zeeschuimer / 4CAT | twscrape | Nitter | Contournement structurel |
|---|---|---|---|---|
| **Arbres de réponses complets** | Seulement ce que l'utilisateur déroule (« Show more replies ») ; `conversation_id` et `in_reply_to` conservés | `tweet_replies` / `tweet_thread` paginent, mais X masque des réponses (ranking, « show probable spam ») ; non exhaustif | Affichage partiel, pas de pagination profonde | Reconstruire l'arbre par `conversation_id` à partir de plusieurs captures ; accepter un taux de couverture mesuré ; privilégier Bluesky pour les études de reply-tree exhaustives |
| **Followers / following** | Non capturés (sauf navigation manuelle des listes, lente) | `followers()` / `following()` disponibles mais fortement rate-limités, échantillon tronqué sur gros comptes | Non | Remplacer le graphe de follow par des graphes d'interaction (RT/quote/reply/mention), méthodologiquement défendable ; cibler les followers uniquement pour un petit nombre de comptes-clés |
| **Historique / recherche exhaustive** | La recherche X renvoie un échantillon non reproductible, pas d'`until`/`since` fiables | Idem (search = échantillon « Latest » paginé, souvent < 1 000 résultats par requête) ; `user_tweets` plafonné à ~3 200 | Idem | Collecte **prospective quotidienne** par requêtes découpées (mots-clés × jours × langues), stockage incrémental ; documenter la non-exhaustivité |
| **Retweeters / likers** | Non (liste visible mais rarement déroulée) | `retweeters()` ok (tronqué) ; likes non publics depuis 2024 | Non | Mesurer la diffusion via quotes + réponses + métriques agrégées (`retweet_count`) |
| **Volume / continuité** | Manuel (humain dans la boucle) | Automatisable mais dépend de comptes bannissables, CAPTCHA/Cloudflare (commits 2026-09) | Instances publiques instables, pression juridique | Mélanger les deux : twscrape pour le flux, Zeeschuimer pour les captures ciblées « preuve » ; archiver en WACZ ce qui compte |
| **Médias / vidéos** | URL des médias présentes dans le JSON | URL présentes | Proxy média | Télécharger immédiatement (yt-dlp / auto-archiver) : les URL expirent, les posts sont supprimés |
| **Statut légal / éthique** | Capture de ce qu'un humain voit ; pas d'automatisation → le plus défendable (RGPD : base « recherche », minimisation) | Violation des ToS X ; risque de bannissement ; posture à documenter (DSA art. 40 ne couvre pas le scraping) | Mise en demeure X Corp 2026-08-24 ; dépôt archivé | Rédiger une politique de collecte (finalité, durée, pseudonymisation — 4CAT a un module « anonymise », refactorisé 2026-10), ne jamais héberger de front-end public |
| **Comptes supprimés/suspendus** | Capturés au moment T seulement | Idem | Idem | Horodater chaque capture, conserver le brut, re-visiter périodiquement les comptes-clés pour détecter suspensions |

### C.4 Points de vigilance 2026

- X : *pay-per-use* uniquement, aucune voie académique ; toute brique « API Twitter » (gazouilloire, DMI-TCAT, Hoaxy, Botometer, CooRnet via CrowdTangle, minet `twitter`) est hors jeu pour un budget nul.
- Nitter : l'incident juridique d'août-septembre 2026 montre que les proxys front-end X peuvent disparaître du jour au lendemain ; ne pas en dépendre.
- Botometer-X : archive figée, inutilisable pour des comptes créés après mai 2023 ; coupure des endpoints historiques le 2026-11-02.
- Telethon a quitté GitHub (2026-02-21) : vérifier la nouvelle forge avant de figer une dépendance.
- Argilla ralentit (dernier commit 2025-08) : préférer Label Studio.
- ArchiveBox reste en pré-release 0.9 ; browsertrix-crawler est la brique de preuve la plus mûre.
- Les éléments marqués [non vérifié] (Junkipedia, Communalytic, SMAT, PullPush, Meta Content Library, CARDS 2 / modèles HF, Politoscope, Matriochka, GDELT, EMM, Berkeley Protocol, Wayback SPN) doivent être revérifiés avant citation dans un livrable.
