from datetime import datetime

from database import get_db
from database.models import Question

def add_question_db(q_text, answer, v1, v2, v3, v4):
    db = next(get_db())
    new_question = Question(q_text=q_text, answer=answer, v1=v1,v2=v2,v3=v3, v4=v4,
                            question_reg_date=datetime.now())
    db.add(new_question)
    db.commit()
    return 'Questions added to database'


def show_question():
    db = next(get_db())
    questions = db.query(Question).all()
    return questions[:20]