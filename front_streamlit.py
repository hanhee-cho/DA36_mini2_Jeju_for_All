import pandas as pd
import streamlit as st
from final import recommend_category
from final import recommend_user_info
from final import combine_recommend
from final import final_recommend
import os
from PIL import Image

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
    # st.image("data/jeju.gif", use_column_width=True)
    st.image("data/jeju.gif", use_container_width=True)
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
    # if st.button("시작 화면으로️"):
    #     go_to_page(1)
    st.write('-'*10)
    # sidebar input
    with st.sidebar:
        st.header('여행객 정보를 입력해주세요 😄')
        # 연령대 선택

        age_group = st.slider("**연령대**", min_value=10, max_value=60, step=10)
        gender_str = st.radio("**성별**", options=["남성", "여성"])
        gender = 0 if gender_str == "남성" else 1
        comp_num = st.number_input("**동반자 수 (최대 10명)**", min_value=0, max_value=10, value=0,step=1)

        st.header("어떤 여행지를 원하시나요?")
        selected_category = st.selectbox(
            "카테고리 선택",
            ("관광지", "대형체육시설", "전시/기념관", "대형레저시설", "공원", "영화/연극/공연")
        )

        st.header("당신의 여행 스타일은?")
        # 슬라이더로 1부터 8까지 점수 선택
        activate_score = st.slider("**휴식형vs체험형**", min_value=1, max_value=7)
        famous_score = st.slider("**유명관광지 vs 나만 알고 싶은 곳**", min_value=1, max_value=7)
        planned_score = st.slider("**J의 여행 vs P의 여행**", min_value=1, max_value=7)
        picture_score = st.slider("**눈에 담으면 돼 vs 남는 건 사진뿐**", min_value=1, max_value=7)


        st.write("**장애인 편의 시설**")
        filter_dspsn_prkplce_at = st.checkbox("🅿️ 장애인 주차장")
        filter_dspsn_toilet_at = st.checkbox("🚻 장애인 화장실")
        filter_wchair_hold_at = st.checkbox("👨🏻‍🦽 휠체어 보유")
        filter_guid_dog_acp_posbl_at = st.checkbox("🦮 안내견 출입 가능")
        filter_brll_guid_at = st.checkbox("👆 점자 안내")
        filter_klang_vic_guid_at = st.checkbox("🔈 한국어 음성 안내")

    # 첫 번째 구간
    # 선택된 옵션 - 메인 페이지에 표시

    st.subheader('📌 여행객 정보')
    st.markdown(f"""
    ##### 👤 기본 정보
    - **연령대**: {age_group}
    - **성별**: {gender_str}
    - **동반자 수**: {comp_num}명
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
    """)

    selected_facilities = []

    if filter_dspsn_prkplce_at:
        selected_facilities.append("장애인 주차장")
    if filter_dspsn_toilet_at:
        selected_facilities.append("장애인 화장실")
    if filter_wchair_hold_at:
        selected_facilities.append("휠체어 보유")
    if filter_guid_dog_acp_posbl_at:
        selected_facilities.append("안내견 출입 가능")
    if filter_brll_guid_at:
        selected_facilities.append("점자 안내")
    if filter_klang_vic_guid_at:
        selected_facilities.append("한국어 음성 안내")

    # 선택된 시설이 있으면 쉼표로 구분해 출력하고, 없으면 '선택된 항목 없음' 출력
    if selected_facilities:
        facilities_text = ", ".join(selected_facilities)
        st.markdown(f"**장애인 편의 시설:** {facilities_text}")
    else:
        st.markdown("**장애인 편의 시설:** 선택된 항목 없음")
    st.write('-' * 20)

    # 첫 번째 컨테이너
    with st.container():
        st.subheader('📌 놓칠 수 없는 명소')
        if st.button("🔎 추천 장소 보기"):
            place_list = final_recommend(gender, age_group, comp_num, activate_score, famous_score, planned_score,
                                         picture_score,
                                         selected_category, ct_sim, main_df,
                                         filter_dspsn_prkplce_at=filter_dspsn_prkplce_at,
                                         filter_dspsn_toilet_at=filter_dspsn_toilet_at,
                                         filter_wchair_hold_at=filter_wchair_hold_at,
                                         filter_guid_dog_acp_posbl_at=filter_guid_dog_acp_posbl_at,
                                         filter_brll_guid_at=filter_brll_guid_at,
                                         filter_klang_vic_guid_at=filter_klang_vic_guid_at)

            st.session_state['place_list'] = place_list
            for idx, place_name in enumerate(place_list):
                if (df['place'] == place_name).any():
                    photo = df.loc[df['place'] == place_name, 'photo'].values[0]
                else:
                    photo = "data_2/11.jpg"
                if (df['place'] == place_name).any():
                    address = df.loc[df['place'] == place_name, 'address'].values[0]
                else:
                    address = "제주도 어딘가"
                if (df['place'] == place_name).any():
                    description = df.loc[df['place'] == place_name, 'description'].values[0]
                else:
                    description = f"{place_name}에 대한 설명 이러쿵 저러쿵"
                if (df['place'] == place_name).any():
                    link = df.loc[df['place'] == place_name, 'link'].values[0]
                else:
                    link = 'http://..'

                # photo = df.loc[df['place'] == place_name, 'photo'].values[0]
                # address = df.loc[df['place'] == place_name, 'address'].values[0]
                # description = df.loc[df['place'] == place_name, 'description'].values[0]
                # link = df.loc[df['place'] == place_name, 'link'].values[0]
                if idx==0:
                    with st.container():
                        col1, col2 = st.columns([1,1.2])
                        with col1:
                            # st.image(photo, use_column_width=True, caption=place_name)
                            st.image(photo, use_container_width=True, caption=place_name)
                        with col2:
                            st.markdown(f"#### Top{idx + 1}.")
                            st.markdown(f"##### {place_name}")
                            st.write(f"*({address})*")
                            st.write(description)
                            st.markdown(
                                f"""
                                <style>
                                .link-button {{
                                    display: inline-block;
                                    background-color: #1a1d53;
                                    color: #ffffff !important;
                                    padding: 10px 12px;
                                    text-align: center;
                                    text-decoration: none;
                                    border-radius: 6px;
                                    font-size: 12px;
                                }}
                                .link-button:hover {{
                                    background-color: #5fd6f3;
                                }}
                                </style>
                                <a class="link-button" href="{link}" target="_blank">Link</a>
                                """, unsafe_allow_html=True)

                    st.write('-'*20)
                    st.subheader("여긴 어떠세요?")

                elif idx<=3:
                    with st.container():
                        col1, col2=st.columns([1,2])
                        with col1:
                            # st.image(photo, use_column_width=True, caption=place_name)
                            st.image(photo, use_container_width=True, caption=place_name)
                        with col2:
                            st.markdown(f"#### Top{idx + 1}.")
                            st.markdown(f"##### {place_name}")
                            st.write(f"*({address})*")
                            st.write(description)
                            st.markdown(
                                f"""
                                <style>
                                .link-button {{
                                    display: inline-block;
                                    background-color: #1a1d53;
                                    color: #ffffff !important;
                                    padding: 7px 10px;
                                    text-align: center;
                                    text-decoration: none;
                                    border-radius: 6px;
                                    font-size: 12px;
                                }}
                                .link-button:hover {{
                                    background-color: #5fd6f3;
                                }}
                                </style>
                                <a class="link-button" href="{link}" target="_blank">Link</a>
                                """, unsafe_allow_html=True)
            st.write('-' * 20)

    # if st.button("더 많은 추천 장소 보러 가기➡️"):
    #     go_to_page(3)
    col1, col2, col3 = st.columns([2, 2.5, 2])  # 좌측, 중앙, 우측 열로 나누기

    with col3:
        if st.button("더 많은 추천 장소➡️"):
            go_to_page(3)

