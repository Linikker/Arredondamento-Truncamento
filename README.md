# 🧮 Analisador de Arredondamento e Truncamento de Ponto Flutuante  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Ativo-success)
![IEEE754](https://img.shields.io/badge/IEEE-754-orange)

Um programa interativo em **Python** que demonstra, de forma didática, como funcionam as **regras de arredondamento e truncamento de números reais**, segundo o padrão **IEEE 754 (round half to even)** — o mesmo utilizado em linguagens como C, Java, Python e em processadores modernos.  

O objetivo é permitir que o usuário visualize **como cada dígito influencia o resultado final**, mostrando passo a passo a **regra aplicada**, o **número original**, o **resultado arredondado** e o **resultado truncado**.  

---

## 🚀 Funcionalidades  

- ✅ Recebe um número real digitado pelo usuário  
- ✅ Permite escolher quantas casas decimais devem ser mantidas  
- ✅ Analisa os dígitos relevantes da parte fracionária (`d₁`, `d₂`, `d₃`...)  
- ✅ Aplica:  
  - **Truncamento** (simples corte dos dígitos extras)  
  - **Arredondamento IEEE 754** (round half to even)  
- ✅ Exibe qual **regra foi aplicada** e o resultado de ambos os métodos  
- ✅ Pergunta se o usuário deseja repetir o processo ou encerrar  

---

## 🧠 Regras Implementadas  

| Condição | Ação (Arredondamento) | Descrição |
|-----------|------------------------|------------|
| `dₙ₊₁ > 5` | Soma 1 em `dₙ` | Arredonda para cima |
| `dₙ₊₁ < 5` | Mantém `dₙ` | Arredonda para baixo |
| `dₙ₊₁ = 5` e dígitos seguintes > 0 | Soma 1 em `dₙ` | Arredonda para cima |
| `dₙ₊₁ = 5` e `dₙ` é ímpar | Soma 1 em `dₙ` | Arredonda para o número par mais próximo |
| `dₙ₊₁ = 5` e `dₙ` é par | Mantém `dₙ` | Não altera o valor |
| **Truncamento** | Mantém `dₙ` | Apenas corta os dígitos extras, sem arredondar |

---

## 💻 Exemplo de Execução  

```bash
Digite um número real: 0.078179
Quantas casas decimais após a vírgula? 3

--- Análise ---
Número original: 0.078179
Parte fracionária: 078179
d3 = 8 | d4 = 1 | d5 = 7
Regra aplicada: d_corte < 5 → arredonda para baixo (mantém)
Arredondado (3 casas): 0.078
Truncado    (3 casas): 0.078
---------------------------

Deseja testar outro número? (s/n): s

```

## 🧩 Estrutura do Projeto
.
├── main.py        # Código-fonte principal do programa
└── README.md      # Documentação do projeto


## ⚙️ Como Executar

  ### 1️⃣ Pré-requisitos

    Python 3.8+ instalado no sistema

  ### 2️⃣ Clonar o repositório
    git clone https://github.com/SEU_USUARIO/analisador-arredondamento.git
    cd analisador-arredondamento

  ### 3️⃣ Executar o programa
    python3 main.py


## 📘 Referências

📖 IEEE Standard for Floating-Point Arithmetic (IEEE 754-2019) - [ ↗️ ](https://ieeexplore.ieee.org/document/8766229)

🐍 Python Documentation: Built-in round() function - [ ↗️ ](https://docs.python.org/3/library/functions.html#round)

💡 Numerical Computing Guide — Oracle Docs - [ ↗️ ](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html)


## 👨‍💻 Autor
Gustavo Liniker
📧 Contato:  liniker.gu@hotmail.com

💡 Projeto criado para fins de estudo e demonstração de aritmética de ponto flutuante.
