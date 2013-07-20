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
	
	- output.py
		Este arquivo é responsável por construir a saída da primeira aba (primeira etapa do programa)
		
		Das linhas 13 a 22 o programa recebe os valores e campos escolhidos pelo usuário, testa se são validos e
		cria as variáveis de interpolações máximas e mínimas.
		Nas linhas 28,29,55 e 77 o programa designa em qual caso as condições se encontram.
		Se estiver em água saturada, é interpolado então todos os valores máximos e mínimos, assim como o titulo.
		Caso esteja em superaquecido ou comprimido, é carregada uma nova tabela de valores e em seguida interpolados os
		valores. Em todas as três condições, os valores são gravados na variável vlr, onde o campo ['data'] possui o output
		impresso na tela em forma de string, e os demais campos, como ['Pressure'] ou ['Energy'] contem os valores exatos na
		forma de float. A variável vlr é retornada por este módulo. 
		
	- output1.py
		Este arquivo contem o tratamento dos dados da saída da segunda etapa do programa (turbina). Como retorno, é gerado uma string 'prova'
		contendo o texto a ser impresso na tela.
		
	- ui.py
		Este arquivo controla toda a interface gráfica do programa. 
		A classe termo é responsável pela aparência da primeira aba (que
		contem a primeira parte do trabalho). O método show atualiza o quadro branco da saída enquanto a inicialização da classe é
		criado os botões/caixas de seleção/Texto da interface, decidido quem será ou não mostrado, seus estados iniciais e os eventos.
		A classe Rankine faz um processo análogo a classe Termo para a segunda aba/etapa do programa
		A classe MainUI é o núcleo da interface. Ela quem irá gerencias as classes Termo e Rankine, controlando as abas e atualização
		das saídas.
		
	- main.py
		Este arquivo é bem simples e simplesmente inicializa uma aplicação, pede ao sistema um frame e mantem o programa em um laço de funcionamento,
		limpando por fim a memoria utilizada pelo programa.
