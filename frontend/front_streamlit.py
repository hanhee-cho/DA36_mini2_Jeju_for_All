import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm
from sklearn.preprocessing import LabelEncoder
from catboost import Pool
from sklearn.model_selection import train_test_split
from catboost import CatBoostRegressor
import unicodedata
from itertools import combinations
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import KeyedVectors

main_df = pd.read_csv('./data/main_data.csv')
real_df = pd.read_csv('./data/real_data.csv')
ct_sim = pd.read_csv('./data/ct_sim.csv', index_col=0)
df=pd.read_csv('./data/df.csv')

if 'page' not in st.session_state:
    st.session_state['page'] = 1
# 페이지 변경 함수
def go_to_page(page_num):
    st.session_state['page'] = page_num

if st.session_state['page'] == 1:
    st.image("./data/jeju-min.gif",width=1000)
    import base64
    # 로컬 GIF 파일을 base64로 인코딩하여 HTML에 삽입하기
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    # 로컬 GIF 파일 경로 설정
    img_path = './data/jeju-min.gif'  # 사용자의 GIF 파일 경로로 변경
    # base64 인코딩한 이미지 삽입
    base64_img = get_base64_of_bin_file(img_path)
    # CSS를 사용하여 배경 이미지 스타일 적용
    st.markdown(
        f"""
        <style>
        .full-bg {{
            background-image: url("data:image/gif;base64,{base64_img}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            position: fixed;
            width: 100%;
            height: 90%;
            top: 0;
            left: 0;
            z-index: -1;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    # full-bg라는 클래스가 있는 div 추가
    st.markdown('<div class="full-bg"></div>', unsafe_allow_html=True)

    # 콘텐츠 추가 (선택 사항)
    st.title("제주, 어디까지 가봤니?")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
        ### **Jeju for All 제주의 아름다움을 누구나 경험할 수 있도록!**  
        장애 유무와 관계없이 안전하고 편리하게 여행할 수 있는 배리어프리 명소와 여행 팁을 소개합니다.  
        편안한 제주 여행을 위한 모든 정보를 한눈에 만나보세요.
    """)
    if st.button("나만을 위한 여행지 추천 받기 ❤️"):
        go_to_page(2)

