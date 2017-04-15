#!/bin/bash

docker run \
  -it --rm \
  --link elasticsearch:elasticsearch \
  -v $PWD:/project \
  --workdir /project \
  medined/bogart-python-elasticsearch \
  /bin/bash
