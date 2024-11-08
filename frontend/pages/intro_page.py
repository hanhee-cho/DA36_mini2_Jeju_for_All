import streamlit as st

def display():
    # if 'page' not in st.session_state:
    #     st.session_state['page'] = 1

    # 페이지 변경 함수
    def go_to_page(page_num):
        st.session_state['page'] = page_num


    # 로컬 GIF 파일을 base64로 인코딩하여 HTML에 삽입하기
    # import base64
    # def get_base64_of_bin_file(bin_file):
    #     with open(bin_file, 'rb') as f:
    #         data = f.read()
    #     return base64.b64encode(data).decode()
    #
    # # 로컬 GIF 파일 경로 설정
    # img_path = './frontend/data/jeju.GIF'  # 사용자의 GIF 파일 경로로 변경
    # # base64 인코딩한 이미지 삽입
    # base64_img = get_base64_of_bin_file(img_path)
    # # CSS를 사용하여 배경 이미지 스타일 적용
    # st.markdown(
    #     f"""
    #         <style>
    #         .full-bg {{
    #             background-image: url("data:image/gif;base64,{base64_img}");
    #             background-size: cover;
    #             background-position: center;
    #             background-repeat: no-repeat;
    #             position: fixed;
    #             width: 80%;
    #             height: 100%;
    #             top: 0;
    #             left: 0;
    #             z-index: -1;
    #         }}
    #         </style>
    #         """,
    #     unsafe_allow_html=True
    # )
    # full-bg라는 클래스가 있는 div 추가
    st.markdown('<div class="full-bg"></div>', unsafe_allow_html=True)

    # 콘텐츠 추가 (선택 사항)
    st.title("🍊제주, 어디까지 가봤니?🍊")
    st.markdown("<br>", unsafe_allow_html=True)
    # st.write("제주의 아름다움을 누구나 경험할 수 있도록! \n장애 유무와 관계없이 안전하고 편리하게 여행할 수 있는 배리어프리 명소와 여행 팁을 소개합니다. \n편안한 제주 여행을 위한 모든 정보를 한눈에 만나보세요.")
    st.markdown("""
            ### **Jeju for All 제주의 아름다움을 누구나 경험할 수 있도록!**  
            장애 유무와 관계없이 안전하고 편리하게 여행할 수 있는 배리어프리 명소와 여행 팁을 소개합니다.  
            편안한 제주 여행을 위한 모든 정보를 한눈에 만나보세요.
            """)
    # if st.button("나만을 위한 여행지 추천 받기 ❤️"):
    #     # go_to_page(2)
    #     st.session_state.page = "recommendations"

    # 첫 페이지에서 버튼 클릭으로 페이지 이동
    col1, col2, col3 = st.columns([2, 1, 2])  # 좌측, 중앙, 우측 열로 나누기

    with col3:
        if st.button("나만을 위한 여행지 추천 받기 ❤️"):
            go_to_page("user_recommendations") #on_click=go_to_page, args=("recommendations",))