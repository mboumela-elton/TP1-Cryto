# TP - Crypto

## Exercice 2
J'ai fait mes observations sur l'intranet de l'ensea :
- Nom du sujet
<br>Pays FR
<br>État / Province Île-de-France
<br>Localité Cergy
<br>Organisation ECOLE NATIONALE SUP. DE <br>L'ELECTRONIQUE ET DE SES APPLICATIONS
<br>Nom courant intranet.ensea.fr 

- Nom de l’émetteur
<br>Pays GR
<br>Organisation Hellenic Academic and Research Institutions CA
<br>Nom courant GEANT TLS ECC 1 

- Validité
<br>Pas avant
<br>Tue, 26 Aug 2025 13:03:29 GMT
<br>Pas après
<br>Wed, 26 Aug 2026 13:03:29 GMT 

- Informations sur la clé publique
<br>Algorithme Elliptic Curve
<br> Taille de la clé 256
<br> Valeur publique
04:9B:56:73:E0:42:7B:92:9C:52:67:43:12:66:D8:0D:1D:21:27:5B:C7:4B:3A:79:52:77:4B:EA:DE:55:6F:77:C9:FC:D3:C9:C5:E5:B4:6F:2B:DC:C1:7A:46:4E:FC:A9:44:50:00:F7:BC:92:92:9F:DB:F9:B3:3E:C9:91:90:55:FF

- Algorithme de signature ECDSA with SHA-384

- empreinte numéEmpreintes numériques
SHA-256 11:F5:A6:09:E7:D7:87:28:F9:97:F7:C9:42:12:B8:24:96:A7:DD:F3:38:E5:29:9C:3D:6B:80:0F:E2:98:6B:98
SHA-1 96:9C:82:42:B4:BA:E4:23:AB:4D:89:36:45:33:40:99:47:82:EC:CE

- Une autorité de certification est un organisme intermédiaire entre l'émetteur et le recepteur qui va vérifier l'identité du demandeur et signer son certificat avec sa propre clé privée.
- Une Infrastructure à Clé Publique (PKI) gère la création, l'émission et la validation des certificats numériques, l'authentification des utilisateurs et des dispositifs, et la protection des communications via le chiffrement. Elle assure également le cycle de vie des certificats (renouvellement et révocation) et contribue à la conformité aux normes de sécurité, établissant une chaîne de confiance.

- Chaîne de Confiance :
<br>L’utilisateur génère une paire de clés (publique/privée).
<br>Il crée une demande de signature (CSR) contenant :
Sa clé publique.
Ses informations d’identité.
<br>Il soumet le CSR à la RA avec les justificatifs.
<br>La RA vérifie l’identité et transmet à la CA.
<br>La CA signe le certificat avec sa clé privée pCA.
<br>Le certificat signé est renvoyé à l’utilisateur.
<br>La clé privée reste toujours chez l’utilisateur (ou Key Escrow).

- Lorsqu'un certificat numérique est révoqué, il perd sa validité avant sa date d'expiration, ce qui peut entraîner des restrictions d'accès pour les utilisateurs et signaler un problème de sécurité.

Pour vérifier la révocation d'un certificat, deux méthodes sont couramment utilisées :

    Liste de Révocation de Certificats (CRL) : Une liste émise par l'autorité de certification (CA) contenant les certificats révoqués. L'utilisateur doit régulièrement télécharger cette liste pour vérifier un certificat.

    Protocole de Statut de Certificat en Ligne (OCSP) : Une méthode en temps réel permettant de vérifier instantanément l'état d'un certificat en envoyant une requête à un serveur OCSP.

    - Les extensions présents dans le certificat serve de description :
    Subject Alternative Name : indique les différents nom de domaine par lesquelles la page est accessible
    Key Usage : spécifie l'utilisation prévu du certificat
    Extended key : permet de savoir qui va l'utiliser en l'occurrence souvent le serveur et le client
    et il y a des ID comme Subject Key ID, Authority Key ID.

