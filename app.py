from flask_codemirror.fields import CodeMirrorField
from flask import Flask, render_template
from flask_codemirror import CodeMirror
from wtforms.fields import SubmitField
from flask_wtf import FlaskForm
import Gramatica as ast
import graphviz

SECRET_KEY = 'secret!'
CODEMIRROR_THEME = 'material-darker'
CODEMIRROR_ADDONS = (('display','autorefresh'),)
CODEMIRROR_LANGUAGES = ['julia']

app = Flask(__name__)
app.config.from_object(__name__)
codemirror = CodeMirror(app)

analyzer = ""
data_error = ""
table_simbol = ""
report_ast = ""
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
    global analyzer
    global data_error
    global table_simbol
    if text != None:
        try:
            analyzer = ast.execute_grammar(text)    # interpreta la entrada.
            data_error = analyzer.get_excepcion()   # obtiene toda excepcion y lo manda a la tabla de errores.
            out = analyzer.get_consola()            # obtiene la salida en consola y luego se manda. 
            table_simbol = analyzer.Table
        except Exception as e:
            out = f"WARNING!!! ({e})"
            data_error = None
            table_simbol = None
    else:
        out = ""
    return render_template('index.html', source_form=source_form, out=out, data_error=data_error, table_simbol=table_simbol)

@app.route('/Home')
def Home():
    return render_template('Home.html')

@app.route('/Reporte')
def Reporte():
    global report_ast
    try:    
        init = ast.Node_Ast("ROOT") #
        instr = ast.Node_Ast("INSTRUCCIONES")
        for instruccion in analyzer.get_instruccion():
            instr.crearNodo(instruccion.AST())
        init.crearNodo(instr)
        report_ast = analyzer.GENERATE_AST(init).pipe().decode('utf-8') # SE EJECUTA CON LIBRERIA.
    except Exception as e:
        print(f"WARNING!! - {e}")
    return render_template('Reporte.html', report_ast = report_ast)

if __name__ == "__main__":
    app.run(debug=True)
