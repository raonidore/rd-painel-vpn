<template>
  <div id="app">
    <header>
      <img src="../assets/logo-rd.png" alt="Logo RD" class="logo" />
      <h1>RD - Painel VPN</h1>
    </header>

    <main>
      <section v-if="!usuario">
        <h2>Login</h2>
        <form @submit.prevent="fazerLogin">
          <input v-model="email" type="email" placeholder="E-mail" required />
          <input v-model="senha" type="password" placeholder="Senha" required />
          <button type="submit">Entrar</button>
        </form>
        <p v-if="erro" class="erro">{{ erro }}</p>
      </section>

      <section v-else>
        <h2>Bem-vindo, {{ usuario.nome }} ({{ usuario.perfil }})</h2>
        <button @click="logout">Sair</button>

        <div class="painel">
          <h3>Últimos Logs</h3>
          <ul>
            <li v-for="log in logs" :key="log.id">
              {{ log.data_hora }} - {{ log.acao }} ({{ log.detalhes }})
            </li>
          </ul>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      senha: '',
      usuario: null,
      erro: '',
      logs: []
    };
  },
  methods: {
    async fazerLogin() {
      try {
        const res = await fetch('http://localhost:8000/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email: this.email, senha: this.senha })
        });

        if (!res.ok) throw new Error('Login inválido');

        this.usuario = await res.json();
        this.carregarLogs();
        this.erro = '';
      } catch (err) {
        this.erro = err.message;
      }
    },
    async carregarLogs() {
      const res = await fetch('http://localhost:8000/logs');
      this.logs = await res.json();
    },
    logout() {
      this.usuario = null;
      this.email = '';
      this.senha = '';
      this.logs = [];
    }
  }
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
  background: #f5f5f5;
  margin: 0;
  padding: 0;
}
#app {
  max-width: 600px;
  margin: 40px auto;
  background: white;
  padding: 20px;
  border-radius: 8px;
}
.logo {
  width: 80px;
}
header {
  display: flex;
  align-items: center;
  gap: 20px;
}
form input {
  display: block;
  width: 100%;
  margin-bottom: 10px;
  padding: 8px;
}
button {
  padding: 10px 20px;
  background: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}
.erro {
  color: red;
}
.painel {
  margin-top: 20px;
}
</style>