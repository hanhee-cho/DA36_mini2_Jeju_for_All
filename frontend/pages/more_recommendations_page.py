import streamlit as st

def display_recommendations():
    st.title("Top5 - Top10")
    st.write('-'*20)

    # 페이지 변경 함수
    def go_to_page(page_num):
        st.session_state['page'] = page_num

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

    # 페이지 하단에 양 옆에 버튼 배치
    col1, col2, col3 = st.columns([2, 4, 2])  # 좌측, 중앙, 우측 열로 나누기

    with col1:
        if st.button("⬅️이전으로"):
            go_to_page("user_recommendations")

    with col3:
        if st.button("할인 정보 보기➡️"):
            go_to_page("discount")
