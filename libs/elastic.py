import os
from elasticsearch import Elasticsearch

option = {'hosts': [os.environ.get('SY_ELASTIC_HOST')]}
if os.environ.get('SY_STAGE', '') == 'PRODUCTION':
    option['use_ssl'] = True
    option['ca_certs'] = os.environ.get('SY_ELASTIC_CA_PATH')

es = Elasticsearch(**option)

print('es 연결!')
print(es.info())
