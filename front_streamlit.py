import streamlit as st

# 배경색 설정 (고정)
sidebar_bg_color = "#ffe8be"  # 사이드바 배경색
main_bg_color = "#fffee1"     # 메인 페이지 배경색

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

# sidebar input
with st.sidebar:
    st.header('여행객 정보를 입력해주세요 😄')

    # 연령대 선택
    age_group = st.selectbox(
        "- 연령대",
        ("10대", "20대", "30대", "40대", "50대", "60대 이상")
    )

    # 성별 선택
    gender = st.radio(
        "- 성별",
        ("여성", "남성")
    )

    # 동반객 인원수 선택
    companion_count = st.number_input(
        "- 동반객 인원수 (최대 10명)",
        min_value=0,
        max_value=10,
        value=0,
        step=1
    )

    # 여행 스타일 선택 (여러 개 선택 가능)
    travel_style = st.multiselect(
        "- 여행 스타일",
        ["자연 탐방", "도시 탐험", "문화 체험", "휴식", "액티비티", "미식 탐방"]
    )

    # Barrier Free 옵션 체크박스
    st.write("- 장애인 편의 시설")
    barrier_free_options = {
        "장애인 주차장": st.checkbox("장애인 주차장"),
        "장애인 화장실": st.checkbox("장애인 화장실"),
        "휠체어 보유": st.checkbox("휠체어 보유"),
        "안내견 동반 가능": st.checkbox("안내견 동반 가능"),
        "점자 안내": st.checkbox("점자 안내"),
        "한국어 음성 안내": st.checkbox("한국어 음성 안내"),
    }
selected_barrier_free = [key for key, value in barrier_free_options.items() if value]


# 첫 번째 구간
# 선택된 옵션 - 메인 페이지에 표시

st.subheader('📌 여행객 정보')
st.markdown(f"""
- **연령대**: {age_group}
- **성별**: {gender}
- **동반객 인원수**: {companion_count}명
- **여행 스타일**: {", ".join(travel_style) if travel_style else "선택 없음"}
- **장애인 편의 시설**: {", ".join(selected_barrier_free) if selected_barrier_free else "선택 없음"}
---
""")

st.subheader('📌 추천 장소')

import streamlit as st

# 첫 번째 컨테이너
with st.container():
    col1, col2 = st.columns(2)
    # col1, col2 = st.columns([2, 1])  # 첫 번째 열을 두 배 더 넓게 설정
    with col1:
        st.image("data/9.81파크.jpg", caption="< 9.81 파크 >", use_column_width=True)  # 이미지 경로를 실제 이미지 파일 경로로 바꾸세요.
    # 두 번째 열에 다른 내용 추가
    with col2:
        # st.markdown("[여기 클릭하여 여행지 정보 보기](https://www.981park.com/)", unsafe_allow_html=True)
        st.markdown(
            """
            <style>
            .link-button {
                display: inline-block;
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                border-radius: 5px;
                font-size: 16px;
            }
            .link-button:hover {
                background-color: #45a049;
            }
            </style>
            <a class="link-button" href="https://www.981park.com/" target="_blank">여기 클릭하여 여행지 정보 보기</a>
            """, unsafe_allow_html=True
        )

st.markdown("<br><h5>️ 더 많은 추천 장소 ➡️ </h5>", unsafe_allow_html=True)
# 두 번째 컨테이너
with st.container():
    col1, col2 = st.columns([2, 1])  # 첫 번째 열을 두 배 더 넓게 설정
    with col1:
        st.image("data/그리스신화박물관.jpg", caption="< 그리스 신화 박물관 >", use_column_width=True)  # 이미지 경로를 실제 이미지 파일 경로로 바꾸세요.
    # 두 번째 열에 다른 내용 추가
    with col2:
        st.write( "제주시 한림읍 금악리 제주-중문간 평화로 중간 교통요충지에 들어선 그리스신화박물관은 대지 2만평, "
    "연건평 1000평 규모로 유럽 유명 박물관이 소장한 그리스신화 관련 작품만을 엄선해 3년여의 재현 과정을 거쳐 선보이는 "
    "세계 최초의 그리스신화 전문 박물관이다. 바티칸 등 서양 주요 박물관 및 미술관의 그리스신화 주제의 유명 명화와 "
    "대리석 조각상 등 총 200여 점을 재현해 놓아 유럽에 가지 않고도 유럽 유명 박물관 20여 곳에 흩어져 있는 "
    "그리스로마신화 관련 소장품을 제주에서 생동감 있게 관람할 수 있다.")
        st.markdown("[여기 클릭하여 여행지 정보 보기](http://www.greekmythology.co.kr/default/)", unsafe_allow_html=True)

# 세 번째 컨테이너
with st.container():
    # 두 열로 나누기
    col1, col2 = st.columns([1, 1])  # 두 번째와 세 번째 컨테이너의 열은 동일한 크기로 설정
    with col1:
        st.write("첫 번째 열 내용 3")
    with col2:
        st.write("두 번째 열 내용 3")
