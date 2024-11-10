import streamlit as st
import os
from PIL import Image

def display_recommendations(places, images):
    st.title("Top5 - Top10")
    st.write('-'*20)

    # 페이지 변경 함수
    def go_to_page(page_num):
        st.session_state['page'] = page_num

    # 장소와 이미지를 3열로 나누어 표시
    # 이미지 사이즈 설정 (예: 300x200)
    img_width, img_height = 300, 250
    resized_images = [Image.open(image_path).resize((img_width, img_height)) for image_path in images[4:10]]

    # 첫 번째 container (위쪽 3개 이미지)
    with st.container():
        cols = st.columns(3)
        for idx, (place, description) in enumerate(places[4:7]):  # 상위 3개 장소
            with cols[idx]:
                st.write(f'Top{idx + 5}')
                st.write(f'{place}')
                st.image(resized_images[idx], use_column_width=True)
                st.write(description)

    # 두 번째 container (아래쪽 3개 이미지)
    with st.container():
        cols = st.columns(3)
        for idx, (place, description) in enumerate(places[7:10]):  # 하위 3개 장소
            with cols[idx]:
                st.write(f'Top{idx + 8}')
                st.write(f'{place}')
                st.image(resized_images[idx + 3], use_column_width=True)
                st.write(description)

    # with st.container():
    #     cols = st.columns(3)
    #     for idx, (place, description) in enumerate(places[4:10]):
    #         with cols[idx % 3]:  # 열 순환
    #             st.image(images[4:10][idx], caption=place, use_column_width=True)
    #             st.write(description)

    # with st.container():
    #     col1, col2, col3 = st.columns([1, 1, 1])
    #     col4, col5, col6 = st.columns([1, 1, 1])
    #     with col1:
    #         st.image("data/그리스신화박물관.jpg", caption="그리스신화박물관", use_column_width=True)
    #         st.write("제주시 한림읍 금악리 제주-중문간 평화로 중간 교통요충지에 어쩌구")
    #     with col2:
    #         st.image("data/그리스신화박물관.jpg", caption="그리스신화박물관", use_column_width=True)
    #         st.write("제주시 한림읍 금악리 제주-중문간 평화로 중간 교통요충지에 어쩌구")
    #     with col3:
    #         st.image("data/그리스신화박물관.jpg", caption="그리스신화박물관", use_column_width=True)
    #         st.write("제주시 한림읍 금악리 제주-중문간 평화로 중간 교통요충지에 어쩌구")
    #     with col4:
    #         st.image("data/그리스신화박물관.jpg", caption="그리스신화박물관", use_column_width=True)
    #         st.write("제주시 한림읍 금악리 제주-중문간 평화로 중간 교통요충지에 어쩌구")
    #     with col5:
    #         st.image("data/그리스신화박물관.jpg", caption="그리스신화박물관", use_column_width=True)
    #         st.write("제주시 한림읍 금악리 제주-중문간 평화로 중간 교통요충지에 어쩌구")
    #     with col6:
    #         st.image("data/그리스신화박물관.jpg", caption="그리스신화박물관", use_column_width=True)
    #         st.write("제주시 한림읍 금악리 제주-중문간 평화로 중간 교통요충지에 어쩌구")

    st.write('-' * 20)

    # 페이지 하단에 양 옆에 버튼 배치
    col1, col2, col3 = st.columns([2, 4, 2])  # 좌측, 중앙, 우측 열로 나누기

    with col1:
        if st.button("⬅️이전으로"):
            go_to_page("user_recommendations")

    with col3:
        if st.button("할인 정보 보기➡️"):
            go_to_page("discount")



