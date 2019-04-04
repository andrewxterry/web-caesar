from caesar import rotate_character, encrypt
from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True 


page_header = '''

<!doctype html>
    <html>
        <head>
            <style>
                body{{
                    display: block;
                }}
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}

                .textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                    display: block;
                }}
            </style>
        </head>
        <body>
'''

page_footer = '''
        </body>
    </html>
'''


rotate_form = '''
    <form action="/rotate" method="post">
        <label>Rotate by
        <input type="text" name="rot" placeholder="0"/> 
        </label>
        <br>
        <textarea class="textarea" name="text">{0}</textarea>

        <input type="submit"/>
    </form>
'''

@app.route("/rotate", methods=['POST'])
def rotate_char():

    num = request.form['rot']
    char = request.form['text']

    solution = encrypt(str(char), int(num))

    # display = "<h1>" + solution + "</h1>"

    # content = page_header + display + page_footer

    return rotate_form.format(solution)



@app.route('/') 
def index():
    content = page_header + rotate_form.format("") + page_footer

    return content




app.run()