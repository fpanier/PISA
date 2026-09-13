# Coût-efficacité : convertir vingt-neuf listes de leviers en une seule hiérarchie

Les vingt-neuf sections précédentes chiffrent en livres par élève, en livres par école, en dollars par
participant, en pourcentage de budget, en euros par redoublement évité : ces unités ne s'additionnent pas.
Cette section construit une métrique unique — l'euro 2026 par élève et par an, aux prix de la Fédération
Wallonie-Bruxelles, rapporté au dixième d'écart-type attendu à l'échelle —, l'applique aux leviers du
corpus, et modèle le décalage entre l'économie du redoublement et la dépense qui doit la précéder.

---

## 1. Les trois métriques disponibles, et pourquoi aucune ne se transpose telle quelle

**Les années de scolarité ajustées (LAYS).** Angrist, Evans, Filmer, Glennerster, Rogers et Sabarwal
convertissent 150 évaluations d'impact conduites dans 46 pays en une unité commune — l'année de scolarité
d'un système très performant — rapportée à 100 dollars par enfant. Les trois approches les plus efficientes
— informer sur les bénéfices, coûts et qualité de l'éducation ; cibler l'enseignement sur le niveau réel de
l'enfant plutôt que sur sa classe d'âge ; la pédagogie structurée, c'est-à-dire séquences de leçons,
matériel lié, formation et suivi — délivrent environ trois LAYS pour 100 dollars, quand l'apport d'intrants
seuls n'en délivre presque rien (Angrist *et al.*, Banque mondiale / Center for Global Development, 2020 ;
version relue par les pairs, *Journal of Development Economics*, 2025). Niveau de preuve : synthèse d'essais
randomisés et d'évaluations quasi-expérimentales. Trois limites, énoncées par les auteurs : les données de
coût sont l'intrant le plus faible — 72 des 150 estimations seulement en disposent ; la conversion des
écarts-types en LAYS suppose des hypothèses sur la distribution des acquis ; « il serait imprudent de se
concentrer sur de petites différences de coût-efficacité ». Et tout le corpus porte sur des pays à revenu
faible et intermédiaire, où le contrefactuel est souvent l'absence d'enseignement effectif.

**Les *Smart Buys* du GEEAP.** Le panel réuni par le FCDO, la Banque mondiale, l'UNICEF et l'USAID classe
les interventions après examen de plus de 13 000 études et retenue de plus de 550 évaluations. Sont *Great
Buys* : l'information sur les bénéfices, coûts et qualité de l'éducation ; la pédagogie structurée ;
l'enseignement ciblé par niveau d'acquisition. Sont *Bad Buys* : le matériel informatique seul, et l'apport
d'intrants isolés — manuels, enseignants supplémentaires pour réduire la taille des classes, bâtiments,
dotations, salaires, bibliothèques (GEEAP, 2023). Le panel pondère en faveur des dispositifs éprouvés « à
l'échelle du système ou, au minimum, dans des centaines d'écoles », mais écrit que ses recommandations « ne
doivent pas être lues comme universellement applicables » et que sa base probante est « principalement »
celle des pays à revenu faible et intermédiaire. Transposer « salaires » à la FWB serait un contresens : la
ligne vise l'ajout d'intrants sans changement pédagogique, pas la rémunération.

**Les ratios du Washington State Institute for Public Policy.** Cette agence non partisane rapporte des
bénéfices actualisés sur la vie entière au coût de mise en œuvre, avec une analyse de Monte-Carlo à 10 000
tirages et des taux d'actualisation réels de 2 %, 3,5 % et 5 % (WSIPP, 2023). Elle applique surtout cinq
décotes multiplicatives aux tailles d'effet publiées ; pour le domaine K-12 : une étude conduite par le
concepteur du programme voit son effet multiplié par **0,43**, une étude à mesure de résultat faible par
**0,23**, une étude en conditions non réelles par **0,22**. Limite de transposition : les bénéfices sont
valorisés aux prix de l'État de Washington, dont la section 25 a montré que la part imputée à la criminalité
évitée est sans commune mesure avec la Belgique — et le ratio de 246 pour 1 affiché pour le tutorat par les
pairs (26 714 dollars de bénéfices pour 109 dollars de coût, revue de mars 2020) rappelle que, quand le
dénominateur est quasi nul, le ratio explose sans que l'information gagne en fiabilité.

