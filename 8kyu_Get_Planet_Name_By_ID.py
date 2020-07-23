def get_planet_name(id):
    return {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }.get(id, None)



# def get_planet_name(i):
#     names = ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
#     return names[i]

print(get_planet_name(3))
