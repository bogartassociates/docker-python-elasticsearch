# Working With Python and Elasticsearch

* https://hub.docker.com/r/medined/bogart-python-elasticseach/
* https://github.com/bogartassociates/docker-python-elasticsearch
* http://click.pocoo.org/5/quickstart/

* https://elasticsearch-py.readthedocs.io/en/master/

## Using virtualenv

virtualenv venv
. venv/bin/activate
pip install --editable .
deactivate

## Python

es = Elasticsearch("elasticsearch")

## Elasticsearch

```
docker pull docker.elastic.co/elasticsearch/elasticsearch:5.3.0

docker run \
 --detach \
 --name elasticsearch \
 --rm=true \
 -p 9200:9200 \
 -e "http.host=0.0.0.0" \
 -e "transport.host=127.0.0.1" \
 -e "xpack.security.enabled=false" \
  docker.elastic.co/elasticsearch/elasticsearch:5.3.0
```

## Using Curl

### Insert

```
cat << EOF > data.json
{ "field" : "value" }
EOF

curl \
  -H "Content-Type: application/json" \
  -H "Cache-Control: no-cache" \
  -XPOST "http://elasticsearch:9200/indexname/typename/$(cat /proc/sys/kernel/random/uuid)" \
  -d @data.json
```

### List Indexes

```
curl -XGET http://elasticsearch:9200/_cat/indices?v
```

### Count Documents In Index

```
curl -sS -XGET http://elasticsearch:9200/indexname/_count | jq '.count'
```

### Query

```
curl -XGET http://elasticsearch:9200/_search
```
