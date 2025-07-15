# 🎬 Sistema de Cadastro de Filmes e Séries

Este é um sistema simples em Python que permite o **cadastro, listagem, atualização e remoção de filmes e séries**, além de **gerenciamento de usuários com autenticação segura**. O sistema funciona no terminal e utiliza **SQLite** como banco de dados.

---

## 📦 Funcionalidades

- ✅ Cadastro de títulos (filmes e séries)
- 📋 Listagem de todos os títulos cadastrados
- ✏️ Atualização de títulos
- 🗑️ Remoção de títulos
- 👤 Cadastro de usuários com:
  - Nome
  - E-mail
  - Senha segura (validação de complexidade)
  - Permissão de administrador
- 🔒 Validação de senha forte e e-mail com regex
- 💾 Banco de dados SQLite integrado

---

## 🧠 Tecnologias utilizadas

- Python 3.x
- SQLite (nativo do Python)
- Módulos padrão:
  - `sqlite3`
  - `re`
  - `getpass`
  - `os`
  - `time`

---

## 🚀 Como executar o projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/GianFerreiraDev/sistema-cadastro-filmes-series.git
   cd sistema-cadastro-filmes-series
   ```

2. Execute o arquivo principal:
   ```bash
   python cadastro_filmes_series.py
   ```

O sistema criará automaticamente o banco de dados `filmes_series.db` com as tabelas necessárias (`usuarios` e `titulos`).

---

## 🧪 Validação de segurança

- As senhas dos usuários precisam atender os seguintes critérios:
  - Mínimo 8 caracteres
  - Pelo menos 1 letra maiúscula
  - Pelo menos 1 letra minúscula
  - Pelo menos 1 número
  - Pelo menos 1 caractere especial (ex: `!@#$%`)
  
- E-mails são validados com expressão regular padrão.

> ⚠️ **Importante**: As senhas ainda são armazenadas em texto puro. Para maior segurança, é recomendável usar hashing (ex: `bcrypt`) em futuras versões.

---

## 📁 Estrutura dos arquivos

```
.
├── banco.py                  # Toda lógica de banco de dados e operações
├── cadastro_filmes_series.py # Interface de terminal e controle do sistema
├── filmes_series.db          # Criado automaticamente na primeira execução
```

---

## 💡 Melhorias futuras

- [ ] Implementar login de usuário
- [ ] Restringir visualização de títulos por usuário
- [ ] Interface Web (Django ou Flask)
- [ ] Versão mobile
- [ ] Exportação de dados para CSV
- [ ] Backup automático do banco

---

## 🧑‍💻 Autor

**Gian Ferreira**  
[GitHub](https://github.com/GianFerreiraDev)

