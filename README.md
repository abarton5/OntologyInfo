# OntologyInfo
A simply project for querying Ontology info using the REST API

## Requirements
Requires:
-  Python 3
-  requests library (pip install requests)

## Running
Can be ran in a command line with a compatable python environment with

```
python GetOntologyInfo.py
```

### Running with Docker

A prebuilt docker image is availiable and can be ran with:

```
docker run bartona029/python_ontology:alpine
```

## Docker building

A docker image can be built from the docker file provided with the following command:

```
docker build -t <your tag> .
```

If you have a repository account this can be published with

```
docker push <your tag>
```

