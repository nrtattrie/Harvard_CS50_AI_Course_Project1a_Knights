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

    # Knowledge stating Knight or Knave is true
    Or(AKnight, AKnave),
    # Knowledge stating not Knight and Knave
    Not(And(AKnight, AKnave)),

    # Knowledge stating if a Knight, implies A's statement is true
    Implication(AKnight, And(AKnight, AKnave)),
    # Knowledge stating if a Knave, implies A's statement is false
    Implication(AKnave, Not(And(AKnight, AKnave)))



)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(

    # Knowledge stating Knight or Knave is true
    Or(AKnight, AKnave),
    # Knowledge stating not Knight and Knave
    Not(And(AKnight, AKnave)),
    # Knowledge stating Knight or Knave is true
    Or(BKnight, BKnave),
    # Knowledge stating not Knight and Knave
    Not(And(BKnight, BKnave)),

    # Knowledge stating if A is a Knight, A's statement is true
    Implication(AKnight, And(AKnave, BKnave)),
    # Knowledge stating if A is a Knave, A's statement is false
    Implication(AKnave, Not(And(AKnave, BKnave)))

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(

    # Knowledge stating Knight or Knave is true
    Or(AKnight, AKnave),
    # Knowledge stating not Knight and Knave
    Not(And(AKnight, AKnave)),
    # Knowledge stating Knight or Knave is true
    Or(BKnight, BKnave),
    # Knowledge stating not Knight and Knave
    Not(And(BKnight, BKnave)),

    # A says "We are the same kind."
    Implication(AKnight, And(AKnight, BKnight)),
    Implication(AKnave, Not(And(AKnave, BKnave))),
    # B says "We are of different kinds."
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(

    # Knowledge stating Knight or Knave is true
    Or(AKnight, AKnave),
    # Knowledge stating not Knight and Knave
    Not(And(AKnight, AKnave)),
    # Knowledge stating Knight or Knave is true
    Or(BKnight, BKnave),
    # Knowledge stating not Knight and Knave
    Not(And(BKnight, BKnave)),
    # Knowledge stating Knight or Knave is true
    Or(CKnight, CKnave),
    # Knowledge stating not Knight and Knave
    Not(And(CKnight, CKnave)),

    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Implication(Or(AKnight, AKnave), AKnight),
    Implication(Not(Or(AKnight, AKnave)), AKnave),
    # B says "A said 'I am a knave'."
    Implication(BKnight, Or(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))),
    Implication(BKnave, Or(Not(Implication(AKnight, AKnave)), Not(Implication(AKnave, Not(AKnave))))),
    # B says "C is a knave."
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),
    # C says "A is a knight."
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
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
