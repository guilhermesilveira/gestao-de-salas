# Sistema de Gestão de Salas

Um sistema Django para gerenciamento de salas e agendamentos com sistema de autenticação completo.

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

## 🔐 Sistema de Autenticação

O sistema inclui um sistema de login tradicional completo:

### Funcionalidades
- **Login de Usuário**: Autenticação com username e senha
- **Cadastro de Usuário**: Criação de novas contas (apenas username e senha obrigatórios)
- **Logout**: Encerramento seguro de sessão
- **Dashboard Protegido**: Área restrita apenas para usuários autenticados
- **Mensagens Flash**: Sistema de notificações para feedback do usuário

### URLs do Sistema
- `/` - Página inicial (acessível a todos)
- `/login/` - Tela de login
- `/register/` - Tela de cadastro
- `/dashboard/` - Dashboard (requer autenticação)
- `/logout/` - Logout do usuário

### Segurança
- Proteção CSRF em todos os formulários
- Validação de senhas do Django
- Redirecionamentos seguros após login/logout
- Decorator `@login_required` para views protegidas

## 🏗️ Estrutura do Projeto

```
gestao-de-salas/
├── gestao_salas/          # Configurações principais do projeto
│   ├── settings.py        # Configurações Django (inclui auth)
│   └── urls.py           # URLs principais
├── webapp/                # Aplicação principal
│   ├── templates/         # Templates HTML
│   │   ├── base.html     # Template base com navegação
│   │   ├── welcome.html  # Página inicial
│   │   ├── login.html    # Tela de login
│   │   ├── register.html # Tela de cadastro
│   │   └── dashboard.html # Dashboard protegido
│   ├── views.py          # Views da aplicação (inclui auth)
│   └── urls.py           # URLs da aplicação
├── manage.py             # Script de gerenciamento Django
├── requirements.txt       # Dependências Python
└── README.md             # Este arquivo
```

## 🌟 Funcionalidades

- **Sistema de Autenticação**: Login, cadastro e logout completos
- **Página de Boas-vindas**: Interface moderna com Bootstrap 5.3
- **Dashboard Protegido**: Área restrita para usuários logados
- **Design Responsivo**: Adaptável a diferentes tamanhos de tela
- **Estrutura Modular**: Preparado para expansão futura
- **Navegação Inteligente**: Menu adaptativo baseado no status de autenticação

## 🎨 Tecnologias Utilizadas

- **Backend**: Django 5.2.5
- **Autenticação**: Sistema nativo do Django
- **Frontend**: Bootstrap 5.3 (via CDN)
- **Ícones**: Font Awesome 6.0
- **Banco de Dados**: SQLite (padrão Django)
- **Python**: 3.8+

## 📱 Interface

A aplicação possui uma interface moderna e responsiva com:
- **Navbar Adaptativo**: Mostra opções diferentes para usuários logados/não logados
- **Sistema de Mensagens**: Alertas para feedback do usuário
- **Formulários Estilizados**: Login e cadastro com validação visual
- **Dashboard Informativo**: Estatísticas e ações rápidas
- **Design Responsivo**: Funciona em dispositivos móveis e desktop

## 🔧 Desenvolvimento

### Criar uma nova view
1. Adicione a função em `webapp/views.py`
2. Configure a URL em `webapp/urls.py`
3. Crie o template correspondente em `webapp/templates/webapp/`

### Proteger uma view com autenticação
```python
from django.contrib.auth.decorators import login_required

@login_required
def minha_view(request):
    # Esta view só pode ser acessada por usuários logados
    pass
```

### Executar testes
```bash
python manage.py test
```

### Criar superusuário (para admin)
```bash
python manage.py createsuperuser
```

## 🚀 Como Usar

1. **Acesse a aplicação**: http://127.0.0.1:8000/
2. **Crie uma conta**: Clique em "Criar Conta" e preencha username e senha
3. **Faça login**: Use suas credenciais na tela de login
4. **Acesse o dashboard**: Após o login, você será redirecionado para o dashboard
5. **Navegue pelo sistema**: Use o menu superior para acessar diferentes funcionalidades

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
