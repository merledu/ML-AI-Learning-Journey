from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    ## OR--> it can be either nave or knight (in only one case its true)
    ## NOT(AND())--> if its both than its false (beacuse they cant be both)
    ## IMPLICATION(NOT(AND))--> because it is all false it cannot be a knight
    ## knight always speaks the truth this it cannot be both

    Or(AKnight,AKnave),Not(And(AKnight,AKnave)),
    Implication(Not(And(AKnight,AKnave)),AKnave)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    ## OR--> a or b can be either knave or knight
    ## Implication(Not(And(AKnave,BKnave)),AKnave) --> if both a and b are knaive 
    ## that means knave is telling truth that cannot happen that means for it to 
    ## be knave it has to lie it should be flase
    ##  Implication(AKnave,BKnave) --> b wil only be knave when a says truth
    Or(AKnight,AKnave),Or(BKnight,BKnave),
    Implication(AKnave,BKnight),# because if a is knaove that means it lies so b is knight
    Implication(And(AKnight,BKnight),AKnight),
    Implication(Not(And(AKnave,BKnave)),AKnave),
    




)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
#knowledge2 = And(
    # TODO
#)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
#knowledge3 = And(
    # TODO
#)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1)
        #("Puzzle 2", knowledge2),
        #("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
