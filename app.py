from flask import Flask, render_template, redirect, url_for, session, request
from plagiarism_detection import cosine_similarity
from coba import plagiarism_checker

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    # fungsi ketika pengguna mengirimkan masukkan berupa dokumen
    if request.method == 'POST':
        # pengambilan data dokumen masukkan dari form
        document_1 = request.form.get('document_1', None)
        document_2 = request.form.get('document_2', None)
        
        if document_1 and document_2:
            try:
                # pengoperan data dokumen masukkan ke fungsi cosine_similarity
                result = plagiarism_checker(document_1, document_2)
            
            except:
                # if documents only contain stopword/s
                warning = "Document 1 or Document 2 can't only contain stopword"
                return render_template('home.html', warning=warning, result=None), 200 
            
            # perenderan halaman home beserta hasil dari fungsi cosine_similarity
            return render_template('home.html',document_1=document_1,document_2=document_2, result=result), 200
        
        else:
            warning = "Document 1 and Document 2 can't be NULL"
            return render_template('home.html', warning=warning, result=None), 200 
        # return render_template('home.html', result=result), 200
    
    # fungsi jika pengguna mengakses halaman home
    elif request.method == 'GET':
        # perenderan halaman home
        return render_template('home.html',document_1=None, document_2=None, result=None, warning=""), 200
    
    return 404

@app.route('/about')
def about():
    if request.method == 'GET':
        return render_template('about.html'),200
    
# @app.route('/contact')
# def contact():

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)