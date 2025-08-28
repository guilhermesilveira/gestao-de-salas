# Sistema de Gestão de Salas

Um sistema Django para gerenciamento de salas e agendamentos.

## 🚀 Instalação e Configuração

### Pré-requisitos
- Python 3.8+
- pip

### Passos para instalação

1. **Clone o repositório**
   ```bash
   git clone <url-do-repositorio>
   cd gestao-de-salas
   ```

2. **Crie e ative o ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações**
   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor de desenvolvimento**
   ```bash
   python manage.py runserver
   ```

6. **Acesse a aplicação**
   Abra seu navegador e acesse: http://127.0.0.1:8000/

## 🏗️ Estrutura do Projeto

```
gestao-de-salas/
├── gestao_salas/          # Configurações principais do projeto
├── webapp/                # Aplicação principal
│   ├── templates/         # Templates HTML
│   ├── views.py          # Views da aplicação
│   └── urls.py           # URLs da aplicação
├── manage.py             # Script de gerenciamento Django
├── requirements.txt       # Dependências Python
└── README.md             # Este arquivo
```

## 🌟 Funcionalidades

- **Página de Boas-vindas**: Interface moderna com Bootstrap 5.3
- **Design Responsivo**: Adaptável a diferentes tamanhos de tela
- **Estrutura Modular**: Preparado para expansão futura

## 🎨 Tecnologias Utilizadas

- **Backend**: Django 5.2.5
- **Frontend**: Bootstrap 5.3 (via CDN)
- **Banco de Dados**: SQLite (padrão Django)
- **Python**: 3.8+

## 📱 Interface

A aplicação possui uma interface moderna e responsiva com:
- Navbar com logo da aplicação
- Card principal com mensagem de boas-vindas
- Seção de recursos com ícones
- Botões de ação
- Footer informativo

## 🔧 Desenvolvimento

### Criar uma nova view
1. Adicione a função em `webapp/views.py`
2. Configure a URL em `webapp/urls.py`
3. Crie o template correspondente em `webapp/templates/webapp/`

### Executar testes
```bash
python manage.py test
```

### Criar superusuário (para admin)
```bash
python manage.py createsuperuser
```

## 📄 Licença

Este projeto está sob a licença MIT.

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📞 Suporte

Para dúvidas ou suporte, entre em contato através dos issues do repositório.
