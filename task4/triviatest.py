from pyswip import Prolog

prolog = Prolog()
prolog.consult("harrypotter_kb.pl")

# Query 1: Find Harry's house assignment
print(list(prolog.query("house_member(harry, House)")))

# Query 2: Find who uses a phoenix feather wand core
print(list(prolog.query("wand_core(Wizard, phoenix_feather)")))

# Query 3: Find everyone belonging to Gryffindor house
print(list(prolog.query("house_member(Wizard, gryffindor)")))

# Query 4: Find Draco's deduced trait using Rule 1
print(list(prolog.query("character_trait(draco, Trait)")))

# Query 5: Find all wizards deduced as purebloods using Rule 2
print(list(prolog.query("blood_status(Wizard, pureblood)")))

# Query 6: Find all wizards deduced as muggleborns using Rule 2
print(list(prolog.query("blood_status(Wizard, muggleborn)")))
