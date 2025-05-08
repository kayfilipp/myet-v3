class Question:

    def __repr__(self):
        return f"Question(id={self.id}, body={self.body[:20]}..., subtrait={self.subtrait}, facet={self.facet}, w={self.weight})"

    def __init__(self, id: str, body: str, facet=None, subtrait=None, weight: float=0):
        self.id = id
        self.body = body
        self.facet = facet
        self.subtrait = subtrait 
        self.weight = weight 

        self.answer:int = None