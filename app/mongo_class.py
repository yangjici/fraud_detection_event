import pymongo

class intoMongo():
    '''a module to import json into a MongoDB database.
    '''
    def init_mongo_client():
        # Initiate Mongo client
        client = pymongo.MongoClient()

        # Access database created for these articles
        db = client

        # Access collection created for these articles
        coll = db.data

        # Access articles collection in db and return collection pointer.
        return db.data

    def writing(info):
        # Insert each doc into Mongo
        .insert(info)

    if __name__ == '__main__':

        # Initialize db & collection
        data = init_mongo_client()