---

## 2. La métrique retenue, et la décote d'échelle

La métrique est : **euro 2026 par élève et par an, recalculé aux prix FWB, divisé par le dixième
d'écart-type attendu à l'échelle.** Trois règles la construisent.

*Les coûts se recalculent, ils ne se convertissent pas.* La méthode des ingrédients — dénombrer les
ressources nécessaires puis les valoriser au prix de marché du décideur concerné — est le standard du champ
(Levin *et al.*, 2018), reprise par l'EEF : coûts additionnels par rapport à la pratique ordinaire, répartis
entre prérequis, démarrage et récurrent, amortis sur trois ans (*Cost Evaluation Guidance*, 2023). Les
montants publiés en livres ou en dollars sont convertis au taux de référence de la Banque centrale
européenne du 11 septembre 2026 (1 £ = 1,1653 € ; 1 $ = 0,8627 €) **sans réindexation** : ce sont des
planchers.

*L'effet à retenir est celui de l'échelle, pas celui du pilote.* Trois corpus en fixent l'ampleur. Kraft et
Blazar établissent que les programmes de coaching de plus de cent enseignants ne produisent qu'« un tiers à
la moitié » des effets des plus petits (*Education Next*, 2018). Kraft montre sur 1 942 tailles d'effet
issues de 747 essais randomisés que la médiane des études de plus de 2 000 élèves est de 0,03 écart-type
contre 0,24 pour celles de moins de 100 (*Educational Researcher*, 2020). Kraft, Schueler et Falken donnent
la mesure la plus directe : sur 265 essais randomisés de tutorat, l'effet groupé passe de **0,55**
écart-type pour les programmes servant moins de 100 élèves à **0,32** entre 100 et 399, **0,25** entre 400
et 999, et **0,14** au-delà de 1 000 — décroissance quasi linéaire, estimation de référence à l'échelle de
0,16 à 0,21 (EdWorkingPaper 24-1031, 2024). **Règle appliquée ici : un effet mesuré sur moins de cent
enseignants, moins de mille élèves, ou par les concepteurs du dispositif est multiplié par 0,4 ; un effet
déjà mesuré sur plus de cent écoles en conditions réelles est conservé tel quel.**

*Les coûts se ventilent en trois natures, et le temps enseignant se valorise.* Non récurrents (écriture de
référentiels, agrément de ressources, validation d'un outil de dépistage) ; récurrents en biens et services
(licences, épreuves, matériel) ; récurrents en personnel — l'essentiel, puisque coaching et tutorat sont du
face-à-face « sans économies d'échelle » (Kraft & Blazar, 2018). L'EEF en fait son principe 4 : exclure le
temps de préparation, de formation et de remplacement « rend les programmes artificiellement bon marché ».

---

## 3. Le taux de change de référence : ce que coûte un dixième d'écart-type acheté au prix courant

Que produit un euro dépensé sans intention particulière ? Jackson et Mackevicius agrègent toutes les études
américaines à identification causale crédible du lien entre dépense et résultats — 31, dont 28 rapportent un
effet positif. Une hausse de 1 000 dollars par élève et par an, maintenue quatre ans, élève les scores de
**0,0316 écart-type** et l'accès au supérieur de 2,8 points de pourcentage ; une telle politique améliore
les résultats ou le parcours « plus de 90 % du temps », et les auteurs ne détectent pas de rendement
décroissant aux niveaux de dépense observés (*American Economic Journal: Applied Economics*, 2024 ; NBER
Working Paper 28517, 2021). Niveau de preuve : méta-analyse d'évaluations quasi-expérimentales.

Traduit dans notre métrique : **0,1 écart-type coûte 12 658 dollars cumulés par élève, soit 2 730 euros par
élève et par an pendant quatre ans.** C'est le prix de la dépense indifférenciée : tout levier très en
dessous bat l'option « dépenser davantage », et toute promesse d'un ratio de quelques euros doit être
regardée avec suspicion.

---

## 4. La table

Coûts recalculés aux prix FWB, dépenses unitaires 2023-2024 des *Indicateurs de l'enseignement 2025* (5 548
€ par élève en maternel, 6 163 € en primaire, 9 557 € en secondaire ordinaire).

