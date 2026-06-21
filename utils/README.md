# Utilitários (Utils)

Pacote contendo funções e módulos Python auxiliares, criados para serem importados em vários pontos do projeto. Isso promove a padronização das rotinas e reduz a duplicação de código.

### Módulos Atuais:
- **`experiment_logger.py`**: Script customizado e automatizado que rastreia os pipelines durante as buscas em grade (`GridSearchCV`). Ele é responsável por extrair sistematicamente os resultados do modelo testado (incluindo configurações com e sem o SMOTE) e persistir os melhores scores dentro do arquivo de log único na pasta `/results`.