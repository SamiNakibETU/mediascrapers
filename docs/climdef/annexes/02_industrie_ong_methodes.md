# 02 — Rapports d'enquête de l'industrie, des plateformes et des ONG/think-tanks : données, indicateurs et méthodes de détection des comportements coordonnés inauthentiques

Revue de littérature — axe « industrie / plateformes / ONG ». Rédigé le 2026-10-03.

## Avertissement méthodologique sur la vérification des sources

- **Contrainte technique rencontrée** : dans l'environnement d'exécution, la politique réseau a bloqué (« egress blocked ») *toutes* les tentatives de récupération de page (WebFetch) vers les domaines concernés (transparency.meta.com, microsoft.com/cdn-dynmedia, openai.com, blog.google, tiktok.com, graphika.com, disinfo.eu, checkfirst.network, isdglobal.org, open.clemson.edu, recordedfuture.com, maldita.es, fsi.stanford.edu, alliance4europe.eu, atlanticcouncil.org, arxiv.org, wikipedia.org, etc.). Seul github.com était joignable. Le quota de recherche web de la session a ensuite été épuisé (200/200).
- **Conséquence** : **aucune URL ci-dessous n'a pu être vérifiée par chargement direct de la page**. Toutes les URL sont donc marquées **[URL non vérifiée par WebFetch]** ; elles proviennent des résultats de moteur de recherche (titres + URL renvoyés par le moteur), ce qui en fait des références *probables* mais non confirmées. Les faits tirés des extraits de recherche sont signalés « (extrait de recherche) ». Les éléments issus de la connaissance antérieure du rédacteur, sans confirmation par la recherche de cette session, sont marqués **[non vérifié]**.
- Recommandation : avant toute citation dans un document final, ouvrir chaque URL et confirmer titre, date et contenu.

Abréviations : CIB = Coordinated Inauthentic Behavior (Meta) ; IO = information operation ; FIMI = Foreign Information Manipulation and Interference ; GAN = generative adversarial network ; LLM = large language model ; TDS = traffic distribution system.

---

## (A) Tableau des sources