| Levier | Coût publié (monnaie, année) | Coût, € 2026 par élève et par an | Effet publié | Effet retenu à l'échelle | € par 0,1 ET | Niveau de preuve |
|---|---|---|---|---|---|---|
| Dépistage + littératie précoce, Mississippi | 112 $/élève de M à 3e/an (2017) | 97 € | 0,14-0,18 ET | 0,14-0,18 (déjà 134 376 élèves) | **54-69 €** | quasi-expérimental, deux devis |
| Observation-rétroaction structurée par la direction, Houston | 9,26 $/élève/an, coût marginal (2017) | 8 € *hors* infrastructure d'évaluation | +0,10 an 1, nul an 2 | 0,05 | **16 €** | essai randomisé, 58 écoles, un district |
| Évaluation formative embarquée, Angleterre | 1,20 £/élève/an (2018) | 1,40 € hors temps ; **226 €** si le temps est libéré | +0,10 ET (p = 0,09) | 0,09-0,10 | **1 € à 250 €** | essai randomisé, 140 écoles, 25 393 élèves |
| Coaching individualisé | 3 700 $/enseignant (2011) | 3 192 €/enseignant, soit 250 €/élève au fondamental | +0,18 ET | 0,06-0,09 | **277-416 €** | méta-analyse de 60 devis causaux |
| *Mathematics Mastery* | 131 £/élève/an au primaire (2015) | 153 € | +0,073 ET groupé, non significatif isolément | 0,073 | **209 €** | deux essais randomisés, 127 écoles |
| Tutorat à dose crédible | 907 $/élève tutoré/an (2021, prospectif) | 782 € | 0,288 ET | 0,16-0,21 | **373-489 €** | 265 essais randomisés |
| *Dépense supplémentaire indifférenciée* (repère) | 1 000 $/élève/an, 4 ans (2024) | 863 € | 0,0316 ET | 0,0316 | **2 730 €** | méta-analyse, 31 études causales |
| Pôles de mathématiques (*Maths Hubs*) | 2,7 £/élève/an (2024) | 3,15 € ; 2,8 M€ pour 900 000 élèves | aucune estimation causale | — | **indéfini** | description non évaluée |
| *Lesson study* | 53,78 £/élève/an (2017) | 63 € | +0,02 puis +0,03, IC incluant zéro | 0 | **indéfini** | essai randomisé, 181 écoles, sécurité maximale |
| ICCAMS (évaluation formative en mathématiques) | 15 £/élève/an (2021) | 17,5 € | g = +0,04, non significatif | 0 | **indéfini** | essai randomisé, 18 052 élèves |
| *Check & Connect* | 1 955 $/élève/an (2018) | 1 687 € ; 152 M€ pour 10 % des élèves | nul sur les acquis | 0 | **indéfini** | essai randomisé, Chicago |

**« Indéfini » n'est pas « mauvais », c'est pire :** on ne divise pas par zéro, et la dépense a eu lieu —
les 63 euros par élève du *lesson study* ont été engagés dans 181 écoles pendant deux ans pour zéro mois de
progrès, mise en œuvre jugée conforme. **Un coût faible ne fait pas un bon ratio :** ICCAMS coûte 17,5 euros
et ne produit rien parce que la chaîne casse à la diffusion — 55 % des enseignants référents ont délivré
moins de sessions que prévu, 13 % seulement ont tenu l'heure prescrite. **Le meilleur ratio documenté à
l'échelle d'un système entier est le dépistage adossé à une intervention de lecture financée**, à 54-69
euros par dixième d'écart-type : quarante fois mieux que la dépense indifférenciée.

