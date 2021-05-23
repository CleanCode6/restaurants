# Overview

데모 실행
```
flask run
```
실행 후

브라우저 상 localhost:5000 에 접속합니다.

**Environment**
python: 3.9.2
flask: 2.0.1

# Route (Page)
Flask 웹 프레임워크를 이용하여 구현되어 있으며, Jinja2 템플릿 기반의 SSR(Server Side Rendering) 방식으로 웹페이지가 제공됩니다. 

두가지 페이지로 구성되어 있습니다.

/restaurants -> 목록 (GET)
/restaurants/{id} -> 상세 (GET)

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

app.py
- 웹 페이지 라우팅
- restaurants_list_route()
- restaurant_route()
page_maker.py
- 웹 페이지 렌더러
- make_restaurant_page(restaurants) : html
- make_restaurants_list_page([restaurants]): html
controller.py
- restaurants_list_controller(requests)
- restaurant_controller(rest_id) 
model.py
- schema 데이터 클래스
- restaurants.py
db_connection.py
- DB connector 클래스
- connect_to_db()
- get_restaurants() : [restaurants]
- get_restaurant(id) restaurants
- close()
curator.py
- 음식점 추천
- curate_restaurant(restaurants, conditions) : [restaurants]
distance_operator.py
- 거리 계산
- calculate_distance(rx, ry, cx, cy): int 
template
- HTML 템플릿 파일

# Flow

설계 문서 Repository의 SDD를 참조하세요.

# Etc
HTML Template: https://github.com/startbootstrap/startbootstrap-shop-homepage

**Constants Value 정의**
한식(0), 중식(1), 양식(2), 일식(3), 카페(4)

등록순(0), 평점순(1), 거리순(2)

**위경도 값**
중앙대정문:37.5066244,126.9524722
중앙대후문:37.5066412,126.9524722
상도역:37.4995973,126.9372955
흑석역:37.5090436,126.9612882 