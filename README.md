# 🚀 VM Translator - UFMA 2026.1

![Python Version](https://img.shields.io/badge/python-3.13%2B-blue)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

Projeto desenvolvido para a disciplina de **Compiladores** da Universidade Federal do Maranhão (UFMA). O objetivo é construir um tradutor VM → Assembly Hack.

---

## 👥 Integrantes

| Nome                             | Matrícula   |
| :------------------------------- | :---------- |
| **Anderson Almeida da Silveira** | 20240065590 |
| **Jeysraelly Almone da Silva**   | 20250071222 |

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.13
* **Gerenciador de Pacotes:** `uv`
* **Framework de Testes:** `pytest`

---

## Estrutura do Projeto

* `parser.py`: responsável pela leitura e interpretação dos comandos presentes no arquivo VM.
* `code_writer.py`: responsável pela geração do código Assembly correspondente aos comandos identificados pelo parser.
* `main.py`: realiza a integração entre os módulos do sistema, coordenando o processo de tradução.
* `tests/`: contém os arquivos utilizados para validação das funcionalidades implementadas.

---

## Funcionalidades Implementadas

### Parser

* Leitura de arquivos VM;
* Remoção de comentários e linhas em branco;
* Identificação do tipo de comando;
* Recuperação dos argumentos associados a cada instrução.

### Operações Aritméticas e Lógicas

* `add`
* `sub`
* `neg`
* `and`
* `or`
* `not`

### Operações Relacionais

* `eq`
* `gt`
* `lt`

### Acesso à Memória

#### Push

* `push constant`
* `push local`
* `push argument`
* `push this`
* `push that`
* `push temp`
* `push static`

#### Pop

* `pop local`
* `pop argument`
* `pop this`
* `pop that`
* `pop temp`
* `pop static`

---

## Execução

Para executar o tradutor, utilize o comando:

```bash
python main.py
```

O arquivo VM definido na função principal será processado e o código Assembly correspondente será gerado automaticamente.

---

## Exemplo de Entrada

```vm
push constant 7
push constant 8
add
pop local 0
```

## Exemplo de Saída

```asm
@7
D=A
@SP
A=M
M=D
@SP
M=M+1
```
