# Discord-C2C
Simple command controll made in python using discord server and channel to interact

Ola a todos, sou estudante de cybersecurity e esse projeto foi feito apenas com finalidade de ESTUDO, o seu uso em ambientes NÃO autorizados é crime, e o autor não se responsabiliza por qualquer uso da ferramenta.

![image](https://github.com/FromAbbys/Discord-C2C/assets/99764742/4d83e341-a0d5-48e5-9316-3e7415ef57bc)

O command controll funciona de forma simples, ao criar um server no discord e adicionar seu bot, ele passara a responder os comandos do servidor como inputs para a vitima.

Exemplo:

![image](https://github.com/FromAbbys/Discord-C2C/assets/99764742/b81c12ae-3653-433f-808c-ef88da89ff73)


Suas funções e forma de uso sera explica de forma melhor abaixo. 


Command

Executa comandos na maquina alvo e tem um retorno da saida do mesmo. Ex: !command "ls -la"

A foto acima ilustra o resultado do comando.

Donwload

É possivel baixar arquivos do host que o bot esta rodando, basta voce executar o comando no discord: !donwload <path do arquivo>

Demonstração abaixo:

Arquivo na maquina alvo:
![image](https://github.com/FromAbbys/Discord-C2C/assets/99764742/b2d86411-56ab-479f-9732-272d2c71d2a1)

Executando o download:
![image](https://github.com/FromAbbys/Discord-C2C/assets/99764742/21d6bc80-ce2c-4fbb-8789-c7a934c9e233)


O arquivo sera enviado em outro canal:

![image](https://github.com/FromAbbys/Discord-C2C/assets/99764742/09307d34-a697-4687-bf71-db6c3a85eba1)


Upload

É possivel enviar arquivos para o computador alvo, no momento, o arquivo sera enviado diretamente para o local onde o codigo em execucao esta armazenado, exemplo, se o arquivo do executavel ou do python estiver no diretorio home, o upload sera feito para la.
Um pouco diferente no uso basta executar o comando da seguinte forma, escolher um arquivo para ser usado de upload, e digitar o comando !upload e enviar junto do anexo, que o mesmo sera salvo:


Arquivo que sera upado:
![image](https://github.com/FromAbbys/Discord-C2C/assets/99764742/b7a46284-f070-4cbd-8dea-14b72842be02)

Comando sendo executado:

![image](https://github.com/FromAbbys/Discord-C2C/assets/99764742/6b8f23db-18f4-4857-814f-a0f9164a7e2c)


E agora, no diretorio onde o codigo esta salvo:

![image](https://github.com/FromAbbys/Discord-C2C/assets/99764742/efde6bbe-491e-40dc-9ac3-daca91d0f90d)


![image](https://github.com/FromAbbys/Discord-C2C/assets/99764742/f44fb436-f5bd-4ff8-8e05-7d47aa161494)



Shot

Tira um print da tela principal do alvo, para usar basta !shot 


Webcam

A webcam é ligada, tira uma foto, e a envia para o discord, logo apos a webcam é desligada e o arquivo apagado do buffer. O uso: !webcam, no caso de não existencia de webcam ou erro ao iniciar a mesma, uma mensagem de erro sera enviada.

Limpar

Comando para apagar as mensagem do chat do discord, uso: !limpar
