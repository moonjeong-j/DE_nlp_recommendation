from flask import Flask, render_template, request
import db
import model

#db
# db.dbcon()
# db.create_table()
# db.dbcon()
# db.create_table_target()
# db.dbcon()
# db.create_table_df()

#data load
df=model.data_load()


#flask

app = Flask(__name__)

@app.route('/')
def user_input():
   return render_template('user_input.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   
   if request.method == 'POST':
      #input 받아오기
      price = int(request.form["num"])
      keyword = request.form["name"]
      # result =request.form
      
      #db에 반영
      db.dbcon2()
      db.insert_data_user(keyword, price)
      
      # model : predict
      place = model.find_simi_place(df, keyword, price, 1)
      place = place[['name', 'address', 'price']].values.tolist()[0]
      place_name =place[0]
      place_address =place[1]
      place_price = place[2]

      #db에 반영
      db.dbcon2()
      db.insert_data_output(place_name,place_address,place_price)

      # return render_template("result.html",result = y_pred_int)
      return render_template("result.html", place_name=place_name, place_address=place_address, place_price=place_price)

# @app.route('/getinfo')
# def getinfo():
#     result = db.select_all_target()
#     return render_template("result.html", result=result)


if __name__ == '__main__':
   app.run('0.0.0.0', port=4000, debug=False)

# db.select_all()