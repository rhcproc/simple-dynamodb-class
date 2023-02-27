
import dotenv
import os

class Config:
    DYNAMODB_ACCESS_KEY_ID = os.environ.get('DYNAMODB_ACCESS_KEY_ID')
    DYNAMODB_SECRET_ACCESS_KEY = os.environ.get('DYNAMODB_SECRET_ACCESS_KEY')
    DYNAMODB_REGION_NAME = 'ap-northeast-2'

config = Config()
