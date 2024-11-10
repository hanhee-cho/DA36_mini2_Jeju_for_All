import streamlit as st
import os
from pages import intro_page, user_recommendations_page, more_recommendations_page, discount_page
from utils.style import set_background
from model import recommendation_model


# data_1과 data_2 폴더에서 모든 jpg 파일 경로 동적으로 가져오기
data_1_images = [os.path.join("data/data_1", file) for file in os.listdir("data/data_1") if file.endswith(".jpg")]
data_2_images = [os.path.join("data/data_2", file) for file in os.listdir("data/data_2") if file.endswith(".jpg")]


places_1 = [
    ("김녕 해수욕장", "에메랄드빛 바다가 펼쳐진 제주 동부의 아름다운 해수욕장"),
    ("에코랜드 테마파크", "제주 숲 속 기차여행을 즐길 수 있는 자연 테마파크"),
    ("카멜리아힐", "수많은 동백꽃이 아름답게 피어나는 정원"),
    ("섭지코지", "제주의 동쪽 해안 절경을 감상할 수 있는 명소"),
    ("절물자연휴양림", "숲 속에서의 힐링을 즐길 수 있는 자연휴양림"),
    ("9.81파크", "제주에서 즐기는 레이싱과 익스트림 스포츠의 천국"),
    ("훈데르트바서파크", "예술과 자연이 어우러진 독특한 건축물과 정원"),
    ("선녀와 나무꾼 테마공원", "옛 제주 생활 문화를 체험할 수 있는 테마파크"),
    ("서프라이즈 테마파크", "다양한 체험과 볼거리가 있는 가족 테마파크"),
    ("더마파크", "말과 함께하는 이색적인 체험 공간")
]

places_2 = [
    ("김만덕기념관", "제주 역사 속 김만덕의 삶과 정신을 기리는 기념관"),
    ("그리스신화박물관", "그리스 신화 속 이야기와 작품을 전시하는 박물관"),
    ("국립제주박물관", "제주도의 역사와 문화를 만날 수 있는 국립 박물관"),
    ("너븐숭이4.3기념관", "제주 4.3 사건을 기리는 역사 기념관"),
    ("제주항공우주박물관", "항공과 우주에 관한 다양한 전시와 체험을 제공하는 박물관"),
    ("제주도립미술관", "제주도 예술 작품들을 감상할 수 있는 미술관"),
    ("제주현대미술관", "현대 예술 작품들이 전시된 독특한 미술 공간"),
    ("ICC제주국제컨벤션센터", "국제회의와 행사들이 열리는 컨벤션센터"),
    ("남원큰엉해변", "제주의 아름다운 바위와 절벽이 어우러진 해변"),
    ("선녀와 나무꾼테마공원", "제주 전통과 옛 생활을 체험할 수 있는 테마공원")
]

#-------------------------------------------------------------------------------#

# 스타일 적용
set_background() # 배경

# 페이지 진행 상테를 세션 상태로 관리
if "page" not in st.session_state:
    st.session_state.page = "intro"

# 현재 페이지에 따라 다른 화면 보여줌
if st.session_state.page == "intro":
    intro_page.display()

elif st.session_state.page == "user_recommendations":
    user_info = user_recommendations_page.sidebar_inputs()
    user_recommendations_page.display_user_info(*user_info)
    user_recommendations_page.display_recommendations()

elif st.session_state.page == "more_recommendations":
    more_recommendations_page.display_recommendations(places_1, data_1_images)

elif st.session_state.page == "discount":
    discount_page.show_discount_coupon()




