from pymongo import MongoClient
# Establish connection to MongoDB
con = MongoClient('mongodb://localhost:27017')
# Select the database
db = con['crud']
# Select the collection
col = db['Intern']
# Optional: Print confirmation
print("connect")