<h1 align="center">🧮 calculator-with-gui-in-python</h1>

<p align="center">
  Uma calculadora simples com interface gráfica feita em Python usando Tkinter.
</p>

<p align="center">
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/panda12332145/calculator-with-gui-in-python">
  <a href="https://github.com/panda12332145/calculator-with-gui-in-python/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/panda12332145/calculator-with-gui-in-python">
  </a>
  <a href="https://github.com/panda12332145/calculator-with-gui-in-python/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/panda12332145/calculator-with-gui-in-python?style=social">
  </a>
  <br>
  <img alt="Python version" src="https://img.shields.io/badge/python-3.9%2B-blue?logo=python&logoColor=white">
  <img alt="GUI" src="https://img.shields.io/badge/GUI-Tkinter-green">
</p>

<p align="center">
  <a href="#-sobre">Sobre</a> •
  <a href="#-funcionalidades">Funcionalidades</a> •
  <a href="#-demonstração">Demonstração</a> •
  <a href="#-como-executar">Como executar</a> •
  <a href="#-estrutura-do-projeto">Estrutura</a> •
  <a href="#-autor">Autor</a>
</p>

---

<h2 id="-sobre">🔖 Sobre</h2>

Calculadora de mesa com interface gráfica (GUI) desenvolvida em **Python**, utilizando o módulo **`tkinter`** para a janela e os botões e o módulo **`math`** para os cálculos especiais (como o valor de π).

O projeto é ideal para quem está aprendendo Python e quer ver um exemplo prático de como criar janelas, botões e eventos com Tkinter.

<h2 id="-funcionalidades">✨ Funcionalidades</h2>

| Botão | Função |
|:-----:|--------|
| `0` – `9` | Entrada de números |
| `+` `-` `X` `/` | As quatro operações básicas |
| `=` | Exibe o resultado da operação |
| `.` | Ponto decimal para números quebrados |
| `π` | Insere o valor de pi (alterna entre `3.14` e o valor completo de `math.pi`) |
| `x²` | Calcula a raiz quadrada do número no visor |
| `≅` | Arredonda o número no visor para o inteiro mais próximo |
| `AC` | Limpa o visor (All Clear) |

<h2 id="-demonstração">📽 Demonstração</h2>

<p align="center">
  <kbd>
    <img width="280" style="border-radius: 5px" height="400" alt="Interface da calculadora" src="github%20assets/Menu.jpg">
  </kbd>
</p>

<h2 id="-tecnologias">🛠 Tecnologias</h2>

- [Python 3.9+](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (interface gráfica — já vem com o Python)
- [math](https://docs.python.org/3/library/math.html) (cálculos especiais)

<h2 id="-como-executar">⚙️ Como executar</h2>

### Pré-requisitos

- **Python 3.9** ou superior instalado. Confira com:
  ```bash
  python --version
  ```
- O **Tkinter** normalmente já acompanha o Python no Windows e macOS. No Linux (Debian/Ubuntu), se necessário, instale com:
  ```bash
  sudo apt install python3-tk
  ```

### Passo a passo

1. Clone o repositório:
   ```bash
   git clone https://github.com/panda12332145/calculator-with-gui-in-python.git
   ```

2. Entre na pasta do projeto:
   ```bash
   cd calculator-with-gui-in-python
   ```

3. Execute a calculadora:
   ```bash
   python CalculadoraComGui.py
   ```
   > No Linux/macOS, pode ser necessário usar `python3` em vez de `python`.

<h2 id="-estrutura-do-projeto">📁 Estrutura do projeto</h2>

```
calculator-with-gui-in-python/
├── CalculadoraComGui.py   # Código-fonte da calculadora (lógica + interface)
├── README.md              # Documentação do projeto
└── github assets/
    └── Menu.jpg           # Captura de tela da interface
```

<h2 id="-melhorias-futuras">🚀 Melhorias futuras</h2>

Algumas ideias para evoluir o projeto:

- [ ] Tratar divisão por zero e entradas inválidas
- [ ] Permitir operações encadeadas (ex: `2 + 3 + 4`)
- [ ] Adicionar suporte ao teclado
- [ ] Corrigir o rótulo do botão de raiz quadrada (`x²` → `√`)
- [ ] Modernizar o layout com `ttk` ou temas

> Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request* com sugestões!

<h2 id="-autor">👾 Autor</h2>

<img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/73090399?v=4" width="100px;" alt="Foto do autor"/>

Feito por **Panda12332145** 👋🏽

[![GitHub](https://img.shields.io/badge/GitHub-panda12332145-black?logo=github)](https://github.com/panda12332145)
