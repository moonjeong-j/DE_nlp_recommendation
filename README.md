# KEYWORD 분석을 통한 강남역 맛집 추천 시스템

## 1. 프로젝트 설명

### (1) 주제 및 데이터 소개
- 주제:
- 데이터
    - 망고플레이트 사이트 중 강남역 데이터를 bs4, selenium으로 크롤링한 데이터
    - 가게이름, 주소, 음식카테고리, 가격, 리뷰수, 리뷰(문자열)
    - 1643*6 data
    
### (2) 구현 파이프라인, 사용 Tool

<img width = "700" src ="https://user-images.githubusercontent.com/102526342/222613652-97de87fb-6eff-404a-8762-0a0a3ddac4ac.png">

- 데이터 적재
    - PostgreSQL을 사용하여 사용자가 입력한 데이터를 실시간으로 받아볼수 있게 설계
- 데이터 모델링
    - sklean의 TfidfVectorizer로 리뷰를 피쳐벡터화
    - sklearn의 cosine_similarity로 코사인 유사도를 구하여 리뷰텍스트 분석
    - 유저가 keyword를 입력하면 가장 유사도가 높은 레스토랑(음식점 or 카페)가 나오도록 모델링
- 대시보드 
    - metabase를 이용, 맛집 데이터 분석에 대한 통계정보 제시
- Front end
    - Flask api
    
## 2. 결과 화면

### (1) 사용자 키워드 입력

<img width ="500" src ="https://user-images.githubusercontent.com/102526342/222617111-1c2f4b24-4031-48a0-a5f9-f3652cbcbbb6.png">

### (2) 강남역 맛집 추천

<img width ="500" src="https://user-images.githubusercontent.com/102526342/222617275-661286a6-cfd3-4663-aa31-ef6d6f58f336.png">


