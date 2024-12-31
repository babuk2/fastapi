import requests
from fastapi import HTTPException, Depends
from core.database import get_mongo_db, mongo_db


# API 서비스 키
service_key = "AqY7NHy8gn1ROMIJWrGmm/88icACyjAmgAILkaaEobA8fXaertUF4eWXC1pD+qUo7JZYA4T5Ec3Z5bbD5tK8pA=="



# API 설정
API_SETTINGS = {

    #=====================
    #     [고용산업]
    #=====================
    # ---------------------------- 동해시 공장등록현황
    "factory_registration": "use_mongo",
    # ---------------------------- 동해시 창업보육센터 입주기업 정보
    "startup_incubation": "use_mongo",
    
    #=====================
    #     [공공행정]
    #=====================
    # ---------------------------- 강원도 동해시_성별 및 연령별 1인가구 수
    "single_person_households": "use_mongo",
    # ---------------------------- 동해시 패밀리사이트
    "family_site": "use_mongo",
    # ---------------------------- 강원특별자치도 동해시_주민등록인구 현황
    "population": "use_mongo",
    # ---------------------------- 강원특별자치도 동해시_장례식장
    "funeral_home": {
        "base_url": "https://api.odcloud.kr/api/15040143/v1/uddi:af19d509-3c48-455a-8f55-a73d30e0d0f7",
        "page": 1,
        "perPage": 10,
    },
    # ---------------------------- 강원도 동해시_지방세우편물 발송 현황
        "local_tax_mail": {
        "base_url": "https://api.odcloud.kr/api/15092034/v1/uddi:8d56c914-9d21-458f-b2f9-eb657d7bae90",
        "page": 1,
        "perPage": 100,
    },
    # ---------------------------- 강원특별자치도 동해시_행정업무용PC장애처리내역
        "administrative_pc_failure": {
        "base_url": "https://api.odcloud.kr/api/15123662/v1/uddi:ab6fec1c-804c-4aed-b88e-c8309aa6af87",
        "page": 1,
        "perPage": 100,
    },   
    # ---------------------------- 강원특별자치도 동해시_독거노인현황
        "elderly_living_alone": {
        "base_url": "https://api.odcloud.kr/api//15129797/v1/uddi:1bd3dd3c-afdc-4ee3-bac8-965c7b8f0746",
        "page": 1,
        "perPage": 100,
    },   
    # ---------------------------- 동해시시설관리공단_홈페이지 우편번호
        "dcf_homepage_zip_code": {
        "base_url": "https://api.odcloud.kr/api/15075517/v1/uddi:85732c24-ceb6-4d76-81fa-9ee849b834ff",
        "page": 1,
        "perPage": 100,
    },   
    # ---------------------------- 동해시시설관리공단_사이트맵
        "dcf_site_map": {
        "base_url": "https://api.odcloud.kr/api/15075519/v1/uddi:e31e9269-6252-434c-a3aa-e24d8887179c",
        "page": 1,
        "perPage": 100,
    },   
        # ---------------------------- 동해시시설관리공단_홈페이지 관람정보
        "dcf_homepage_viewing_information": {
        "base_url": "https://api.odcloud.kr/api/15075518/v1/uddi:1dc5ad66-6bc6-4734-8a53-862723b714ff",
        "page": 1,
        "perPage": 100,
    },   
    
    #=====================
    #      [문화관광]
    #=====================
    # ---------------------------- 강원특별자치도 동해시_음식점현황
    "restaurants": "use_mongo",
    # ---------------------------- 강원특별자치도 동해시_숙박업소
    "accommodations": "use_mongo",
    # ---------------------------- 강원특별자치도 동해시_관광객 수 정보
    "tourist_count": {
        "base_url": "https://api.odcloud.kr/api/15029860/v1/uddi:191ccf4d-9aec-4c52-b139-9c2eee7245ce",
        "page": 1,
        "perPage": 20,
    },
    # ---------------------------- 강원특별자치도 동해시_관광명소현황
    "tourist_sites": {
        "base_url": "https://api.odcloud.kr/api/15029894/v1/uddi:305afb54-e9a6-4cc7-8958-9fee36abfdd9",
        "page": 1,
        "perPage": 50,
    },
    
    # ---------------------------- 천지명양수륙재의찬요정보
    "temple": {
        "base_url": "https://api.odcloud.kr/api/15030373/v1/uddi:bba5f580-8b5d-4477-9655-b10df54e269f",
        "page": 1,
        "perPage": 1,
    },
    # ---------------------------- 동해시시설관리공단 체육시설요금
	"dcf_sports_facility_fee": {
        "base_url": "https://api.odcloud.kr/api/15075285/v1/uddi:5c0234bf-b03b-40bd-9e54-c7beb11a77ac",
        "page": 1,
        "perPage": 50,
    }, 
	# ---------------------------- 동해시시설관리공단 예약현황
	"dcf_reservation_status": {
        "base_url": "https://api.odcloud.kr/api/15075520/v1/uddi:687e77fb-0581-494e-b397-f9007cb1558a",
        "page": 1,
        "perPage": 50,
    }, 
	# ---------------------------- 동해시시설관리공단 홈페이지 디자인관리
    "dcf_homepage_design_management": {
        "base_url": "https://api.odcloud.kr/api/15075515/v1/uddi:f9a4b133-11f1-48bd-9706-c1040b8c8379",
        "page": 1,
        "perPage": 50,
    }, 
	# ---------------------------- 동해시시설관리공단 체육시설 예약정보
    "dcf_sports_facility_reservation_information": {
        "base_url": "https://api.odcloud.kr/api/15075286/v1/uddi:0536e4b5-d499-404c-a1cc-d0944ee1c1b9",
        "page": 1,
        "perPage": 50,
    }, 
	# ---------------------------- 동해시시설관리공단 망상리조트 체크인
	"dcf_mangsang_resort_check_in": {
        "base_url": "https://api.odcloud.kr/api/15075296/v1/uddi:e24feb0d-c740-483b-9fe9-a85ece34563f",
        "page": 1,
        "perPage": 50,
    }, 
	# ---------------------------- 동해시시설관리공단 체육시설 휴일설정
	"dcf_sports_facility_holiday_setting": {
        "base_url": "https://api.odcloud.kr/api/15075287/v1/uddi:ad8017b1-c5dd-494e-8c2a-ffe1c9269443",
        "page": 1,
        "perPage": 50,
    }, 
	# ---------------------------- 동해시시설관리공단 망상오토캠핑리조트 예약수
    "dcf_mangsang_auto_camping_resort_reservation_number": {
        "base_url": "https://api.odcloud.kr/api/15075514/v1/uddi:086742e5-208b-4ed5-8037-817613a81ec3",
        "page": 1,
        "perPage": 50,
    }, 
	# ---------------------------- 동해시시설관리공단 홈페이지 메인알림창
	"dcf_homepage_main_notification_window": {
        "base_url": "https://api.odcloud.kr/api/15075516/v1/uddi:aa859f4d-3e90-49b7-9a48-ae2f4d5b4f91",
        "page": 1,
        "perPage": 50,
    }, 
	# ---------------------------- 동해시시설관리공단 망상오토캠핑장 기타금액정보
	"dcf_mangsang_auto_camping_site_other_fee_information": {
        "base_url": "https://api.odcloud.kr/api/15075513/v1/uddi:75a5c46b-21ed-4103-8149-9ad99d7f1a48",
        "page": 1,
        "perPage": 50,
    }, 
	# ---------------------------- 동해시시설관리공단 망상오토캠핑장 접속기록
	"dcf_mangsang_auto_camping_site_access_history": {
        "base_url": "https://api.odcloud.kr/api/15075297/v1/uddi:a5a0b6ce-94b7-4b24-aa59-a6812545eb34",
        "page": 1,
        "perPage": 50,
    }, 
    #=====================
    #      [교통물류]
    #=====================
	# ---------------------------- 강원특별자치도 동해시 여객터미널정보
    "passenger_terminal_information": {
        "base_url": "https://api.odcloud.kr/api/15040144/v1/uddi:5ca25378-77da-4d01-a5f6-c22d600c567a",
        "page": 1,
        "perPage": 20,
    }, 
	# ---------------------------- 강원특별자치도 동해시 버스정류장정보
	"bus_stop_information": {
        "base_url": "https://api.odcloud.kr/api/15041541/v1/uddi:67e05100-269d-4ce4-9153-8057354fab85",
        "page": 1,
        "perPage": 20,
    }, 
	# ---------------------------- 강원특별자치도 동해시 도로현황
	"road_status": {
        "base_url": "https://api.odcloud.kr/api/3084099/v1/uddi:8eb01771-7e55-4d22-b6ba-fc5683e46ae4",
        "page": 1,
        "perPage": 20,
    }, 
	# ---------------------------- 강원특별자치도 동해시 이사화물업체 현황
	"moving_cargo_company": {
        "base_url": "https://api.odcloud.kr/api/15128774/v1/uddi:59a2f083-398f-415b-80ee-ba03e2d1a7db",
        "page": 1,
        "perPage": 20,
    }, 
	# ---------------------------- 동해시시설관리공단 동해시종합버스터미널 환경친화차 이용현황 : ★이거 또 왜 안돼?
	"integrated_bus_terminal_eco_vehicle": {
        "base_url": "https://api.odcloud.kr/api/15029860/v1/uddi:191ccf4d-9aec-4c52-b139-9c2eee7245ce",
        "page": 1,
        "perPage": 20,
    }, 
	# ---------------------------- 강원도 동해시 교통량 유동인구 정보 조회 서비스: ★이거 또 왜 안돼?
	"traffic_volume_and_floating_population": {
        "base_url": "https://api.odcloud.kr/api/15029860/v1/uddi:191ccf4d-9aec-4c52-b139-9c2eee7245ce",
        "page": 1,
        "perPage": 20,
    }, 
	# ---------------------------- 강원도 동해시 교통시설정보 조회 서비스: ★이거 또 왜 안돼?
	"trans_facility_information_search": {
        "base_url": "https://api.odcloud.kr/api/15029860/v1/uddi:191ccf4d-9aec-4c52-b139-9c2eee7245ce",
        "page": 1,
        "perPage": 20,
    }, 

    #=====================
    #      [보건의료]
    #=====================
	# ---------------------------- 강원도 동해시 공중위생업 현황
    "status_of_public_health_industry": {
        "base_url": "https://api.odcloud.kr/api/15006951/v1/uddi:107d7e97-a962-479b-aa1f-9e575cb12045",
        "page": 1,
        "perPage": 20,
    }, 
	# ---------------------------- 강원도 동해시 산후조리원 등록 현황
	"status_of_postpartum_care_center_registration": {
        "base_url": "https://api.odcloud.kr/api/15112875/v1/uddi:570a2298-1cb4-498c-bff6-e6682ad65903",
        "page": 1,
        "perPage": 20,
    }, 
	# ---------------------------- 강원도 동해시 정신건강의학과 요양병원 정신건강센터 현황
	"status_of_mental_health_center_in_psychiatric_hospital": {
        "base_url": "https://api.odcloud.kr/api/15103822/v1/uddi:2a283022-5fdf-4312-80e5-8c6e337b5ede",
        "page": 1,
        "perPage": 20,
    }, 
	# ---------------------------- 국민건강보험공단 특정 지역 및 상병별 관내외 입원 진료인원
	"number_of_inpatients_in_and_out_of_the_district_by_specific_region_and_disease": {
        "base_url": "https://api.odcloud.kr/api/15126917/v1/uddi:06a9b194-cfd3-41c0-affd-d7fa4187e839",
        "page": 1,
        "perPage": 20,
    }, 

    #=====================
    #      [식품건강]
    #=====================  
    # ---------------------------- 강원특별자치도 동해시 착한가격업소지정현황
    "status_of_good_price_stores": {
        "base_url": "https://api.odcloud.kr/api/3077962/v1/uddi:3bce9c9d-8811-4d3f-800b-9a6fa2b82598",
        "page": 1,
        "perPage": 60,
    }, 
    #=====================
    #      [농축수산]
    #=====================  
	# ---------------------------- 강원특별자치도 동해시 축산업 등록현황
	'status_of_livestock_industry_registration': {
        "base_url": "https://api.odcloud.kr/api/15006405/v1/uddi:09db1c26-5ab7-4838-8fc5-9766c01af94f",
        "page": 1,
        "perPage": 50,
    }, 
	# ---------------------------- 강원도 동해시 낚시어선업
	'fishing_boat_industry': {
        "base_url": "https://api.odcloud.kr/api/15043213/v1/uddi:3ed72c76-2d3a-42e3-bee6-dfad6bf1482d",
        "page": 1,
        "perPage": 50,
    }, 
	# ---------------------------- 강원특별자치도 동해시 농림축산식품사업지원시설현황
	'support_for_agriculture_forestry_livestock_and_food_business': {
        "base_url": "https://api.odcloud.kr/api/3072996/v1/uddi:111db2cf-dccb-4548-9eb1-9d6ab8754433",
        "page": 1,
        "perPage": 50,
    }, 
	# ---------------------------- 강원도 동해시 반려동물등록현황
	'status_of_companion_animal_registration': {
        "base_url": "https://api.odcloud.kr/api/15088611/v1/uddi:77c6ab9e-5364-4bb9-94e3-9b0dd0cc0375",
        "page": 1,
        "perPage": 50,
    }, 
    #=====================
    #      [국토관리]
    #=====================  
	# ---------------------------- 강원특별자치도 동해시 시유지현황
	'current_status_of_city_property': {
        "base_url": "https://api.odcloud.kr/api/15029858/v1/uddi:5e9cca71-789a-45ce-bbeb-e9dff7ca859f",
        "page": 1,
        "perPage": 50,
    }, 
	# ---------------------------- 강원특별자치도 동해시 골재채취업등록현황
	'status_of_aggregate_mining_employment_registration': {
        "base_url": "https://api.odcloud.kr/api/3045116/v1/uddi:f303f9ef-4746-4513-a540-9cfd8eba3abb",
        "page": 1,
        "perPage": 50,
    }, 
	# ---------------------------- 강원특별자치도 동해시 주택보급률
	'housing_supply_rate': {
        "base_url": "https://api.odcloud.kr/api/15107590/v1/uddi:3a858c9c-54e3-4cc8-85ea-ae5fc6261517",
        "page": 1,
        "perPage": 50,
    }, 
	# ---------------------------- 강원특별자치도 동해시 원룸 및 오피스텔 현황
	'status_of_one_room_and_officetel': {
        "base_url": "https://api.odcloud.kr/api/15127165/v1/uddi:995b718a-19d8-4690-8dda-ccd4bf584708",
        "page": 1,
        "perPage": 50,
    }, 


    #=====================
    #      [환경기상]
    #===================== 
    # ---------------------------- 강원특별자치도 동해시 석면조사대상 건축물 현황
      'status_of_buildings_subject_to_asbestos_investigation': {
        "base_url": "https://api.odcloud.kr/api/3046203/v1/uddi:c39d3c2a-7d45-4358-b748-ce077e95703b",
        "page": 1,
        "perPage": 50,
    }, 
    # ---------------------------- 강원특별자치도 동해시 상하수도요금
      'water_and_sewage_rates': {
        "base_url": "https://api.odcloud.kr/api/15043236/v1/uddi:89630a7b-142d-4d80-b32d-b28e33c3a185",
        "page": 1,
        "perPage": 50,
    }, 
    # ---------------------------- 강원특별자치도 동해시 천곡동굴산 식물정보
      'cheongok_cave_mountain_plant_information': {
        "base_url": "https://api.odcloud.kr/api/15030374/v1/uddi:f7acaf4f-7783-42aa-a0dc-c882b1e7853a",
        "page": 1,
        "perPage": 50,
    }, 
    # ---------------------------- 강원특별자치도 동해시 사업장폐기물 배출자 신고정보
      'business_waste_discharger_reporting_information': {
        "base_url": "https://api.odcloud.kr/api/15060366/v1/uddi:8ac9bd50-648f-487f-82fb-ec8bb1711a86",
        "page": 1,
        "perPage": 50,
    }, 
    # ---------------------------- 강원도 동해시 스마트 워터 미터 위치
      'smart_water_meter_location': {
        "base_url": "https://api.odcloud.kr/api/15103864/v1/uddi:e6ffcb33-0680-430e-a863-ef21c10b8266",
        "page": 1,
        "perPage": 50,
    }, 
    # ---------------------------- 강원특별자치도 동해시 의류수거함정보
      'clothing_collection_box_information': {
        "base_url": "https://api.odcloud.kr/api/15128329/v1/uddi:8c88bfce-c1df-464f-84bb-dd9a8dc7601e",
        "page": 1,
        "perPage": 50,
    }, 
    # ---------------------------- 동해시시설관리공단 쓰레기종량제봉투 LOT정보
      'waste_volume_based_system_bag_lot_information': {
        "base_url": "https://api.odcloud.kr/api/15075295/v1/uddi:153f5a6c-0740-4066-8ee5-a299d929da9b",
        "page": 1,
        "perPage": 50,
    }, 
    # ---------------------------- 동해시시설관리공단 쓰레기종량제봉투 단가
      'waste_volume_based_system_bag_unit_price': {
        "base_url": "https://api.odcloud.kr/api/15075294/v1/uddi:d11bef62-be58-411c-8240-fe12538154d6",
        "page": 1,
        "perPage": 50,
    }, 
    # ---------------------------- 동해시시설관리공단 쓰레기종량제봉투 재고
      'waste_volume_based_system_bag_inventory': {
        "base_url": "https://api.odcloud.kr/api/15075291/v1/uddi:24489c36-3272-426b-bd86-ed5cded8e6bc",
        "page": 1,
        "perPage": 50,
    }, 
    # ---------------------------- 동해시시설관리공단 쓰레기종량제봉투 지정판매소
      'waste_volume_based_system_bag_designated_sales_office': {
        "base_url": "https://api.odcloud.kr/api/15075289/v1/uddi:0e248f4d-b412-4447-93b7-f0500e5b2fdf",
        "page": 1,
        "perPage": 50,
    }, 
    # ---------------------------- 동해시시설관리공단 쓰레기종량제봉투 전화접수
      'waste_volume_based_system_bag_telephone_reception': {
        "base_url": "https://api.odcloud.kr/api/15075290/v1/uddi:de886348-f22c-439a-92f7-ee976250d26a",
        "page": 1,
        "perPage": 50,
    }, 
    # ---------------------------- 동해시시설관리공단 쓰레기종량제봉투 수불
      'waste_volume_based_system_bag_receipt_and_payment': {
        "base_url": "https://api.odcloud.kr/api/15075292/v1/uddi:3c47489d-4821-40a7-87b4-9fb48dee94bf",
        "page": 1,
        "perPage": 50,
    }, 
    # ---------------------------- 동해시시설관리공단 쓰레기종량제봉투 포장단위
      'waste_volume_based_system_bag_packaging_unit': {
        "base_url": "https://api.odcloud.kr/api/15075288/v1/uddi:9c817f97-572f-4562-a43d-96a4fc6d16bf",
        "page": 1,
        "perPage": 50,
    }, 
    # ---------------------------- 동해시시설관리공단 쓰레기종량제봉투 발주 상세내역
         'waste_volume_based_system_bag_order_details': {
        "base_url": "https://api.odcloud.kr/api/15075293/v1/uddi:dfa80595-8213-41d2-9f1a-b1540c679eb0",
        "page": 1,
        "perPage": 50,
    },


    #=====================
    #      [재정금융]
    #===================== 
	# ----------------------------강원특별자치도 동해시 지방세 납부 현황
      'local_tax_payment_status': {
        "base_url": "https://api.odcloud.kr/api/15079798/v1/uddi:d32bd21d-30bb-4e2e-9ee2-ee809b7e5936",
        "page": 1,
        "perPage": 50,
    },
	# ----------------------------강원특별자치도 동해시 세원 유형별 과세 현황
      'taxation_status_by_tax_source_type': {
        "base_url": "https://api.odcloud.kr/api/15079798/v1/uddi:d32bd21d-30bb-4e2e-9ee2-ee809b7e5936",
        "page": 1,
        "perPage": 50,
    },
	# ----------------------------강원특별자치도 동해시 지방세 체납현황
      'local_tax_arrears_status': {
        "base_url": "https://api.odcloud.kr/api/15079803/v1/uddi:c47c6a64-b4b5-4897-8c1b-f49e7b689460",
        "page": 1,
        "perPage": 50,
    },
	# ----------------------------강원특별자치도 동해시 지방세 징수현황
      'local_tax_collection_status': {
        "base_url": "https://api.odcloud.kr/api/15079785/v1/uddi:70780521-f628-4955-9a41-815b59419c42",
        "page": 1,
        "perPage": 50,
    },
	# ----------------------------강원특별자치도 동해시 1인당 지방세 부담액
      'local_tax_burden_per_person': {
        "base_url": "https://api.odcloud.kr/api/15079784/v1/uddi:49a77d85-ee76-4273-b35c-81ede5e2c874",
        "page": 1,
        "perPage": 50,
    },
	# ----------------------------강원특별자치도 동해시 지방세 과세 현황
      'local_tax_assessment_status': {
        "base_url": "https://api.odcloud.kr/api/15079787/v1/uddi:52538ffd-bec2-4daf-a836-8ad218cc2a30",
        "page": 1,
        "perPage": 50,
    },
	# ----------------------------강원특별자치도 동해시 지방세 미환급 현황
      'local_tax_non_refund_status': {
        "base_url": "https://api.odcloud.kr/api/15079802/v1/uddi:c3b25ad9-e682-4a0c-a10c-c9237b8cf15e",
        "page": 1,
        "perPage": 50,
    },
	# ----------------------------강원특별자치도 동해시 지방세 비과 감면율 현황
      'local_tax_exemption_rate_status': {
        "base_url": "https://api.odcloud.kr/api/15079795/v1/uddi:c8d2ce68-b4f6-47ba-a96f-9d096e917e0c",
        "page": 1,
        "perPage": 50,
    },
	# ----------------------------강원특별자치도 동해시 지방세납세자별 부과징수현황
      'local_tax_assessment_and_collection_status_by_taxpayer': {
        "base_url": "https://api.odcloud.kr/api/15079792/v1/uddi:33d13f9d-625e-4652-b7d8-ddf57881590f",
        "page": 1,
        "perPage": 50,
    },
    #=====================
    #      [재난안전]
    #===================== 
    # ----------------------------강원도 동해시 인명구조기구함
      'lifesaving_device_box': {
        "base_url": "https://api.odcloud.kr/api/15102515/v1/uddi:d09fbc92-54a4-4404-96ab-e4a8e0e6c8eb",
        "page": 1,
        "perPage": 50,
    },

    # ========================================================== 보류 ========================================================== 
    # ========================================================== 동해시시설관리공단_동해시시설관리공단 체육시설 시설 : 동해시설관리공단 데이터 제공 방식은 구려서 추후 크롤링으로 변경  
    "sports_facilities": {
        "base_url": "https://api.odcloud.kr/api/15075285/v1/uddi:5c0234bf-b03b-40bd-9e54-c7beb11a77ac",
        "page": 1,
        "perPage": 20,
    },
    #동해시시설관리공단_동해시종합버스터미널 환경친화차 이용현황
    
    # ========================================================== 보류 ==========================================================


}

