import pytholog as pl

def kings():
    kb = pl.KnowledgeBase("Kings")

    #TELL
    kb(
        [
           "king(john)", # John is a King
           "person(richard)", #Richard is a person
           "person(X) :- king(X)", #If X is a king then X is also a person
           "brother(richard,john)",
        ]
    )

    #ASK
    print(kb.query(pl.Expr("king(john)")))
    print(kb.query(pl.Expr("king(richard)")))
    print(kb.query(pl.Expr("brother(richard, X)")))

def animals():
    kb = pl.KnowledgeBase("animals")
    kb([
        #TELL
        "animal(X) :- mammal(X)", # all mammals are animals
        "mammal(X) :- feline(X)", # all felines are mammals
        "feline(X) :- cat(X)", # all cats are feline
        "feline(X) :- lion(X)", # all lions are feline
        "mammal(X) :- canine(X)", # all canines are mammals
        "canine(X) :- dog(X)", # all dogs are canines
        "canine(X) :- wolve(X)", # all wolves are canines
        "animal(X) :- reptile(X)", # all reptiles are animals
        "reptile(X) :- turtle(X)",  # all turtles are reptiles.
        "dog(beagle)",
        "wolve(gray)",
        "lion(african)",
        "turtle(loggerhead)",
        "cat(black)"
        
        
        
 

        
    ])
    #ASK
    print(kb.query(pl.Expr("animal(loggerhead)")))
    print(kb.query(pl.Expr("canine(beagle)")))
    print(kb.query(pl.Expr("animal(X)"))) #beagle, gray, african, loggerhead, black
    print(kb.query(pl.Expr("mammal(X)"))) #beagle, gray, african, black


def kinship():
    kb = pl.KnowledgeBase("kinship")
    kb([
        # and = "," or = ";"    
        "mother(M,C :- female(M) , parent(M,C))", # if M is a female and M is a parent to C then mother(M,C)
        "parent(P,C) :- child(C,P)", # if C is a child of P then P is a parent of child
        "grandparent(G,C) :- parent(G,P) , parent(P,C)" # if G is parent to P and P is parent to C then G is grandparent to C

        "female(melanie)",
        "child(eden, melanie)",
        "child(eden,kenny)",
        "child(kenny,joan)"
        
        
     ])
    print(kb.query(pl.Expr("grandparent(joan,eden)")))
    

def main():
    
    #kinship()
    #kings()
    animals()

if __name__ == "__main__":
    main()