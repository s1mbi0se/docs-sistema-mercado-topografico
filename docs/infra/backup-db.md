---
hide:
  - toc
---

# Precisando gerar um dump do banco? É super simples!


## Execute trocando os valores pela instancia desejada
```shell
  mysqldump --user={DB_USER} --password={DB_PASSWORD} --host={DB_HOST} --port={DB_PORT} --no-tablespaces {DATABASE} > {DUMP_PATH/FILE.sql}
```

# Exemplo prático de um dump do seu banco local:


> mysqldump --user=<span style="color:red;">root</span> --password=<span style="color:red;">root</span> --host=<span style="color:red;">127.0.0.1</span> --port=<span style="color:red;">3306</span> --no-tablespaces <span style="color:red;">sistema_mercado_topografico_development</span> > <span style="color:red;">./sistema_mercado_topografico_development-dump.sql</span>
