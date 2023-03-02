def dbcon():
    import psycopg2
    global conn
    conn = psycopg2.connect(
                            host="ziggy.db.elephantsql.com",
                            database="zjnlucdp",
                            user="zjnlucdp",
                            password="Ya0npQ0oIfCJkni0ucOOKIJJb0ZG0rEO")

#postgres://zjnlucdp:Ya0npQ0oIfCJkni0ucOOKIJJb0ZG0rEO@ziggy.db.elephantsql.com/zjnlucdp

def dbcon2():
    import psycopg2
    global conn
    conn = psycopg2.connect(
                        host="peanut.db.elephantsql.com",
                        database="jchnbigi",
                        user="jchnbigi",
                        password="BlQnHLCe3PnZpWFcrylTXpZjakNEHGVH")


def create_table_users():
    try:
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS users")
        c.execute("CREATE TABLE users (keyword varchar(50), price integer )")
        conn.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        conn.close()

def insert_data_user(num, name):
    try:
        import csv

        c = conn.cursor()
        setdata = (num, name)
        c.execute("INSERT INTO users VALUES (%s, %s)", setdata)
        conn.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        conn.close()

####################################

def create_table_output():
    try:
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS output")
        c.execute("CREATE TABLE output (name varchar(50), address varchar(50), price int)")
        conn.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        conn.close()

def insert_data_output(place_name,place_address,place_price):
    try:
        c = conn.cursor()
        setdata = (place_name,place_address, place_price)
        c.execute("INSERT INTO output VALUES (%s, %s, %s)", setdata)
        conn.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        conn.close()

#############################################################################
# def create_table_df_res_caf():
#     try:
#         c = conn.cursor()
#         c.execute("DROP TABLE IF EXISTS df_res_caf")
#         c.execute("""CREATE TABLE df_res_caf (name varchar(50),
#                                               address varchar(50),
#                                               category varchar(50),
#                                               price integer,
#                                               rvw_cnt integer,
#                                               rating float,
#                                               lat float,
#                                               lng float,
#                                               p_id integer,
#                                               reviews varchar(32768),
#                                               tags varchar(8192)
#                                               )""")
#         conn.commit()
#     except Exception as e:
#         print('db error:', e)
#     finally:
#         conn.close()

# def insert_data_df_res_caf(num):
#     try:
#         import csv
#         sql = """INSERT INTO df_res_caf (name, address, category, price, rvw_cnt, rating, lat, lng, p_id, reviews, tags) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
#         f = 

#         c = conn.cursor()
#         setdata = (num,)
#         c.execute("INSERT INTO target VALUES (%s)", setdata)
#         conn.commit()
#     except Exception as e:
#         print('db error:', e)
#     finally:
#         conn.close()

# #테이블 전체 비우기
# cur.execute('TRUNCATE passenger')
# conn.commit()

# # insert 쿼리문
# sql = """INSERT INTO passenger (Survived, Pclass, Name, Sex, Age, "Siblings/Spouses Aboard", "Parents/Children Aboard", Fare) values(%s,%s,%s,%s,%s,%s,%s,%s)"""

# #파일 읽기
# import csv
# f = open('titanic.csv',"r")
# csvReader = csv.reader(f)

# next(csvReader, None) #첫번째 행 제외

# for row in rd:
#     cur.execute(sql, (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

# connection.commit()
# connection.close()
# f.close()

