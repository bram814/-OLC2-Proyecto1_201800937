from flask_codemirror.fields import CodeMirrorField
from flask import Flask, render_template
from flask_codemirror import CodeMirror
from wtforms.fields import SubmitField
from flask_wtf import FlaskForm
import Gramatica as ast

SECRET_KEY = 'secret!'
CODEMIRROR_THEME = 'material-darker'
CODEMIRROR_ADDONS = (('display','autorefresh'),)
CODEMIRROR_LANGUAGES = ['julia']

app = Flask(__name__)
app.config.from_object(__name__)
codemirror = CodeMirror(app)

class CODEMIRROR_MY_FORM(FlaskForm):
    source_code = CodeMirrorField(
        language = 'julia', 
        config = {
            'lineNumbers'    : 'true', 
            'identWhithTabs' : 'true',
            'electricChars'  : 'true',
            'autocorrect'    : 'true',
            })
    submit = SubmitField('Submit')
    
@app.route('/', methods = ['GET', 'POST'])
def index():
    source_form = CODEMIRROR_MY_FORM()
    out = ""
    text = source_form.source_code.data

    if text != None:
        out = ast.execute_grammar(text)
    else:
        out = ""
        
    return render_template('index.html',source_form=source_form, out=out)

@app.route('/Home')
def Home():
    return render_template('Home.html')

@app.route('/Reporte')
def Reporte():
    return render_template('Reporte.html')

if __name__ == "__main__":
    app.run(debug=True)