Le deuxième meilleur ratio a un coût affiché trompeur. À Houston, 29 des 58 écoles publiques ont été tirées
au sort ; leurs directions ont reçu 300 heures de formation au management sur deux ans ; 270 évaluations
intermédiaires sans enjeu, fournies aussi aux témoins, alimentaient les entretiens individuels. Les
directions traitées ont observé et coaché leurs enseignants 0,55 fois de plus par mois, contre 0,04 chez les
témoins (Fryer, NBER, 2017). Les 9,26 dollars ne couvrent que la formation : l'infrastructure d'évaluation,
elle, n'existe pas en FWB et constitue la véritable dépense.

---

## 5. Le prix du temps enseignant, et pourquoi il change les classements

Les *Indicateurs de l'enseignement 2025* le chiffrent sans hypothèse externe. Les traitements payés
directement par la FWB représentent 7 649,0 millions d'euros pour 111 071,8 équivalents temps plein, soit
**68 865 euros par ETP et par an**, charges comprises ; la charge hebdomadaire est de 24 périodes de 50
minutes au primaire, 22 au secondaire. Il s'ensuit qu'**une période hebdomadaire libérée sur l'année coûte 2
869 euros par enseignant du fondamental et 3 130 euros au secondaire.** Rapporté aux 476 700 élèves du
fondamental ordinaire pour 37 282 ETP, soit 12,8 élèves par ETP, libérer une période hebdomadaire pour tous
coûte **224 euros par élève et par an, soit 107 millions d'euros** — 1 553 emplois.

Ce chiffre retourne un classement. L'essai *Embedding Formative Assessment* affiche 1,20 livre par élève et
par an, le coût le plus bas du corpus. Mais il consomme dix-huit ateliers mensuels de deux heures, soit
dix-huit heures par enseignant et par an, un peu plus d'une demi-période hebdomadaire. Valorisée au coût FWB
et rapportée aux 8,3 élèves par ETP du secondaire, cette ressource vaut **226 euros par élève et par an** :
cent-soixante fois le coût affiché. Tout dépend donc de la question « d'où vient l'heure ? ». Prise sur du
temps déjà disponible, elle ne coûte presque rien au budget ; libérée et remplacée, elle fait sortir le
dispositif de la catégorie « coût très faible ». C'est ce qui explique les échecs de la section 17 : deux
essais randomisés ont produit zéro parce que le temps qu'ils supposaient n'était pas financé.

---

## 6. Financer la transition : le redoublement est une dépense engagée, pas une trésorerie

La dernière estimation officielle du surcoût du redoublement en FWB porte sur 2011 : 51,3 millions d'euros
au primaire et 365,3 millions au secondaire hors CEFA, soit 10,9 % du budget de ces niveaux (Fédération
Wallonie-Bruxelles, 2013, citée par Baye, Chenu, Crahay, Lafontaine et Monseur, ULiège, 2014).
L'Administration générale de l'enseignement l'a réévalué à 43 et 344,5 millions pour 2020. Indexé sur la
hausse de la dépense par élève depuis 2020-2021 (+21 % au primaire, +18 % au secondaire), l'ordre de
grandeur actuel est d'environ **465 millions d'euros par an** (calcul propre à cette note).

Ce montant n'est pas disponible : il correspond à des années-élèves consommées, financées par le
capital-périodes calculé sur les effectifs. Trois décalages séparent la décision de la trésorerie. Le
décalage de scolarité : un élève non retenu en deuxième secondaire quitte le système quatre à cinq ans après
la décision. Le décalage statutaire : **65,7 % des 111 072 ETP de la FWB occupent un poste à titre
définitif**, de sorte que la baisse des effectifs ne réduit les emplois que par attrition. Le décalage
politique, enfin, puisque l'économie prend la forme de postes retirés à des écoles.

Un modèle simple en fixe l'ampleur. Hypothèses posées, non prédictives : remplacement à 50 millions d'euros
par an dès la première année (tutorat pour 5 % des élèves, 35 millions ; dépistage langagier ; concertation)
; division par deux du surcoût en dix ans ; économie nulle les deux premières années, puis montée linéaire.

