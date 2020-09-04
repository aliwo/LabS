import os
from elasticsearch import Elasticsearch

option = {'hosts': [f'{"https" if os.environ.get("SY_STAGE") == "PRODUCTION" else "http"}://{os.environ.get("SY_ELASTIC_USER", "")}:{os.environ.get("SY_ELASTIC_PASSWORD", "")}@{os.environ.get("SY_ELASTIC_HOST")}:9200']}
if os.environ.get('SY_STAGE', '') == 'PRODUCTION':
    option['use_ssl'] = True
    option['ca_certs'] = os.environ.get('SY_ELASTIC_CA_PATH')

es = Elasticsearch(**option)

print(es.info())


es.get('sy-users')
