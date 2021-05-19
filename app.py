from flask import Flask, jsonify, request

app = Flask(__name__)
List = [
  {
    'id' :1,
    'Contact':u'912349567',
    'Name':u'Monique',
    'done':False
  },
  {
    'id' :2,
    'Contact':u'4567897104',
    'Name':u'Kip',
    'done':False
  }
]
#@app.route("/")

  
@app.route("/add-data", methods=["POST"])

def add_task():
 if not request.json:
    return jsonify({
    "status":"error",
    "message": "Please provide the data!"
    },400)

 contact = {
    'id': tasks[-1]['id'] + 1,
    'Name': request.json['Name'],
    'Contact': request.json.get('Contact', ""),
    'done': False
 }

 List.append(contact)
 return jsonify({
   "status":"success",
   "messsage":"Contact added successfully!"
 })

 @app.route("/get-data")
 def get_task():
   return jsonify({
     "data":List
   })

if __name__ == "__main__":
  app.run(debug=True)