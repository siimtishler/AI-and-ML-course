For the input formatting i am using the methid suggested in Moodle. 
The premise/premises are inside of a list, that is inside of a tuple with
the conclusion. ([premises], conclusion)

This is a quite readable format and easy to convert sentences into
a data format for the forward chaining algorithm

* Egg is fragile. Egg falls down. Egg contains liquid.
* If the egg is fragile and it falls down, it breaks.
* If the egg breaks and it contains liquid, it makes a mess. 
* If the egg is spoiled and the egg breaks, it smells
```
clauses_egg = [
    ([],"fragile"),
    ([],"falls down"),
    ([],"contains liquid"),
    (["fragile", "falls down"],"breaks"),
    (["breaks","contains liquid"], "makes mess"),
    (["spoiled", "breaks"],"smells"),
]
```
The output from the algorithm with different queries:

```
queries_egg = ["breaks", "makes mess", "smells"]
queryResults(queries_egg, clauses_egg, "Egg")

OUTPUT:
Egg -> breaks
Egg -> makes mess
Egg not smells
```
The egg breaking is a true because both the premises required for "breaks" are facts. We can prove "makes mess" because "fragile" is also a fact and we know previously that also "breaks" is true. So we can infere that "makes mess" is true.

The egg only smells if its also spoiled. Since it is not in our KB that the egg smells, we can not infere that the when the egg breaks, it also smells.

```
queryResults("spoiled", clauses_egg, "Egg")

OUTPUT:
Egg not spoiled
```

If i were to change the KB to:
```
clauses_egg = [
    ([],"fragile"),
    ([],"falls down"),
    ([],"spoiled"),         # Added spoiled
    ([],"contains liquid"),
    (["fragile", "falls down"],"breaks"),
    (["breaks","contains liquid"], "makes mess"),
    (["spoiled", "breaks"],"smells"),
]
```
The same query as before would output
```
queries_egg = ["breaks", "makes mess", "smells"]
queryResults(queries_egg, clauses_egg, "Egg")

OUTPUT:
Egg -> breaks
Egg -> makes mess
Egg -> smells
```


