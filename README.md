# 🍝 🦐 Restaurant Orders 🍛 🥘

Bem-vindo ao repositório do projeto **Restaurant Orders**, uma ferramenta de construção de cardápios para o Restaurante **Restaurant Orders**! Este projeto foi desenvolvido como parte de um curso, com foco na prática de habilidades essenciais em programação e desenvolvimento de software.

---

## 📝 Sobre o Projeto

O **Restaurant Orders** é uma aplicação que ajuda o restaurante a gerar cardápios personalizados, considerando possíveis restrições alimentares e a disponibilidade dos ingredientes em estoque. Atualmente, o restaurante realiza a gestão de receitas e estoque através de arquivos CSV, o que torna o processo ineficiente. Este projeto busca otimizar essa gestão e oferecer uma solução prática e eficiente.

Você encontrará neste projeto:

- Classes para mapear pratos, receitas e ingredientes.
- Funcionalidades para gerar cardápios personalizados.
- Um sistema para gerenciar o estoque de ingredientes.
- Testes automatizados para garantir a qualidade do código.

---

## 🚵 Habilidades Exercitadas

Durante o desenvolvimento deste projeto, as seguintes habilidades foram exercitadas:

- **Uso de Hashmaps**: Estruturas de dados `Dict` e `Set` no Python.
- **Testes de Software**: Implementação e execução de testes para garantir o funcionamento correto do código.
- **Orientação a Objetos**: Design e implementação de classes para organizar a lógica do projeto.

---

## 📂 Estrutura do Projeto

O projeto está organizado da seguinte forma:

```plaintext
📁 data/
   ├── inventory_base_data.csv  # Dados de estoque base
   └── menu_base_data.csv       # Dados de cardápio base

📁 src/
   ├── models/                  # Modelos principais
   │   ├── dish.py              # Classe para representar pratos
   │   ├── ingredient.py        # Classe para representar ingredientes
   │   └── __init__.py
   ├── services/                # Serviços principais
   │   ├── inventory_control.py # Controle de estoque
   │   ├── menu_builder.py      # Construção de cardápios
   │   ├── menu_data.py         # Manipulação de dados do cardápio
   │   └── __init__.py
   ├── app.py                   # Ponto de entrada da aplicação
   └── __init__.py

📁 tests/                       # Testes automatizados
   ├── dish/
   │   ├── test_dish.py         # Testes para a classe Dish
   │   └── __init__.py
   ├── ingredient/
   │   ├── test_ingredient.py   # Testes para a classe Ingredient
   │   └── __init__.py
   └── __init__.py
```

---

## 🛠️ Como Rodar o Projeto

1. Clone este repositório:

    ```bash
    git clone https://github.com/vicentevendramin/restaurant-orders.git
    cd restaurant-orders
    ```

2. Crie e ative um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt # Production
    pip install -r dev-requirements.txt # Development
    ```

4. Execute os testes para verificar o funcionamento:

    ```bash
    pytest # Development
    ```
