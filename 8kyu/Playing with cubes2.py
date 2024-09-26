class Cube(object):
    def __init__(self, side=0):
        """Constructor with optional integer argument"""
        # Ensure the side is always a positive integer
        self.__side = abs(side)

    def get_side(self):
        """Return the side of the Cube"""
        return self.__side

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self.__side = abs(new_side)