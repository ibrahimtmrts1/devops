from flask import Flask, render_template,request
app=Flask(__name__)
 
@app.route('/')
def entry_page()->'html':
    return render_template('einstein.html',page_title='Wellcome to Little Einstein Project')
 
 
@app.route('/sum',methods=['POST'])
def sum()->'html':
    x=int(request.form['firstValue'])
    y=int(request.form['secondValue'])
    return render_template('result.html',page_title='Calculation result',sum_result=(x+y),first_value=x,second_value=y,)
 
app.run(debug=True)