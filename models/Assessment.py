from models.Question import Question
from models.User import User 
import pandas as pd 
from . import DB

class Assessment:

    """
    limit: how many questions load from db 
    chunk_size: how many questions are displayed at the same time 
    """

    def __init__(self, user: User=None, limit: int=None, chunk_size: int=1):
        self.user = user
        self.started = False 
        self.completed = False

        self.limit = limit 
        self.questions = self.__get_questions() 
        self.answered_questions: list[Question] = []
        self.current_questions: list[Question] = [] 

        self.chunk_size = chunk_size

        self.results = None

    def __get_questions(self):
        query = "select * from question"
        if self.limit:
            query += f" limit {self.limit}"

        questions = DB.run_query(query)
        return [Question(**row) for row in questions]
    
    def answer_question(self, id, answer):
        next((question for question in self.current_questions if question.id == id), None).answer = answer

    def next_n(self):
        # gets the next n unanswered question and places them in the queue 
        # places current questions into answered bin
         
        assert self.questions != [], "question bank cannot be empty"

        self.answered_questions += self.current_questions
        self.current_questions = self.questions[0:self.chunk_size] 
        self.questions = self.questions[self.chunk_size:]

    def last_n(self):
        # puts the current queue back in the question bank and draws from the answered questions 

        assert self.answered_questions != [], "answered questions cannot be empty"

        # put the current queue away
        self.questions = self.current_questions + self.questions 

        # grab the last n questions we answered, put them in current 
        # remove them from the answered bank
        self.current_questions = self.answered_questions[-self.chunk_size:]
        self.answered_questions = self.answered_questions[:-self.chunk_size]

    def start(self):
        self.started = True 
        self.next_n()

    def submit(self):
        self.completed = True 
        self.calculate_score()
        self.save_assessment()

    def calculate_score(self):
        _dict = [question.__dict__ for question in self.answered_questions]
        df = pd.DataFrame(_dict)
        df['score'] = df['weight'] * df['answer']
        df = df.groupby('facet')['score'].sum().reset_index()
        
        self.results = df.to_dict(orient='records')

    def save_assessment(self):
        pass

    @property
    def has_next(self):
        return self.questions != []
    
    @property 
    def has_previous(self):
        return self.answered_questions != []