from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
import os

app = FastAPI(title="RD - Painel VPN")

# CORS (para permitir acesso do frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, defina domínios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Banco de dados
DB_NAME = os.getenv("DB_NAME", "painelvpn.db")

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# Modelos de entrada
class LoginRequest(BaseModel):
    email: str
    senha: str

# Rotas

@app.get("/")
def home():
    return {"status": "ok", "mensagem": "RD Painel VPN API v1.0.0"}

@app.post("/login")
def login(data: LoginRequest):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (data.email, data.senha))
    user = cursor.fetchone()
    conn.close()

    if not user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    return {
        "id": user["id"],
        "nome": user["nome"],
        "email": user["email"],
        "perfil": user["perfil"]
    }

@app.get("/usuarios")
def listar_usuarios():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email, perfil, ativo FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return [dict(u) for u in usuarios]

@app.get("/logs")
def listar_logs():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs ORDER BY data_hora DESC LIMIT 100")
    logs = cursor.fetchall()
    conn.close()
    return [dict(l) for l in logs]

@app.get("/filtros")
def listar_filtros():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM filtros_salvos ORDER BY criado_em DESC")
    filtros = cursor.fetchall()
    conn.close()
    return [dict(f) for f in filtros]
