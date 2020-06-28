from elasticsearch import Elasticsearch


es = Elasticsearch(hosts=['192.168.219.53'])

print(es.info())