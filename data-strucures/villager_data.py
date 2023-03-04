"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """


#     filename = open(filename)

#     species = set()

#     for line in filename:
#         line = line.split("|")
#         species.add(line[1])

#     return species

# print(all_species("villagers.csv"))


def get_villagers_by_species(filename, search_string="Deer"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    # villagers = []
    # filename = open(filename)
    # for line in filename:
    #     line = line.split("|")
    #     name = line[0]
    #     species = line[1]
    #     #print(species)
    #     if search_string in species:
    #         villagers.append(name)

    # return sorted(villagers)


print(get_villagers_by_species("villagers.csv", search_string="Deer"))


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO:
    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []
    filename = open(filename)
    for line in filename:
        line = line.split("|")
        hobby = line[3]
        name = line[0]

        if hobby == "Fitness":
            fitness.append(name)
        elif hobby == "Nature":
            nature.append(name)
        elif hobby == "Education":
            education.append(name)
        elif hobby == "Music":
            music.append(name)
        elif hobby == "Fashion":
            fashion.append(name)
        elif hobby == "Play":
            play.append(name)

    return [fitness, nature, education, music, fashion, play]


print(all_names_by_hobby("villagers.csv"))


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    filename = open(filename)
    for line in filename:
        line = line.rstrip()
        all_data.append(line)
        tuple(all_data)
        all_data.append("ggggg")

    return all_data


print(type(all_data))
print(all_data("villagers.csv"))


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
