from flask import Flask,render_template,redirect,request,url_for
import json
import collections
from web3 import Web3


ganache_url="http://127.0.0.1:8545"
web3=Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]
  
if((web3.isConnected())):
    print("Connected to the Network")
else:
    print("Connection Failed")

account=web3.toChecksumAddress("0x18E2CA79709063F9211DD75B9c7AAc9A8a27E68C")


# # block=web3.eth.blockNumber
# # print(web3.eth.getBalance(account))



abi=json.loads('[{"inputs":[],"name":"Result","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"address","name":"add","type":"address"}],"name":"add_candidate","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"uint256","name":"addhar","type":"uint256"},{"internalType":"uint32","name":"age","type":"uint32"},{"internalType":"address","name":"add","type":"address"},{"internalType":"string","name":"p","type":"string"}],"name":"add_voter","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"all_results","outputs":[{"components":[{"internalType":"address","name":"id","type":"address"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint256","name":"vote","type":"uint256"}],"internalType":"struct voting.result[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"cand","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"j","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"passw","type":"string"}],"name":"login","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"result_list","outputs":[{"internalType":"address","name":"id","type":"address"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint256","name":"vote","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"st","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"vot","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"voteFor","type":"address"},{"internalType":"address","name":"add","type":"address"}],"name":"vote","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"passw","type":"string"}],"name":"voter_address","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"voter_list","outputs":[{"internalType":"address","name":"id","type":"address"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"password","type":"string"},{"internalType":"uint256","name":"addhar","type":"uint256"},{"internalType":"bool","name":"voted","type":"bool"},{"internalType":"uint32","name":"age","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"winnerdis","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
#0xe43095654E09D430b462D2ACDe9C6c1Ee7e9F80C,0x000CbE1ab1acf4027388705c23ED0CCF0cd348F8,0x9b79D2dB7E69fF553DBeab9E10c6ed7755B98092,0x99fAee9f69ADADAB58031D9551d01FcDDe5C4030]

contract=web3.eth.contract(address=account,abi=abi)




candidates={'CSE':'0x40C262C71A9c44E378Df7027e9e9011725CBeDEe','ECE':'0x98A86a8b3B7f3be75E4760de97EcD401CfeF8AA2','Mechanical':'0xe43095654E09D430b462D2ACDe9C6c1Ee7e9F80C','Civil':'0x000CbE1ab1acf4027388705c23ED0CCF0cd348F8','Chemical':'0x9b79D2dB7E69fF553DBeab9E10c6ed7755B98092','Metllurgical':'0x99fAee9f69ADADAB58031D9551d01FcDDe5C4030'}

for i in candidates:
    tx_hash=contract.functions.add_candidate(i,candidates[i]).transact()
    tx_reciept=web3.eth.waitForTransactionReceipt(tx_hash)
print("Candidates Registresion Done")

@app.route("/",methods=['GET','POST'])



l=[]
r=[]
vtad="0x0000000000000000000000000000000000000000"
log="not log"
tt='GOT'
app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
def hello(l=l,r=r):
    global vtad
    global log
    global tt
    if request.method == 'GET' and tt=="GOT":
        if log=="Logged In":
            return render_template('index.html',name="you are in",done=True)
        else:
            return render_template('index.html',name="BLOCKCHAIN",done=False)
    elif request.method == 'GET' and vtad!="0x0000000000000000000000000000000000000000" and tt!="GOT" :
        if vtad in l:
            return render_template('index.html',name="you already voted Chill man",done=True)
        elif tt=="You Can't vote yourself":
             return render_template("index.html",name="You cant vote yourself",done=True)
        elif tt=="Already voted":
             l=l.append(vtad)
             return render_template("index.html",name="Succesful you voted ",done=True)
        elif tt=="Already voted":
             return render_template("index.html",name="Registered Succesfully ",done=True)
    elif request.method == 'POST':
         l1=[]
         d={}
         address=request.form['address']
         name=request.form['name']
         passw=request.form['passw']
         addhar=request.form['addhar']
         age=request.form['age']
         name=str(name)
         passw=str(passw)
         addhar=int(addhar)
         age=int(age)
         address=str(address)
         # Type=request.form['type']
         # mail=request.form['mail']
         # return redirect(url_for("vote",name=name))
         capvot=contract.functions.add_voter(name,addhar,age,address,passw).transact()
         capvot_reciept=web3.eth.waitForTransactionReceipt(capvot)
         capvot=contract.functions.add_voter(name,addhar,age,address,passw).call()
         if address in r:
             return render_template('index.html',name="Already Registered")  
         elif capvot=="Already Registered":
             r.append(address)
             return render_template('index.html',name="Registered succesfully")
         else:
             return render_template('index.html',name="Not register")


@app.route("/login",methods=["GET","POST"])
def login():
     global log
     global vtad
     if request.method=='GET' and log=="Logged In":
         return redirect(url_for("vote"))

     elif request.method=='GET' and log!="Logged In":
         return render_template('login.html',error="Login Not done yet")

     else:
         username=request.form['username']
         password=request.form['password']
         username=str(username)
         password=str(password)
         log=contract.functions.login(username,password).call()
         vtad=contract.functions.voter_address(username,password).call()
         return redirect(url_for("vote"))
         # if(log=="Logged In"):
         #     return redirect(url_for("vote",name="Login Done"))
         # else:
         #     return render_template('login.html',error="Sorry YOu are a fucker")


        






# @app.route('/',methods=['GET','POST'])
# def register(r=r):





@app.route("/vote",methods=["GET","POST"])
def vote(l=l):
     global log
     global vtad
     global tt
     if request.method=='GET':
        if log=="Logged In":
            return render_template("vote1.html",done=True)
        else:
            return redirect(url_for("login"))
     else:
         vote=request.form['submit']
         tt=contract.functions.vote(candidates[vote],vtad).transact()
         tt_reciept=web3.eth.waitForTransactionReceipt(tt)
         tt=contract.functions.vote(candidates[vote],vtad).call()
         return redirect(url_for("hello"))

       
      


@app.route("/<name>")
def voter(name): 
     return f"<h1>{name}</h1>"


@app.route("/logout")
def logout():
    global log
    global vtad
    global tt
    tt="GOT"
    log='Not log'
    vtad="0x0000000000000000000000000000000000000000"
    return redirect(url_for('hello'))

@app.route("/result",methods=["GET", "POST"])
def result():
    if request.method == 'GET' and vtad!="0x0000000000000000000000000000000000000000" and tt!="GOT":
        winner=contract.functions.Result().transact()
        winner_receipt=web3.eth.waitForTransactionReceipt(winner)
        winner=contract.functions.Result().call()
        Result=contract.functions.all_results().call()
        Result=Result[-6:]
        # Winner=[item for item, count in collections.Counter(winner).items() if count > 1]
        Winner=[i[1] for i in Result if i[2]==winner]

        return render_template("result.html",winner=Winner,cse=Result[0][2],ece=Result[1][2],mech=Result[2][2],civil=Result[3][2],chem=Result[4][2],met=Result[5][2],done=True)
    else:
        return f"<h1>Chill Bro First You then Please Come Again</h1>"



app.run(debug=True)