| Fin d'année | 2 | 4 | 5 | 7 | 12 |
|---|---|---|---|---|---|
| Solde annuel (M€) | −50 | −3,5 | +20 | +66 | +182 |
| Cumul (M€) | −100 | **−130** | −110 | −1 | +679 |

**Le point bas est de 130 millions d'euros cumulés à la fin de la quatrième année ; l'équilibre annuel est
atteint la cinquième, l'avance remboursée la septième.** Non une économie sèche, donc, mais un
investissement à quatre ans de trésorerie négative — le présenter autrement garantit l'abandon au premier
conclave budgétaire. Et réduire le redoublement ne produit pas, en soi, d'apprentissages : la revue
européenne la plus récente lui attribue d = −0,08 sur les acquis (section 24). C'est une source de
financement, pas un levier.

---

## Controverses et limites

**Les données de coût sont le maillon faible du champ.** Sur les quinze essais randomisés bien dimensionnés
de tutorat retenus dans la méta-analyse de 89 programmes de Nickow, Oreopoulos et Quan, **quatre seulement
documentent le coût de mise en œuvre** ; la proportion d'évaluations incluant un chiffrage est passée de 17
% de 541 évaluations à 30 % de 103 (Kohlmoos & Steinberg, Accelerate, 2025). Toute table de coût-efficacité
repose donc sur un échantillon non aléatoire de dispositifs dont les promoteurs ont accepté de publier le
prix. Les seuils usuels sont d'ailleurs conventionnels : ceux de Kraft — moins de 500 $ par élève = faible,
500 à 4 000 $ = modéré, au-delà = élevé, en dollars 2016 — reposent, l'auteur le dit, « sur un échantillon
de 68 interventions seulement » et ne sont « qu'un guide approximatif ».

**Le dénominateur n'est pas homogène, et le ratio ignore la distribution.** Un dixième d'écart-type sur une
épreuve conçue par l'équipe de recherche et un dixième sur un examen national externe ne valent pas la même
chose : Kraft mesure une médiane de 0,17 sur mesures étroites contre 0,10 sur mesures larges, et le WSIPP
applique une décote de 0,23 aux mesures faibles. Aucune conversion fiable n'existe entre écart-type
anglo-saxon et point PISA ; cette section s'en abstient comme les précédentes. Enfin, un dispositif qui
déplace la moyenne de 0,1 écart-type peut creuser l'écart social — Angleterre depuis 2019, Louisiane pendant
la réforme curriculaire (sections 1 et 10) : sur un système dont l'écart entre quartiles extrêmes atteint 92
points PISA, un classement par coût-efficacité moyen n'est pas un classement par équité. Le contrefactuel
diffère aussi : les ratios américains sur la petite enfance portent sur des enfants qui, non admis,
n'accédaient à aucun accueil éducatif, quand celui de la FWB est un enseignement maternel gratuit encadré
par des instituteurs diplômés (section 25).

**Une approche concurrente donne un autre classement.** La valeur marginale des fonds publics — disposition
à payer divisée par coût net pour l'État — appliquée à 133 politiques américaines place en tête les
investissements directs dans la santé et l'éducation des enfants pauvres, souvent au-delà de 5 (Hendren &
Sprung-Keyser, *Quarterly Journal of Economics*, 2020). Plus complète, mais elle exige des données
administratives longitudinales sur trente ans que la FWB n'a pas.

**Ce que je n'ai pas pu vérifier.** Trois éléments ont été écartés : le chiffre de « 400 millions, un peu
plus de 6 % du budget » qui circule dans la presse belge, dont le calcul d'origine reste introuvable ; une
version des seuils de coût de l'EEF plafonnant la catégorie « faible » à 170 £, contredite par le document
méthodologique de l'agence, qui indique environ 200 £ ; et l'existence d'une analyse coût-efficacité publiée
portant spécifiquement sur un dispositif scolaire de la FWB. L'estimation de l'AGE pour 2020, enfin, me
parvient par voie de presse et non par une publication administrative consultable.

---

## Ce que cela signifie pour la Fédération Wallonie-Bruxelles

