# Descrição dos arquivos:

	
	- pontos.py
		Este arquivo será responsável pela leitura dos dados nas tabelas (arquivos *.csv) e gerar um objeto com os valores.
		#Objeto water
		
		Na linha 34 é aberto o arquivo csv e salvo na variável csvfile.
		Da linha 36 à 59 é gerado vetores contendo os dados de forma organizada.
		Da linha 61 à 65 é declarado os campos de interesse do objeto.
		Da linha 66 à 75 os vetores são copiados para os respectivos campos do objeto.
		O método print_all pode ser utilizado para imprimir todos os campos do objeto

		#Objeto waterNext
		
		Este objeto é semelhante ao objeto water, porém é reservado para as condições de vapor superaquecido e 
		liquido comprimido, onde há apenas um valor para cada campo.
	
	- saida.py
		Este arquivo é responsável por construir a saída da primeira aba (primeira etapa do programa)
		
		Das linhas 10 a 19 o programa recebe os valores e campos escolhidos pelo usuário, testa se são validos e
		cria as variáveis de interpolações máximas e mínimas.
		Nas linhas 23,24,40 e 52 o programa designa em qual caso as condições se encontram.
		Se estiver em água saturada, é interpolado então todos os valores máximos e mínimos, assim como o titulo.
		Caso esteja em superaquecido ou comprimido, é carregada uma nova tabela de valores e em seguida interpolados os
		valores. Em todas as três condições, os valores são gravados na variável 'valores' na forma de uma string
		
	- interface.py
		Este arquivo gerencia a interface do programa usando a biblioteca curses. A classe Menu apresenta a saída e projeta as chamadas dos cálculos iniciais.
		A classe SubMenu faz a leitura da pressão para os casos de superaquecido e liquido comprimido.
		a classe Data mantem armazenado os valores e opções escolhidos pelo usuário.
		
		
	- main.py
		Este arquivo é bem simples e simplesmente inicializa uma aplicação curses, mantendo ela presa no ambiente curses ate ser finalizada
