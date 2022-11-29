# Flappy Bird

O PyGame foi um projeto proposto pelos professores e coordenadores da disciplina "Design de Software" do curso de Engenharia do Instituto de Ensino e Pesquisa (Insper). O projeto consiste na criação e desenvolvimento de um jogo escolhido pelos desenvolvedores escrito totalmente na linguagem Python, o projeto teve um desenvolvimento que durou aproximadamente 3 semanas e o jogo conta com aspectos comumente encontrados nos jogos atualmente, como: efeitos sonoros, jogabilidade fluida e desafiadora.

Nome do Jogo: Flappy Bird

Desenvolvedores: Gabriel Fernando Missaka Mendes e Luigi Zema Matizonkas

## Como se joga

No jogo, o jogador deverá clicar com o botão do mouse para fazer com que o personagem (que é um passáro) passe por entre os canos que aparecerão durante o jogo, tomando cuidado para não bater neles. 

## Como Baixar o Jogo

1 - Primeiramente acesse o link do jogo no GitHub: https://github.com/gabrielfmendesm/Projeto-Final-Flappy-Bird.

2 - Após acessar o link, clique no botão verde "Code" ou "Código" e clique em "Download ZIP" (ou se preferir, poderá abrir com o github desktop) para baixar o pasta compactada com os arquivos do jogo.

3 - Após efetuar o download da pasta, abra ela no seu IDE de prefêrencia (VsCode, PyCharm, etc).

4 - Assim que todos os arquivos estiverem prontos, execute o arquivo "jogo.py" ele irá executar o código raiz do jogo que fará com que o Flappy Bird seja executado. 

5 - Assim que a tela do jogo abrir, tudo estará pronto para jogar.

## Requisitos

É necessário instalar o seguinte pacote no Python:
* PyGame

Para instalar esse pacote no Python, digite o seguinte comando no terminal do seu IDE:

```bash
pip install pygame
```

## Instruções do Jogo

O objetivo principal em Flappy Bird é clicar com o botão do mouse para guiar o personagem por entre os canos que aparecerem. A cada clicada, o personagem voa para cima elevendo a sua altura e possibilitando a passagem pelo meio dos canos, caso o jogador não clique no mouse, o personagem irá parar de voar e começará a cair. Além das instruções básicas, existem algumas regras:

* Caso o personagem toque em qualquer parte dos canos, falhando em passar pelo meio, o jogador perderá o controle do personagem e uma tela de Game Over aparecerá;

* O jogador precisa evitar fazer com que o personagem (passáro) toque no chão ou na parte superior da tela, caso isso ocorrá o jogador também perderá o controle do personagem e o jogo será perdido;

* A pontuação só será contada caso o jogador passe com o personagem entre os canos (sendo a única maneira dele se manter vivo), caso contrário ele perderá o jogo;
    
* A cada passada por entre os canos, a pontuação do jogador aumenta e ao final de cada jogada, a jogada com maior pontuação fica guardada para outros tentarem bate-la.

 ## Outras Informações
 
 Vídeo de Demonstração do Jogo: 

 Referências do jogo: Utilizamos as imagens, sprites e áudios do seguinte repositório a baixo no jogo.
 
 Link do Repositório GitHub: https://github.com/samuelcust/flappy-bird-assets.
