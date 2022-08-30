from pymongo import MongoClient
conn = MongoClient("mongodb+srv://med:MOHAMED1234@cluster0.1jqb7.mongodb.net/?retryWrites=true&w=majority")
print(conn.test)