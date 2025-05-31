class WorldManager():
    def __init__(self):
        self.towns = self.load_town_file()
        self.ships = ShipManager()
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
    def disp_ship_list(self):
        return self.ships.disp_ships()
    
class Town():
    def __init__(self, name, population, parent):
        self.name = name
        self.population = population
        self.parent = parent
    
    def __str__(self):
        return f"{self.name} - Pops {self.population}" 

class ShipManager():
    def __init__(self):
        self._ship_factory = ShipFactory()
        self.ships = []
        with open("data/ships.txt", "r") as f:
            ship_lines = f.read().splitlines()[1:]
            for ship in ship_lines:
                ship = ship.split(', ')
                for i in range(int(ship[2])):
                    self.ships.append(self._ship_factory.create_ship(ship[0],ship[1]))
    
    def disp_ships(self):
        ship_list = []
        for ship in self.ships:
            ship_list.append(str(ship))
        return ship_list

class ShipFactory():
    def __init__(self):
        self.ship_classes = {}
        with open("data/ship_classes.txt", "r") as f:
            ship_class_lines = f.read().splitlines()[1:]
            for ship in ship_class_lines:
                ship = ship.split(', ')
                self.ship_classes[ship[0]] = {"capacity":ship[1],
                                        "cost":ship[2],
                                        "upkeep":ship[3]}
    def create_ship(self, shipname, location):
        return Ship(location, name=shipname, ship_dict=self.ship_classes[shipname])


class Ship():
    def __init__(self, location, name="Generic Ship", ship_dict={"capacity":0, "cost":0, "upkeep":0}):
        self.location = location
        self.name = name
        self.capacity = ship_dict["capacity"]
        self.cost = ship_dict["cost"]
        self.upkeep = ship_dict["upkeep"]
        self.cargo = {}
    def load_cargo(self, cargo):
        pass
    def type(self):
        return "name"
    def __str__(self):
        return f"{self.name}, in {self.location}"