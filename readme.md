# Air Traffic Monitoring
O objetivo desse repositório é estudar a implementação de uma arquitetura de software baseada em Pub/Sub para monitoramento de tráfego aéreo.

A arquitetura proposta é composta por:
- Uma aplicação que recebe dados de aeronaves em tempo real e publica em um tópico do Pub/Sub.
- Uma aplicação que recebe os dados do tópico do Pub/Sub e realiza update em um delta table.



## Arquitetura

TBD

## Tecnologias

- Python
- RabbitMQ
- Delta Lake

## Experimento

1. Suba o RabbitMQ através do comando `docker-compose up`, ele vai subir containers conforme a configuração do arquivo `docker-compose.yml`.
2. Rode a aplicação para publicar mensagens `python publisher/capture.py`.
3. Rode a aplicação para capturar mensagens `python consumer/process.py`.