# 페이지별 내용 표시
elif st.session_state['page'] == 2:
    # 배경색 설정 (고정)
    sidebar_bg_color = "#ffe8be"  # 사이드바 배경색
    main_bg_color = "#fffee1"  # 메인 페이지 배경색

    # CSS 스타일을 적용하여 배경 색 변경
    st.markdown(f"""
        <style>
        /* 사이드바 배경 색 설정 */
        section[data-testid="stSidebar"] > div:first-child {{
            background-color: {sidebar_bg_color};
        }}
        /* 메인 페이지 배경 색 설정 */
        .stApp {{
            background-color: {main_bg_color};
        }}
        </style>
        """, unsafe_allow_html=True)

    # 페이지 제목
    st.title('🍊모두를 위한 제주🍊')
    if st.button("시작 화면으로️"):
        go_to_page(1)
    st.write('-'*10)
    # sidebar input
    with st.sidebar:
        st.header('여행객 정보를 입력해주세요 😄')
        # 연령대 선택
        age_group = st.selectbox(
            "**연령대**",
            ("10대", "20대", "30대", "40대", "50대", "60대 이상")
        )

        # 성별 선택
        gender = st.radio(
            "**성별**",
            ("여성", "남성")
        )

        # 동반객 인원수 선택
        companion_count = st.number_input(
            "**동반자 수 (최대 10명)**",
            min_value=0,
            max_value=10,
            value=0,
            step=1
        )
        st.header("어떤 여행지를 원하시나요?")
        selected_category = st.selectbox(
            "**여행지 분류**",
            ("관광지", "대형체육시설", "전시/기념관", "대형레저시설", "공원", "영화/연극/공연")
        )

        st.header("당신의 여행 스타일은?")
        # 슬라이더로 1부터 8까지 점수 선택
        activate_score = st.slider("**휴식형    vs     체험형**", min_value=1, max_value=7)
        famous_score = st.slider("**유명관광지 vs 나만 알고 싶은 곳**", min_value=1, max_value=7)
        planned_score = st.slider("**J의 여행 vs P의 여행**", min_value=1, max_value=7)
        picture_score = st.slider("**눈에 담으면 돼 vs 남는 건 사진뿐**", min_value=1, max_value=7)


        # Barrier Free 옵션 체크박스
        st.write("**장애인 편의 시설**")
        # st.subheader("장애인 편의 시설")
        barrier_free_options = {
            "장애인 주차장": st.checkbox("🅿️ 장애인 주차장"),
            "장애인 화장실": st.checkbox("🚻 장애인 화장실"),
            "휠체어 보유": st.checkbox("👨🏻‍🦽 휠체어 보유"),
            "안내견 동반 가능": st.checkbox("🦮 안내견 동반 가능"),
            "점자 안내": st.checkbox("👆 점자 안내"),
            "한국어 음성 안내": st.checkbox("🔈 한국어 음성 안내"),
        }
    selected_barrier_free = [key for key, value in barrier_free_options.items() if value]

    # 첫 번째 구간
    # 선택된 옵션 - 메인 페이지에 표시

    st.subheader('📌 여행객 정보')
    st.markdown(f"""
    ##### 👤 기본 정보
    - **연령대**: {age_group}
    - **성별**: {gender}
    - **동반객 인원수**: {companion_count}명
    """)

    st.markdown(f"""
    ##### 🎡 여행지
    - **원하는 분류**: {selected_category if selected_category else '선택 없음'}""")

    st.markdown(f"""
    ##### 💼 여행 스타일
    - **휴식형(1) vs 체험형(7)**: {activate_score if activate_score else '선택 없음'}
    - **유명관광지(1) vs 나만 알고 싶은 곳(7)**: {famous_score if famous_score else '선택 없음'}
    - **J의 여행(1) vs P의 여행(7)**: {planned_score if planned_score else '선택 없음'}
    - **눈에 담으면 돼(1) vs 남는 건 사진뿐(7)**: {picture_score if picture_score else '선택 없음'}
    """)
    st.markdown(f"""
    ##### 🔎 기타
    - **장애인 편의 시설**: {", ".join(selected_barrier_free) if selected_barrier_free else "선택 없음"}
    ---
    """)

    # 첫 번째 컨테이너
    with st.container():
        st.subheader('📌 놓칠 수 없는 명소')
        # col1, col2 = st.columns(2)
        col1, col2 = st.columns([1, 1.2])  # 첫 번째 열을 두 배 더 넓게 설정
        with col1:
            st.image("data/9.81파크.jpg", width=300)

        with col2:
            st.markdown("##### 9.81 파크")
            st.write(
                "_주소: 제주특별자치도 제주시 애월읍 어음리 산 131_<br>9.81파크는 '중력'을 주제로 다양한 체험과 레포츠 활동을 제공하는 제주도의 테마파크입니다."
                " 짚라인, 회전 기구 등 다양한 액티비티가 준비되어 있어 모든 연령대의 방문객들이 즐길 수 있습니다. 홈페이지에서 시설 정보, 예약 안내, 이벤트 소식도 확인할 수 있습니다.", unsafe_allow_html=True)
            st.markdown(
                """
                <style>
                .link-button {
                    display: inline-block;
                    background-color: #1a1d53;
                    color: #ffffff !important;
                    padding: 15px 25px; 
                    text-align: center;
                    text-decoration: none;
                    border-radius: 8px;
                    font-size: 16px;
                }
                .link-button:hover {
                    background-color: #5fd6f3;
                }
                </style>
                <a class="link-button" href="https://www.981park.com/" target="_blank">Link</a>
                """, unsafe_allow_html=True
            )
    st.write('-' * 30)

    st.subheader("여긴 어떠세요?")
    # 두 번째 컨테이너
    with st.container():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image("data/그리스신화박물관.jpg", use_column_width=True)  # 이미지 경로를 실제 이미지 파일 경로로 바꾸세요.
        with col2:
            # st.write("**#1**")
            st.markdown("##### 그리스 신화 박물관")
            st.write("제주시 한림읍 금악리 제주-중문간 평화로 중간 교통요충지에 들어선 그리스신화박물관은 대지 2만평, 연건평 1000평 규모로 유럽 유명 박물관이 소장한 그리스신화 관련.. _더보기_")
            # st.markdown(
            #     "<br>제주시 한림읍 금악리 제주-중문간 평화로 중간 교통요충지에 들어선 그리스신화박물관은 대지 2만평, 연건평 1000평 규모로 유럽 유명 박물관이 소장한 그리스신화 관련.. _더보기_",
            #     unsafe_allow_html=True)
            st.markdown(
                """
                <style>
                .link-button {
                    display: inline-block;
                    background-color: #1a1d53;
                    color: #ffffff !important;
                    padding: 7px 10px;
                    text-align: center;
                    text-decoration: none;
                    border-radius: 4px;
                    font-size: 10px;
                }
                .link-button:hover {
                    background-color: #5fd6f3;
                }
                </style>
                <a class="link-button" href="http://www.greekmythology.co.kr/default/" target="_blank">Link</a>
                """, unsafe_allow_html=True
            )

    st.markdown("<br>", unsafe_allow_html=True)
    # 세 번째 컨테이너
    with st.container():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image("data/빛의벙커.jpg", use_column_width=True)  # 이미지 경로를 실제 이미지 파일 경로로 바꾸세요.
            col1.empty()
        with col2:
            st.markdown("##### 빛의 벙커")
            st.write("옛 국가 기간통신시설이던 오래된 벙커가 2012년 민간에 매각돼 ‘빛의 벙커’로 태어났다. 빛의 벙커는.. _더보기_")
            st.markdown(
                """
                <style>
                .link-button {
                    display: inline-block;
                    background-color: #1a1d53;
                    color: #ffffff !important;
                    padding: 3px 5px;
                    text-align: center;
                    text-decoration: none;
                    border-radius: 2px;
                    font-size: 10px;
                }
                .link-button:hover {
                    background-color: #5fd6f3;
                }
                </style>
                <a class="link-button" href="https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=a1b8c604-0c55-4127-ba19-86d8b36ec947" target="_blank">Link</a>
                """, unsafe_allow_html=True
            )
    if st.button("더 많은 추천 장소 보러 가기➡️"):
        go_to_page(3)
