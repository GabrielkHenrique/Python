#Meu primeiro programa de verdade em python não foi finalizado mas espero um dia retomar esse projeto com um conhecimento maior e fazer oq eu quero
print('bem vindo qual será seu nome?')
nome = input('Digite seu nome')
print('Sistema:Os comandos basicos são: A para atacar D para defender F para fugir')
hp = 10
print('Você era um fazendeiro vivendo no interior de um reino ditsante mas desistiu e foi viver grander aventuras!.'
 'você equipou sua unica arma um machado dado pelo seu avô há muito tempo e partiu para a floresta negra lá você encontrou um pequeno goblin distraido')
e1 = input('O que deseja fazer?(A para atacar D para defender F para fugir )')
def evento1():
    if e1 == "A":
        print('Você atacou globin de surpresa mas ainda sim ele conseguiu revidar você perdeu 1 ponto de vida mas o derrotou seu hp esta em')
        hp =9
        print(hp)
    elif e1 == 'D':
        print('Ele não te atacou para você querer defender mas ao ver você se protegendo ele só te ignorou e continuou andando')
        print(hp)
    elif e1 == 'F':
        print('Ele te olhou com uma cara estranha enquanto você se esgueirava para fugir dele mas ele nem ligou mas isso também aumentou muito seu ego')
        print('mais tarde naquele mesmo dia voltando pra sua tribo esse pequeno goblin se exibiu de ter afugentado um humano e foi parabenizado por seus')
        print('companheiros, entre os goblin você ficou conheciodo como mido que na lingua deles significa aquele que teme')
    else:
        print('Esse comando não foi reconhecido não se esqueça de não dar espaçoes e que a letra seja maiscula!')

evento1()
print('============================================================================================================')
print('Após seu encontro com esse pequeno monstro você percebeu que o caminho não seria facil mas você não desistiu e seguiu em direção ao ')
direcao = input('Escolha a direção (N para norte, S para o sul,O para oeste e L para o leste)')
def evento2():
    if direcao == 'N':
        print('Você foi para o norte e subiu numa montanha gelada demorou mais de uma semana lá você encontrou uma mansão e um senhor com cabelos e barbas longas e brancas te avistou!')
        print('velho:há tanto tempo não veja uma pessoa por aqui... venha entre!')
        print('Você decide entrar e conta as suas histórias até ali e descobre que aquele senhor mora ali sozinho já que sua esposa faleceu seu nome é Smith')
        print('Sr Smith: Oh então está viajando sem rumo? nessa idade! aliás quantos anos você tem?')
        idade = input('Minha idade é')
        def idade1():
            if idade <= 18:
                print('Smith: Você é muito jovem! é perigosos sair andando assim')
            else:
                print('Smith: Achei que fosse mais novo perdão')
        idade1()
        print('Bom acho que o melhor caminho pra quem está sem caminho seria ou uma cidade grande ou uma dungeon mas não acho que você possa ir em uma dungeon com um rank tão baixo')
        print('Eu sugiro que vá para uma guilda descobrir seu rank')
        print('Muitos dias se passraram da sua viagem até a cidade grande mais proxima a cidade Lexisan')
    elif direcao == 'S':
        print('O sul era um lugar desertico você não achou nada mas quando estava a beira da morte no meio do nada alguns mercadores de escravos deacharam e você foi escravizado')
        print('O lider dos mercadores era um homem baixinho que usava um terno branco seus cabelos eram vermelhos mesmo sendo baixo dava uma sensação assustadora olhar para ele')
        print('Você foi preso em uma jaula e perdeu a conta de quanto tempo ficou lá')
        print('Você conseguiu fazer alguns amigos mesmo numa situação tão tragica todo dia você se arrependia de ter escolhido o sul e de ter começado essa aventura')
        print('Seu melhor amigo era um homem raposa que ficava na cela ao lado depois de mais 1 anos preso os mercadores de escravos se meteram em problemas e morreram evocê consgeuiu fugir')
        print('Noah:Sugiro que você vá a Lexisan e se junte a uma guilda nós fizemos tanto esforço físico trabalhando aqui tenho certeza que arrumara um emprego lá ')
        print( 'eu voltarei pra minha terra natal')
    elif direcao == 'O':
        print('Você foi para o oeste lá achou uma praia era linda e tinha muita gente você nadou e fez alguns amigos e conseguiu um lugar para comer e dormir mas eles mandaram você embora depois de uns dias')
        print('Eles te aconselharam a ir a capital e ir na guilda para arrumar algum emprego')
    elif direcao == 'L':
        print('Você chegou numa grande cidade e achou um panfleto dizendo que a guilda estava recrutando e você foi até lá')
    else:
        print('Esse comando não foi reconhecido não se esqueça de não dar espaçoes e que a letra seja maiscula!')
        evento2()
evento2()



