import streamlit as st
#
# # 배경색 설정 (고정)
# sidebar_bg_color = "#ffe8be"  # 사이드바 배경색
# main_bg_color = "#fffee1"     # 메인 페이지 배경색
#
# # CSS 스타일을 적용하여 배경 색 변경
# st.markdown(f"""
#     <style>
#     /* 사이드바 배경 색 설정 */
#     section[data-testid="stSidebar"] > div:first-child {{
#         background-color: {sidebar_bg_color};
#     }}
#     /* 메인 페이지 배경 색 설정 */
#     .stApp {{
#         background-color: {main_bg_color};
#     }}
#     </style>
#     """, unsafe_allow_html=True)
#
# # 페이지 제목
# st.title('🍊모두를 위한 제주🍊')
#
# # sidebar input
# with st.sidebar:
#     st.header('여행객 정보를 입력해주세요 😄')
#
#     # 연령대 선택
#     age_group = st.selectbox(
#         " - 연령대",
#         ("10대", "20대", "30대", "40대", "50대", "60대 이상")
#     )
#
#     # 성별 선택
#     gender = st.radio(
#         " - 성별",
#         ("여성", "남성")
#     )
#
#     # 동반객 인원수 선택
#     companion_count = st.number_input(
#         "- 동반객 인원수 (최대 10명)",
#         min_value=0,
#         max_value=10,
#         value=0,
#         step=1
#     )
#
#     # 여행 스타일 선택 (여러 개 선택 가능)
#     travel_style = st.multiselect(
#         " - 여행 스타일",
#         ["자연 탐방", "도시 탐험", "문화 체험", "휴식", "액티비티", "미식 탐방"]
#     )
#
#     # Barrier Free 옵션 체크박스
#     st.write(" - 장애인 편의 시설")
#     barrier_free_options = {
#         "장애인 주차장": st.checkbox("장애인 주차장"),
#         "장애인 화장실": st.checkbox("장애인 화장실"),
#         "휠체어 보유": st.checkbox("휠체어 보유"),
#         "안내견 동반 가능": st.checkbox("안내견 동반 가능"),
#         "점자 안내": st.checkbox("점자 안내"),
#         "한국어 음성 안내": st.checkbox("한국어 음성 안내"),
#     }
# selected_barrier_free = [key for key, value in barrier_free_options.items() if value]
#
#
# # 첫 번째 구간
# # 선택된 옵션 - 메인 페이지에 표시
#
# st.subheader('📌 여행객 정보')
# st.markdown(f"""
# - **연령대**: {age_group}
# - **성별**: {gender}
# - **동반객 인원수**: {companion_count}명
# - **여행 스타일**: {", ".join(travel_style) if travel_style else "선택 없음"}
# - **장애인 편의 시설**: {", ".join(selected_barrier_free) if selected_barrier_free else "선택 없음"}
# ---
# """)
#
# # st.subheader('📌 놓칠 수 없는 명소')
#
# import streamlit as st
#
# # 첫 번째 컨테이너
# with st.container():
#     st.subheader('📌 놓칠 수 없는 명소')
#     # col1, col2 = st.columns(2)
#     col1, col2 = st.columns([1, 1.2])  # 첫 번째 열을 두 배 더 넓게 설정
#     with col1:
#         st.image("data/9.81파크.jpg", caption="< 9.81 파크 >",  width=300)
#
#     with col2:
#         st.write("_주소: 제주특별자치도 제주시 애월읍 어음리 산 131_<br>9.81파크는 제주도에 위치한 특별한 테마파크로, '중력'이라는 흥미로운 주제를 바탕으로 다양한 체험과 놀이를 제공하는 공간입니다. "
#                  "저희 파크는 자연과 어우러진 여러 레포츠 활동과 체험 프로그램을 통해 모든 연령대의 방문객들에게 즐거운 경험을 선사하고 있습니다. "
#                  "짚라인, 회전 기구 등 다양한 액티비티가 준비되어 있어 가족 단위 방문객부터 친구들과 함께 오신 분들까지 모두 만족하실 수 있습니다."
#                  "저희 홈페이지에서는 파크의 다양한 시설과 프로그램에 대한 상세한 정보는 물론, 예약 안내와 이벤트 소식도 확인하실 수 있습니다.", unsafe_allow_html=True)
#         st.markdown(
#             """
#             <style>
#             .link-button {
#                 display: inline-block;
#                 background-color: #1a1d53;
#                 color: #ffffff !important;
#                 padding: 8px 13px;
#                 text-align: center;
#                 text-decoration: none;
#                 border-radius: 6px;
#                 font-size: 16px;
#             }
#             .link-button:hover {
#                 background-color: #5fd6f3;
#             }
#             </style>
#             <a class="link-button" href="http://www.greekmythology.co.kr/default/" target="_blank">Link</a>
#             """, unsafe_allow_html=True
#         )
# st.write('-'*30)
# st.markdown("<br><h5>️ 더 많은 추천 장소 ➡️ </h5>", unsafe_allow_html=True)
# # 두 번째 컨테이너
# with st.container():
#     col1, col2 = st.columns([1, 3])
#     with col1:
#         st.image("data/그리스신화박물관.jpg", caption="< 그리스 신화 박물관 >", use_column_width=True)  # 이미지 경로를 실제 이미지 파일 경로로 바꾸세요.
#     with col2:
#         # st.write("**#1**")
#         st.markdown("**#1**<br>제주시 한림읍 금악리 제주-중문간 평화로 중간 교통요충지에 들어선 그리스신화박물관은 대지 2만평, 연건평 1000평 규모로 유럽 유명 박물관이 소장한 그리스신화 관련.. _더보기_", unsafe_allow_html=True)
#         st.markdown(
#             """
#             <style>
#             .link-button {
#                 display: inline-block;
#                 background-color: #1a1d53;
#                 color: #ffffff !important;
#                 padding: 7px 10px;
#                 text-align: center;
#                 text-decoration: none;
#                 border-radius: 4px;
#                 font-size: 10px;
#             }
#             .link-button:hover {
#                 background-color: #5fd6f3;
#             }
#             </style>
#             <a class="link-button" href="http://www.greekmythology.co.kr/default/" target="_blank">Link</a>
#             """, unsafe_allow_html=True
#         )
#
# st.markdown("<br>", unsafe_allow_html=True)
# # 세 번째 컨테이너
# with st.container():
#     col1, col2 = st.columns([1, 3])
#     with col1:
#         st.image("data/빛의벙커.jpg", caption="< 빛의 벙커 >", use_column_width=True)  # 이미지 경로를 실제 이미지 파일 경로로 바꾸세요.
#         col1.empty()
#     with col2:
#         # st.write("**#2**")
#         st.markdown("**#2**<br>옛 국가 기간통신시설이던 오래된 벙커가 2012년 민간에 매각돼 ‘빛의 벙커’로 태어났다. 빛의 벙커는.. _더보기_", unsafe_allow_html=True)
#         st.markdown(
#             """
#             <style>
#             .link-button {
#                 display: inline-block;
#                 background-color: #1a1d53;
#                 color: #ffffff !important;
#                 padding: 3px 5px;
#                 text-align: center;
#                 text-decoration: none;
#                 border-radius: 2px;
#                 font-size: 10px;
#             }
#             .link-button:hover {
#                 background-color: #5fd6f3;
#             }
#             </style>
#             <a class="link-button" href="https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=a1b8c604-0c55-4127-ba19-86d8b36ec947" target="_blank">Link</a>
#             """, unsafe_allow_html=True
#         )