- comme son nom l'indique, un certificat auto signé est un certificat de clé publique qu'un utilisateur émet en son propre nom, par opposition à un certificat émis par une autorité de certification. Un tel certificat est facile à produire et ne coûte rien. Cependant, il ne fournit aucune valeur de confiance.

## Exercice 4

### 4.4.1
Un bloc Bitcoin est une unité fondamentale de la blockchain, comprenant plusieurs éléments clés.

#### 1. En-tête de Bloc
L'en-tête contient des informations essentielles :
- **Version** : Indique la version du logiciel.
- **Hash du bloc précédent** : Référence le bloc précédent, garantissant la continuité.
- **Merkle Root** : Représente l'ensemble des transactions via une structure Merkle.
- **Timestamp** : L'heure de création du bloc.
- **Difficulté** : Spécifie la difficulté du réseau pour miner le bloc.
- **Nonce** : Utilisé pour trouver un hash valide lors du minage.

#### 2. Transactions
Chaque bloc contient une liste de transactions valides, comprenant des entrées (références aux transactions précédentes) et des sorties (montants et adresses des destinataires).

#### 3. Taille du Bloc
La taille totale, limitée à 1 Mo, inclut toutes les transactions et métadonnées.

#### 4. Frais de Transfert
- Un bloc Bitcoin est une unité fondamentale de la blockchain, comprenant plusieurs éléments clés.

#### 1. En-tête de Bloc
L'en-tête contient des informations essentielles :
- **Version** : Indique la version du logiciel.
- **Hash du bloc précédent** : Référence le bloc précédent, garantissant la continuité.
- **Merkle Root** : Représente l'ensemble des transactions via une structure Merkle.
- **Timestamp** : L'heure de création du bloc.
- **Difficulté** : Spécifie la difficulté du réseau pour miner le bloc.
- **Nonce** : Utilisé pour trouver un hash valide lors du minage avec pour but de garantir l'unicité du bloc.

#### 2. Transactions
Chaque bloc contient une liste de transactions valides, comprenant des entrées (références aux transactions précédentes) et des sorties (montants et adresses des destinataires).

#### 3. Taille du Bloc
La taille totale, limitée à 1 Mo, inclut toutes les transactions et métadonnées.

#### 4. Frais de Transfert
Les frais associés aux transactions sont versés aux mineurs pour leur validation.
Ces éléments garantissent la sécurité et l'intégrité de la blockchain Bitcoin.

### 4.4.2
La taille moyenne d’un bloc Bitcoin varie en fonction de l’activité du réseau et des transactions incluses. Voici les points clés :

Taille maximale théorique : 1 Mo pour le bloc de base (depuis le protocole original), mais avec SegWit et les optimisations, la taille effective peut atteindre environ 4 Mo en poids.
Taille moyenne actuelle : généralement entre 1,3 Mo et 2,5 Mo par bloc, selon la congestion du réseau et l’utilisation de SegWit.
Intervalle de création : un bloc est miné en moyenne toutes les 10 minutes.

### 4.4.3
Étapes de la création d’un nouveau bloc
La création d’un bloc :

- la collecte des transactions en attente dans le mempool (La mempool est la “file d’attente” des transactions Bitcoin non confirmées. Chaque transaction validée par un nœud y reste temporairement jusqu’à ce qu’un mineur la sélectionne pour l’insérer dans un bloc.
). Ces transactions sont regroupées et vérifiées pour s’assurer qu’elles respectent les règles du protocole (signatures valides, absence de double dépense).
- Ensuite, le mineur construit l’en-tête du bloc, qui contient notamment le hash du bloc précédent, un horodatage, la racine de l’arbre de Merkle des transactions et le fameux nonce. Le mineur modifie ce nonce en permanence afin de trouver un hash qui respecte la difficulté imposée. Une fois ce hash valide trouvé, le bloc est considéré comme résolu et peut être diffusé au réseau.
- Les autres nœuds vérifient alors sa validité avant de l’ajouter à leur copie de la blockchain.

