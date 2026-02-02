# garmin-data-lake
**Datalake Analítico com Garmin**

## Objetivo
Construir, na prática, um data lake analítico em arquitetura moderna, cobrindo todo o ciclo de dados — ingestão, transformação e disponibilização para análise — com foco em boas práticas de engenharia de dados.

O projeto utiliza dados do **Garmin Connect** para monitorar e analisar métricas pessoais (do próprio autor) de saúde e performance esportiva, com ênfase em atividades físicas (principalmente corrida) e correlação com dados de sono, frequência cardíaca e indicadores diários de saúde.

---

## Arquitetura & Stack
- **Cloud:** AWS  
  - Amazon S3 (Data Lake)  
  - Amazon Athena (Query Engine)
- **Orquestração:** Apache Airflow
- **Transformações:** Python e dbt
- **Arquitetura de dados:** Bronze / Silver / Gold
- **Visualização:** Metabase ou ferramenta equivalente
- **Versionamento:** GitHub

---

## Escopo
- Ingestão de dados a partir do Garmin Connect
- Persistência de dados brutos no Data Lake (camada Bronze)
- Tratamento, normalização e modelagem analítica (camadas Silver e Gold)
- Orquestração de pipelines com Airflow
- Disponibilização de métricas e dashboards analíticos

---

## Fase Atual do Projeto
Nesta primeira fase, a ingestão de dados é realizada **manualmente via exportação de arquivos CSV** do Garmin Connect.

Essa abordagem permite:
- Validar a arquitetura do data lake
- Definir contratos de dados e schemas
- Desenvolver pipelines de ingestão e transformação de forma incremental
- Reduzir acoplamento com a API durante a fase inicial

A ingestão automatizada via API do Garmin Connect está planejada para uma **fase posterior**, reaproveitando a mesma estrutura de dados e pipelines já estabelecidos.

---

## Estrutura do Projeto

```text
garmin-data-lake/
├── dags/                    # DAGs do Airflow
├── docs/                    # Documentação e diagramas
├── data/
│   ├── raw/                 # Dados brutos (ex: CSV exportado do Garmin)
│   └── bronze/              # Dados normalizados na camada Bronze
├── src/
│   ├── ingestion/           # Lógica de extração (CSV / API)
│   ├── bronze/              # Processamento e persistência Bronze
│   └── silver/              # Transformações e modelagem analítica
├── tests/                   # Testes do projeto
├── README.md
└── requirements.txt
