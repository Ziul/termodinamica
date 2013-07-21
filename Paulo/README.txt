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

# Uso:

	Vá ate o diretório conde se encontra os arquivos pelo terminal e entre com o seguinte comando:
		python main.py
		
	O programa será carregado, apresentando no momento a tela de estado termodinâmico. O texto que surgirá será algo semelhante à:
	
		0. < Temperature >                [°C]
		1. < Volume >               [m³/kg]
		2. exit 


	Todo o texto que  tiver entre <> poderá ser alterado utilizando as setas <- e -> do teclado. As setas para cima e para baixo selecionam a linha. Se a linha selecionada
	não for a 'exit', o usuário poderá escrever um numero qualquer que deseja para aquela linha, pressionando ENTER após escrever o numero para efetivar a entrada deste. 
	Segue um exemplo de uma tela já preenchida:
	
		0. < Pressure >           20.0 [kPa]
		1. < Entropy >            2.0[kJ/kg.K]
		2. exit 

		 
	Se o usuário quiser, ele pode entrar com valores em notação cientifica, como  3e25 ou 5e-6. Preenchido os valores para as duas primeiras linhas,  o usuário deve pressionar 
	ENTER novamente, para que seja calculado a entrada dos dados e apresentado a saída, como segue abaixo:
	
		0. < Pressure >           20.0 [kPa]
		1. < Entropy >            2.0[kJ/kg.K]
		2. exit 


           Esta no estado de água saturada

  Temperature           =       60.06 [°C]
     Pressure           =       20.0 [kPa]
   Volume_min           =       0.001017 [m³/kg]
   Volume_max           =       7.6481 [m³/kg]
   Energy_min           =       251.4 [kJ/kg]
   Energy_max           =       2456.0 [kJ/kg]
 Enthalpy_min           =       251.42 [kJ/kg]
 Enthalpy_max           =       2608.9 [kJ/kg]
  Entropy_min           =       0.832 [kJ/kg.K]
  Entropy_max           =       7.9073 [kJ/kg.K]
        Titulo          =       0.165081339307
-------------------------------------------------------------
              Valores interpolados:

       Volume           =       0.632380239439 [m³/kg]
       Energy           =       474.87060902 [kJ/kg]
     Enthalpy           =       487.512728224 [kJ/kg]
      Entropy           =       1.5533476743 [kJ/kg.K]


	Caso o usuário entre com valores que não se encaixem em água saturada, o programa irá requisitar um novo valore de pressão, afim de selecionar qual tabela será
	consultada para fornecer os dados. Nesta nova tela, será apresentado valores de pressão já pre-definidos, como apresentado abaixo:
	
            é necessário a entrada de um novo valor de pressão


	Pressure                <10> [kPa]

	Utilizando <- e -> novamente, selecione qual pressão deseja selecionar e pressione ENTER para continuar. Será então apresentado os valores calculado, caso seja possível:
	
            é necessário a entrada de um novo valor de pressão


	Pressure                <200> [kPa]


          Esta no estado vapor superaquecido

  Temperature           =       594.378238342 [°C]
     Pressure           =       200.0 [kPa]
       Volume           =       2.0 [m³/kg]
       Energy           =       3292.59803109 [kJ/kg]
     Enthalpy           =       3692.59515544 [kJ/kg]
      Entropy           =       8.76445854922 [kJ/kg.K]

	


	Caso sejam fornecidos dados que não estejam no intervalo da tabela, o programa irá apresentar o erro:
	
               é necessário a entrada de um novo valor de pressão


	Pressure                <50> [kPa]


          Esta no estado vapor superaquecido


	Faixa de valores fora do intervalo de amostra
	A value in x_new is below the interpolation range.

	Provavelmente fora do intervalo de interpolação

	
	Observe que o programa caracteriza em qual estado estaria a matéria, porém a linha "A value in x_new is below the interpolation range." indica que o valor para a segunda entrada 
	(no caso o valor de volume era 2, sendo que seria necessário o valor mínimo de 3.2403) estava abaixo do menor valor existente na tabela.
	
	Em alguns momento, a tela não é atualizada com o devido estado do menu. Esta atualização pode ser forçada com o pressionamento da setas para cima ou para baixo.
	
	Caso o usuário tente rodar o programa sem entrar com algum dado, ou o programa entre em algum caso de erro, será apresentada a mensagem de erro na tela (conforme abaixo), 
	de preferência sem que o programa seja finalizado, podendo voltar ao estado anterior pressionando as setas para cima ou para baixo:
	
		0. < Temperature >                [°C]
		1. < Volume >               [m³/kg]
		2. exit 


		local variable 'value2' referenced before assignment
		['Temperature', ' ']

