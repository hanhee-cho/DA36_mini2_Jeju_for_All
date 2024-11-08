import streamlit as st

def show_discount_coupon():
    st.header("🍊Jeju for All에서 할인 혜택 받으세요~🍊 ")
    # st.write("할인 정보를 제공합니다.")
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.image("data/Jeju_for_All_discount.jpg", width=400)

    # 페이지 변경 함수
    def go_to_page(page_num):
        st.session_state['page'] = page_num

    # 첫 페이지에서 버튼 클릭으로 페이지 이동
    col1, col2, col3 = st.columns([2, 2, 2])  # 좌측, 중앙, 우측 열로 나누기

    with col3:
        if st.button("처음 화면으로"):
            go_to_page("user_recommendations")