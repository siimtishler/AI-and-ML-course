clauses_test = [
    ([], "A"),
    ([], "B"),
    (["L", "M"], "P"),
    (["B", "L"], "M"),
    (["A", "P"], "L"),
    (["A", "B"], "L"),
    (["P"], "Q")
]

clauses2_test = [
    ([],"A"),
    (["A"], "B"),
    (["B"], "C"),
    (["C"], "D"),
    (["D"], "E"),
    (["E"], "F"),
]

# Egg is fragile. Egg falls down. Egg contains liquid. 
# If the egg is fragile and it falls down, it breaks. 
# If the egg breaks and it contains liquid, it makes a mess. 
# If the egg is spoiled and the egg breaks, it smells"

clauses_egg = [
    ([],"fragile"),
    ([],"falls down"),
    ([],"spoiled"),
    ([],"contains liquid"),
    (["fragile", "falls down"],"breaks"),
    (["breaks","contains liquid"], "makes mess"),
    (["spoiled", "breaks"],"smells"),
]

def forward_chaining(clauses, query):
    inferred = set()
    new_symbols = True  # Loop while we infer new stuff

    while new_symbols:
        new_symbols = False
        for clause in clauses:
            premises, conclusion = clause
            if all(premise in inferred for premise in premises) and conclusion not in inferred:
                if conclusion == query:
                    # print(conclusion)
                    return True  # The query symbol is entailed
                inferred.add(conclusion)
                new_symbols = True

    return False  # No new symbols, query symbol was not seen


def queryResults(queries, clauses, thing = "thing"):
    for query in queries:
        result = forward_chaining(clauses, query)

        if result:
            print(f"{thing} -> {query}")
        else:
            print(f"{thing} not {query}")

queries_egg = ["breaks", "makes mess", "smells"]
queryResults(queries_egg, clauses_egg, "Egg")



