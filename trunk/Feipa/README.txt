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
	
	- janela.py
		Arquivo contendo os objetos de interface que serão utilizados pelo programa
		
	- termo.py
		Este arquivo contem as rotinas de gerenciamento das interfaces de acordo com a primeira parte do programa, decidindo em
		qual estado a matéria se encontra e tomando as devidas decisões
		
	-rankine.py
		Este arquivo contem a interface do novo módulo, onde é carregada a imagem da turbina e requisitado ao usuario que entre com
		as condições de cada turbina, apresentando assim o calculo das entalpias quando os valores são validos, ou apresentando '-----'
		quando é inserido valores inválidos para o calculo.
	
	- main.py
		Este arquivo é bem simples e simplesmente inicializa uma aplicação, pede ao usuário que escolha entre o modulo para o ciclo de Rankine ou 
		o calculo do estado termodinâmico. Em seguida é feito a chamada do modulo ao qual o usuário escolheu.
