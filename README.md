# Projeto da disciplina
Este trabalho tem como objetivo a implementação de uma aplicação de rede para no mínimo 3 computadores ou conexões. Deve-se utilizar os conceitos de socket, considerando funções primitivas, como socket(), read() ou recv(), write(), dependendo da linguagem utilizada, o nome dessas funções pode mudar. Linguagens permitidas: C, C++, Python, Node, PHP e Java. Uso de Thread é obrigatório.

# INTRODUÇÃO
A aplicação escolhida para implementação foi o jogo da forca. O jogo da forca é um jogo no qual o jogador (ou jogadores) tem que acertar qual é a palavra proposta, tendo como dica o número de letras (indicado pela quantidade de _) e o tema ligado à palavra. O jogo termina quando a palavra é acertada ou quando as partes corpóreas do enforcado são preenchidas.
	Para começar o jogo, é necessário desenhar o número de riscos ou _ correspondentes ao lugar de cada letra da palavra. Por exemplo:
JOGO DA FORCA => _ _ _ _   _ _   _ _ _ _ _
	Feito isso, o jogador da vez deve tentar adivinhar a palavra ou chutar uma letra. Cada letra acertada é colocada no espaço correspondente.
	JOGO DA FORCA => _ O _ O   _ _   _ O _ _ _
	Contudo, se a letra escolhida não estiver na palavra, então uma parte do corpo do enforcado é preenchida. Além disso, o jogador pode escolher entre falar uma letra ou tentar adivinhar a palavra falando a palavra que pensa que é. Caso o jogador tente adivinhar a palavra  e erre, então ele é eliminado (ou perderá o jogo, caso seja o único jogador).

# PRINCIPAIS FUNCIONALIDADES DA APLICAÇÃO
A classe Player() foi destinada para salvar as informações dos clientes (jogadores). Tais como o id, o nome, o score, o endereço e o cliente.
A classe Hangman() foi implementada para iniciar o servidor. Tem como principal função gerenciar a lógica do jogo.

