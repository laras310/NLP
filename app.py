from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        document_1 = request.form.get('document_1', None)
        document_2 = request.form.get('document_2', None)
        
        # if document_1 is not None
        if document_1:
            # if document_2 is None then processing document_1 without document_2
            if not document_2:
                # passing document_1 to the nlp function
                result = None
                return render_template('home.html', result=result), 200
            
            # passing document_1 and document_2 to the nlp function
            result = None
            return render_template('home.html', result=result), 200
        
        return 404
    
    elif request.method == 'GET':
        return render_template('home.html'), 200
    
    return 404

# @app.route('/about')
# def about():
    
# @app.route('/contact')
# def contact():

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)