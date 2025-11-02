-- Criação da tabela de usuários
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    perfil TEXT CHECK(perfil IN ('admin', 'suporte')) NOT NULL,
    ativo INTEGER DEFAULT 1,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela de logs (auditoria)
CREATE TABLE logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    acao TEXT NOT NULL,
    detalhes TEXT,
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- Criação da tabela de filtros salvos
CREATE TABLE filtros_salvos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    nome TEXT NOT NULL,
    parametros TEXT NOT NULL,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- Inserção de usuários de exemplo
INSERT INTO usuarios (nome, email, senha, perfil) VALUES
('Raoni Admin', 'admin@painelvpn.com', 'admin123', 'admin'),
('Suporte 1', 'suporte@painelvpn.com', 'suporte123', 'suporte');

-- Inserção de logs de exemplo
INSERT INTO logs (usuario_id, acao, detalhes) VALUES
(1, 'Login', 'Admin acessou o sistema'),
(2, 'Revogação', 'Suporte revogou acesso de usuário X');

-- Inserção de filtros salvos
INSERT INTO filtros_salvos (usuario_id, nome, parametros) VALUES
(1, 'Acessos de hoje', '{"data_inicio":"2025-11-02","data_fim":"2025-11-02"}'),
(2, 'Revogações da semana', '{"acao":"Revogação","periodo":"últimos 7 dias"}');
