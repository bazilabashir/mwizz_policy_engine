from elasticsearch import Elasticsearch

class ESConnector:
    def __init__(self):
        self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
        print("Elastic Search is up and running !!")
        # health = es.cluster.health()
        # print("Elastic Search is up and running !!")
        # print(health)

    def insert_doc(self,doc):
        result = self.es.index(index='my_index', doc_type='_doc', body=doc)
        print(result)