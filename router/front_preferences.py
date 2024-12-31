from fastapi import APIRouter, HTTPException,Depends, status
from sqlalchemy.orm import Session
from core.database import get_db
from typing import List, Dict
from model.front_preferences import FrontPreferences
from schema.front_preferences import FrontPreferencesSchema

router = APIRouter()

# @router.get("/front-preferences", response_model=List[FrontPreferencesSchema])
# def get_preferences(db: Session = Depends(get_db)):

#     preferences = db.query(FrontPreferences).all()
    
#     print(preferences)
#         # 카테고리별 데이터 그룹화
#     formatted_data: Dict[str, List[Dict[str, str]]] = {}

#     for item in preferences:
#         category = item["category"]
        
#         # 카테고리별 초기화
#         if category not in formatted_data:
#             formatted_data[category] = []
#         # 필요한 데이터만 추가
#         formatted_data[category].append({
#             "title": item["title"],
#             "route": item["end_point"]
#         })


#     return formatted_data
    

#     if not preferences:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="preferences not found")
    
#     return preferences

@router.get("/front-preferences")
async def get_front_preferences(session = Depends(get_db)):
    preferences = session.query(FrontPreferences).all()
    
    # title과 end_point만 추출하여 새로운 딕셔너리 리스트 생성
    result = [
        {"category": pref.category, "title": pref.title, "route": pref.end_point} 
        for pref in preferences
    ]
    
    return result