**L'ordre de priorité budgétaire se déduit de la table, pas d'une préférence.** Trois leviers battent la
dépense indifférenciée d'un facteur dix à cinquante : le dépistage précoce adossé à une intervention de
lecture financée (54-69 € par dixième d'écart-type), l'observation-rétroaction conduite par la direction (16
€, sous réserve de l'infrastructure d'évaluation), l'évaluation formative embarquée si et seulement si son
temps est disponible. Trois autres, entre 200 et 500 €, restent défendables sur une population ciblée :
paquet curriculaire, coaching, tutorat. Quatre ne doivent pas être financés en l'état, non parce qu'ils
coûtent cher mais parce que leur dénominateur est nul : *lesson study*, diffusion en cascade non financée en
temps, mentorat de type *Check & Connect*, réduction de la taille des classes.

**Le premier arbitrage n'est pas un achat, c'est une infrastructure.** Le ratio de Houston suppose des
évaluations intermédiaires sans enjeu, communes, régulières et séparées de toute appréciation individuelle :
une dépense non récurrente de conception, une dépense récurrente de correction et de restitution
centralisées. C'est le seul investissement qui conditionne plusieurs autres leviers, et il est compatible
avec la liberté d'enseignement puisqu'il porte sur l'information produite, non sur la méthode.

**Le temps enseignant doit être budgété, ou le dispositif abandonné.** Une période hebdomadaire pour tous
les enseignants du fondamental coûte 107 millions d'euros ; un dispositif consommant dix-huit heures
annuelles par enseignant coûte, s'il faut le remplacer, plus de deux cents euros par élève. La FWB déclare
en TALIS 2018 un temps de travail total de 35,0 heures contre 41,5 en moyenne OCDE (section 7) : la marge
existe, mais elle suppose une renégociation de la composition du service, donc un accord syndical, non une
circulaire. Entre les deux — ne rien financer et espérer la bonne volonté — se trouve ce qui a produit zéro
dans les deux plus grands essais anglais.

**La gouvernance partagée change le coût, pas le classement.** La forme qui survit le mieux à un système à
réseaux multiples est le pôle disciplinaire à adhésion volontaire, animé par des enseignants détachés, sans
autorité hiérarchique : à 2,7 livres par élève et par an en Angleterre, l'équivalent coûterait 2,8 millions
d'euros par an pour 900 000 élèves. C'est le plus faible coût du dossier — et le seul dont l'effet n'ait
jamais été estimé causalement. À présenter comme tel : un pari organisationnel à faible coût et faible
risque, à évaluer par tirage au sort d'écoles volontaires *avant* généralisation.

**Le séquencement budgétaire doit être annoncé d'emblée.** Sous un déficit de 1,5 milliard d'euros et avec
l'enseignement à 54 % des dépenses, aucune de ces mesures ne se finance par de l'argent neuf : elle se
finance par la conversion progressive du surcoût du redoublement — environ 465 millions par an — en dépense
de remplacement, avec un creux de trésorerie de l'ordre de 130 millions cumulés sur quatre ans. Ce creux est
le vrai objet de la négociation politique. Le masquer, en présentant l'économie du redoublement comme
immédiatement disponible, est la manière la plus sûre de faire échouer la réforme à mi-parcours — le
scénario de la section 18, où le levier le plus équitable du dossier a été détruit par la suppression de sa
ligne budgétaire la plus modeste.

---

## Sources

- Angrist, N., Evans, D. K., Filmer, D., Glennerster, R., Rogers, F. H., Sabarwal, S. (2020). *How to Improve
  Education Outcomes Most Efficiently? A Comparison of 150 Interventions Using the New Learning-Adjusted Years
  of Schooling Metric* (Policy Research Working Paper 9450). Banque mondiale / Center for Global Development
  Working Paper 558.
  https://www.cgdev.org/sites/default/files/how-improve-education-outcomes-most-efficiently-comparison-150-interventions-using-new.pdf
- Angrist, N., Evans, D. K., Filmer, D., Glennerster, R., Rogers, F. H., Sabarwal, S. (2025). « How to improve
  education outcomes most efficiently? A review of the evidence using a unified metric ». *Journal of
  Development Economics*, 172. https://www.sciencedirect.com/science/article/pii/S0304387824001317
- Baye, A., Chenu, F., Crahay, M., Lafontaine, D., Monseur, C. (2014). *Le redoublement en Fédération
  Wallonie-Bruxelles*. Rapport d'expertise, Université de Liège, 13 mars 2014.
  https://orbi.uliege.be/bitstream/2268/165801/1/Le%20redoublement%20en%20FWB.pdf
- Banque centrale européenne (2026). *Euro foreign exchange reference rates*, 11 septembre 2026.
  https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html
- Education Endowment Foundation (2023). *Cost Evaluation Guidance for EEF Evaluations*, février 2023.
  https://d2tic4wvo1iusb.cloudfront.net/production/documents/evaluation/evaluation-design/Cost-Evaluation-Guidance-Feb_2023.pdf
- Fédération Wallonie-Bruxelles, ETNIC (2025). *Les indicateurs de l'enseignement 2025*, 20e édition (données
  2023-2024).
  https://www.enseignement.be/fileadmin/portail_age/uploads/Systeme_educatif/Chiffres-cles/Indicateurs/indicateurs-enseignement_2025.pdf
