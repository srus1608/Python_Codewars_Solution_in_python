class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    
    def is_worth_it(self):
        # Calculate the weight of the crew
        crew_weight = self.crew * 1.5
        # Calculate the weight of the ship excluding the crew
        weight_without_crew = self.draft - crew_weight
        # Determine if the ship is worth looting
        return weight_without_crew > 20