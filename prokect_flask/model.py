
def data_load():
    import pandas as pd
    import psycopg2
    conn = psycopg2.connect(
                            host="ziggy.db.elephantsql.com",
                            database="zjnlucdp",
                            user="zjnlucdp",
                            password="Ya0npQ0oIfCJkni0ucOOKIJJb0ZG0rEO")
    c = conn.cursor()
    c.execute("SELECT * from df_res_caf")
    result = c.fetchall()
    conn.close()
    df_result =pd.DataFrame(result, columns=['name', 'address', 'category', 'price', 'rvw_cnt', 'reviews'])
    return df_result




def find_simi_place(df, place_name, price, top_n=1):
    # from sklearn.feature_extraction.text import CountVectorizer  # 피체 벡터화
    from sklearn.metrics.pairwise import cosine_similarity  # 코사인 유사도
    # from numpy import vectorize
    from sklearn.feature_extraction.text import TfidfVectorizer
    import pandas as pd
    import numpy as np

    ##
    # vectorizer = TfidfVectorizer(ngram_range=(1,3),
    # min_df=2,
    # max_features=10000,
    # sublinear_tf=True,
    # lowercase=False,
    # use_idf=True)

    # x_data_vec = vectorizer.fit_transform(df['reviews'])

    # from sklearn.metrics.pairwise import cosine_similarity
    # cosine = cosine_similarity(x_data_vec, x_data_vec)
    # consine_sorted = cosine.argsort()[:,::-1]

    # score = (
    #     +cosine*1
        
    # )
    
    ##score_sorted import
    score_sorted = np.load('./similarity_array.npy')

    ## price 필터링
    try:
        df=df[df['price']<= price]
    except Exception as e:
        print('db error:', e)
    

    ## place_name=keyword 유사도 필터링
    compare = 0
    index = 0
    
    contains_name = df[df['name'].str.contains(place_name)]
    contains_name = contains_name.iloc[0:1]
    
    if contains_name.empty:
        print('DataFrame is empty!\nSearch blog review..')
        contains_name = df[df['reviews'].str.contains(place_name)]
        
        for i in range(len(contains_name['reviews'])):
            if contains_name['reviews'].iloc[i].count(place_name) > compare:
                compare = contains_name['reviews'].iloc[i].count(place_name)
                index = i
        contains_name = contains_name.iloc[index:index+1]
        
        if contains_name.empty:
            print('No Data')
            
    place_index = contains_name.index.values
    similar_indexes = score_sorted[place_index, :(top_n)]
    similar_indexes = similar_indexes.reshape(-1)
    
    return df.iloc[similar_indexes]

