import streamlit as st

# 사이드바
def sidebar_inputs():
    # 배경색 설정
    sidebar_bg_color = "#ffe8be"
    main_bg_color = "#fffee1"

    # CSS 스타일 적용
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
    st.write('-' * 10)

    # 사이드바 input
    with st.sidebar:
        st.header('여행객 정보를 입력해주세요 😄')
        # 사용자 정보 입력
        age_group = st.selectbox("**연령대**", ("10대", "20대", "30대", "40대", "50대", "60대 이상"))
        gender = st.radio("**성별**", ("여성", "남성"))
        companion_count = st.number_input("**동반자 수 (최대 10명)**", min_value=0, max_value=10, value=0, step=1)

        # 여행 스타일 선택
        st.header("당신의 여행 스타일은?")
        activate_score = st.slider("**휴식형 vs 체험형**", min_value=1, max_value=7)
        famous_score = st.slider("**유명관광지 vs 나만 알고 싶은 곳**", min_value=1, max_value=7)
        planned_score = st.slider("**J의 여행 vs P의 여행**", min_value=1, max_value=7)
        picture_score = st.slider("**눈에 담으면 돼 vs 남는 건 사진뿐**", min_value=1, max_value=7)

        # Barrier Free 옵션 체크박스
        st.write("**장애인 편의 시설**")
        barrier_free_options = {
            "장애인 주차장": st.checkbox("🅿️ 장애인 주차장"),
            "장애인 화장실": st.checkbox("🚻 장애인 화장실"),
            "휠체어 보유": st.checkbox("👨🏻‍🦽 휠체어 보유"),
            "안내견 동반 가능": st.checkbox("🦮 안내견 동반 가능"),
            "점자 안내": st.checkbox("👆 점자 안내"),
            "한국어 음성 안내": st.checkbox("🔈 한국어 음성 안내"),
        }
        selected_barrier_free = [key for key, value in barrier_free_options.items() if value]

    # 입력된 데이터를 반환
    return age_group, gender, companion_count, activate_score, famous_score, planned_score, picture_score, selected_barrier_free


# 유저 정보 보여주기
def display_user_info(age_group, gender, companion_count, activate_score, famous_score, planned_score, picture_score, selected_barrier_free):
    # 선택된 정보 메인 화면에 표시
    st.subheader('📌 여행객 정보')
    st.markdown(f"""
    ##### 👤 기본 정보
    - **연령대**: {age_group}
    - **성별**: {gender}
    - **동반객 인원수**: {companion_count}명
    """)

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


def display_recommendations():

    # 페이지 변경 함수
    def go_to_page(page_num):
        st.session_state['page'] = page_num

    # 첫 번째 컨테이너
    with st.container():
        st.subheader('📌 놓칠 수 없는 명소')
        # col1, col2 = st.columns(2)
        col1, col2 = st.columns([1, 1.2])  # 첫 번째 열을 두 배 더 넓게 설정
        with col1:
            st.image("./data/9.81파크.jpg", width=300)

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
            st.image("./data/그리스신화박물관.jpg", use_column_width=True)  # 이미지 경로를 실제 이미지 파일 경로로 바꾸세요.
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
            st.image("./data/빛의벙커.jpg", use_column_width=True)  # 이미지 경로를 실제 이미지 파일 경로로 바꾸세요.
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


    # 페이지 하단에 양 옆에 버튼 배치
    col1, col2, col3 = st.columns([2, 2.5, 2])  # 좌측, 중앙, 우측 열로 나누기

    with col3:
        if st.button("더 많은 추천 장소➡️"):
            go_to_page("more_recommendations")