def fetch_data_from_api(api_name: str) -> dict:
    
    """
    특정 API를 호출하거나 MongoDB 데이터를 반환.
    - api_name: API 설정 이름
    """
    
    
    if api_name not in API_SETTINGS:
        raise HTTPException(status_code=400, detail=f"Unknown API name: {api_name}")
        
    # MongoDB를 사용할 경우 처리
    if API_SETTINGS[api_name] == "use_mongo":
        return fetch_data_from_mongo(api_name)

    
    # 외부 API 호출
    api_config = API_SETTINGS[api_name]
    base_url = api_config["base_url"]

    # 기본 `page`와 `perPage`를 설정
    params = {
        "page": api_config.get("page", 1),
        "perPage": api_config.get("perPage", 10),
        "serviceKey": service_key,
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code != 200:
        raise print(HTTPException(status_code=response.status_code, detail="외부 API 호출 실패"))
    
    
    return response.json()['data']

def fetch_data_from_mongo(collection_name : str, db = mongo_db()) -> list:
    """
    MongoDB에서 데이터를 가져오는 함수.
    collection_name 적용하기
    """
    collection = db[collection_name]
    data = list(collection.find({}, {"_id": 0}))  # `_id` 필드는 제외
    
    if not data:
        raise HTTPException(status_code=404, detail="No data found in MongoDB.")
    
    return data
