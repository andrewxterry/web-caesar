from flask import Flask, redirect

app = Flask(__name__)
app.config['DEBUG'] = True 


page_header = '''

<!doctype html>
    <html>
        <head>
            <style>
                form{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }

                .textarea{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
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
        <input type="text" name="rot"/>
        </label>

        <input class="textarea" type="textarea" name="text"/>

        <input type="submit"/>
    </form>
'''




@app.route('/')

def index():
    content = page_header + rotate_form + page_footer

    return content


app.run()