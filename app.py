from flask import Flask, render_template, redirect, url_for, session, request
from plagiarism_detection import cosine_similarity

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
        
        # pengoperan data dokumen masukkan ke fungsi cosine_similarity
        result = cosine_similarity(document_1, document_2)
        
        # perenderan halaman home beserta hasil dari fungsi cosine_similarity
        return render_template('home.html',document_1=document_1,document_2=document_2, result=result), 200
        # return render_template('home.html', result=result), 200
    
    # fungsi jika pengguna mengakses halaman home
    elif request.method == 'GET':
        # perenderan halaman home
        return render_template('home.html',document_1=None, document_2=None, result=None), 200
    
    return 404

# @app.route('/about')
# def about():
    
# @app.route('/contact')
# def contact():

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)