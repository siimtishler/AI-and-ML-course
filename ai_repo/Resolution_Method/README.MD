At first creating the resolve() function was necessary,
To test this with the table
```
C1 = ["a", "b"]
C2 = ["a", "-b"]
print(resolve(C1, C2))
Output: ['a']

C1 = ["a", "b", "-c"]
C2 = ["a", "c"]
print(resolve(C1, C2))
Output: ['a', 'b']
```
For any two clauses C1 and C2, if C1 has a literal L1 and C2 has L2
which is the complement of literal L1, then delete L1 and L2 from C1 and
C2 and construct the disjunction of remaining literals. The result so obtained
is called the resolvant of C1 and C2.

Everything works but when I use the algorithm given in Moodle (slightly modified) with my resolve()
function it doesnt work. I got stuck and could not finish it sadly.

I did the CNF on by pen and paper and also with the logic tools. 

The unicorn clauses would be:
```
KB = [
    ["-Mythical" , "Immortal"],
    ["Mythical" , "Mammal"],
    ["Horned" , -"Immortal"],
    ["Horned" , "-Mammal"],
    ["-Horned" , "Magical"],
]
```

The correct answers would be that it can be proven given the KB
that the unicorn is horned and magical, but it cannot be proven that the
unicorn is mythical.

I successfully completed the forward chaining task and. 
But the forward chaining cannot be used for the unicorn task because it contains horn
clauses. Forward chaining is not a complete in the sense, that it will not always find a solution
given some KB.

Additionally forward chaining doesnt really handle negations. 
Eg. -Mythical. For the forward chaining algorithm it is essentially a completely new literal
and not the complement of another literal. 