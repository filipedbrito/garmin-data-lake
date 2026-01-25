# garmin-data-lake
**Datalake Analítico com Garmin**

## Objetivo
Construir, na prática, um data lake analítico em arquitetura moderna, utilizando serviços da AWS e orquestração de pipelines, cobrindo todo o ciclo de dados: ingestão, transformação e disponibilização para análise.

O projeto utiliza dados do **Garmin Connect** para monitorar e analisar métricas pessoais de saúde e performance esportiva — eu mesmo serei o “cliente final” — com foco em atividades físicas (principalmente corrida) e correlação com dados como sono, frequência cardíaca e indicadores diários de saúde.

---

## Arquitetura & Stack
- **Cloud:** AWS  
  - Amazon S3 (Data Lake)  
  - Amazon Athena (Query Engine)
- **Orquestração:** Apache Airflow
- **Transformações:** Python e dbt
- **Arquitetura de dados:** Bronze / Silver / Gold
- **Visualização:** Metabase (ou ferramenta equivalente)
- **Versionamento:** GitHub

---

## Escopo
- Ingestão automatizada de dados via API
- Persistência de dados brutos no Data Lake (camada Bronze)
- Tratamento, normalização e modelagem analítica (camadas Silver e Gold)
- Orquestração de pipelines com Airflow
- Disponibilização de métricas e dashboards analíticos

---

## Status
**Work in Progress (WIP)**  
Projeto em desenvolvimento contínuo, com entregas incrementais.

---

### Próximos passos
- Implementação da ingestão via API do Garmin Connect
- Estruturação inicial da camada Bronze
- Criação das primeiras tabelas analíticas
- Dashboard de acompanhamento de performance