- Fryer, R. G. (2017). *Management and Student Achievement: Evidence from a Randomized Field Experiment*.
  NBER Working Paper 23437. https://www.nber.org/papers/w23437
- GEEAP — Akyeampong, K., Andrabi, T., Banerjee, A., Banerji, R., Dynarski, S., Glennerster, R.,
  Grantham-McGregor, S., Muralidharan, K., Piper, B., Ruto, S., Saavedra, J., Schmelkes, S., Yoshikawa, H.
  (2023). *2023 Cost-Effective Approaches to Improve Global Learning: What does recent evidence tell us are «
  Smart Buys » for improving learning in low- and middle-income countries?* FCDO, Banque mondiale, UNICEF,
  USAID.
  https://thedocs.worldbank.org/en/doc/231d98251cf326922518be0cbe306fdc-0200022023/related/GEEAP-Report-Smart-Buys-2023-final.pdf
- Hendren, N., Sprung-Keyser, B. (2020). « A Unified Welfare Analysis of Government Policies ». *The Quarterly
  Journal of Economics*, 135(3), 1209-1318. https://academic.oup.com/qje/article/135/3/1209/5781614
- Jackson, C. K., Mackevicius, C. L. (2024). « What Impacts Can We Expect from School Spending Policy?
  Evidence from Evaluations in the United States ». *American Economic Journal: Applied Economics*, 16(1),
  412-446. https://www.aeaweb.org/articles?id=10.1257/app.20220279
- Jackson, C. K., Mackevicius, C. (2021). *The Distribution of School Spending Impacts*. NBER Working Paper
  28517, révision juillet 2021. https://www.nber.org/system/files/working_papers/w28517/w28517.pdf
- Kohlmoos, L., Steinberg, M. P. (2025). *Conducting Cost Analysis of Tutoring Interventions: A Guide for
  Program Providers and Researchers*. Accelerate, février 2025.
  https://accelerate.us/wp-content/uploads/2025/02/Cost-Report_final.pdf
- Kraft, M. A. (2020). « Interpreting Effect Sizes of Education Interventions ». *Educational Researcher*,
  49(4), 241-253. https://journals.sagepub.com/doi/10.3102/0013189X20912798
- Kraft, M. A., Blazar, D. (2018). « Taking Teacher Coaching to Scale: Can Personalized Training Become
  Standard Practice? ». *Education Next*, 18(4).
  https://www.educationnext.org/taking-teacher-coaching-to-scale-can-personalized-training-become-standard-practice/
- Kraft, M. A., Blazar, D., Hogan, D. (2018). « The Effect of Teacher Coaching on Instruction and Achievement:
  A Meta-Analysis of the Causal Evidence ». *Review of Educational Research*, 88(4), 547-588.
  https://doi.org/10.3102/0034654318759268
