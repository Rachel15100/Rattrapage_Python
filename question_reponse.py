import random

Question=[["Qu'est-ce que Git ?","Git est un système de gestion de versions décentralisé."] ,
          ["Qu'est-ce que Python ?" ,"Python est un langage de programmation interprété."], 
          ["Qu'est-ce que Linux ?" ,"Linux est un système d'exploitation open source."]]

def randomQuestion(Question):
    imin=0
    imax=len(Question)-1
    val=random.randint(imin, imax)
    choixQuestion=Question[val][0]
    reponseAttendue=Question[val][1]
    return choixQuestion, reponseAttendue

chaine=randomQuestion(Question)
question=chaine[0]
reponse=chaine[1]


def testReponse(question, reponse):
    print(question)
    test=input("Veuillez répondre à la question : \n")
    if test.lower()==reponse.lower():
        print("Bonne réponse")
    else:
        print("Faux, la réponse était : ", reponse)

testReponse(question, reponse)import random

Question=[["Qu'est-ce que Git ?","Git est un système de gestion de versions décentralisé."] ,
          ["Qu'est-ce que Python ?" ,"Python est un langage de programmation interprété."], 
          ["Qu'est-ce que Linux ?" ,"Linux est un système d'exploitation open source."]]

def randomQuestion(Question):
    imin=0
    imax=len(Question)-1
    val=random.randint(imin, imax)
    choixQuestion=Question[val][0]
    reponseAttendue=Question[val][1]
    return choixQuestion, reponseAttendue

chaine=randomQuestion(Question)
question=chaine[0]
reponse=chaine[1]


def testReponse(question, reponse):
    print(question)
    test=input("Veuillez répondre à la question : \n")
    if test.lower()==reponse.lower():
        print("Bonne réponse")
    else:
        print("Faux, la réponse était : ", reponse)

testReponse(question, reponse)