elif st.session_state['page'] == 3:
    # 배경색 설정 (고정)
    main_bg_color = "#fffee1"  # 메인 페이지 배경색

    # CSS 스타일을 적용하여 배경 색 변경
    st.markdown(f"""
        <style>
        /* 메인 페이지 배경 색 설정 */
        .stApp {{
            background-color: {main_bg_color};
        }}
        </style>
        """, unsafe_allow_html=True)

    st.title("Top5 - Top10")
    st.write('-'*20)
    with st.container():
        col1, col2, col3 = st.columns([1, 1, 1])
        col4, col5, col6 = st.columns([1, 1, 1])
        with col1:
            st.image("data/그리스신화박물관.jpg", caption="그리스신화박물관", use_column_width=True)
            st.write("제주시 한림읍 금악리 제주-중문간 평화로 중간 교통요충지에 어쩌구")
        with col2:
            st.image("data/그리스신화박물관.jpg", caption="그리스신화박물관", use_column_width=True)
            st.write("제주시 한림읍 금악리 제주-중문간 평화로 중간 교통요충지에 어쩌구")
        with col3:
            st.image("data/그리스신화박물관.jpg", caption="그리스신화박물관", use_column_width=True)
            st.write("제주시 한림읍 금악리 제주-중문간 평화로 중간 교통요충지에 어쩌구")
        with col4:
            st.image("data/그리스신화박물관.jpg", caption="그리스신화박물관", use_column_width=True)
            st.write("제주시 한림읍 금악리 제주-중문간 평화로 중간 교통요충지에 어쩌구")
        with col5:
            st.image("data/그리스신화박물관.jpg", caption="그리스신화박물관", use_column_width=True)
            st.write("제주시 한림읍 금악리 제주-중문간 평화로 중간 교통요충지에 어쩌구")
        with col6:
            st.image("data/그리스신화박물관.jpg", caption="그리스신화박물관", use_column_width=True)
            st.write("제주시 한림읍 금악리 제주-중문간 평화로 중간 교통요충지에 어쩌구")

    st.write('-' * 20)
    if st.button("이전 페이지"):
        go_to_page(2)
    if st.button("다음 페이지"):
        go_to_page(4)

elif st.session_state['page'] == 4:
    st.title("배리어프리 어쩌구")
    st.write("쿠폰을 받아가셔요.")
    if st.button("처음 페이지"):
        go_to_page(2)
    if st.button("이전 페이지"):
        go_to_page(3)