Le minage est le processus par lequel les mineurs utilisent leur puissance de calcul pour résoudre un problème cryptographique complexe. Concrètement, ils cherchent un hash de l’en-tête du bloc qui commence par un certain nombre de zéros, ce qui prouve qu’ils ont investi du travail (Proof-of-Work). Ce mécanisme joue plusieurs rôles essentiels : il permet de valider les transactions en les inscrivant dans un bloc, il sécurise le réseau en rendant les attaques extrêmement coûteuses, et il régule l’émission de nouveaux bitcoins en récompensant le mineur qui trouve le bloc. Sans minage, il n’y aurait ni consensus ni protection contre la falsification des données.

La difficulté est un paramètre qui détermine à quel point il est difficile de trouver un hash valide pour un bloc. Plus la difficulté est élevée, plus le nombre de calculs nécessaires augmente, ce qui demande davantage de puissance de calcul. Elle évolue automatiquement tous les 2016 blocs (environ toutes les deux semaines) afin de maintenir un temps moyen de 10 minutes par bloc. Si les mineurs deviennent plus nombreux ou plus puissants, la difficulté augmente pour compenser. À l’inverse, si la puissance totale du réseau diminue, la difficulté baisse. Ce mécanisme d’ajustement garantit la stabilité et la régularité de la blockchain.

À l’heure actuelle, au bloc numéro 924561, la difficulté du réseau Bitcoin impose que le hash d’un bloc valide commence par environ 19 zéros hexadécimaux en moyenne. Ce nombre de zéros est directement lié au niveau de difficulté : plus il y a de zéros requis, plus il est improbable de trouver un hash valide par hasard, et plus le travail de calcul est conséquent. Ce seuil évolue régulièrement en fonction de la puissance totale du réseau, mais au moment indiqué, la cible correspond à un hash avec ces 19 zéros initiaux, ce qui illustre bien la complexité croissante du minage.

**Réflexion sur la dérivation de la quantité maximale de bitcoins**

Le total maximum de bitcoins est de 21,000,000 BTC, ce qui découle d'une série géométrique. La première récompense est de 50 BTC par bloc. La formule de la somme infinie de cette série est :

\[
50 \times 210\,000 \times \sum_{n=0}^{\infty} \left( \frac{1}{2} \right)^n = 50 \times 210\,000 \times 2 = 21\,000\,000
\]

Je vais présenter les réponses sous forme numérotée avec des labels en gras pour plus de clarté.
## Récompenses et halving de Bitcoin

1. **Montant initial de la récompense (4.11):** 50 BTC par bloc.

2. **Particularité du bloc genesis, bloc #0 (4.12):** La récompense de 50 BTC du coinbase est techniquement spéciale et n’est pas dépensable; le bloc est “intégré en dur” et sert de point d’origine de la chaîne. Et bien évidemment il n'a pas de hash du block précédent.

3. **Message inscrit dans le bloc #0 (4.13):** “The Times 03/Jan/2009 Chancellor on brink of second bailout for banks”.

4. **Numéro du bloc du premier halving (4.14):** Bloc 210 000.

5. **Nouvelle récompense après le premier halving (4.15):** 25 BTC par bloc.

6. **Fréquence des halvings en blocs (4.16):** Tous les 210 000 blocs.

7. **Intervalle en années entre deux halvings (4.17):** Environ 4 ans.

8. **Nombre de halvings déjà survenus (4.18):** 4 (2012, 2016, 2020, 2024).

9. **Récompense actuelle par bloc (4.19):** 3,125 BTC.

10. **Année approximative du dernier bitcoin miné (4.20):** Vers 2140.

11. **Nombre total maximum de bitcoins (4.21):** 21 000 000 BTC.