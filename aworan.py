from elasticsearch import Elasticsearch
import click
import json
import os

# connect-to-elasticsearch-host HOST and PORT
# list-indexes
# list-mapping-for-index INDEX-NAME
# display-records RECORD_COUNT
# define transformation function for field
# dry-run RECORD_COUNT
# copy SOURCE_INDEX to TARGET_INDEX using reindex

@click.group()
def cli():
    pass

@click.command()
def listIndexes():
    es = Elasticsearch(["elasticsearch"],
          sniff_on_start=True,
          sniff_on_connection_fail=True,
          sniffer_timeout=60,
          maxsize=10)
    for key in es.indices.get_alias("*"):
        click.echo(key)

cli.add_command(listIndexes)
