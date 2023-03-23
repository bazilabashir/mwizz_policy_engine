import pymongo

class DBConnector:
    def __init__(self):
        connection_string = "mongodb://localhost:27017"
        client = pymongo.MongoClient(connection_string)
        self.db = client['mwizz_db']

    def db_insert(self,collection,data):
        print(data)
        self.db[collection].insert_one(data)
        print("inserted in DB")

    def db_find(self,collection,status = None):
        print("finding data !!!")
        res =[]
        if status:
            entries = self.db[collection].find({"status":"init"})
        else:
            entries= self.db[collection].find()
        for entry in entries:
            print(entry)
            res.append(entry)
        # res = self.db[collection].find_one({"policyID":"xyz123"})
        # res = self.db[collection].find({"Severity":"Critical"})
        

        # print(res)
        return res

    # def db_update_status(self,collection,data,status):
    #     value = {"$set":{"status":status}}
    #     self.db[collection].update_one({data,value})
    

    def db_delete_all(self,collection):
        self.db[collection].delete_many({})
