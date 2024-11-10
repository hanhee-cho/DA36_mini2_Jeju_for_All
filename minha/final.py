#%%
import pandas as pd
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

main_df=pd.read_csv('./data/main_data.csv')
real_df=pd.read_csv('./data/real_data.csv')
ct_sim = pd.read_csv('./data/ct_sim.csv', index_col=0)

real_df['FCLTY_NM'] = real_df['FCLTY_NM'].astype(str)

X = real_df[['GENDER', 'AGE_GRP', 'TRAVEL_STYL_5',
       'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
       'TRAVEL_COMPANIONS_NUM','FCLTY_NM']]
y = real_df['DGSTFN']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.2, random_state=0)

cat_features = ['GENDER', 'AGE_GRP', 'TRAVEL_STYL_5','TRAVEL_STYL_6',
                'TRAVEL_STYL_7', 'TRAVEL_STYL_8', 'FCLTY_NM']

# 범주형 데이터 처리를 위한 Pool객체 생성
X_train_pool = Pool(X_train, y_train, cat_features = cat_features)
X_test_pool = Pool(X_test, y_test, cat_features = cat_features)

cb_reg = CatBoostRegressor(
    n_estimators = 5000,
    depth = 5,
    learning_rate = .03,
    loss_function = 'RMSE',
    eval_metric = 'RMSE',
    l2_leaf_reg = 10,
    early_stopping_rounds = 200,
    random_state = 0,
    # random_seed=0
)
cb_reg.fit(X_train_pool, eval_set = X_test_pool, verbose = 100)

real_df['FCLTY_NM'] = real_df['FCLTY_NM'].apply(lambda x: unicodedata.normalize('NFKC', str(x)).strip())
places = list(real_df['FCLTY_NM'].unique())

dgstfn_pred_df = pd.DataFrame(index=X_train.index, columns=places)
predicted_dgstfn = cb_reg.predict(X_train_pool)

for place in places:
    dgstfn_pred_df[place] = predicted_dgstfn

def recommend_user_info(gender, age_group, comp_num, styl5, styl6, styl7, styl8):

    user_features = pd.DataFrame({
        'GENDER': [gender],
        'AGE_GRP': [age_group],
        'TRAVEL_STYL_5': [styl5],
        'TRAVEL_STYL_6': [styl6],
        'TRAVEL_STYL_7': [styl7],
        'TRAVEL_STYL_8': [styl8],
        'TRAVEL_COMPANIONS_NUM': [comp_num]
    })

    pred_stfn = {}

    for place in places:
        user_features_place = user_features.copy()  
        user_features_place['FCLTY_NM'] = place 

        user_pool_place = Pool(user_features_place, cat_features=cat_features + ['FCLTY_NM'])
        
        stfn = cb_reg.predict(user_pool_place)[0]
        stfn=round(stfn,3)
        pred_stfn[place] = stfn

    sorted_recommendations = sorted(pred_stfn.items(), key=lambda x: x[1], reverse=True)
    result_df = pd.DataFrame(sorted_recommendations, columns=['FCLTY_NM', 'rate_pred'])
    
    return result_df

def recommend_category(selected_category, ct_sim, main_df):
    # 선택된 카테고리의 유사도 순으로 정렬
    sim_scores = ct_sim[selected_category].sort_values(ascending=False)
    recommended_places = []  # 추천할 장소 리스트
    category_similarity = {}  # 추천 장소와 유사도 저장할 딕셔너리

    # 유사도가 높은 카테고리부터 장소 추천
    for category in sim_scores.index:  
        facilities = main_df[main_df['CTGRY_TWO_NM'] == category]['FCLTY_NM']

        for fclty in facilities:
            if fclty not in recommended_places:  # 중복된 장소 제외
                recommended_places.append(fclty)
                # 선택된 카테고리와 유사 카테고리의 유사도 저장
                similarity = ct_sim[selected_category][category]
                similarity=round(similarity,3)
                if similarity==1.000:
                    similarity=0.700
                category_similarity[fclty] = similarity
                
    # 추천 장소와 유사도를 데이터프레임으로 변환
    recommendations_df = pd.DataFrame(list(category_similarity.items()), columns=['FCLTY_NM', 'similarity'])
    return recommendations_df
