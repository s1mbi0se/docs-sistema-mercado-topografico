import os
from jinja2 import Environment, FileSystemLoader

# Carregar variáveis de ambiente
env_vars = os.environ

# Configurar o Jinja
env = Environment(loader=FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)

# Substituir variáveis em todos os arquivos .md
for root, dirs, files in os.walk('./'):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path)
            template = env.get_template(relative_path)
            output = template.render(env_vars)
            with open(file_path, 'w') as f:
                f.write(output)
