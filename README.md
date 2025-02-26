# README pour le projet Sms_app

## Description

Sms_app est une application développée avec Kivy et KivyMD qui permet d'envoyer des messages SMS et WhatsApp via l'API Twilio. L'application offre une interface utilisateur simple pour saisir les informations nécessaires et envoyer des messages à plusieurs contacts.

## Fonctionnalités

- **Écran de connexion** : Saisissez votre numéro Twilio, votre SID de compte et votre token d'authentification.
- **Envoi de messages** : Envoyez des messages SMS ou WhatsApp à plusieurs contacts.
- **Sélection de contacts** : Chargez des contacts à partir d'un fichier VCF.
- **Interface utilisateur intuitive** : Utilisation de KivyMD pour une expérience utilisateur agréable.

## Prérequis

- Python 3.x
- Kivy
- KivyMD
- Plyer
- Twilio

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/votre-repo.git
   ```

2. Accédez au répertoire du projet :
   ```bash
   cd votre-repo
   ```

3. Installez les dépendances requises :
   ```bash
   pip install kivy kivymd plyer twilio
   ```

## Utilisation

1. Exécutez l'application :
   ```bash
   python main.py
   ```

2. Sur l'écran de connexion, entrez vos informations Twilio :
   - Numéro Twilio
   - SID de compte
   - Token d'authentification

3. Une fois connecté, vous pouvez :
   - Écrire votre message.
   - Sélectionner des contacts à partir d'un fichier VCF.
   - Envoyer le message via SMS ou WhatsApp.

## Code

Voici un aperçu du code principal de l'application :

```python
from kivymd.app import MDApp
from kivy.lang import Builder
from twilio.rest import Client

class Sms_app(MDApp):
    def build(self):
        # Code pour construire l'interface utilisateur
        pass

    def send_message(self):
        # Code pour envoyer un message SMS
        pass

    def send_whatsap(self):
        # Code pour envoyer un message WhatsApp
        pass
```

## Aide

Pour toute question ou problème, veuillez consulter le fichier `info.txt` pour des instructions d'utilisation supplémentaires ou contactez le développeur.

## License

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

---
