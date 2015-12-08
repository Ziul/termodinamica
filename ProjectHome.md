# Trabalho #

### Support for ###

  1. Python 2.7.x


---


Pacotes necessários para o programa funcionar::

  1. wxpython	->	_criação das janelas_
  1. scipy		->	_garantir a interpolação_
  1. numpy		->	_dependência da scipy_

## Instalação dos pacotes ##

##### Ubuntu #####
```bash

```
	sudo apt-get install python-matplot* scipy* python-wxgtk2.8
```
```
##### Fedora #####
```bash

```
	sudo yum install python-matplot* scipy* python-wxgtk2.8
```
```
##### Windos / MacOS #####

  * Instalando o Python

> Execute o "python-2.7.5.msi", que pode ser baixado de: http://www.python.org/download/releases/2.7.5/

> É altamente recomendado que instale a versão 32bits no windows, por não haver a biblioteca _Numpy_ já compilada para Windows 64bits

> Baixe o arquivo http://python-distribute.org/distribute_setup.py e execute-o (2 cliques)

> Set os endereços C:\Python27\;C:\Python27\Scripts\ como variáveis de ambiente (PATH)
> > Tutorial ensinando a setar variaveis de ambiente:
> > > http://www.computerhope.com/issues/ch000549.htm


> Normalmente algumas versões do Windows requerem uma reinicialização par recarregar as novas variáveis de ambiente.

> Abra o promt de comando e entre com a seguinte linha de comando:
```
		easy_install pip
```
  * Instalando as bibliotecas extras

> Em seguida digite:
> ```bash

```
		pip install virtualenv
		pip install wx
		pip install pylab
		pip install scipy
		pip install numpy
```
```
> Caso uma das linhas acima venha a apresentar erros de não encontrar o pacote, pode-se baixar os executaveis para instalação nos seguintes endereços:

> http://sourceforge.net/projects/numpy/files/NumPy/1.7.0/

> http://sourceforge.net/projects/scipy/files/scipy/0.11.0/

> http://sourceforge.net/projects/wxpython/files/wxPython/2.9.4.0/

> http://sourceforge.net/projects/matplotlib/files/matplotlib/matplotlib-1.2.0/

> Obs.: É importante observar que muitas vezes os servidores do pip estão sobrecarregados e o arquivo apenas não termina o download.


## Executando o programa ##

  * Para inicializar o programa, inicialize o arquivo "main.py".
> > É importante frisar que os demais arquivos devem estar na mesma organização apresentada no arquivo compactado

  * Ao inicializar o programa, será requisitada a escolha entre
> > 'Pressão' ou 'Temperatura'

  * Na janela seguinte, será requisitada a escolha entre:
> > 'Volume Especifico','Energia Interna', 'Entalpia' ou 'Entropia'

  * Na janela seguinte será requisitado um valor para a escolha feita de 'Temperatura' ou 'Pressão'.

  * Na próxima janela será requisitado um valor para a escolha entre as quatro outras opções.

  * Se os valores inseridos estiverem no intervalo do banco de dados (tabelas), o programa apresentará os resultados em uma nova janela

  * Caso o intervalo esteja fora do previsto, o programa dará um erro, avisando a falha

  * Por fim o programa irá se fechar

  * Para reiniciar o programa, basta reabri-lo

## Observações ##


> Python é uma linguagem interpretada. Desta forma, criar um executável é, de certa forma, incoerente - porém não impossível.
> A forma padrão mais próxima de como é criado um 'executável' de um programa em Python é inserir o trexo "#!/usr/bin/python"
> em sua primeira linha e dar permissões de executável ao arquivo `*`.py. Desta forma o código torna-se um script executável.

> É possível gerar um arquivo compilado (e assim sendo binário) de um programa em Python. Basta o comando:
```
		python -m py_compile *.py
```
> Desta forma para cada `*`.py será criado um respectivo `*`.pyc. Em todo caso, será necessário as bibliotecas no sistema para
> que o programa continue sendo executado.