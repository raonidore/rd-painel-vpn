#!/bin/bash

echo "🔧 Iniciando instalação do RD - Painel VPN..."

# Atualiza pacotes
sudo apt update && sudo apt upgrade -y

# Instala dependências básicas
sudo apt install -y python3 python3-pip python3-venv git unzip nginx

# Cria ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instala dependências do backend
pip install -r backend/requirements.txt

# Configura banco de dados SQLite (ou PostgreSQL se preferir)
echo "🧠 Criando banco de dados..."
sqlite3 painelvpn.db < dump.sql

# Configura variáveis de ambiente
cp .env.example .env

# Permissões
chmod +x install.sh

echo "✅ Instalação concluída!"
echo "➡️ Para iniciar o sistema, execute:"
echo "source venv/bin/activate && python backend/app/main.py"