#%%
def combine_recommend(gender, age_group, comp_num, styl5, styl6, styl7, styl8, selected_category, ct_sim, main_df):
    user_info = recommend_user_info(gender, age_group, comp_num, styl5, styl6, styl7, styl8)
    category = recommend_category(selected_category, ct_sim, main_df)
    # 유사도에 맞추어 평점 정규화 (1~5) -> (0~1)
    user_info['rate_pred_normalized'] = (user_info['rate_pred'] - 1) / (5 - 1)

    combined_df = pd.merge(user_info, category, on='FCLTY_NM', how='inner')
    combined_df['final_score'] = combined_df['rate_pred_normalized'] * 0.8 + combined_df['similarity'] * 0.2
    combined_df = combined_df.sort_values(by='final_score', ascending=False).reset_index(drop=True)

    return combined_df

def final_recommend(gender, age_group, comp_num, styl5, styl6, styl7, styl8, selected_category, ct_sim, main_df,
                            filter_dspsn_prkplce_at=False, filter_dspsn_toilet_at=False, filter_wchair_hold_at=False,
                            filter_guid_dog_acp_posbl_at=False, filter_brll_guid_at=False, filter_klang_vic_guid_at=False):
    
    barrier_free= [
        'DSPSN_PRKPLCE_AT',      # 장애인 주차장 여부
        'DSPSN_TOILET_AT',       # 장애인 화장실 여부
        'WCHAIR_HOLD_AT',        # 휠체어 보유 여부
        'GUID_DOG_ACP_POSBL_AT', # 안내견 출입 가능 여부
        'BRLL_GUID_AT',          # 점자 안내 여부
        'KLANG_VIC_GUID_AT'      # 한국어 음성 안내 여부
    ]

    recommendations = combine_recommend(gender, age_group, comp_num, styl5, styl6, styl7, styl8, selected_category, ct_sim, main_df)
    # final_recommendations와 main_df를 병합하여 배리어 프리 정보 추가
    combined_df = pd.merge(recommendations, main_df[['FCLTY_NM'] + barrier_free], on='FCLTY_NM', how='left')

    # 조건에 맞춰 필터링 적용 (True인 것만 필터링)
    if filter_brll_guid_at:
        idx = combined_df[combined_df['BRLL_GUID_AT'] == 0].index
        combined_df = combined_df.drop(idx)
        combined_df.reset_index(drop=True, inplace=True)

    if filter_guid_dog_acp_posbl_at:
        idx = combined_df[combined_df['GUID_DOG_ACP_POSBL_AT'] == 0].index
        combined_df = combined_df.drop(idx)
        combined_df.reset_index(drop=True, inplace=True)

    if filter_dspsn_toilet_at:
        idx = combined_df[combined_df['DSPSN_TOILET_AT'] == 0].index
        combined_df = combined_df.drop(idx)
        combined_df.reset_index(drop=True, inplace=True)

    if filter_wchair_hold_at:
        idx = combined_df[combined_df['WCHAIR_HOLD_AT'] == 0].index
        combined_df = combined_df.drop(idx)
        combined_df.reset_index(drop=True, inplace=True)

    if filter_dspsn_prkplce_at:
        idx = combined_df[combined_df['DSPSN_PRKPLCE_AT'] == 0].index
        combined_df = combined_df.drop(idx)
        combined_df.reset_index(drop=True, inplace=True)

    if filter_klang_vic_guid_at:
        idx = combined_df[combined_df['KLANG_VIC_GUID_AT'] == 0].index
        combined_df = combined_df.drop(idx)
        combined_df.reset_index(drop=True, inplace=True)

    # 중복된 장소 이름을 제거하고, 상위 10개 추천 장소 선택
    filtered_recommendations = combined_df.drop_duplicates(subset='FCLTY_NM')['FCLTY_NM'].head(10).reset_index(drop=True)
    place_list=filtered_recommendations.tolist()
    return place_list

# data_1=final_recommend(0, 20, 3, 7, 4, 5, 6, '관광지', ct_sim, main_df,
#                             filter_dspsn_prkplce_at=True, filter_dspsn_toilet_at=True, filter_wchair_hold_at=False,
#                             filter_guid_dog_acp_posbl_at=False, filter_brll_guid_at=False, filter_klang_vic_guid_at=False)
#
# data_2=final_recommend(0, 50, 1, 3, 2, 6, 2, '전시/기념관', ct_sim, main_df,
#                             filter_dspsn_prkplce_at=False, filter_dspsn_toilet_at=False, filter_wchair_hold_at=False,
#                             filter_guid_dog_acp_posbl_at=True, filter_brll_guid_at=True, filter_klang_vic_guid_at=False)
#
# print(data_1, data_2)

