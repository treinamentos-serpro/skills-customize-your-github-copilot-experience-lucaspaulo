
# 📘 Assignment: Hangman Game

## 🎯 Objective

Pratique manipulação de strings, loops, condicionais, entrada de dados e seleção aleatória em Python ao criar uma versão funcional do jogo da Forca.

## 📝 Tasks

### 🛠️ Inicializar o Jogo

#### Descrição
Prepare o estado inicial do jogo selecionando uma palavra secreta aleatoriamente e criando as variáveis necessárias para acompanhar os palpites do jogador.

#### Requisitos
O programa concluído deve:

- Selecionar a palavra secreta aleatoriamente a partir da lista fornecida.
- Criar uma coleção para armazenar as letras já adivinhadas.
- Definir o número máximo de tentativas incorretas permitidas.
- Exibir a palavra oculta usando um marcador para cada letra ainda não descoberta, como `_ _ _ _ _ _`.

### 🛠️ Implementar a Rodada de Adivinhação

#### Descrição
Implemente o loop principal para que o jogador informe letras, acompanhe seu progresso e receba o resultado final da partida.

#### Requisitos
O programa concluído deve:

- Solicitar ao jogador um palpite de letra a cada rodada.
- Atualizar o progresso quando o palpite estiver na palavra secreta.
- Reduzir o número de tentativas restantes quando o palpite estiver incorreto.
- Encerrar quando todas as letras forem descobertas ou quando as tentativas incorretas terminarem.
- Exibir uma mensagem informando se o jogador venceu ou perdeu.