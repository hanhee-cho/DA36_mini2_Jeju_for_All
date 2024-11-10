import streamlit as st
from pages import intro_page, user_recommendations_page, more_recommendations_page, discount_page
from utils.style import set_background
from model import *

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
    more_recommendations_page.display_recommendations()

elif st.session_state.page == "discount":
    discount_page.show_discount_coupon()


