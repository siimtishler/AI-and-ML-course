def simple_resolution_solver(KB, neg_alpha):
    todo = [neg_alpha]
    done = KB.copy()
    while todo:
        current = todo.pop()
        if isinstance(current, str):
            current = [current]
        for clause in done:
            resolvents = resolve(current, clause)
            # print(resolvents)
            for resolvent in resolvents:
                if not resolvent:
                    return True
                elif resolvent not in done and resolvent not in todo:
                    todo.append(resolvent)
        done.append(current)
    return False

def resolve(c1, c2):
    new_clause = []

    if isinstance(c1, str):
        c1 = [c1]
    if isinstance(c2, str):
        c2 = [c2]

    for literal1 in c1:
        for literal2 in c2:
            if literal1 == '-' + literal2 or literal2 == '-' + literal1:
                resolvent = [lit for lit in c1 if lit != literal1] + [lit for lit in c2 if lit != literal2]
                new_clause.extend(resolvent)

    new_clause = list(set(new_clause))
    new_clause.sort()
    if isinstance(new_clause, str):
        new_clause = [new_clause]
    return new_clause

KB = [
    ["-Mythical", "Immortal"],
    ["Mythical", "Mammal"],
    ["Horned", "-Immortal"],
    ["Horned", "-Mammal"],
    ["-Horned", "Magical"],
]

query = ["-Mythical"]

result = simple_resolution_solver(KB, query)

if result:
    print("Proof found: KB entails the query.")
else:
    print("No proof found: KB does not entail the query.")

KB2 = [["-P", "Q"], ["-R", "P"], ["-R", "S", "T"], ["-T", "-U"], ["-Q", "U"], ["R"]]
query1 = ["-S"]
result1 = simple_resolution_solver(KB2, query1)
print("Problem 1 Result:", result1)  # Expected output: True ;(