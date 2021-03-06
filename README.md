
# Toolkits for DiseaseOntology

## Installation
```bash
python3 -m pip install disease_ontology
```

## Sub Commands
![](https://suqingdong.github.io/disease_ontology/images/cmd.png)

### 1 `build`

> build/update the database

```bash
# examples

# build from website
disease_ontology build

# build from local file
disease_ontology build -o doid.obo
```

![](https://suqingdong.github.io/disease_ontology/images/build.png)

### 2 `version`

> show the version of database

```bash
# examples

disease_ontology version
```
![](https://suqingdong.github.io/disease_ontology/images/version.png)

### 3 `query`

> get the DOID from database

```bash
# examples

# default query
disease_ontology query "heart disease"

# query with limit and score_cutoff params
disease_ontology query "heart" -l 10 -s 90
```

![](https://suqingdong.github.io/disease_ontology/images/query-1.png)
![](https://suqingdong.github.io/disease_ontology/images/query-2.png)

## Disease Ontology
- [downloads](https://disease-ontology.org/downloads/)
- [releases](https://github.com/DiseaseOntology/HumanDiseaseOntology/tree/main/src/ontology/releases)
- [doid.obo](https://raw.githubusercontent.com/DiseaseOntology/HumanDiseaseOntology/main/src/ontology/doid.obo)
- [doid.owl](https://raw.githubusercontent.com/DiseaseOntology/HumanDiseaseOntology/main/src/ontology/doid.owl)
