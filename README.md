🛡️ RD - Painel VPN v1.0.0

Sistema de gerenciamento de acessos VPN com autenticação, auditoria, exportação de relatórios e interface web moderna.

Desenvolvido para uso interno da equipe RD, com foco em segurança, rastreabilidade e facilidade de uso.
📸 Captura de Tela

 Em breve

🚀 Funcionalidades

    Login com permissões por perfil (admin e suporte)

    Cadastro, recuperação e exclusão de usuários

    Painel com ações recentes e alertas

    Central de Auditoria com busca, filtros e exportação

    Filtros salvos com nome personalizado

    Exportação em PDF/CSV

    Registro de conexões VPN com data/hora

    Interface web com Vue.js + Vite

    Backend em Python (Flask)

    Banco de dados PostgreSQL

    Instalação automatizada via install.sh

🧱 Estrutura do Projeto

rd-painel-vpn-v1.0.0/

├── backend/ # API Flask + banco de dados

├── frontend/ # Interface Vue.js

├── docs/ # Documentação institucional

├── dump.sql # Estrutura do banco de dados

├── install.sh # Script de instalação automatizada

└── README.md

⚙️ Instalação Local
Pré-requisitos

    Python 3.10+

    Node.js 18+

    PostgreSQL 14+

    Git

Passos
bash
Copiar

git clone https://github.com/raonidore/rd-painel-vpn.git
cd rd-painel-vpn
chmod +x install.sh
./install.sh

🌐 Acesso ao Sistema

Após a instalação, acesse:

http://localhost:5173

Usuário padrão: admin

Senha: admin123
🛠️ Tecnologias Utilizadas

    Python

    Flask

    PostgreSQL

    Vue.js

    Vite

    Git

📄 Licença

Este projeto é de uso interno da RD. Todos os direitos reservados.
👨‍💻 Desenvolvido por

Raoni Dore

Engenheiro de Software • DevOps • Segurança da Informação

github.com/raonidore