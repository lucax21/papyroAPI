# Papyro: uma rede social para leitores

A quantidade de leitores no Brasil vem decaindo, segundo dados da pesquisa Retratos da Leitura no Brasil, feita pelo Instituto Pró-Livro (IPL) (2020). De 2015 para 2019, a porcentagem de leitores no Brasil caiu de 56% para 52%. O número de brasileiros com mais de 5 anos que nunca leram nenhum livro, nos últimos três meses, representam 48% da população. O brasileiro lê, em média, cinco livros por ano, sendo aproximadamente 2,4 livros lidos apenas em parte e 2,5 inteiros. Segundo o estudo, um dos fatores que influencia a leitura é o incentivo de outras pessoas.

Assim, essa rede social nasce com o intuito de incentivar a interação social e a leitura, compreendendo os seguintes pontos:

1.	Permitir a criação e a visualização de avaliações de livros.
2.	Permitir a criação e o gerenciamento do histórico de livros do usuário.
3.	Permitir buscas de usuários e livros.
4.	Permitir a criação e o gerenciamento de conta de usuário.
5.	Prover uma interface intuitiva.

## Como funciona?

Para que seja possível a execução, é necessário que uma série de requisitos sejam instalados antes da entrada no projeto. Esses requisitos são:
-	Docker v20.10.17 (ou equivalente)
-	Yarn v1.22.19
-	Node v8.11.0
-	Expo v5.4.12
-	Android Studio (Opcional)
-	Visual Code (Opcional)
-	ESLint v2.2.6 (Opcional)
-	WSL v2

E deve ser executado junto a sua API https://github.com/wgiacomin/papyro, nosso frontend.

## Passo a Passo (Windows):

Para a execução do backend, é necessário que o repositório esteja baixado, o Docker esteja em execução e exista um arquivo denominado .env junto ao repositório. Esse arquivo deve ter sido disponibilizado por algum membro da equipe.

Após conferir a existência de todas os pré-requisitos, abra o PowerShell como Administrador (menu Iniciar > PowerShell > clique com o botão direito do mouse > Executar como Administrador), navegue até o repositório utilizando o comando “cd” e insira o comando `docker compose build` e posteriormente `docker compose up`.
Esse comando será mantido em execução pelo tempo em que o backend estiver sendo necessário. Os dois comandos, juntos, garantem a subida do banco de dados e a construção do sistema utilizado na API. Porém, um último passo é necessário para que os dados artificiais sejam inseridos e o banco de dados tenha suas tabelas alimentadas. Para que isso seja, possível, abra um novo terminal no Powershell e execute o comando `docker ps`.

Observe que existirão dois containers em execução. Procure pelo container chamado “papyroapi_api” ou algo similar e copie o “CONTAINER ID” dele. Com essa informação, execute o comando `docker exec <CONTAINER ID> alembic upgrade head`. Isso irá permitir que tantos os dados tanto o banco sejam atualizados para a última versão e contenham dados de teste.




