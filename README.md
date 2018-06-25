# Lógica de Programação Apliaca à Criação e Análise da Forma

<hr>

Prof. Fernando Ferraz Ribeiro \| fernando.ribeiro@ufba.br

<hr>

[Informações](./Ficha_de_inscricao/informacoes.md)

<hr>

Forum de comunicação do curso:

[https://groups.google.com/forum/#!forum/20181lpacaf](https://groups.google.com/forum/#!forum/20181lpacaf)

<hr>

## [Guia de instalação do ambiente de  Trabalho](./guia_install/readme.md)

## Plano de Curso

<hr>
<hr>

### Aula 01 - (12/4/2018)


[SLIDES](./Aula_01/Aula_01-introducao_a_programacao.pdf)

1. Apresentação do curso

    * Metodoloagia
    * Avaliações

1. Funcionamento do Laboratório


1. Introdução

   * Conceito de algoritmo
   * História da programação
   * Programação Aplicada à arquitetura e urbanismo
   * A linguagem Python

1. Instalação

    * CPython 2.7x IDLE


1. Operações matemáticas no Python Shell

   * Operadores matemáticos

   * Divisão inteira e divisão real

      * Mod e Div

   * Níveis de Parênteses


1. Exercício sugerido 01 - Use o Python Shell como uma calculadora


1. Referências e *links* ùteis

   * Python

      [Python Foundaition](https://www.python.org/)

      [Python Brasil](http://python.org.br/)

   * Rhinoceros

      [Rhino3D.com](http://www.rhino3d.com/)

      [food 4 Rhino](http://www.food4rhino.com/)
   * Grasshopper

      [Grasshopper 3d](http://www.grasshopper3d.com/)

   * Between the Folds

      [Between the Folds](https://www.betweenthefolds.com/)



<hr>

### Aula 02 - (19/4/2018)

[notas de aula](https://github.com/255ribeiro/LPACAF/blob/master/Aula_02/LPACAF-Aula_02.ipynb)


1. Variáveis
    * Tipos de variáveis
        * Lógicas
        * Inteiras
        * Reais (ponto flutuante)
        * *Strings*

1. Editor de arquivos

   * abrir editor
   * salvar arquivo
   * editar
   * executar


1. Entradas e saídas
    * input()
    * raw_input()
    * print

1. Condicionais lógicas

   * if
   * else
   * elif



1. Exercício 02 - inverter os algarismos de um número inteiro de 3 digitos usando Mod e/ou Div


1. Arquivos dos Exemplos da Aula

[Calcúlo do número de espelhos de uma escada](./Aula_02/escada_aula_02.py)

1. Referências e *links* ùteis

Cursos de Python:

   * Em portugues:

      [Tutoriais para iniciantes sugeridos pela comunidade Python Brasil](http://python.org.br/introducao)

      [Apostilas de Python sugeridas pelo blog Café com Código](http://cafecomcodig0.com.br/5-apostilas-de-python-gratis-pdf/)


<hr>

### Aula 03 - (26/4/2018)

[notas de aula](https://github.com/255ribeiro/LPACAF/blob/master/Aula_03/LPACAF-Aula_03.ipynb)

1. Palavras reservadas

   * [Lista de palavras reservadas do Python 2.7x](https://docs.python.org/2/reference/lexical_analysis.html#keywords)

1. Funções e Métodos

   * [Funções *Built-in*](https://docs.python.org/2/library/functions.html#)


1. Bibliotecas

   * Importanto módulos
       * [Biblioteca keyword](https://docs.python.org/2/library/keyword.html)

       * [Biblioteca Math](https://docs.python.org/2/library/math.html)
            * math.sin()
            * math.sqrt()

       * [Biblioteca datetime](https://docs.python.org/2/library/datetime.html)
            * datetime.date()
            * datetime.timedelta()

   * 3 formas de importação

      * import *nome_do_módulo*
      * import *nome_do_módulo* as *chamada_do_módulo*
      * from *nome_do_módulo* import *função_ou_classe_do_módulo*

   * importação from \_\_future\_\_

1. Funções definidas pelo usuário

   * def
   * parâmetros de entrada
   * retorno

1. Exercício 03 - [Bhaskara](./Aula_03/Bhaskara.pdf)

1. Referências e *links* ùteis

   * IDE [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows)

   * Distribuição [Anaconda](https://www.anaconda.com/download/)

   * O software [Processing](https://processing.org/download/) possui um modo de programação em Python

<hr>

### Aula 04 - (3/5/2018)

[Arquivo da Aula](./Aula_04/AULA_04.gh) <br /> Clique com o botão direito para baixar

1. iteráveis

   * [listas](https://docs.python.org/2/tutorial/datastructures.html#)
      * fila
      * pilha
      * lista
      * operações em listas
         * função range()
         * função len()
         * função list()

   * tuples

   * strings

1. Repetições

   * while

   * for

1. Exercício 04 - Sequência de Fibonacci

1. Arquivos dos Exemplos da Aula

    [Arquivo .gh da Aula - Final](./Aula_04/AULA_04_FINAL.gh) <br />
    [Exemplos Loops While e For](./Aula_04/exemplos_for_e_while.py) <br />
    [Exemplo Loop For](./Aula_04/exemploFor.py)


1. Referências e *links* ùteis

<hr>

### Aula 05 - (10/5/2018)

1. Alguns comandos do Rhinoceros

    * Curvas
        - Point
        - Line
        - Circle
        - Arc
        - Polyline
        - Curve
        - InterpCrv

    * Superfícies
        * PlanarSrf
        * ExtrudeCrv
        * ExtrudeSrf
        * Pipe
        * Loft

    * Sólidos
        - Cap
        - Box
        - Sphere
        - BooleanUnion
        - BooleanDifference
        - BooleanIntersection

1. Editor de Python do Rhinoceros

    * Abrindo o Editor
    * imptando Bibliotecas
    * Criando geometria (rs.Add...)
    * Utilizando variáveis
    * Entrada de dados (rs.Get...)
    * Loops
    * Armazenando Geometria em listas.


1. Exercício 05 - Inverter os algarismos de um número inteiro de qualquer tamanho usando listas.

1. Arquivos dos Exemplos da Aula
    * [Pilar Tubular - Extrude](./Aula_05/exemplo_rhino_pilar_tubular_extrude.py)
    * [Pilar Tubular - Pipe](./Aula_05/exemplo_rhino_pilar_tubular_pipe.py)

1. Referências e *links* ùteis

    * [Tutorial Rhino Modelagem 3D](https://www.youtube.com/watch?v=NKkXMKKA_Cs&list=PL68tctImfhCR2zFIxzEs95v5ETSXe9r14)

    * [Rhino Python](http://developer.rhino3d.com/5/guides/rhinopython/)

    * [Tutorial Rhino Python em vídeo (eng)](https://www.youtube.com/watch?v=wdY1T0XLzkE&list=PL594EB4471E93F2DA)

<hr>

### Aula 06 - (17/5/2018)

1. Instalação do Grasshopper
1. Instalação do Grasshopper Python Component

1. Interface do Grasshopper

   * Parâmetros de entrada
   * Sequência de comandos
   * Bake
   * Exemplos
   * Listas
   * Exemplos

1. Sequência de colunas no Grasshopper

1. Grasshopper Python Component (GhPython)

1. Exercício 06 - Criar sequência de colunas do GhPython.

1. Arquivos dos Exemplos da Aula
    * [Sequencia de Pilares - Rhino Python](./Aula_06/exemplo_rhino_pilotis_tubulares_pipe.py)
    * [Exemplo Didático - Revisão do Loop for](./Aula_06/exemplo_didatico_revisao_do_loop_for.py)
    * [Seqência de Pilares - Grasshopper](./Aula_06/Aula_06_sequencia_de_pilares.gh)

1. Referências e *links* ùteis

<hr>

### Aula 07 - (24/5/2018)

[Arquivo base da Aula](./Aula_07/AULA_07_base.gh)

1. Treliças


1. Arquivos dos Exemplos da Aula
    * [Treliças](./Aula_07/AULA_07_final.gh)


1. Referências e *links* ùteis

<hr>

### Alua 08 - (7/6/2018)

[Arquivo base da Aula](https://github.com/255ribeiro/LPACAF/blob/master/Aula_08/Aula_08_base.gh)

. Malha de pontos regular
   * Duplo for

1. Exercício 07 - Transformar Malha de Pontos em Malha de Pilares com altura paramétrica

[Arquivo final da Aula](https://github.com/255ribeiro/LPACAF/blob/master/Aula_08/Aula_08_final.gh)


1. Malha de pontos irregular
   * recebendo listas

[Arquivo base da Aula](https://github.com/255ribeiro/LPACAF/blob/master/Aula_08/Aula_08_base.gh)

[Arquivo Final da Aula](https://github.com/255ribeiro/LPACAF/blob/master/Aula_08/Aula_08_final.gh)

1. Exercício 08 - Adicionar linhas de eixo das vigas em um dos sentidos da malha

1. Referências e *links* ùteis



<hr>

### Alua 09 - (14/6/2018)

1. Malha de pontos irregular
   * recebendo listas

[Arquivo base da Aula](https://github.com/255ribeiro/LPACAF/blob/master/Aula_08/Aula_09_base.gh)

[Arquivo Final da Aula](https://github.com/255ribeiro/LPACAF/blob/master/Aula_08/Aula_09_final.gh)

1. Exercício 08 - Adicionar linhas de eixo das vigas em um dos sentidos da malha

1. Referências e *links* ùteis

<hr>

### Alua 10 - (21/6/2018)

[Arquivo base da Aula](https://github.com/255ribeiro/LPACAF/blob/master/Aula_10/Aula_10_base.gh)


1. Edfício de Multiplos pavimentos

1. Exercício 9 - ????

1. Referências e *links* ùteis

[Arquivo final da Aula](https://github.com/255ribeiro/LPACAF/blob/master/Aula_10/Aula_10_final.gh)


<hr>

### Alua 11 - (28/6/2018)

1. trabalhando com Planos Parte I

1. Exercício 12 - ????

1. Referências e *links* ùteis


<hr>

### Alua 12 - (5/7/2018)

1. trabalhando com Planos Parte II

[Arquivo base da Aula](https://github.com/255ribeiro/LPACAF/blob/master/Aula_12/Aula_12_base.gh)

[Arquivo final da Aula](https://github.com/255ribeiro/LPACAF/blob/master/Aula_12/Aula_12_final.gh)

1. Referências e *links* ùteis

<hr>

### Alua 13 - (12/7/2018)

1. trabalhando com Planos Parte III

1. Exercício 13 - ????

1. Referências e *links* ùteis

<hr>

### Alua 14 - (19/7/2018)

1. Fractais

[Arquivo base da Aula](https://github.com/255ribeiro/LPACAF/blob/master/Aula_14/Sierpinski3Dbase.gh)
1. Exercício 14 - ????

1. Referências e *links* ùteis

<hr>

### Alua 15 - (26/7/2018)

1. Orientação de trabalhos

<hr>

### Alua 16 - (???)

1. Orientação de trabalhos

<hr>

### Alua 17 - (2/8/2018)

1. Encerramento do Curso


2. Referências e *links* ùteis

[Tutoriais de C# para Grasshopper](http://designalyze.com/course/intro-c-scripting-grasshopper)

[Compilando um componente Python no Rhino 6](https://discourse.mcneel.com/t/tutorial-creating-a-grasshopper-component-with-the-python-ghpy-compiler/38552)

<hr>
<hr>
