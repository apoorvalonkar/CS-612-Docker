from flask import Flask, redirect, url_for, request, Response
from flask_cors import CORS
from dataFunction import *

app = Flask(__name__)
#cors = CORS(app, resources={"/": {"origins": "*"}})

@app.route('/cars',methods = ['GET','POST'])
def get_cars():
   if request.method=='POST':
      print (request.data.decode("UTF-8"))
      insertCars(request.data.decode("UTF-8"))
      return 'inserted'
   else:
      return Response(fetchAll(),mimetype='application/json')

@app.route('/cars/<int:postID>',methods = ['GET'])
def get_car(postID):
   return Response(fetchData(postID),mimetype='application/json')

if __name__ == '__main__':
   app.run(host= '0.0.0.0',port=4200)
