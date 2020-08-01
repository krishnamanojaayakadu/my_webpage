from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>')
def project(page_name):
    return render_template(page_name)

def write_to_csv(data):
	with open('C:/Users/King/Desktop/myweb/database.csv',mode='a', newline='') as database:
		email=data['email']
		subject=data['subject']
		message=data['message']
		file=csv.writer(database, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
		file.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
            data= request.form.to_dict()
            write_to_csv(data)
            return redirect('sentmessage.html') 
    else:
    	return'something is wrong'



