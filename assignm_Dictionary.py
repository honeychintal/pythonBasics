myDict ={
    "vocation":"""Vocation can refer simply to an occupation,
                 or it can refer to a strong desire to pursue
                  a particular kind of work or course of action.""",
    "sumptuous": """Sumptuous is used to describe things that are 
                    extremely costly, rich, luxurious, or magnificent.""",
    "fidelity": """Fidelity refers to the quality or state of being 
                    faithful to someone, such as a spouse, or something, such as one's country.""",
    "decry":"""Decry is a formal word that means "to express strong disapproval of.""",
    "perfunctory":"""Perfunctory is used to describe something that 
                    is done without energy or enthusiasm, as a duty or out of habit.""",
    "meld":"""Meld means "to blend or mix together.""",
    "behest":"""A behest is an authoritative order or an urgent prompting.""",
    "abundance":["a very large quantity of something.",
            "(in solo whist) a bid by which a player undertakes to make nine or more tricks."]
}
getkey = input("Input the word for meaning: ")
if(myDict.__contains__(getkey)):
    print(myDict[getkey])
else:
    print("Not Found!!")