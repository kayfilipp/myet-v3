class Personality:

    def __init__(self, name: str, description: str, image_path: str, scores: dict):

        self.name = name 
        self.description = description
        self.image_path = image_path
        self.scores = scores

    def euclidean_distance(self, assessment_scores:dict):
        # accepts another dictionary of scores and returns the euclidean distance
        return sum(
            (self.scores[key] - assessment_scores[key]) ** 2 
            for key in self.scores.keys()
        )
    
class PersonalityPicker:

    # returns the closest personality type 

    def __init__(self, personalities: list[Personality]):
        self.personaliities = personalities

    def get_personality_match(self, assessment_scores: dict):
        
        results = [
            {'personality': personality, 'distance': personality.euclidean_distance(assessment_scores)}
            for personality in self.personaliities
        ]

        return sorted(results, key=lambda personality: personality['distance'], reverse=True)[0]