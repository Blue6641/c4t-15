pokedex = {
    "RAICHU" : '''raichu has a regional variant that is Electric/Psychic.
    It evolves from Pikachu when exposed to a Thunder Stone.
    All Pikachu in Alola will evolve into this form regardless of their origin.''',
    "ONIX" : '''Onix resembles a giant chain of gray boulders that become smaller towards the tail.
    It has a rocky spine on its head and a pair of black eyes right beneath it.
    This Pokémon has a magnet in its brain that serves as an internal compass.
    Its body absorbs many hard objects, making its body very solid.
    As it grows older, it becomes more rounded and smoother, eventually becoming similar to black diamonds.''',
    "SQUIRTLE" : '''Squirtle’s shell is not merely used for protection.
    The shell’s rounded shape and the grooves on its surface help minimize resistance in water,
    enabling this Pokémon to swim at high speeds.'''
}

while True:
    lookup = input("Enter name of Pokemon: ")
    print("Pokemon's Description: ", pokedex[lookup.upper()])