class WorldManager():
    def __init__(self):
        self.towns = self.load_town_file()
        # self.load_ship_file()
        # self.goods = self.load_goods_file()

    def load_town_file(self):
        towns = []
        with open("data/towns.txt", "r") as f:
            town_lines = f.read().splitlines()[1:]
            for town_line in town_lines:
                town_line = town_line.split(", ")
                name = town_line[0]
                population = town_line[1]
                parent = None
                if town_line[2] != "none":
                    parent = town_line[2]
                new_town = Town(name, population, parent)
                towns.append(new_town)
        return towns
    
    def num_of_towns(self):
        return len(self.towns)

    def disp_town_list(self):
        town_list = []
        for town in self.towns:
            town_list.append(str(town))
        return town_list
    # def dist(self, town1, town2):

class Town():
    def __init__(self, name, population, parent):
        self.name = name
        self.population = population
        self.parent = parent
    
    def __str__(self):
        return f"{self.name} - Pops {self.population}" 