📄 Arquivo: README.md

Esse arquivo vai na raiz do projeto: rd-painel-vpn-v1.0.0/README.md
📥 Conteúdo completo do README.md:
🛡️ RD - Painel VPN

Sistema de gerenciamento de acessos VPN com controle de usuários, auditoria, filtros salvos e exportação de relatórios.
🚀 Funcionalidades

    Login com permissões por perfil (admin e suporte)

    Cadastro, revogação e exclusão de usuários

    Painel com ações recentes e alertas

    Central de Auditoria com busca, filtros e exportação

    Filtros salvos com nome personalizado

    Exportação em PDF/CSV

    Instalação via script automatizado

    Deploy via GitHub (futuramente)

📦 Requisitos

    Ubuntu 20.04 ou superior

    Python 3.8+

    Git

    SQLite (ou PostgreSQL, opcional)

    Nginx (opcional para produção)

🛠️ Instalação
bash
Copiar

# Clone o repositório (ou copie os arquivos)
git clone https://github.com/rdinfra/painel-vpn.git
cd painel-vpn

# Torne o script executável
chmod +x install.sh

# Execute a instalação
sudo ./install.sh

🔐 Acesso inicial

Usuário 	Senha 	Perfil
admin@painelvpn.com 	admin123 	admin
suporte@painelvpn.com 	suporte123 	suporte
Exportar
Copiar
📁 Estrutura do projeto

rd-painel-vpn/

├── backend/

├── frontend/

├── install.sh

├── dump.sql

├── .env.example

├── docs/

└── assets/

🧪 Testes e validação

Após a instalação, ative o ambiente virtual e rode o backend:
bash
Copiar

source venv/bin/activate
python backend/app/main.py

Acesse o sistema via navegador:

http://localhost:8000 (ou porta configurada)
📄 Licença

MIT © RD Infra