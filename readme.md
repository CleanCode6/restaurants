# 실행 화면

![image](https://s3.ap-northeast-2.amazonaws.com/6unu.net/ezgif.com-gif-maker.gif)



# Overview

CAU Restaurant Guide의 음식점 조회/추천 부분 구현 결과물입니다.

구현 내용은 아래와 같은 요구를 포함합니다.

**[음식점 조회]**

USE CASE : 1번

REQ-08 : 이용자는 지도에서 마킹된 장소(식당)또는 리스트중 한 장소를 선택하여 장소에 대한 정보를 볼 수 있다.

REQ-09 : 이용자가 음식점을 클릭하면 거리, 이름, 가격, 오픈시간, 전화번호, 평균 별점, 메뉴, 리뷰를 제공한다.

**[음식점 추천]**

USE CASE : 2번

REQ-04 : 추천리스트는 이용자의 취향 문답을 기준으로 평점 4.0 이상 음식점을 상위에 배치해서 추천한다.

REQ-05 : 추천리스트 외의 전체 음식점 목록이 평점순으로 화면에 나타난다.

REQ-07 : 이용자가 따로 음식점을 확인하고 싶을 때, 전체식당 목록에서, 높은 평점순 그리고 최단거리 순서, 음식의 종류 정렬방식을 선택할 수 있다.

더 자세한 명세는 document에서 확인할 수 있습니다.

Domain Model Document : https://github.com/CleanCode6/CAU_Restaurant_Guide/blob/main/Domain%20Model.pdf

System Design Document : https://github.com/CleanCode6/CAU_Restaurant_Guide/blob/main/CAU_Restaurant_Guides_System_Design_Document.pdf


# 데모 실행
```
flask run
```
실행 후

브라우저 상 localhost:5000 에 접속합니다.

**Environment**
- python: 3.9.2
- flask: 2.0.1

# Route (Page)
Flask 웹 프레임워크를 이용하여 구현되어 있으며, Jinja2 템플릿 기반의 SSR(Server Side Rendering) 방식으로 웹페이지가 제공됩니다. 

두가지 페이지로 구성되어 있습니다.

- /restaurants -> 목록 (GET)
- /restaurants/{id} -> 상세 (GET)

# Schema

Restaurants Schema 예시

```
{
	"restaurant_id": "string" // (PK)
	"restaurant_name": "string",
	"description": "string",
	"rating": 3.2,
	"menu": [{
		"menu_name": "string",
		"price": 10000
	}],
	"category": 0,
	"image": "string",
	"position_x": 37.5066244,
	"position_y": 126.9524722,
}
```

# Request Form

다음 형태로 요청(GET)을 보냅니다.

```
{
	"category": 0, // 한식
	"order": 1, // 평점순
	"pos": 2 // 흑석역
}
```
다음 형태로 QueryStringParameter로 전달합니다. 

```
GET /restaurants?category=0&order=1&pos=2
```

# Project Directory

1. app.py
- **웹 페이지 라우팅**
- restaurants_list_route()
- restaurant_route()
2. page_maker.py
- **웹 페이지 렌더러**
- make_restaurant_page(restaurants) : html
- make_restaurants_list_page([restaurants]): html
3. controller.py
- restaurants_list_controller(requests)
- restaurant_controller(rest_id) 
4. model.py
- **schema 데이터 클래스**
- restaurants.py
5. db_connection.py
- **DB connector 클래스**
- connect_to_db()
- get_restaurants() : [restaurants]
- get_restaurant(id) restaurants
- close()
6. curator.py
- **음식점 추천**
- curate_restaurant(restaurants, conditions) : [restaurants]
7. distance_operator.py
- **거리 계산**
- calculate_position(rx, ry, cx, cy): float
8. map_generator.py
- **지도 생성**
- request_map_url(params): str(google maps url)
9. template
- **HTML 템플릿 파일**

# Flow

설계 문서 Repository의 SDD를 참조하세요.

# Etc
HTML Template: https://github.com/startbootstrap/startbootstrap-shop-homepage

**Constants Value 정의**

- 한식(0), 중식(1), 양식(2), 일식(3), 카페(4)

- 평점순(0), 거리순(1)

- 중앙대정문(0), 중앙대후문(1), 상도역(2), 흑석역(3)

**위경도 값**
- 중앙대정문:37.5066244,126.9524722
- 중앙대후문:37.5066412,126.9524722
- 상도역:37.4995973,126.9372955
- 흑석역:37.5090436,126.9612882 

**구글맵 관련 이슈**
구글맵 static api에서 위치가 정확히 표시되지 않는 경우가 있는데, 이는 location parameter로 넘겨주는 위경도 값이 소수점 6자리까지만 받기 때문에 나타나는 문제입니다. 예를 들어 위경도 값이 (37.1234567, 126.1234567)와 같이 주어진 경우 소수점 버림으로 인하여 다음과 같이 (37.123456, 126.123456) 위경도로 변환되어 찍히게 됩니다.
