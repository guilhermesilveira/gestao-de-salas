# Criando código
Sempre que criar código você não deve inventar links ou features que não foram pedidas.
Sempre que criar ou alterar o frontend de uma tela, ao terminar a historia lembre de levantar a tela e tirar um screenshot dela.

# Python - Boas Práticas

## Estrutura e Organização
- Use type hints em todas as funções e métodos
- Prefira early returns para reduzir complexidade
- Use o princípio da responsabilidade única - métodos devem ter baixa complexidade
- Extraia loops complexos em métodos separados
- Use Path do pathlib para manipulação de caminhos
- Evite capturar exceções genéricas - trate casos específicos quando necessário

## Formatação e Linting
- Use Ruff para formatação e linting automático
- Configure Ruff com regras estritas para manter qualidade do código
- Execute `ruff check` e `ruff format` antes de commits
- Use `ruff --fix` para correções automáticas

## Imports e Dependências
- Use imports absolutos quando possível
- Agrupe imports: stdlib, third-party, local
- Use `from pathlib import Path` em vez de `import os.path`
- Prefira `typing` para type hints complexos

# Frontend

## JavaScript (Vanilla)
- Use ES6+ features (const, let, arrow functions, template literals)
- Prefira `querySelector` e `addEventListener` em vez de jQuery
- Use `fetch` API para requisições HTTP
- Implemente tratamento de erros adequado
- Use `async/await` para operações assíncronas
- Mantenha funções pequenas e com responsabilidade única

## Bootstrap
- Use classes utilitárias do Bootstrap 5 quando possível
- Prefira componentes nativos do Bootstrap em vez de customizações
- Use sistema de grid responsivo do Bootstrap
- Mantenha consistência visual usando variáveis CSS do Bootstrap
- Use `base.html` como template base sempre que possível

## CSS - Metodologia BEM
- **Block**: Componente independente (ex: `.card`, `.button`)
- **Element**: Parte de um bloco (ex: `.card__title`, `.card__body`)
- **Modifier**: Variação de um bloco ou elemento (ex: `.card--featured`, `.button--primary`)

### Exemplos de Nomenclatura BEM:
```css
/* Bloco */
.card { }

/* Elementos */
.card__header { }
.card__title { }
.card__body { }
.card__footer { }

/* Modificadores */
.card--featured { }
.card--featured .card__title { }
.button--primary { }
.button--secondary { }
```

### Regras BEM:
- Use `__` para elementos
- Use `--` para modificadores
- Evite mais de 2 níveis de aninhamento
- Mantenha nomes descritivos e semânticos
- Use kebab-case para nomes compostos

# Testing
If you want to run the manage.py runserver, first check that its not yet running. If it is running (use ps), kill it first.

# Comandos Úteis

## Ruff
```bash
ruff check .                    # Verificar problemas
ruff format .                   # Formatar código
ruff --fix .                    # Corrigir automaticamente
ruff check --select E,W        # Apenas erros e warnings
```

## Django
```bash
python manage.py runserver      # Servidor de desenvolvimento
python manage.py makemigrations # Criar migrações
python manage.py migrate        # Aplicar migrações
python manage.py collectstatic  # Coletar arquivos estáticos
```

## Desenvolvimento
```bash
# Verificar se servidor está rodando
ps aux | grep runserver

# Matar processo se necessário
kill -9 <PID>
```