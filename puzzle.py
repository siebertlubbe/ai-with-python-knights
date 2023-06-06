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
    # Game fundamentals
    # You are either a knight or a knave
    Or(AKnight, AKnave),
    # You cannot be a knight and knave at the same time
    Not(And(AKnight, AKnave)),

    # A says "I am both a knight and a knave."
    Or(
        # If A is a Knight then what they say is true
        And(AKnight, And(AKnight, AKnave)),
        # If A is a Knave then what they say is not true
        And(AKnave, Not(And(AKnight, AKnave)))
    )
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Game fundamentals
    # You are either a knight or a knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    # You cannot be a knight and knave at the same time
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),

    # A says "We are both knaves."
    Or(
        # If A is a Knight then what they say is true
        And(AKnight, And(AKnave, BKnave)),
        # If A is a Knave then what they say is not true
        And(AKnave, Not(And(AKnave, BKnave)))
    )    
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Game fundamentals
    # You are either a knight or a knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    # You cannot be a knight and knave at the same time
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),

    # A says "We are the same kind."
    Or(
        # If A is a Knight then what they say is true
        And(AKnight, Or(
            And(AKnight, BKnight),
            And(AKnave, BKnave)
        )),
        # If A is a Knave then what they say is not true
        And(AKnave, Not(Or(
            And(AKnight, BKnight),
            And(AKnave, BKnave)
        )))
    ),

    # B says "We are of different kinds."
    Or(
        # If B is a Knight then what they say is true
        And(BKnight, Or(
            And(AKnave, BKnight),
            And(AKnight, BKnave)
        )),
        # If B is a Knave then what they say is not true
        And(BKnave, Not(Or(
            And(AKnave, BKnight),
            And(AKnight, BKnave)
        )))
    )    
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Game fundamentals
    # You are either a knight or a knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    # You cannot be a knight and knave at the same time
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    # B says "A said 'I am a knave'."
    Or(
        # If B is a Knight then what they say is true
        And(BKnight, Or(
            # If A is a Knight then what they say is true
            And(AKnight, AKnave),
            # if A is a Knave then what they said is not true
            And(AKnave, Not(AKnave))
        )),
        # If B is a Knave then what they say is true
        And(BKnave, Not(Or(
            # If A is a Knight then what they say is true
            And(AKnight, AKnave),
            # if A is a Knave then what they said is not true
            And(AKnave, Not(AKnave))
        )))
    ),

    # B says "C is a knave."
    Or(
        # If B is a Knight then what they say is true
        And(BKnight, CKnave),
        # If B is a Knave then what they say is not true
        And(BKnave, Not(CKnave))
    ),

    # C says "A is a knight."
    Or(
        # If C is a Knight then what they say is true
        And(CKnight, AKnight),
        # If C is a Knave then what they say is not true
        And(CKnave, Not(AKnight))
    )
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
