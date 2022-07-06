from flask import Flask, jsonify, request
from flask_restful import reqparse
import requests 

app = Flask(__name__)

@app.route("/hello")
def hello():
    x= "First page"
    return x

@app.route('/bfhl',methods=['GET','POST'])
def splitArr():
    #nums=request.args["numbers"]
    # nums=request.args
    # print(nums)
    # nums.to_dict()
    # print(type(nums))
    # nums=dict(nums)
    # print("2.",type(nums))
    # return jsonify(nums)

    # nums= list(request.args["numbers"])

    x=reqparse.RequestParser()
    x.add_argument("numbers",type=list)
    y=x.parse_args()
    nums=y["numbers"]
    print("***",nums)
    is_success=True
    user_id="San_Pati_28201"
    a,b=[],[]
    for i in nums:
        if i.isdigit():
            if(int(i)%2 == 0):
                a.append(i)
            else:
                b.append(i)
        else:
            is_success=False
            break
    
    if is_success:
        dic={
            "is_success":is_success,
            "user_id":user_id,
            "odd":b,
            "even":a
        }
    else:
        dic={
            "is_success":is_success,
            "user_id":user_id
        }
    return dic


app.run(debug=True)