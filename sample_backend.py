import random
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#@app.route('/users')
#def get_filtered_user():
#   search_username = request.args.get('name') #accessing the value of parameter 'name'
#   search_job = request.args.get('job')
#   if search_username :
#      subdict = {'users_list' : []}
#      for user in users['users_list']:
#         #if user['name'] == search_username:
#            #subdict['users_list'].append(user)
#         if user['job'] == search_job:
#            subdict['users_list'].append(user)
#      return subdict
#   return users

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
   if id :
      for user in users['users_list']:
        if user['id'] == id:
            if request.method == 'GET':
               return user
            elif request.method == 'DELETE':
                users['users_list'].remove(user) #removes user, 204 code
                resp = jsonify({}), 204
                return resp
      resp = jsonify({"error": "User not found"}), 404 #jsonify built in, converts object to json
      return resp
   return users

@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      if search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd['id'] = generate_id()
      users['users_list'].append(userToAdd)
      #resp = jsonify(success=True)
      resp = jsonify(userToAdd), 201
      #resp.status_code = 201
      #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp

def generate_id():
    newId = ""
    for i in range(3):
        newId += chr(random.randint(97,122))
    for i in range(3):
        newId += chr(random.randint(48,57))
    return newId
    #return "abc123"

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'def456', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      },
      {
         "id": "qwe123",
         "job": "Zookeeper",
         "name": "Cindy"
      }
   ]
}

