class Engine:
    def __init__(self, init_actors=[], init_loc=0, carry_limit=2):
        self.NORTH = init_actors
        self.SOUTH = []
        self.farmer_location = init_loc  # 0 -> north, 1 -> south
        self.carry_limit = carry_limit

    def get_north(self):
        return self.NORTH

    def get_south(self):
        return self.SOUTH

    def get_farmer_location(self):
        return  self.farmer_location
    def get_selectable_actors(self):
        if self.farmer_location == 0:
            return self.NORTH
        else:
            return self.SOUTH

    def ended(self):
        if len(self.NORTH) <= 0 and len(self.SOUTH) >= 1:
            return True

