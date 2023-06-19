# Discord-C2C
Simple command controll made in python using discord server and channel to interact

Ola a todos, sou estudante de cybersecurity e esse projeto foi feito apenas com finalidade de ESTUDO, o seu uso em ambientes NÃO autorizados é crime, e o autor não se responsabiliza por qualquer uso da ferramenta.

![image](https://github.com/FromAbbys/Discord-C2C/assets/99764742/4d83e341-a0d5-48e5-9316-3e7415ef57bc)

O command controll funciona de forma simples, ao criar um server no discord e adicionar seu bot, ele passara a responder os comandos do servidor como inputs para a vitima.

Exemplo:

![image](https://github.com/FromAbbys/Discord-C2C/assets/99764742/b8b5ee00-f23e-42a9-a43f-8fe5e570981d)

Suas funções e forma de uso sera explica de forma melhor abaixo. 


Command

Executa comandos na maquina alvo e tem um retorno da saida do mesmo. Ex: !command "ls -la"

A foto acima ilustra o resultado do comando.

Donwload

É possivel baixar arquivos do host que o bot esta rodando, basta voce executar o comando no discord: !donwload <path do arquivo>

Demonstração abaixo:

![image](https://github.com/FromAbbys/Discord-C2C/assets/99764742/d12d517b-9caa-44f9-b939-0d39bae16dce)

O arquivo sera enviado em outro canal:

![image](https://github.com/FromAbbys/Discord-C2C/assets/99764742/3aac2bfe-98cf-4586-8616-fd9f23a5eded)


Upload

É possivel enviar arquivos para o computador alvo, no momento, o arquivo sera enviado diretamente para o local onde o codigo em execucao esta armazenado, exemplo, se o arquivo do executavel ou do python estiver no diretorio home, o upload sera feito para la.
Um pouco diferente no uso basta executar o comando da seguinte forma, escolher um arquivo para ser usado de upload, e digitar o comando !upload e enviar junto do anexo, que o mesmo sera salvo:

![image](https://github.com/FromAbbys/Discord-C2C/assets/99764742/69af50b3-bab9-4e38-a3e7-77e361a5d6f7)

![image](https://github.com/FromAbbys/Discord-C2C/assets/99764742/adc21685-b5ca-4ee6-9610-eda313259b7d)

E agora, no diretorio onde o codigo esta salvo:

![image](https://github.com/FromAbbys/Discord-C2C/assets/99764742/a7a1016b-d90a-4a50-a6b1-ebdc3e55dab0)



Shot

Tira um print da tela principal do alvo, para usar basta !shot 


Webcam

A webcam é ligada, tira uma foto, e a envia para o discord, logo apos a webcam é desligada e o arquivo apagado do buffer. O uso: !webcam, no caso de não existencia de webcam ou erro ao iniciar a mesma, uma mensagem de erro sera enviada.

Limpar

Comando para apagar as mensagem do chat do discord, uso: !limpar
