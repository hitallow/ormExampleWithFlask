# Welcome to My Project!

Olá, este projeto faz parte da composição da nota da terceira unidade da disciplina DCT2202 - Projeto e administração de banco de dados.



## Configuração
É requido que você tenha o python em sua máquina.
É indicado, que você crie uma <code>virtualenv</code>, assim você podera isolar o projeto em um ambiente controlado.
<br>


1 - > Primeiro baixe o projeto em sua máquina e caso queira, crie uma <code> venv </code> <br>
2 - > Para instalar as dependências, você pode rodar em seu terminal, na pasta do projeto <code>$ pip install -r requirements.txt</code>

3 - > Agora, você pode optar por usar o Sqlite ou o MariaDB, escolha um e siga os passos para poder utilizar;
<ul>
<li>Se você quiser utilizar o Sqlite, você pode ir ao arquivo 
<code> config.py</code> e descomentar a linha 3 e comentar a linha 2 e pode seguir para o passo 4.</li>
	<li>Caso você queria utlizar o mysql, você precisa criar um database, entre no seu terminal e digite  <code>$ mysql -u root -p</code> logo então, crie um database usando o comando <code>$ create database example</code>, agora, crie um usuário para poder manipular as informações desse database usando <code> CREATE USER 'userOrmExample'@'localhost' IDENTIFIED BY 'password';</code> em seguida, você deve adcionar os privilégios para este usuário, utilize o seguinte comando :  <code> $ GRANT ALL PRIVILEGES ON example . * TO 'userOrmExample'@'localhost'</code>. <br/>
 
> Obs: caso você queria mudar alguma dessas informações, deve alterar os respectivos valores no arquivo, [**config.py**](https://github.com/hitallow/ormExampleWithFlask/blob/master/config.py/).
</li>
</ul>
4 - > Para iniciar seu database <code> $ python run.py db migrate </code> para iniciar a pasta de migrações utilize <code>$ python run.py db migrate</code> e por fim, rode <code>$ flask db upgrade </code> e está tudo pronto.
<br>
5 -> Tudo pronto, agora rode em seu terminal <code>python run.py runserver</code>, verifique onde o sistema está rodando, e digite este endereço na barra de endereços do seu navegador.




