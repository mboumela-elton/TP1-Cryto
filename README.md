# TP - Crypto

## Exercice 1 : Découverte des fonctions de hachage (MD5 et  SHA-1)

MD5 :
- ENSEA | 0a5b32abdb2aaabb9f01d2b7d529aa3a
- eNSEA | 4725a60b2ce918046777d8dab211bd1a
- eNSeA | 848d38ed7319d081b15910d8875522f8
- EN5EA | 04ea3dc371590d20ee2870c845f76fb9

Lorem Ipsum : 00a0b62f6d780b2f751bef0bef712f8c

SHA-1 : 
- ENSEA | e0ccd5c03e1357c13eaa4f6236ea8cd7bfcee8da
- eNSEA | 3ec865b950694e14bf5a53754be2c3ec5bdb961e
- eNSeA | e75fe77bd5ac51bd29e8645de8f9dd857b894c8c
- EN5EA | 54ed4ee67fd5916f4709b2c28327deb9eec397ea

Lorem Ipsum : 252778f95c0fdad122def4bbca4eacf39cb0afc8

### 1.1 / Chaque modification entraine la génération d'un Hash différent : l'effet avalanche est vérifié

### 1.2 / On obtient un Hash de meme longueur. La résistance aux collision semble compromise.

### 1.3 / Pour SHA-1, on remarque que la modification de la fin du message ne modifie pas le Hash. Cela s'explique par la segmentation par bloc pour le hashage. En revanche pour MD5, j ne rencontre pas ce probleme. C'est l'effet avalanche. La résistance à la Seconde Préimage semble compromise.

### 1.4 / Aujourd'hui, il est facile de creer 2 fichiers différent qui seront hasher de la meme facon par SHA-1 ou MD5. Pour la protetion de mot de passe on utilisera alors SHA-2 SHA-3 ou d'autrse fonctions tel que Argon2.

### 1.5 / Le but de sel est d'ajouter une valeur aléatoire au mot de passe avant de la hasher. Cela permet de nulifier les tables de hashage précalculé et de rendre impossible l'identification de 2 utilisateurs ayant le meme mot de passe 