- Kraft, M. A., Falken, G. T. (2021). *A Blueprint for Scaling Tutoring Across Public Schools*. Annenberg
  Institute at Brown University, EdWorkingPaper 20-335.
  https://edworkingpapers.com/sites/default/files/ai20-335.pdf
- Kraft, M. A., Schueler, B. E., Falken, G. T. (2024). *What Impacts Should We Expect from Tutoring at Scale?
  Exploring Meta-Analytic Generalizability*. EdWorkingPaper 24-1031, Annenberg Institute at Brown University.
  https://edworkingpapers.com/sites/default/files/ai24-1031.pdf
- L'Avenir (27 février 2022). « Redoublement : un surcoût d'environ 400 millions d'euros pour la FWB »
  (estimation de l'Administration générale de l'enseignement pour 2020).
  https://www.lavenir.net/actu/societe/2022/02/27/redoublement-un-surcout-denviron-400-millions-deuros-pour-la-fwb-V2XDDJCSHZED7JREVYROVRVZ4I/
- Levin, H. M., McEwan, P. J., Belfield, C., Bowden, A. B., Shand, R. (2018). *Economic Evaluation in
  Education: Cost-Effectiveness and Benefit-Cost Analysis*, 3e éd., SAGE. Méthode des ingrédients, citée comme
  standard de référence par l'EEF (2023) et par l'Institute of Education Sciences.
- Nickow, A., Oreopoulos, P., Quan, V. (2024). « The Promise of Tutoring for PreK-12 Learning: A Systematic
  Review and Meta-Analysis of the Experimental Evidence ». *American Educational Research Journal*, 61(1),
  74-107. https://doi.org/10.3102/00028312231208687
- OCDE (2025). *Education at a Glance 2025 — Country note: Belgium*. Temps d'instruction et durée des congés
  en Communauté française.
  https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/09/education-at-a-glance-2025-country-notes_9749f4ff/belgium_3d277682/0fbd3865-en.pdf
- Speckesser, S. *et al.* (2018). *Embedding Formative Assessment: Evaluation Report and Executive Summary*.
  NIESR pour l'Education Endowment Foundation.
  https://educationendowmentfoundation.org.uk/projects-and-evaluation/projects/embedding-formative-assessment
- UFAPEC (2021). *Redoublement : la Fédération Wallonie-Bruxelles toujours championne !*, analyse 07.21.
  https://www.ufapec.be/nos-analyses/0721-redoublement.html
- Washington State Institute for Public Policy (2023). *Overview of WSIPP's Benefit-Cost Model: A Brief Guide*.
  https://www.wsipp.wa.gov/TechnicalDocumentation/Overview%20of%20WSIPPs%20Benefit-Cost%20Model.pdf
- Washington State Institute for Public Policy (2023). *Benefit-Cost Technical Documentation*, décembre 2023
  (taux d'actualisation réels de 2 %, 3,5 % et 5 % ; facteurs d'ajustement multiplicatifs, exhibit 2.4.1).
  https://wsipp.wa.gov/TechnicalDocumentation/2023/WsippBenefitCostTechnicalDocumentation.pdf
- Washington State Institute for Public Policy. *Benefit-Cost Results: Pre-K to 12 Education*, consulté en
  2026. https://www.wsipp.wa.gov/BenefitCost?topicId=4
- CSC-ACV Enseignement. *Fonctions et charge dans l'enseignement obligatoire* (charge hebdomadaire : 26
  périodes en maternel, 24 en primaire, 22 pour les cours généraux du secondaire ; période de 50 minutes).
  https://www.lacsc.be/ma-carriere/travailler-dans-lenseignement/fonctions-charge/charge-travail-enseignement-obligatoire/obl-fonctions-charge-enseignant

Les tailles d'effet et les coûts publiés repris dans la table proviennent des sections 1, 7, 8, 9, 15, 16,
17, 19, 20, 22, 23, 24, 25 et 26 du présent rapport, où chacune porte sa source primaire. Cette section
n'introduit aucune taille d'effet nouvelle : elle les convertit, les décote et les rapporte à un coût.