elif st.session_state['page'] == 3:
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
    st.title("🍭 이런 곳도 있어요!")
    st.write('-' * 20)

    place_list = st.session_state.get('place_list', [])
    others = place_list[4:10]

    with st.container():
        col1, col2, col3 = st.columns([1, 1, 1])  # 첫 번째 행
        col4, col5, col6 = st.columns([1, 1, 1])  # 두 번째 행

        for idx, place_name in enumerate(others):
            if (df['place'] == place_name).any():
                photo=df.loc[df['place'] == place_name, 'photo'].values[0]
            else:
                photo = "data_2/11.jpg"
            if (df['place']==place_name).any():
                address=df.loc[df['place'] == place_name, 'address'].values[0]
            else:
                address="제주도 어딘가"
            if (df['place']==place_name).any():
                description=df.loc[df['place'] == place_name, 'description'].values[0]
            else:
                description=f"{place_name}에 대한 설명 이러쿵 저러쿵"
            if (df['place']==place_name).any():
                link=df.loc[df['place'] == place_name, 'link'].values[0]
            else:
                link='http://..'
            # photo = df.loc[df['place'] == place_name, 'photo'].values[0]
            # address = df.loc[df['place'] == place_name, 'address'].values[0]
            # description = df.loc[df['place'] == place_name, 'description'].values[0]
            # link = df.loc[df['place'] == place_name, 'link'].values[0]

            # 첫 번째 행: col1, col2, col3에 배치
            if idx < 3:
                with [col1, col2, col3][idx]:  # idx에 맞는 열에 정보 출력
                    st.markdown(f"#### Top{idx + 5}.")
                    st.markdown(f"**{place_name}**")
                    st.write(f"*({address})*")
                    image = Image.open(photo)
                    resized_image = image.resize((230, 230))
                    # st.image(resized_image, use_column_width=True)
                    st.image(resized_image, use_container_width=True)
                    st.write(description)
                    st.markdown(
                        f"""
                        <style>
                        .link-button {{
                            display: inline-block;
                            background-color: #1a1d53;
                            color: #ffffff !important;
                            padding: 7px 10px;
                            text-align: center;
                            text-decoration: none;
                            border-radius: 6px;
                            font-size: 12px;
                        }}
                        .link-button:hover {{
                            background-color: #5fd6f3;
                        }}
                        </style>
                        <a class="link-button" href="{link}" target="_blank">Link</a>
                        """, unsafe_allow_html=True)

            elif idx>=3 and idx<6:
                with [col4, col5, col6][idx-3]:  # idx에 맞는 열에 정보 출력
                    st.markdown(f"#### Top{idx + 5}.")
                    st.markdown(f"**{place_name}**")
                    st.write(f"*({address})*")
                    image = Image.open(photo)
                    resized_image = image.resize((230, 230))
                    # st.image(resized_image, use_column_width=True)
                    st.image(resized_image, use_container_width=True)
                    st.write(description)
                    st.markdown(
                        f"""
                        <style>
                        .link-button {{
                            display: inline-block;
                            background-color: #1a1d53;
                            color: #ffffff !important;
                            padding: 7px 10px;
                            text-align: center;
                            text-decoration: none;
                            border-radius: 6px;
                            font-size: 12px;
                        }}
                        .link-button:hover {{
                            background-color: #5fd6f3;
                        }}
                        </style>
                        <a class="link-button" href="{link}" target="_blank">Link</a>
                        """, unsafe_allow_html=True)



    st.write('-' * 20)

    # 페이지 하단에 양 옆에 버튼 배치
    col1, col2, col3 = st.columns([2, 4, 2])  # 좌측, 중앙, 우측 열로 나누기

    with col1:
        if st.button("⬅️이전으로"):
            go_to_page(2)

    with col3:
        if st.button("할인 정보 보기➡️"):
            go_to_page(4)


elif st.session_state['page'] == 4:
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
    st.header("🍊Jeju for All에서 할인 혜택 받으세요~🍊 ")
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.markdown('<br>', unsafe_allow_html=True)
        st.image("data/Jeju_for_All_discount.jpg", width=400)
    # 첫 페이지에서 버튼 클릭으로 페이지 이동
    col1, col2, col3 = st.columns([2, 2, 2])  # 좌측, 중앙, 우측 열로 나누기

    with col3:
        if st.button("처음 화면으로"):
            go_to_page(2)


