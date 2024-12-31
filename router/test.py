from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text  # text 함수 import
from core.database import get_db
from core.database import get_mongo_db
import requests
from pymongo import MongoClient
import os

router = APIRouter()

@router.get("/test-db")
def test_mongo_connection():
    try:
        # 환경 변수에서 MongoDB URI와 DB 이름을 가져옵니다.
        mongodb_uri = os.getenv("MONGODB_URI", "mongodb+srv://babuk:gjqackMpbzO5Qxos@wnp001.1oip4.mongodb.net/?retryWrites=true&w=majority&appName=WNP001")
        mongodb_db_name = os.getenv("MONGODB_DB_NAME", "DH_INFO")  # 기본값: DH_INFO
        
        # MongoDB에 연결
        client = MongoClient(mongodb_uri)
        
        # MongoDB에서 지정된 데이터베이스 선택
        db = client[mongodb_db_name]
        
        # 특정 컬렉션에서 데이터 조회
        collection_name = "factory_registration"  # 컬렉션 이름을 적절히 수정
        collection = db[collection_name]
        data = list(collection.find({}, {"_id": 0}))  # 데이터를 조회하고 _id 제외
        
        if data:
            print(f"{collection_name} 컬렉션에서 데이터 조회됨:")
            print(data)
        else:
            print(f"{collection_name} 컬렉션에 데이터가 없습니다.")
    
    except Exception as e:
        print(f"MongoDB 연결 실패: {e}")

if __name__ == "__main__":
    test_mongo_connection()
