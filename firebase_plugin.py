FIREBASE_CONFIG = {
    "apiKey": "<your-api-key>",
    "authDomain": "<project-id>.firebaseapp.com",
    "projectId": "<project-id>",
    "storageBucket": "<project-id>.appspot.com",
    "messagingSenderId": "<id>",
    "appId": "<id>"
}

def initialize_firebase():
    print("🔥 Firebase initialized with:")
    for key, val in FIREBASE_CONFIG.items():
        print(f"{key}: {val}")
