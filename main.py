from flask import Flask, render_template, request, redirect
from db import *
from algo import magic
from hashlib import sha512

app = Flask(__name__)


table = []
gkey = ''
validate=''

def make_a_table(key):
    global table
    table = []
    data = get_all_data()
    for row in data:
        n_row = []
        for el in row[:len(row)-1]:
            n_row.append(el)
        n_row[0] = str(n_row[0])
        # print(n_row[0]+'')
        n_row.append(magic(n_row[0]+' '+key, n_row[1]+n_row[2]+n_row[3]))
        table.append(n_row+[''])



@app.route("/data", methods=['post', 'get'])
def index():
    global table
    global validate

    if gkey != '':
        make_a_table(gkey)
    
    if request.method == 'POST':

        op = list(request.form.keys())[-1]

        match op:
            case "inpmaspas":
                print("pushed")
                return redirect("http://127.0.0.1:5000/")
            
            case "add":
                res = request.form.get("res")
                mail = request.form.get("mail")
                log = request.form.get("login")

                if any(len(s) == 0 for s in (res, mail, log)):
                    validate="<h6 class='dangershow'>Вы заполнили не все поля</h6>"
                    return redirect("http://127.0.0.1:5000/data")
                else:
                    validate=""


                add_to_base(get_last_id_p1(), (res, mail, log, ''))
                return redirect("http://127.0.0.1:5000/data")

            case "del":
                id = request.form.get("id")
                delete_from_base(int(id))
                return redirect("http://127.0.0.1:5000/data")
            
            case "delid":
                id = request.form.get("delid")
                delete_from_base(id)
                make_a_table(gkey)

                return redirect("http://127.0.0.1:5000/data")
    else:
        return render_template('index.html', title='О Flask', rows=table, validate=validate)


@app.route("/", methods=['post', 'get'])
def inputkey():
    global gkey
    if request.method == 'POST':
        maspas = request.form.get('maspas')
        k = sha512(''.join(maspas).encode('utf-8')).hexdigest()

        del maspas
        gkey = k
        make_a_table(gkey)

        return redirect("http://127.0.0.1:5000/data")
        
    return render_template('inputform.html')

@app.route("/add", methods=['post'])
def addrec():
    pass



if __name__ == "__main__":
    app.run(debug=True)
