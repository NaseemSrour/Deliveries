import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# For Firebase JS SDK v7.20.0 and later, measurementId is optional
firebaseConfig = {
  "apiKey": "AIzaSyBTLvRG8oknnaRlgr3CWeVlCpQdBAVZ-Zg",
  "authDomain": "take-me-45367.firebaseapp.com",
  "projectId": "take-me-45367",
  "storageBucket": "take-me-45367.appspot.com",
  "messagingSenderId": "495981408208",
  "appId": "1:495981408208:web:8d59bd6ad574e6530f93d5",
  "measurementId": "G-KNXP6CJVZ6"
}

# Use the environment variable GOOGLE_APPLICATION_CREDENTIALS, which contains my private key.
# This variable only applies to your current shell session, so if you open a new session, set the variable again.
firebase_admin.initialize_app()  # Uses the env var above.

db = firestore.client()


# Add data to database:
doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})

# Add another document in the 'users' collection, this time with a slight difference (the 'middlename' field).
doc_ref = db.collection(u'users').document(u'aturing')
doc_ref.set({
    u'first': u'Alan',
    u'middle': u'Mathison',
    u'last': u'Turing',
    u'born': 1912
})


# Read data:
users_ref = db.collection(u'users')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