st.write('-'*30)

# query_params = st.query_params  # 최신 방식
# page = query_params.get("page", ["main"])[0]
# # # 페이지에 따라 다른 내용 표시
# # if page == "other":
# #     st.write("여기는 다른 페이지입니다!")
# # else:
# #     st.write("여기는 메인 페이지입니다!")
# # 다른 페이지로 이동 버튼
# if st.button("더 많은 추천 장소 보러 가기🫠"):
#     st.experimental_set_query_params(page="other")
#

# 세션 상태에 'page'가 없으면 기본값을 1로 설정
if 'page' not in st.session_state:
    st.session_state['page'] = 1

# 페이지 변경 함수
def go_to_page(page_num):
    st.session_state['page'] = page_num

# # 현재 페이지 표시
# st.write(f"Current Page: {st.session_state['page']}")

# 페이지별 내용 표시
if st.session_state['page'] == 1:
    # st.title("Page 1")
    # st.write("This is the content of Page 1.")
    import streamlit as st

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

    # sidebar input
    with st.sidebar:
        st.header('여행객 정보를 입력해주세요 😄')

        # 연령대 선택
        age_group = st.selectbox(
            " - 연령대",
            ("10대", "20대", "30대", "40대", "50대", "60대 이상")
        )

        # 성별 선택
        gender = st.radio(
            " - 성별",
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
            " - 여행 스타일",
            ["자연 탐방", "도시 탐험", "문화 체험", "휴식", "액티비티", "미식 탐방"]
        )

        # Barrier Free 옵션 체크박스
        st.write(" - 장애인 편의 시설")
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

    # st.subheader('📌 놓칠 수 없는 명소')

    import streamlit as st

    # 첫 번째 컨테이너
    with st.container():
        st.subheader('📌 놓칠 수 없는 명소')
        # col1, col2 = st.columns(2)
        col1, col2 = st.columns([1, 1.2])  # 첫 번째 열을 두 배 더 넓게 설정
        with col1:
            st.image("data/9.81파크.jpg", caption="< 9.81 파크 >", width=300)

        with col2:
            st.write(
                "_주소: 제주특별자치도 제주시 애월읍 어음리 산 131_<br>9.81파크는 제주도에 위치한 특별한 테마파크로, '중력'이라는 흥미로운 주제를 바탕으로 다양한 체험과 놀이를 제공하는 공간입니다. "
                "저희 파크는 자연과 어우러진 여러 레포츠 활동과 체험 프로그램을 통해 모든 연령대의 방문객들에게 즐거운 경험을 선사하고 있습니다. "
                "짚라인, 회전 기구 등 다양한 액티비티가 준비되어 있어 가족 단위 방문객부터 친구들과 함께 오신 분들까지 모두 만족하실 수 있습니다."
                "저희 홈페이지에서는 파크의 다양한 시설과 프로그램에 대한 상세한 정보는 물론, 예약 안내와 이벤트 소식도 확인하실 수 있습니다.", unsafe_allow_html=True)
            st.markdown(
                """
                <style>
                .link-button {
                    display: inline-block;
                    background-color: #1a1d53;
                    color: #ffffff !important;
                    padding: 8px 13px;
                    text-align: center;
                    text-decoration: none;
                    border-radius: 6px;
                    font-size: 16px;
                }
                .link-button:hover {
                    background-color: #5fd6f3;
                }
                </style>
                <a class="link-button" href="http://www.greekmythology.co.kr/default/" target="_blank">Link</a>
                """, unsafe_allow_html=True
            )
    st.write('-' * 30)
    # st.markdown("<br><h5>️ 더 많은 추천 장소 ➡️ </h5>", unsafe_allow_html=True)

    if st.button("더 많은 추천 장소 보러 가기🫠"):
        go_to_page(2)
    # 두 번째 컨테이너
    with st.container():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image("data/그리스신화박물관.jpg", caption="< 그리스 신화 박물관 >",
                     use_column_width=True)  # 이미지 경로를 실제 이미지 파일 경로로 바꾸세요.
        with col2:
            # st.write("**#1**")
            st.markdown(
                "**#1**<br>제주시 한림읍 금악리 제주-중문간 평화로 중간 교통요충지에 들어선 그리스신화박물관은 대지 2만평, 연건평 1000평 규모로 유럽 유명 박물관이 소장한 그리스신화 관련.. _더보기_",
                unsafe_allow_html=True)
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
            st.image("data/빛의벙커.jpg", caption="< 빛의 벙커 >", use_column_width=True)  # 이미지 경로를 실제 이미지 파일 경로로 바꾸세요.
            col1.empty()
        with col2:
            # st.write("**#2**")
            st.markdown("**#2**<br>옛 국가 기간통신시설이던 오래된 벙커가 2012년 민간에 매각돼 ‘빛의 벙커’로 태어났다. 빛의 벙커는.. _더보기_",
                        unsafe_allow_html=True)
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
    # if st.button("더 많은 추천 장소 보러 가기🫠"):
    #     go_to_page(2)

elif st.session_state['page'] == 2:
    st.title("그 외 추천 장소")
    # st.write("This is the content of Page 2.")
    st.title("그리스신화박물관")
    st.write(
        "제주시 한림읍 금악리 제주-중문간 평화로 중간 교통요충지에 들어선 그리스신화박물관은 대지 2만평, 연건평 1000평 규모로 유럽 유명 박물관이 소장한 그리스신화 관련 작품만을 엄선해 3년여의 재현 과정을 거쳐 선보이는 세계 최초의 그리스신화 전문 박물관입니다.")

    # 박물관 이미지 추가
    st.image("data/그리스신화박물관.jpg", caption="그리스신화박물관", use_column_width=True)

    if st.button("Go to Page 1"):
        go_to_page(1)
    if st.button("Go to Page 3"):
        go_to_page(3)

elif st.session_state['page'] == 3:
    st.title("Page 3")
    st.write("This is the content of Page 3.")
    if st.button("Go to Page 2"):
        go_to_page(2)
