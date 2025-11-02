import sqlite3
from typing import List, Dict

DB_NAME = "painelvpn.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# 🔐 Autenticação
def autenticar_usuario(email: str, senha: str) -> Dict:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
    user = cursor.fetchone()
    conn.close()
    return dict(user) if user else None

# 👥 Usuários
def listar_usuarios() -> List[Dict]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email, perfil, ativo FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return [dict(u) for u in usuarios]

# 📄 Logs
def listar_logs(limit: int = 100) -> List[Dict]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs ORDER BY data_hora DESC LIMIT ?", (limit,))
    logs = cursor.fetchall()
    conn.close()
    return [dict(l) for l in logs]

# 🔍 Filtros salvos
def listar_filtros() -> List[Dict]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM filtros_salvos ORDER BY criado_em DESC")
    filtros = cursor.fetchall()
    conn.close()
    return [dict(f) for f in filtros]