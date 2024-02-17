from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# from database import SessionLocal
from database import get_db
from domain.question import question_schema,question_crud
from models import Question
from starlette import status


router = APIRouter(
    prefix = '/api/question',
)

# @router.get("/list")
# def question_list(): 
#     with get_db() as db:
#         _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    
#     return _question_list

#--스키마를 사용하는 경우 response_model을 사용하면 에러남
# @router.get("/list", response_model=question_schema.Question)
@router.get("/list", response_model=question_schema.QuestionList)
def question_list(db: Session = Depends(get_db),page: int=0,size: int=10):  #with문 대신에 fastapi depends사용
    total, _question_list = question_crud.get_question_list(db, skip = page*size, limit = size)
    return {'total': total,
            'question_list': _question_list
    }

@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id)
    return question


@router.post("/create", status_code= status.HTTP_204_NO_CONTENT)
def question_create(_question_create: question_schema.QuestionCreate,
                    db: Session = Depends(get_db)):
    question_crud.create_question(db=db, question_create=_question_create)