| # | Organisation | Document (titre exact ou approché) | Date | Objet | URL | Statut |
|---|---|---|---|---|---|---|
| A1 | Meta | *Adversarial Threat Report, First Quarter 2025* (« MAY 2025 FIRST QUARTER Adversarial Threat Report ») | mai 2025 | 3 réseaux CIB (Chine, Iran, Roumanie) | https://transparency.meta.com/sr/Q1-2025-Adversarial-threat-report/ | [URL non vérifiée par WebFetch] |
| A2 | Meta | *Adversarial Threat Report, Second–Third Quarter 2025* (« DECEMBER 2025 SECOND - THIRD QUARTER ») | déc. 2025 | Endless Mayfly (IUVM), Russie/freelances africains, Pologne, Inde, Moldavie ; passage au rythme semestriel | https://transparency.meta.com/sr/Q2-Q3-2025-Adversarial-threat-report/ | [URL non vérifiée par WebFetch] |
| A3 | Meta | *Adversarial Threat Report, Second Half 2026* (« AUGUST 2026 SECOND HALF ») | août 2026 | Rapport semestriel (contenu non consulté) | https://transparency.meta.com/sr/H2-2026-adversarial-threat-report/ | [URL non vérifiée par WebFetch] |
| A4 | Meta | *Quarterly Adversarial Threat Report Q2 2024* | août 2024 | Récap. CIB ; Russie 39 réseaux, Iran 30, Chine 11 depuis 2017 (extrait) | https://transparency.meta.com/sr/Q2-2024-Adversarial-threat-report | [URL non vérifiée par WebFetch] |
| A5 | Meta | *Quarterly Adversarial Threat Report Q1 2024* | mai 2024 | Personas de faux journalistes à photos GAN (extrait) | https://transparency.meta.com/sr/Q1-2024-Adversarial-threat-report | [URL non vérifiée par WebFetch] |
| A6 | Meta | Politique « Inauthentic Behavior » (Community Standards) | continu | Définition CIB / fake accounts | https://transparency.meta.com/policies/community-standards/inauthentic-behavior/ | [URL non vérifiée par WebFetch] |
| B1 | Microsoft MTAC | *Same targets, new playbooks: East Asia threat actors employ unique methods* | avril 2024 | Storm-1376 / Taizi Flood (Spamouflage) ; incendies de Maui/Lahaina ; présentateurs IA | https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/MTAC-East-Asia-Report.pdf (et page : https://www.microsoft.com/en-my/security/security-insider/intelligence-reports/east-asia-threat-actors-employ-unique-methods) | [URL non vérifiée par WebFetch] |
| B2 | Microsoft MTAC | *Nation-states engage in US-focused influence operations ahead of US presidential election* (Election Report 1) | 17 avril 2024 | Storm-1516, Storm-1099, Storm-1679, Storm-1376 | https://nsarchive.gwu.edu/sites/default/files/documents/semon9-ryglx/2024-04-17-MTAC-Report-Nation-states-influence-operations-ahead-US-election.pdf ; billet : https://blogs.microsoft.com/on-the-issues/2024/04/17/russia-us-election-interference-deepfakes-ai/ | [URL non vérifiée par WebFetch] |
| B3 | Microsoft MTAC | *Russia leverages cyber proxies and Volga Flood assets…* (Election Report 4) | été 2024 | Volga Flood (Rybar/Zvinchuk) | https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/MTAC-Election-Report-4.pdf | [URL non vérifiée par WebFetch] |
| B4 | Microsoft MTAC | *MTAC Election Report 5 on Russian Influence* ; billet « Russian election interference efforts focus on the Harris-Walz campaign » | 17 sept. 2024 | Storm-1516, Ruza Flood, Storm-1679, Volga Flood | https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/MTAC-Election-Report-5-on-Russian-Influence.pdf ; https://blogs.microsoft.com/on-the-issues/2024/09/17/russian-election-interference-efforts-focus-on-the-harris-walz-campaign/ | [URL non vérifiée par WebFetch] |
| B5 | Microsoft MTAC | *Iran steps into US election 2024 with cyber-enabled influence operations* | août 2024 | Iran (Storm-2035 etc.) | https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/5bc57431-a7a9-49ad-944d-b93b7d35d0fc.pdf | [URL non vérifiée par WebFetch] |
| B6 | Microsoft MTAC | Billet « As the U.S. election nears, Russia, Iran and China step up influence efforts » | 23 oct. 2024 | Synthèse pré-électorale | https://blogs.microsoft.com/on-the-issues/2024/10/23/as-the-u-s-election-nears-russia-iran-and-china-step-up-influence-efforts/ | [URL non vérifiée par WebFetch] |
| B7 | Microsoft MTAC (via presse) | Données T1 2026 : >1 000 vidéos synthétiques Storm-1516 au T1 2026 | 2026 | Storm-1516 | sources secondaires : https://ukrainianweek.com/storm-1516-russian-disinformation/ ; https://truescreen.io/insights/storm-1516-russia-ai-disinformation-2026/ | [URL non vérifiée par WebFetch] ; rapport primaire MTAC non localisé |
| C1 | OpenAI | *Disrupting malicious uses of our models: an update, February 2025* | fév. 2025 | Surveillance, emplois frauduleux, IO, arnaques, cyber | https://cdn.openai.com/threat-intelligence-reports/disrupting-malicious-uses-of-our-models-february-2025-update.pdf | [URL non vérifiée par WebFetch] |
| C2 | OpenAI | *Disrupting malicious uses of AI: June 2025* | juin 2025 | 10 cas ; Sneer Review, Uncle Spam, Helgoland Bite, VAGue Focus… | https://openai.com/global-affairs/disrupting-malicious-uses-of-ai-june-2025/ ; PDF : https://cdn.openai.com/threat-intelligence-reports/5f73af09-a3a3-4a55-992e-069237681620/disrupting-malicious-uses-of-ai-june-2025.pdf | [URL non vérifiée par WebFetch] |
| C3 | OpenAI | *Disrupting malicious uses of AI: October 2025 (an update)* | oct. 2025 | >40 réseaux perturbés depuis fév. 2024 ; IO russe nouvelle | https://openai.com/global-affairs/disrupting-malicious-uses-of-ai-october-2025/ ; PDF : https://cdn.openai.com/threat-intelligence-reports/7d662b68-952f-4dfd-a2f2-fe55b041cc4a/disrupting-malicious-uses-of-ai-october-2025.pdf | [URL non vérifiée par WebFetch] |
| C4 | OpenAI | *Disrupting malicious uses of AI* (février 2026) | 25 fév. 2026 | Arnaques, campagnes d'influence coordonnées, harcèlement étatique | https://openai.com/index/disrupting-malicious-ai-uses/ (page générique) | [URL non vérifiée par WebFetch] |
| C5 | OpenAI | Rapport juin 2026 (agents IA, désinformation, phishing) | juin 2026 | — | non localisé (sources secondaires seulement) | [non vérifié] |
| C6 | OpenAI | *Operation « Helgoland Bite »: German-language influence activity* | juin 2025 | Cas isolé | https://openai.com/index/disrupting-malicious-uses-of-ai-helgoland-bite/ | [URL non vérifiée par WebFetch] |
| D1 | Google TAG | *TAG Bulletin: Q1 2025* | 2025 | Campagnes d'influence coordonnées | https://blog.google/threat-analysis-group/tag-bulletin-q1-2025/ | [URL non vérifiée par WebFetch] |
| D2 | Google TAG | *TAG Bulletin: Q2 2025* | 21 juil. 2025 | >9 800 chaînes YouTube | https://blog.google/threat-analysis-group/tag-bulletin-q2-2025/ | [URL non vérifiée par WebFetch] |
| D3 | Google TAG | *TAG Bulletin: Q3 2025* | 2025 | 18 532 chaînes, 109 domaines, 12 comptes Ads, 1 blog | https://blog.google/threat-analysis-group/tag-bulletin-q3-2025/ | [URL non vérifiée par WebFetch] |
| D4 | Google TAG | *TAG Bulletin: Q4 2025* | m.à.j. 29 janv. 2026 | 6 280 chaînes PRC, etc. | https://blog.google/threat-analysis-group/tag-bulletin-q4-2025/ | [URL non vérifiée par WebFetch] |
| E1 | X / Twitter | *Information operations on Twitter: principles, process, and disclosure* | 2019 | Doctrine de divulgation | https://blog.x.com/en_us/topics/company/2019/information-ops-on-twitter | [URL non vérifiée par WebFetch] |
| E2 | X / Twitter | *Disclosing state-linked information operations we've removed* | 2021 | Dernières divulgations publiques d'archives | https://blog.x.com/en_us/topics/company/2021/disclosing-state-linked-information-operations-we-ve-removed | [URL non vérifiée par WebFetch] |
| E3 | X / Twitter | *The Twitter Moderation Research Consortium is now open to researchers* | sept. 2022 | TMRC, 52 jeux de données, 9 To, >220 M tweets | https://blog.x.com/en_us/topics/company/2022/twitter-moderation-research-consortium-open-researchers | [URL non vérifiée par WebFetch] |
| E4 | X | *An update on Twitter Transparency Reporting* | 2023 | Abandon du format antérieur | https://blog.x.com/en_us/topics/company/2023/an-update-on-twitter-transparency-reporting | [URL non vérifiée par WebFetch] |
| E5 | X | *Global Transparency Report H1 2024* | 25 sept. 2024 | 464 M comptes suspendus spam/manipulation | https://transparency.x.com/content/dam/transparency-twitter/2024/x-global-transparency-report-h1.pdf | [URL non vérifiée par WebFetch] |
| E6 | Internet Archive | *X/Twitter Information Operations* (sauvegarde des archives IO) | janv. 2024 | Copie des jeux de données IO | https://archive.org/details/X_Twitter_Information_Operations | [URL non vérifiée par WebFetch] |
| F1 | TikTok | *Countering deceptive behavior / Covert Influence Operations Reports* (Transparency Center) | mensuel depuis mai 2024 | Réseaux CIO perturbés | https://www.tiktok.com/transparency/en-us/countering-influence-operations/ | [URL non vérifiée par WebFetch] |
| F2 | TikTok | *Strengthening our approach to countering influence attempts* | 23 mai 2024 | Création du rapport dédié | https://newsroom.tiktok.com/en-us/strengthening-our-approach-to-countering-influence-attempts | [URL non vérifiée par WebFetch] |
| F3 | TikTok | *Sixth Disinformation Code Transparency Report* | 2025 | Élections Croatie, Allemagne, Pologne, Portugal, Roumanie (S1 2025) | https://newsroom.tiktok.com/tiktok-sixth-disinformation-code-transparency-report?lang=en-150 | [URL non vérifiée par WebFetch] |
| G1 | Graphika | *Spamouflage Breakout* | fév. 2023 [non vérifié pour la date] | Spamouflage ; percée hors de son réseau | https://www.graphika.com/reports/spamouflage-breakout | [URL non vérifiée par WebFetch] |
| G2 | Graphika | *The #Americans* | 3 sept. 2024 | 15 comptes X + 1 TikTok Spamouflage se faisant passer pour des Américains | https://www.graphika.com/reports/the-americans | [URL non vérifiée par WebFetch] |
| G3 | Graphika | *Cheap Tricks: How AI Slop Is Powering Influence Campaigns* | nov. 2025 | 9 opérations (CopyCop, Doppelganger, Spamouflage, Falsos Amigos, Overload, Undercut, pro-Inde…) | https://www.graphika.com/reports/cheap-tricks | [URL non vérifiée par WebFetch] |
| G4 | Graphika | *(Don't) Blame it on the Bots* (billet) | s.d. | Mise en garde contre l'étiquette « bot » | https://graphika.com/posts/don-t-blame-it-on-the-bots | [URL non vérifiée par WebFetch] |
| G5 | Graphika | *Deep Learning at Graphika: Scaling Network Maps with Heterogeneous Graph Embedding* ; *How it Works* | s.d. | Méthode cartographique (ATLAS) | https://graphika.com/posts/deep-learning-at-graphika-scaling-network-maps-with-heterogeneous-graph-embedding ; https://www.graphika.com/how-it-works | [URL non vérifiée par WebFetch] |
| G6 | Graphika + Stanford IO | *Unheard Voice: Evaluating five years of pro-Western covert influence operations* | août 2022 | Analyse d'un takedown Meta/Twitter | https://public-assets.graphika.com/reports/graphika_stanford_internet_observatory_report_unheard_voice.pdf | [URL non vérifiée par WebFetch] |
| G7 | Graphika + SIO | *More-Troll Kombat* | déc. 2020 | Réseau lié à l'IRA (Afrique) | https://www.graphika.com/reports/more-troll-kombat | [URL non vérifiée par WebFetch] |
| H1 | EU DisinfoLab (avec Qurium) | *Doppelganger – Media clones serving Russian propaganda* | 27 sept. 2022 | Découverte de l'opération Doppelganger | https://www.disinfo.eu/doppelganger/ ; PDF : https://www.disinfo.eu/wp-content/uploads/2022/09/Doppelganger-1.pdf ; copie : https://nsarchive.gwu.edu/sites/default/files/documents/semon9-giki0/2022-09-27-EUDisinfoLab-Qurium-Doppelganger.pdf | [URL non vérifiée par WebFetch] |
| H2 | EU DisinfoLab | *Doppelganger hub* | continu | Centralisation des enquêtes | https://www.disinfo.eu/doppelganger-hub/ | [URL non vérifiée par WebFetch] |
| H3 | Qurium | *Under the hood of a Doppelgänger* | 2022-2023 | Infrastructure, redirections, Keitaro | https://www.qurium.org/alerts/under-the-hood-of-a-doppelganger/ | [URL non vérifiée par WebFetch] |
| H4 | Auswärtiges Amt (Allemagne) | *Technical Report on an Analysis by the Federal Foreign Office* (Doppelgänger) | 5 juin 2024 | Botnet X Doppelgänger (posters/followers, chaîne FI-KE-D) | https://www.auswaertiges-amt.de/resource/blob/2682484/2da31936d1cbeb9faec49df74d8bbe2e/technischer-bericht-desinformationskampagne-doppelgaenger-1--data.pdf | [URL non vérifiée par WebFetch] |
| H5 | Sekoia.io | *Master of Puppets: uncovering the DoppelGänger pro-Russian influence campaign* | 2023 [non vérifié pour la date] | Infrastructure | https://blog.sekoia.io/master-of-puppets-uncovering-the-doppelganger-pro-russian-influence-campaign | [URL non vérifiée par WebFetch] |
| I1 | Check First + Reset Tech | *Operation Overload: how pro-Russian actors flood newsrooms with fake content and seek to divert their efforts* | juin 2024 | Campagne « Matriochka »/Overload | https://checkfirst.network/wp-content/uploads/2024/06/Operation_Overload_WEB.pdf ; billet : https://checkfirst.network/operation-overload-how-pro-russian-actors-flood-newsrooms-with-fake-content-and-seek-to-divert-their-efforts/ | [URL non vérifiée par WebFetch] |
| I2 | Check First + Reset Tech | *Operation Overload: More Platforms, New Techniques, Powered by AI* | juin 2025 | Extension Telegram/X/Bluesky/TikTok ; IA | https://checkfirst.network/wp-content/uploads/2025/06/Overload%C2%A02_%20Main%20Draft%20Report_compressed.pdf ; billet : https://checkfirst.network/operation-overload-an-ai-fuelled-escalation-of-the-kremlin-linked-propaganda-effort/ | [URL non vérifiée par WebFetch] |
| I3 | SEE Check | *Operation Overload in SEE: Still Active, No Longer Overloading* | 28 janv. 2025 | Réplication régionale | https://seecheck.org/index.php/2025/01/28/operation-overload-in-see-still-active-no-longer-overloading/ | [URL non vérifiée par WebFetch] |
| I4 | EFCSN | *EFCSN Statement on Operation Overload Report* | 2024 | Réaction des fact-checkers | https://efcsn.com/policy/efcsn-statement-on-operation-overload-report-by-checkfirst/ | [URL non vérifiée par WebFetch] |
| J1 | ISD | *Operation Overload's underwhelming influence and evolving tactics* (Digital Dispatch) | 2025 (T2) | ~300 comptes X/Bluesky/TikTok | https://www.isdglobal.org/digital-dispatch/operation-overloads-underwhelming-influence-and-evolving-tactics/ | [URL non vérifiée par WebFetch] |
| J2 | ISD | *Stolen voices: Russia-aligned operation manipulates audio and images to impersonate experts* | 2025 | Clonage vocal / usurpation | https://www.isdglobal.org/digital-dispatch/stolen-voices-russia-aligned-operation-manipulates-audio-and-images-to-impersonate-experts/ | [URL non vérifiée par WebFetch] |
| J3 | ISD + CASM | *What is Beam?* (lancement 14 nov. 2022) ; Method52 (CASM) | 2022 | Outillage détection | https://beamdisinfo.org/what-is-beam/ ; https://www.casmtechnology.com/pages/technology | [URL non vérifiée par WebFetch] |
| K1 | Alliance4Europe (CDN) | *Fool Me Once: Russian Influence Operation Doppelganger Continues on X and Facebook* | sept. 2024 | Persistance Doppelganger | https://alliance4europe.eu/wp-content/uploads/2024/09/CDN-Report-%E2%80%93-Fool-Me-Once_-Russian-Influence-Operation-Doppelganger-Continues-on-X-and-Facebook-%E2%80%93-September-2024.pdf | [URL non vérifiée par WebFetch] |
| K2 | Alliance4Europe | *Illegal Russian Influence Operations Continue Despite Sanctions* | déc. 2024 | Doppelganger & sanctions | https://alliance4europe.eu/russian-influence-doppelganger-report-dec-2024 | [URL non vérifiée par WebFetch] |
| K3 | Alliance4Europe | *Illegal Doppelganger Operation: Targeting the Polish Elections* ; *Polish Election Country Report 2025* | 2025 | Présidentielle polonaise | https://alliance4europe.eu/doppelganger-poland-elections ; https://alliance4europe.eu/report/polish-election-country-report-2025 | [URL non vérifiée par WebFetch] |
| K4 | Alliance4Europe | *Interfering from Exile – Ilan Shor's Demonstrations in Moldova* ; *Still marching on(line): How R-FBI Targets Moldova's Elections* | 2025 | Réseau CIB promouvant un bot Telegram (OK, TikTok, Telegram, FB, IG) | https://alliance4europe.eu/interfering-from-exile ; https://alliance4europe.eu/report/fbi-targets-moldova-elections | [URL non vérifiée par WebFetch] |
| K5 | Alliance4Europe + Globsec | *Election Report: Assessment of FIMI… Czech Election* | déc. 2025 | Tchéquie | https://alliance4europe.eu/wp-content/uploads/2025/12/FRT-24_Globsec_Czech-Election-Report.pdf | [URL non vérifiée par WebFetch] |
| K6 | Alliance4Europe (Trollrensics + RTL) | *Persistent Infrastructure and Cross-Border Influence Operations Targeting [Hungarian elections] – CIB Network* | avril 2026 | Fermes à trolls, législatives hongroises | https://alliance4europe.eu/wp-content/uploads/2026/04/Hungarian-elections-report-CIB-Network.pdf | [URL non vérifiée par WebFetch] |
| K7 | Alliance4Europe | *DISRUPT White Paper* ; *X-ploitation* | 2025 | Cadre de perturbation ; X | https://alliance4europe.eu/report/disruption-framework-white-paper ; https://alliance4europe.eu/x-ploitation | [URL non vérifiée par WebFetch] |
| L1 | Clemson Media Forensics Hub | *Writers of the Storm: Who's Behind the Ongoing Production of Pro-Russian [Disinformation]* (Warren, Linvill et al.) | 2025 [non vérifié pour la date] | Storm-1516 | https://open.clemson.edu/mfh_ci_reports/10/ | [URL non vérifiée par WebFetch] |
| L2 | Clemson MFH | *Hungary for more? Russian Storm-1516 narratives and engagement tactics* (Murray, Linvill, Warren) | 10 avril 2026 | Storm-1516 vs législatives hongroises 2026 | https://open.clemson.edu/mfh_reports/11/ | [URL non vérifiée par WebFetch] |
| L3 | Clemson MFH | Index des rapports | — | — | https://open.clemson.edu/mfh_reports/ | [URL non vérifiée par WebFetch] |
| L4 | VIGINUM (SGDSN) | *Technical report – Storm-1516* (TLP:CLEAR) | 7 mai 2025 | Attribution/mécanique Storm-1516 | https://www.sgdsn.gouv.fr/files/files/Publications/20250507_TLP-CLEAR_NP_SGDSN_VIGINUM_Technical%20report_Storm-1516.pdf | [URL non vérifiée par WebFetch] |
| L5 | EDMO | *Storm-1516, the pro-Russian disinformation operation threatening the public debate* | 2025 | Synthèse | https://edmo.eu/publications/storm-1516-the-pro-russian-disinformation-operation-threatening-the-public-debate/ | [URL non vérifiée par WebFetch] |
| M1 | Recorded Future (Insikt) | *Russia-Linked CopyCop Uses LLMs to Weaponize Influence Content at Scale* (CTA-2024-0509) | 9 mai 2024 | Réseau de faux sites + LLM | https://www.recordedfuture.com/research/russia-linked-copycop-uses-llms-to-weaponize-influence-content-at-scale ; PDF : https://go.recordedfuture.com/hubfs/reports/cta-2024-0509.pdf | [URL non vérifiée par WebFetch] |
| M2 | Recorded Future | *Russia-Linked CopyCop Expands to Cover US Elections, Target Political Leaders* | juin 2024 | 120 nouveaux sites (10-12 mai 2024), >1 000 faux journalistes | https://www.recordedfuture.com/research/copycop-expands-to-cover-us-elections-target-political-leaders | [URL non vérifiée par WebFetch] |
| M3 | Recorded Future | *CopyCop Deepens Its Playbook with New Websites and Targets* | 2025 | ≥200 sites depuis mars 2025 (US, France, Canada) | https://www.recordedfuture.com/research/copycop-deepens-its-playbook-with-new-websites-and-targets | [URL non vérifiée par WebFetch] |
| N1 | Antibot4Navalny (collectif anonyme) | Fils X (ex. thread 1851989389951357437) et entretiens | depuis nov. 2023 | Détection des bots Doppelganger sur X | https://threadreaderapp.com/thread/1851989389951357437 ; entretiens : https://theworld.org/stories/2024/07/10/meet-antibot4navalny-the-mysterious-researchers-exposing-russias-war-on-truth ; https://therecord.media/antibot4navalny-click-here-interview-disinformation-ukraine | [URL non vérifiée par WebFetch] |
| N2 | Re:Baltica | *When pro-Kremlin bots start speaking Latvian* | mars 2024 | Chiffres A4N : ~75 000 comptes/mois, 600 domaines, 5 M vues/nuit | https://en.rebaltica.lv/2024/03/when-pro-kremlin-bots-start-speaking-latvian/ | [URL non vérifiée par WebFetch] |
| N3 | AFP / France 24 | *Pro-Russian disinformation makes its Bluesky debut* | 10 janv. 2025 | Migration vers Bluesky | https://www.france24.com/en/live-news/20250110-pro-russian-disinformation-makes-its-bluesky-debut | [URL non vérifiée par WebFetch] |
| O1 | Stanford Internet Observatory | *Analysis of June 2020 Twitter takedowns linked to China, Russia and Turkey* | juin 2020 | Jeux de données takedown | https://fsi.stanford.edu/news/june-2020-twitter-takedown | [URL non vérifiée par WebFetch] |
| O2 | SIO | *Analysis of Twitter Takedowns Linked to Cuba, the Internet Research Agency, Saudi Arabia, and Thailand* | oct. 2020 | 526 comptes Cuba, 4 802 243 tweets | https://fsi.stanford.edu/news/twitter-takedown-october-2020 | [URL non vérifiée par WebFetch] |
| O3 | SIO | Index « Takedown » | — | — | https://fsi.stanford.edu/taxonomy/term/468 | [URL non vérifiée par WebFetch] |
| P1 | DFRLab (Atlantic Council) | Page programme ; *Atlantic Council's DFRLab independent analysis of networks removed by Facebook in Russia, Georgia, and Myanmar* | 2019-2020 [non vérifié] | Analyses indépendantes de takedowns | https://www.atlanticcouncil.org/programs/digital-forensic-research-lab/ ; https://www.atlanticcouncil.org/news/press-releases/atlantic-councils-dfrlab-independent-analysis-of-networks-removed-by-facebook-in-russia-georgia-and-myanmar/ | [URL non vérifiée par WebFetch] |
| P2 | DFRLab | *Narrative Warfare: How the Kremlin and Russian News Outlets Justified [the invasion]* | fév. 2023 | Traçage narratif | https://www.atlanticcouncil.org/wp-content/uploads/2023/02/Narrative-Warfare-Final.pdf | [URL non vérifiée par WebFetch] |
| P3 | DFRLab + G7 RRM | *G7 RRM Digital Transnational Repression Detection Academy* | nov. 2025 | Formation OSINT | https://www.atlanticcouncil.org/news/press-releases/atlantic-councils-dfrlab-delivers-the-g7-rrm-digital-transnational-repression-detection-academy/ | [URL non vérifiée par WebFetch] |
| Q1 | Maldita.es | *Desinformación y la DANA en España: el rol de las plataformas digitales durante la crisis* | 14 nov. 2024 | Réponse des plateformes (TikTok, X, YouTube, FB, IG, WhatsApp, LinkedIn, Telegram) | https://maldita.es/nosotros/20241114/DANA-desinformacion-plataformas-crisis-respuesta | [URL non vérifiée par WebFetch] |
| Q2 | Maldita.es | *Qué han hecho (y qué no) las plataformas y redes sociales para hacer frente a la desinformación sobre la DANA* | 19 nov. 2024 | idem | https://maldita.es/malditatecnologia/20241119/desinformacion-dana-respuesta-plataformas-redes-sociales/ | [URL non vérifiée par WebFetch] |
| Q3 | (académique) | *Desinformación y catástrofes naturales. El caso de la Dana de Valencia en 2024: análisis de los bulos… de cuatro verificadores españoles* | 2025 | 192 bulos, 185 notes (28 oct.–17 nov. 2024), 4 vérificateurs (Newtral, Verificat, EFE Verifica, Maldita) | https://dialnet.unirioja.es/servlet/articulo?codigo=10358253 | [URL non vérifiée par WebFetch] |
| R1 | Science Feedback | *Twitter/X fails to act on Doppelganger-related notices* | 2024 | Test de signalement | https://science.feedback.org/twitter-x-fails-to-act-on-doppelganger-related-notices/ | [URL non vérifiée par WebFetch] |
| R2 | Global Affairs Canada (RRM) | *Canada targeted in a new Chinese transnational repression campaign linked to 'Spamouflage'* | 2024 | Guides d'identification Microsoft/Graphika/Mandiant | https://www.international.gc.ca/transparency-transparence/rapid-response-mechanism-mecanisme-reponse-rapide/2024-spamouflage.aspx?lang=eng | [URL non vérifiée par WebFetch] |
| S1 | Bastos, M. (Social Media + Society) | *Visual Identities in Troll Farms: The Twitter Moderation Research Consortium* | 2025 | Usage académique des archives TMRC | https://journals.sagepub.com/doi/10.1177/20563051251323652 | [URL non vérifiée par WebFetch] |
| S2 | arXiv | *Evidence of Inter-state Coordination amongst State-backed Information Operations* | 2023 | Coordination inter-États sur archives Twitter | https://arxiv.org/pdf/2305.05907 | [URL non vérifiée par WebFetch] |
| S3 | arXiv | *Beyond Content: Behavioral Policies Reveal Actors in Information Operations* | fév. 2026 | Attribution comportementale | https://arxiv.org/pdf/2602.02838 | [URL non vérifiée par WebFetch] |
| T1-T6 | Logically, Bot Sentinel, Oxford Internet Institute (Computational Propaganda Project), Cardiff CSRI, NewsGuard, Full Fact | voir section B.20 | — | — | **[non vérifié]** : aucune recherche n'a pu être exécutée dans cette session (quota épuisé) ; contenu issu de la connaissance antérieure uniquement |

---

## (B) Fiches par source : données, indicateurs, méthodes

### B.1 Meta — Adversarial Threat Reports (trimestriels 2021-2025, puis semestriels)

**Objet.** Rapports publics depuis 2017 (initialement centrés sur la CIB, élargis ensuite à l'espionnage, la surveillance à louer, les arnaques et aux « comportements adverses assistés par IA ») (extrait de recherche, A2). Le rapport Q2-Q3 2025 (décembre 2025) annonce le passage à une publication semestrielle (extrait, A2) ; un rapport « Second Half 2026 » est daté d'août 2026 (A3).

**Définition opératoire.** La CIB est définie comme un effort coordonné de manipulation du débat public à visée stratégique dans lequel *les faux comptes sont au cœur de l'opération* : des personnes se coordonnent et utilisent de faux comptes pour tromper sur leur identité et leurs intentions (extrait de recherche). La politique « Inauthentic Behavior » (A6) distingue l'« inauthentic behavior » simple (faux comptes, engagement artificiel) de la CIB (réseau + visée) [non vérifié pour la formulation exacte].

**Données / champs exploités (tels que décrits dans les rapports).**
- *Niveau compte* : faux comptes ; **photos de profil générées par GAN** utilisées de façon *cohérente sur plusieurs plateformes* pour des personas de « journalistes fictifs » (Q1 2024, extrait) ; **comptes achetés/acquis** (réseaux russes acquérant des comptes IG/FB/Pages — extrait Q2 2024) ; comptes compromis.
- *Niveau infrastructure* : **domaines de faux médias**, Pages et Groupes liés, sites hors plateforme vers lesquels pointent les liens (constante des rapports) [non vérifié pour les formulations].
- *Niveau comportement* : **récidive** (« recidivist » networks tentant de revenir après suppression — notion centrale des rapports Doppelganger de Meta) [non vérifié] ; **gestion commerciale externalisée** : usage par la Russie de « social media managers freelance en Afrique, non informés » pour contourner la politique CIB (extrait, A2) ; opérateurs « à louer » (firmes de marketing/PR).
- *Niveau IA* : Meta juge que les tactiques GenAI n'ont apporté que des gains « incrémentaux » de productivité et n'ont pas entravé sa capacité de perturbation (extrait, A4/2024).
- *Attribution* : mise à jour d'attribution d'« Endless Mayfly » à l'International Union of Virtual Media (IUVM, Iran) (extrait, A2).

**Méthodes.** Meta décrit une combinaison « d'enquêtes expertes approfondies pour détecter les comportements nouveaux » et « d'améliorations de la détection à l'échelle » (extrait, A2) ; suppression « de l'entièreté du réseau » plutôt que de contenus ; partage d'indicateurs (« threat indicators ») avec l'industrie et les autorités (extrait, A1). Les rapports fournissent pour chaque réseau : origine, cibles, nombre d'actifs supprimés par surface (comptes FB, Pages, Groupes, comptes IG), audience (followers), dépenses publicitaires, attribution (confiance), et des exemples de contenu. Les signaux techniques précis (empreintes d'appareils, IP, etc.) ne sont **pas** publiés — limite structurelle de la transparence des plateformes. [non vérifié pour la liste exhaustive des champs]

**Exemple (extrait de recherche).** Réseau originaire de Chine visant Myanmar, Taïwan, Japon : 157 comptes FB, 19 Pages, 1 Groupe, 17 comptes IG supprimés « avant de bâtir une audience authentique ». Q1 2025 : 17 comptes FB, 22 Pages, 21 comptes IG pour trois réseaux (Chine, Iran, Roumanie).

### B.2 Microsoft Threat Analysis Center (MTAC)

**Objet.** Rapports thématiques (East Asia, Russie, Iran) et série « Election Reports » 2024. Nomenclature « Storm-xxxx » (acteurs non encore attribués) et « Flood » (acteurs russes : Ruza Flood = Doppelganger/SDA ; Volga Flood = Rybar ; Taizi Flood = Spamouflage/Storm-1376).

**Storm-1376 / Taizi Flood / Spamouflage** (B1, avril 2024, extraits) : usage d'**images générées par IA** et de textes traduits en **>30 langues** ; narration du « weather weapon » américain sur les incendies de Maui (août 2023) ; présentateurs de JT générés par IA (outil CapCut) depuis février 2023 ; vidéos « AI-enhanced » visant des parlementaires canadiens ; « hundreds of accounts » pour attiser la colère autour des manifestations pro-palestiniennes (avril-mai 2024). Indicateurs mis en avant : **volume multilingue synchrone**, **réutilisation d'images IA**, **comptes se faisant passer pour des électeurs américains** et **sondant** les publics (questions posées pour tester les clivages).

**Storm-1516** (B2, B4, extraits) : « video forgeries » distinctives ; **blanchiment narratif** (laundering) via vidéos de « faux journalistes » et « lanceurs d'alerte inexistants », puis amplification par **sites d'information inauthentiques** ; pivot (avril 2024) de l'Ukraine vers l'élection US ; T1 2026 : >1 000 vidéos synthétiques recensées par MTAC (source secondaire B7).
**Storm-1679** : pseudo-documentaires (« Olympics Has Fallen », voix IA imitant Tom Cruise) ; usage répété de l'IA générative.
**Volga Flood** : comptes « milbloggers » prétendant diffuser des hack-and-leak ; direction incluant Mikhail Zvinchuk (sanctionné UE), anciens du MoD russe et de Patriot Media (extrait B4).
**Ruza Flood** : réseau Doppelganger. Microsoft note un « synchronized shift » des trois acteurs (Storm-1516, Ruza Flood, Storm-1679) vers la campagne Harris en septembre 2024 — indicateur de **synchronie narrative inter-acteurs** (extrait B4).

**Données / méthode.** MTAC s'appuie sur la télémétrie Microsoft, le suivi de domaines et de l'infrastructure web, l'analyse de vidéos (artefacts IA, voix clonées), le suivi des personas et des **chaînes de blanchiment** (Telegram → sites → influenceurs → médias). Les rapports restent narratifs : peu de champs de données bruts publiés. [non vérifié pour le détail]

### B.3 OpenAI — « Disrupting malicious uses of AI » (fév. 2024 → juin 2026)

**Objet.** Rapports périodiques (fév. 2024 ; mai 2024 ; oct. 2024 ; fév. 2025 ; juin 2025 ; oct. 2025 ; fév. 2026 ; juin 2026) ; >40 réseaux perturbés depuis février 2024 (extrait, C3). Les cas d'IO sont classés comme « covert influence operations ».

**Cas 2025 (extraits C2).**
- *Sneer Review* (Chine) : génération en masse de posts et de **commentaires d'engagement factices** pour simuler un débat organique (TikTok, X, Reddit, Facebook) ; sujets Taïwan, USAID, Mahrang Baloch ; rédaction via ChatGPT de **revues de performance internes** décrivant le fonctionnement de l'opération.
- *Uncle Spam* (Chine) : contenus contradictoires (ex. droits de douane) ; **photos de profil IA** de prétendus vétérans.
- *Helgoland Bite* (Russie) : contenu germanophone sur les élections allemandes 2025, distribution Telegram et X.
- *VAGue Focus* : faible engagement authentique, faible sophistication.

**Données / indicateurs propres à OpenAI.** Position unique : observation des **prompts et des sorties du modèle** (contenu commandé, langues demandées, demandes de traduction, de personas, de « réponses à des commentaires »), des **métadonnées de compte** (horaires d'activité, cohérence avec un fuseau horaire, infrastructure de connexion), et **corrélation hors plateforme** (retrouver les sorties publiées sur les réseaux sociaux). OpenAI utilise l'échelle **Breakout Scale** (Ben Nimmo) pour qualifier l'impact (catégories 1-6) et souligne de façon récurrente le très faible engagement authentique [non vérifié pour les formulations exactes ; Breakout Scale confirmé par la connaissance antérieure, Nimmo 2020, Brookings]. Les rapports insistent sur le fait que l'IA est combinée à des outils classiques (sites, comptes sociaux) (extrait C4/C5).

### B.4 Google — TAG Bulletins (Threat Analysis Group / Google Threat Intelligence Group)

**Objet.** Bulletins trimestriels listant les « coordinated influence operation campaigns » clôturées. Champs publiés par campagne (extraits D2-D4) : **nombre de chaînes YouTube terminées**, **domaines bloqués** de Google News/Discover, **comptes Google Ads supprimés**, **blogs Blogger**, attribution par pays/acteur (Russie, Chine/PRC, Azerbaïdjan, Turquie, Roumanie, Iran, Israël, Ghana…), **langues** du contenu, **thèmes** (pro-gouvernement, critiques d'États tiers), et mention de prestataires (« Russian consulting firm » : 3 opérations distinctes, Q3 2025). Chiffres : Q3 2025 : 18 532 chaînes (+42 % vs Q3 2024), 109 domaines, 12 comptes Ads, 1 blog ; Q2 2025 (21 juil. 2025) : >9 800 chaînes ; Q4 2025 (m.à.j. 29 janv. 2026) : 6 280 chaînes PRC (contenu chinois et anglais sur la PRC et la politique étrangère US).

**Méthode.** Aucune méthodologie n'est détaillée ; les bulletins sont des registres d'actions. Pour la recherche, l'intérêt tient aux **séries temporelles** (volumes par acteur) et à la **multi-langue** comme marqueur de « spamouflage ».

### B.5 X / Twitter — transparence (ce qu'il en reste)

- 2018-2021 : archives publiques d'« information operations » (jeux de données complets : comptes, tweets, médias) ; doctrine « principles, process, and disclosure » (E1, 2019). Taille cumulée : >9 To de médias, >83 000 comptes, >200 M tweets (extrait E2).
- 2022 : création du Twitter Moderation Research Consortium (TMRC) : 52 jeux de données, >220 M tweets, accès réservé aux chercheurs agréés ; fin des diffusions publiques intégrales (extraits E3). Champs des archives [connaissance antérieure, non vérifié] : userid, user_display_name, user_screen_name, user_reported_location, user_profile_description, user_profile_url, follower_count, following_count, **account_creation_date**, **account_language**, tweet_language, tweet_text, **tweet_time**, tweet_client_name, in_reply_to_userid, quoted_tweet_tweetid, is_retweet, retweet_userid, latitude/longitude, quote_count, reply_count, like_count, retweet_count, **hashtags**, **urls**, user_mentions, poll_choices. Ces champs ont servi de référence de facto à la littérature académique (voir axe académique).
- 2023 : abandon du format antérieur de transparence (E4) ; TMRC inactif [non vérifié]. Janv. 2024 : sauvegarde Internet Archive des archives IO « en raison du manque de transparence de X » (E6).
- 2024-2025 : *Global Transparency Report* H1 2024 (25 sept. 2024) : 464 M comptes suspendus pour « spam et manipulation de plateforme » ; H2 2024 : 335 M, « réduction de 28 % » (extraits E5). Aucune divulgation de réseaux étatiques, aucune donnée exploitable pour la recherche.
- Bastos (2025, S1) exploite les identités visuelles des archives TMRC ; arXiv 2305.05907 (S2) exploite les archives pour montrer une coordination inter-États.

### B.6 TikTok — Covert Influence Operations Reports

Rapport dédié créé le 23 mai 2024 (F2), mensuel, remplaçant les divulgations trimestrielles du Community Guidelines Enforcement Report. En 2024 : >50 opérations perturbées ; réseaux chinois de 350 et 16 comptes (extraits). Champs publiés par réseau [extraits + connaissance antérieure, non vérifié pour l'exhaustivité] : **pays source**, **nombre de comptes**, **audience cumulée (followers)**, **pays/public ciblé**, **description du comportement** (ex. « réseau de 65 comptes, 116 612 followers, amplifiant des narratifs pro-iraniens au US/UK »), et **comptes récidivistes** supprimés chaque mois (« attempting to re-establish their presence »). TikTok ne publie pas de signaux techniques ; la définition repose sur la coordination + la dissimulation de l'origine. Le 6e rapport Code de bonnes pratiques UE (F3) mentionne les élections de Croatie, Allemagne, Pologne, Portugal, Roumanie (S1 2025).

### B.7 Graphika

**Méthode générale (G5, extraits).** Cartographie de réseaux (plateforme ATLAS, « AI World Model ») : les relations structurelles entre comptes (abonnements, interactions) sont transformées en cartes puis **segmentées par affinité** via plusieurs modèles : **clustering relationnel** (quand le réseau se décompose en sous-ensembles presque disjoints), **plongements de graphes hétérogènes** combinés à des **plongements de langue** (utilisateurs + contenus), **HDBSCAN** (clustering hiérarchique par densité) pour identifier des groupes d'utilisateurs et leurs relations. La priorisation ne repose pas sur des seuils de volume ou de mots-clés mais sur le clustering, la **dynamique d'amplification**, la **continuité trans-plateforme**. Les rapports complets contiennent cartes de réseau, « raw attribution indicators », topologie multi-plateforme et indicateurs d'attribution avec **scores de confiance** (extrait).

**Indicateurs d'inauthenticité mobilisés (G2, « The #Americans », 3 sept. 2024, extraits).** Photo de profil probablement **générée par IA** (persona « Harlan ») ; **incohérences biographiques** (New-Yorkais vétéran → Floridien de 31 ans) ; **publication de vidéos identiques ou quasi identiques par plusieurs personas à quelques heures d'intervalle** (co-posting) ; **absence de traction** dans les communautés authentiques (métrique d'impact) ; comportement de « seeding and amplifying ». Spamouflage y est identifié via 15 comptes X + 1 TikTok.

**G1 « Spamouflage Breakout »** [date non vérifiée] : montre l'obtention d'engagement hors du réseau ; **G3 « Cheap Tricks »** (nov. 2025) : 9 opérations (CopyCop, Doppelganger, Spamouflage, Falsos Amigos, Overload, Undercut, pro-Inde) ayant délégué création de contenu et de personas à l'IA ; artefacts relevés : présentateurs synthétiques non convaincants, traductions maladroites, **prompts IA oubliés dans les titres** de faux sites (extraits). **G4 « (Don't) Blame it on the Bots »** : mise en garde contre l'inférence « bot » à partir de signaux faibles (handles numériques, création récente) — l'inauthenticité est une question de **coordination et de dissimulation**, non d'automatisation [formulation d'après l'extrait, non vérifiée].

### B.8 EU DisinfoLab (+ Qurium) — Doppelganger, 27 septembre 2022

Opération « Doppelganger » active depuis au moins mai 2022 : clones d'au moins 17 médias (Bild, 20minutes, Ansa, The Guardian, RBC Ukraine, puis Le Monde, Der Spiegel, Fox News…) via **noms de domaine typosquattés** et copie des maquettes (extraits H1). **Outils / données** (extrait) : **Meta Ads Library**, **CrowdTangle**, et données publiques d'**infrastructure Internet**. Infrastructure (H1/H3) : premiers faux sites enregistrés en juillet 2022 ; **Cloudflare** pour masquer le serveur ; **TLD exotiques** (.ltd, .fun, .ws, .today, .cfd, .asia, .vip) ; logiciel **Keitaro** (TDS, société enregistrée en Estonie) pour gérer les redirections ; publicité Facebook et comptes d'amplification sur Facebook et Twitter ; formats vidéos, sondages, articles. **Indicateurs d'infrastructure** ainsi fixés pour toute la littérature ultérieure : domaine sosie + TLD rare + CDN masquant + redirections multi-sauts + pages Facebook jetables + achats publicitaires.

### B.9 Auswärtiges Amt / Sekoia / Science Feedback — Doppelganger côté X

- **Rapport technique allemand (5 juin 2024, H4, extraits)** : réseau X de « centaines de milliers » de comptes inauthentiques, répondant aux vrais utilisateurs **plusieurs fois par seconde** ou utilisant une **combinaison de hashtags tendance** en Allemagne pour obtenir une portée organique ; deux rôles : **« Posters »** (publient les liens) et **« Followers »** (amplifient) ; chaîne de redirection **FI-KE-D** (définie par Qurium) ; **les URL changent chaque jour mais les IP de destination restent identiques** : l'indicateur robuste est « URL différentes → même IP, postées en succession rapide » ; usage de LLM pour articles et posts.
- **Sekoia « Master of Puppets »** (H5) : analyse d'infrastructure (domaines, hébergeurs) [détail non vérifié].
- **Science Feedback** (R1) : expérimentation de **signalement** de contenus Doppelganger à X et mesure du taux de traitement ; **Alliance4Europe « Fool Me Once » (sept. 2024)** et rapport de déc. 2024 (K1-K2) : persistance de l'opération malgré sanctions ; méthode : collecte de posts, suivi des domaines et de la **réponse des plateformes**.

### B.10 Antibot4Navalny — OSINT bénévole sur X

Collectif anonyme actif depuis novembre 2023 (extrait N1). Ordres de grandeur (N2, mars 2024) : ~75 000 comptes/mois, ~600 domaines, jusqu'à 5 M vues en une nuit. **Caractéristiques de compte utilisées comme indicateurs** (extraits N1-N2) :
- **Motif de handle** : nom suivi de **4 à 6 chiffres aléatoires** ; prénom souvent **incohérent avec la langue** de publication ;
- **Alphabétisation des prénoms par cible** : bots « US » à prénoms en D, « France » en J, « Allemagne » en R ;
- **Deux rôles** : « Posters » (partagent les articles) et « Followers » (amplifient ; suivent typiquement **≥3 comptes vérifiés**, souvent sport/musique, pour paraître normaux) ;
- **Cadence** : adaptation du rythme de publication par pays pour éviter la détection (moins de tweets par unité de temps dans l'UE après constat que les bots anglophones rapides étaient suspendus plus vite) — l'opérateur **teste** les systèmes anti-abus ;
- **Domaines** : suivi des redirections vers les clones ; **migration** vers Bluesky observée en janvier 2025 (N3).
Méthode : collecte manuelle/semi-automatisée via l'interface X, requêtes sur les liens, documentation en fils X ; publication de listes de comptes/domaines partagées avec journalistes (Le Monde, Correctiv, etc.) [non vérifié pour le détail des partages].

### B.11 Check First + Reset Tech — Operation Overload (alias « Matriochka » chez VIGINUM)

- **Rapport 1 (juin 2024, I1, extraits)** : collaboration avec >20 médias ; corpus de **>200 courriels** reçus par les rédactions ; >800 organisations ciblées via un réseau de faux comptes X « présentant des marqueurs clairs de CIB » ; mécanisme : *content amalgamation* (contenu fabriqué + QR codes + logos volés) poussé par courriel et par @-mentions pour saturer les fact-checkers.
- **Rapport 2 (juin 2025, I2, extraits)** : >700 courriels collectés depuis sept. 2024 + contenus diffusés sur **Telegram, X, Bluesky, TikTok** ; généralisation de l'**IA** (voix clonées, visuels).
- **Indicateurs (I1-I2 + J1)** : **dates de création de comptes**, **voix off générées par IA**, **logos volés** de médias/universités, **QR codes** intégrés aux images, **interactions avec des réseaux de bots** (co-amplification), **texte identique** dans les courriels et les posts, **ciblage par @-mention** des mêmes vérificateurs, **synchronisation** courriel/publication. ISD (J1, T2 2025) retrouve ~300 comptes sur X/Bluesky/TikTok « en recherchant le contenu lié aux narratifs fréquemment ciblés par les IO russes », puis attribue par dates de création, voix IA, logos volés, QR codes, interactions bots ; évaluation d'impact par **vues/likes** (« underwhelming influence »).

### B.12 ISD — Beam / Method52 et dispatches

Beam (lancé 14 nov. 2022 avec CASM Technology) repose sur **Method52**, environnement de « pipelines » (architectures de composants) de collecte et d'analyse NLP/ML. Pour la CIB, CASM déploie la **détection de communautés** pour repérer botnets et sockpuppets par **« motifs de réplication non naturels »** (extraits J3). Les dispatches ISD (J1, J2) montrent la pratique : recherche par mots-clés narratifs → constitution d'un corpus de comptes → qualification par indicateurs de compte et de média → mesure d'engagement.

### B.13 Alliance4Europe (Counter Disinformation Network)

Rapports électoraux 2024-2026 (K1-K7). Méthodes observables dans les extraits : suivi **multi-plateforme** (Odnoklassniki, TikTok, Telegram, Facebook, Instagram) d'un réseau CIB promouvant un **bot Telegram** (Moldavie, Shor) ; identification de **fermes à trolls** par Trollrensics (partenaire) pour la Hongrie 2026, avec notion d'**« infrastructure persistante »** réutilisée **trans-frontière** (titre K6) ; évaluation de l'**efficacité des réponses** (plateformes, autorités) ; cadre « DISRUPT ». Indicateurs probables [non vérifié] : création de comptes en lots, photos de profil réutilisées, texte identique multi-langues, synchronie.

### B.14 Clemson Media Forensics Hub (Linvill & Warren) — Storm-1516

Première identification publique de la campagne en décembre 2023 (extrait L2) ; active depuis au moins août 2023. Rapports : *Writers of the Storm* (L1) et *Hungary for more?* (10 avril 2026, L2). Éléments de méthode (extraits) : traçage de la **chaîne de blanchiment** (vidéo d'un faux témoin → site d'un **faux média** → relais par **influenceurs rémunérés** → reprise) ; identification d'un **réseau de comptes commerciaux de marketing liés à l'Afrique** ; comptes influenceurs « probablement rémunérés » ; analyse des **narratifs** et des « engagement tactics ». La CNN (30 oct. 2024) relaie leurs travaux sur les vidéos Harris-Walz. Indicateurs mis en avant par Clemson [connaissance antérieure, non vérifié] : réutilisation du même acteur/voix dans plusieurs vidéos, sites créés peu avant la publication, premiers relais sur des comptes pro-russes identifiés, reprise par le « John Mark Dougan network ». Le **rapport technique VIGINUM (7 mai 2025, L4)** formalise la mécanique Storm-1516 (TLP:CLEAR).

### B.15 Recorded Future / Insikt Group — CopyCop

- 9 mai 2024 (M1) : réseau de sites inauthentiques utilisant des LLM pour **plagier et réécrire** des articles (Fox News, Al Jazeera, La Croix, TV5Monde, médias russes) avec biais partisan.
- juin 2024 (M2) : **120 sites enregistrés en 48 h (10-12 mai 2024)** ; >1 000 **personas de faux journalistes** ; **délai <24 h** entre l'article source et sa réécriture publiée.
- 2025 (M3) : ≥200 nouveaux sites depuis mars 2025 (US, France, Canada) ; sites imitant des **marques médias et partis politiques**.
**Indicateurs (extraits + connaissance antérieure [non vérifié])** : **date d'enregistrement groupée** des domaines, **registrar/DNS/hébergeur partagés**, **thèmes WordPress et plugins identiques**, **artefacts de prompts LLM** laissés dans les articles (« As an AI language model… », consignes de ton), **cadence de publication automatique**, **personas** à photos IA, réseau de **liens croisés** entre sites, lien avec John Mark Dougan (ex-policier de Floride) via l'infrastructure.

### B.16 Stanford Internet Observatory — analyses de takedowns (2019-2023)

Travail sur jeux de données partagés par Twitter (juin 2020 : Chine, Russie, Turquie ; oct. 2020 : Cuba, IRA, Arabie saoudite, Thaïlande — 526 comptes cubains, 4 802 243 tweets) et par Meta (ex. 13 juin 2022) (extraits O1-O2). Méthode : « open-source investigation and analysis of datasets shared by the platforms » ; usage d'outils de graphe (Social Links) pour relier groupes, pages et profils (extrait). **Champs typiques exploités dans les white papers SIO** [connaissance antérieure, non vérifié] : distribution des **dates de création** (créations en rafale), **heure de la journée** des publications (fuseau horaire de l'opérateur), **langues** déclarées vs utilisées, **hashtags** dominants, **réseaux de retweets et de mentions** internes au réseau, **nombre de followers** (majoritairement faibles), **profils** (photos volées/GAN, bios copiées), **domaines** liés. Rapports conjoints avec Graphika (G6, G7). Le SIO a cessé ses activités en 2024 [non vérifié].

### B.17 DFRLab (Atlantic Council)

Doctrine : recherche en **sources ouvertes exclusivement**, « transparente, vérifiée, réplicable » (extrait P1) ; analyses indépendantes de réseaux retirés par Facebook (Russie, Géorgie, Myanmar) ; traçage narratif (*Narrative Warfare*, fév. 2023, P2) ; formation G7 RRM (nov. 2025, P3). Méthodes typiques [connaissance antérieure, non vérifié] : recherche d'image inversée, analyse des **métadonnées de pages Facebook** (historique de renommage, pays des administrateurs via « Page Transparency »), **co-publication de liens**, chronologies de création, scraping de **Telegram** pour la remontée des narratifs, cartographie par Gephi/ForceAtlas2.

### B.18 Maldita.es — DANA de Valence (29 oct. 2024)

Rapport du 14 nov. 2024 (Q1) évaluant la réponse de TikTok, X, YouTube, Facebook, Instagram, WhatsApp, LinkedIn et Telegram à la crise de désinformation ; conclusion (extrait) : « aucune action pertinente et spécifique » des grandes plateformes. Méthode [extraits + connaissance antérieure, non vérifié pour les chiffres Maldita] : recension des **bulos** vérifiés, mesure des **vues** cumulées, part de **comptes vérifiés (badge payant X)** et **monétisés** parmi les diffuseurs, **temps de réponse** aux signalements, présence/absence d'étiquettes et de notes communautaires. Travaux académiques connexes (Q3) : 192 bulos / 185 notes de 4 vérificateurs (28 oct.–17 nov. 2024) ; 28 % des bulos originés ou diffusés depuis des environnements journalistiques professionnels (extrait). Ce cas illustre la **désinformation de crise** où la coordination est surtout **opportuniste/monétisée** plutôt qu'étatique.

### B.19 Global Affairs Canada (RRM) — Spamouflage 2024

Attribution d'une campagne de répression transnationale à Spamouflage à l'aide des « guides de recherche open source de Microsoft, Graphika et Mandiant » (extrait R2) : premier exemple public d'un **référentiel d'indicateurs partagé** entre État et industrie pour une même opération.

### B.20 Organisations non documentées dans cette session **[non vérifié — connaissance antérieure uniquement]**

- **Logically** (UK) : plateforme « Logically Intelligence » ; rapports sur réseaux pro-Kremlin et sur des opérations indiennes ; méthode mixte NLP + analystes ; indicateurs d'inauthenticité fondés sur co-posting et synchronie.
- **Bot Sentinel** (Christopher Bouzy) : scoring de comptes X (« normal / satisfactory / disruptive / problematic ») fondé sur un classifieur entraîné sur des comptes suspendus ; publications sur le harcèlement ciblé (ex. Meghan Markle, 2021).
- **Oxford Internet Institute — Computational Propaganda Project** (Howard, Bradshaw) : *Global Inventory of Organized Social Media Manipulation* (2017-2020) ; analyse des archives IRA pour le Sénat américain (2018) ; méthodes : codage de sources secondaires, analyse de contenu, co-occurrence de hashtags, « junk news » par domaine.
- **Cardiff University Crime & Security Research Institute (OSCAR)** : « Hostile Online Media Influence » ; détection de comptes russes sur des médias (commentaires) et sur des opérations « Secondary Infektion » ; indicateurs linguistiques (erreurs non natives), synchronie et réutilisation de contenus.
- **NewsGuard** : notation de fiabilité des sites ; suivi des « AI content farms » (UAIN) et des réseaux de faux sites (Dougan, Storm-1516) ; indicateurs de domaine (absence de mentions légales, auteurs fictifs, LLM artefacts).
- **Full Fact** : outils IA de fact-checking ; peu de travaux CIB stricto sensu.
Ces entrées devront être documentées et vérifiées dans une session ultérieure.

---

## (C) Synthèse — Catalogue des indicateurs d'inauthenticité et de coordination utilisés en pratique

Les indicateurs ci-dessous sont ceux que les rapports recensés déclarent mobiliser. Entre crochets : sources principales (identifiants du tableau A). Les indicateurs sont rarement décisifs isolément ; la pratique des enquêteurs consiste à **cumuler** des signaux de plusieurs niveaux puis à qualifier la **coordination** (synchronie, co-publication) et la **dissimulation** (fausse identité, infrastructure masquée).

### C.1 Niveau compte (identité, profil)
| Indicateur | Données requises | Utilisé par |
|---|---|---|
| Date de création récente ou **créations en rafale** (lots) | account_creation_date | A, I, J1, O, N |
| **Motif de handle** : prénom + 4-6 chiffres aléatoires ; prénoms alphabétisés par pays cible | screen_name | N1, N2 |
| **Incohérence langue/identité** (prénom vs langue des posts ; bio vs localisation) | display_name, bio, tweet_language | N, G2 |
| **Photo de profil GAN/IA** (artefacts : yeux alignés, arrière-plan flou, accessoires fondus) ou **photo volée** (recherche inversée) | image de profil | A5, C2 (Uncle Spam), G2, O |
| **Cohérence trans-plateforme** d'une persona (même photo/bio sur plusieurs sites) | profils multi-plateformes | A5, G5 |
| **Bios copiées / incohérences biographiques** dans le temps | bio, historique | G2 |
| Ratio **followers/following** faible ; followers majoritairement du même réseau | counts, graphe | O, N |
| **Suivi d'un petit nombre de comptes vérifiés** « neutres » (sport, musique) pour paraître normal | following list | N1 |
| **Comptes achetés / compromis / récidivistes** | historique de modération (plateforme) | A1-A4, F1 |
| **Opérateurs à louer** (agences marketing, freelances non informés) | attribution hors plateforme | A2, L2 |

### C.2 Niveau contenu (texte)
| Indicateur | Données | Utilisé par |
|---|---|---|
| **Texte identique / quasi identique** (copier-coller, variantes minimales) entre comptes | corpus de posts | G2, H4, I, O |
| **Traductions mécaniques** en 30+ langues du même message | langue, texte | B1, D |
| **Erreurs linguistiques non natives** ; **artefacts de prompts LLM** (« As an AI… », consignes résiduelles dans titres) | texte, titres de sites | G3, M, Cardiff [non vérifié] |
| Messages **contradictoires** sur un même sujet (stratégie de clivage) | texte | C2 (Uncle Spam) |
| **Commentaires d'engagement factices** autour de posts du même réseau | réponses/commentaires | C2 (Sneer Review) |
| **Hashtags tendance détournés** (combinaisons) | hashtags | H4 |
| **Narratifs** récurrents (Bucha, « failed state », sanctions) → base de recherche par mots-clés | texte | J1, L, P2 |

### C.3 Niveau temporalité
| Indicateur | Données | Utilisé par |
|---|---|---|
| **Co-publication dans une fenêtre courte** (minutes-heures) de mêmes URL/vidéos | timestamps, URL | G2, H4, I |
| **Cadence non humaine** (réponses plusieurs fois/seconde) ou **cadence calibrée** pour éviter la détection | timestamps | H4, N1 |
| **Heures d'activité** concentrées sur un fuseau horaire incompatible avec la localisation déclarée (semaine de travail Moscou/Pékin) | heure locale, bio | O, C [non vérifié] |
| **Délai source→copie <24 h** (réécriture automatisée) | date de publication des articles | M2 |
| **Enregistrement groupé de domaines** (120 en 48 h) | WHOIS/DNS creation date | M2, H1 |
| **Synchronie narrative inter-acteurs** (plusieurs opérations pivotant le même mois) | chronologie des narratifs | B4 |

### C.4 Niveau réseau (structure, interactions)
| Indicateur / méthode | Données | Utilisé par |
|---|---|---|
| **Rôles différenciés** « posters » vs « followers/amplifiers » | graphe de retweets/réponses/abonnements | H4, N1 |
| **Co-retweet / co-URL / co-hashtag** → projection en graphe de similarité et **clustering** | edges comptes-objets | O, G5, J3 (CASM) |
| **Détection de communautés** (clustering relationnel, HDBSCAN, plongements de graphes hétérogènes + texte) | graphe multi-plateforme | G5, J3 |
| **« Motifs de réplication non naturels »** (sockpuppets) | contenu + graphe | J3 |
| **Absence de traction** hors du cluster (faible engagement authentique, Breakout Scale) | métriques d'engagement, portée | G2, C, J1 |
| **Continuité trans-plateforme** (mêmes personas sur X/TikTok/Telegram/Bluesky) | identifiants, médias | G5, I2, N3 |
| **Réseau d'influenceurs rémunérés / comptes marketing** comme couche d'amplification | liens, paiements, bios | L2 |
| **Ciblage par @-mention** des mêmes fact-checkers/médias | mentions | I1 |

### C.5 Niveau média (images, vidéo, audio)
| Indicateur | Données | Utilisé par |
|---|---|---|
| **Images générées par IA** (incohérences physiques, textes illisibles) — ex. « weather weapon » Maui | fichiers image | B1 |
| **Vidéos « forgées »** : faux témoins/journalistes, acteurs réutilisés, **voix clonées** (Tom Cruise ; experts) | vidéo/audio | B2-B4, J2, L |
| **Présentateurs synthétiques** (CapCut) | vidéo | B1, G3 |
| **Logos volés** de médias/universités ; **QR codes** incrustés | image | I, J1 |
| **Réutilisation de la même image/vidéo** par plusieurs comptes (hash perceptuel) | pHash | G2, O [méthode implicite] |
| **Deepfake « AI-enhanced »** de personnalités (Harris) | vidéo | B4 |

### C.6 Niveau infrastructure (web, domaines, hébergement)
| Indicateur | Données | Utilisé par |
|---|---|---|
| **Domaines sosies / typosquattés** + **TLD rares** (.ltd .fun .ws .today .cfd .asia .vip) | WHOIS, DNS | H1 |
| **CDN masquant** (Cloudflare) ; **TDS/redirecteurs** (Keitaro) ; **chaîne FI-KE-D** | HTTP headers, redirections | H1, H3, H4 |
| **URL variables → même IP** de destination, postées en succession rapide | résolution DNS/IP, timestamps | H4 |
| **Registrar, hébergeur, thèmes CMS et plugins partagés** entre faux sites | fingerprinting web | M, G3 |
| **Faux médias créés juste avant publication** ; absence de mentions légales ; auteurs fictifs | WHOIS, pages « about » | L, M, NewsGuard [non vérifié] |
| **Publicités payées** (Meta Ads Library) et pages jetables | Ads Library, CrowdTangle (jusqu'en 2024) | H1 |
| **Comptes de messagerie** et campagnes de courriels de masse vers rédactions | corpus d'e-mails | I1-I2 |
| **Bot Telegram** comme point de ralliement d'un réseau CIB multi-plateforme | liens Telegram | K4 |

### C.7 Enseignements transversaux
1. **Asymétrie de données** : les plateformes (Meta, Google, TikTok, OpenAI) publient des *bilans d'action* (volumes, origine, cible) sans signaux techniques ; les enquêteurs externes compensent par des indicateurs **observables** (profil, texte, temporalité, infrastructure). X est passé d'un modèle d'archives ouvertes (2018-2021, champs riches) à l'opacité (2023-2025).
2. **Convergence des indicateurs** : trois familles reviennent dans presque tous les rapports — (i) persona inauthentique (photo IA/volée, handle aléatoire, bio incohérente), (ii) **co-publication synchrone** de mêmes objets (URL, vidéo, texte), (iii) **infrastructure partagée** (IP, hébergeur, TDS, CMS).
3. **Déplacement vers le média et l'infrastructure** : depuis 2023, l'IA générative banalise les personas et les textes ; les indicateurs les plus robustes deviennent **infrastructurels** (IP/TDS/registrars) et **comportementaux** (rôles posters/followers, cadence), les artefacts IA restant des signaux utiles mais transitoires (« AI slop »).
4. **Mesure d'impact systématique** : Graphika, OpenAI, ISD, Check First concluent presque toujours à un faible engagement authentique ; la Breakout Scale et les ratios vues/likes servent à relativiser.
5. **Défi des opérations « à louer » et des relais rémunérés** (Afrique, influenceurs, marketing) : la frontière entre inauthenticité et sous-traitance brouille les indicateurs de compte et renforce l'importance du **traçage narratif** et de la **chaîne de blanchiment** (Clemson, MTAC, VIGINUM).

---

## Lacunes de cette revue à combler lors d'une prochaine session
- Vérification par chargement direct de toutes les URL (impossible ici : egress bloqué).
- Lecture des PDF primaires (Meta Q1 2025 ; MTAC East Asia et Election Reports ; OpenAI juin/oct. 2025 ; Overload 1 et 2 ; Clemson L1-L2 ; VIGINUM Storm-1516 ; CopyCop CTA-2024-0509) pour extraire les sections « Methodology » mot à mot.
- Documentation de Logically, Bot Sentinel, OII, Cardiff CSRI, NewsGuard, Science Feedback (au-delà de R1), Full Fact.
- Localisation du rapport primaire MTAC 2026 sur Storm-1516 (>1 000 vidéos) et du rapport OpenAI juin 2026.
