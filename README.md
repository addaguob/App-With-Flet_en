# App-With-Flet

## Description

The project was developed to study and practice programming in Python, MySQL database manipulation and Flet for creating graphical interfaces. The idea was to create an application that would allow managing user registration, customers, products, sales and controlling the stock in a simple and efficient way.

## Features

- User Authentication: The system has a login screen for administrator user authentication.
- User Registration: Allows creating users.
- Customer Control: Allows registering and editing customer information.
- Product Management: Allows registering, editing and excluding products from the stock.
- Sales Registration: Allows registering sales, associating the customers and products involved.
- Stock Control: Keeps the product stock updated based on the sales made.

## Tecnologias Utilizadas

- Python
- MySQL
- Flet (interface gráfica)

## Telas:

Login:

![Login](Screens/Login.PNG)

Tela Inicial:

![Tela Inicial](Screens/Home.PNG)

Vendas:

![Vendas](Screens/Sales.PNG)

Produtos:

![Produtos](Screens/Products.PNG)

Clientes:

![Clientes](Screens/Customers.PNG)

Cadastro de Usuários:

![Cadastro de Usuários](Screens/Users.PNG)

## Para testar:

To run the application, make sure you have Python and MySQL installed on your system. In addition, it is recommended to create a virtual environment to isolate the project's dependencies.

1. Clone o repositório em sua máquina local:

   - git clone https://github.com/HelioCard/App-With-Flet.git
   - cd App-With-Flet

2. Instale as dependências do projeto:

   - pip install -r requirements.txt

3. Acesse o MySQL. Crie seu banco de dados (schema) e execute o script da pasta "database_scripts" para criação das tabelas. Há duas opções:

   - create_tables - structure_only.sql (somente criação das tabelas);
   - create_tables - structure_and_some_data.sql (criação das tabelas e inserção de alguns dados para teste)

4. Execute o arquivo main.py. Digite qualquer texto nos campos "Usuário" e "Senha" e clique em "Login" para abrir a tela de configuração inicial do banco de dados. Insira seus dados de conexão e clique em "Salvar". As seguintes telas só abrem na primeira execução, quando ainda não houve configuração:

![Configuração do Banco de Dados](Screens/Config_DB.PNG)

5. Mais uma vez, digite qualquer texto nos campos "Usuário" e "Senha" e clique em "Login" para abrir a tela do cadastro de administrador. Preencha e clique em "Cadastrar":

![Criação do Primeiro Administrador](Screens/Config_Admin.PNG)

6. Faça o Login.

The project was developed for educational purposes and to develop skills in Python, MySQL, and Flet. Feel free to explore the code and adapt it to your needs. If you have any questions or suggestions, please contact me: helio.card@yahoo.com.br
