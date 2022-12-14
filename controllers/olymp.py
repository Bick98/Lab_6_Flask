import constants
from app import app
from flask import render_template, request
@app.route('/olymp/<olymp>')
def olympiad(olymp):
 html = render_template(
 'olymp.html',
 olymp = olymp,
 discription = constants.olympiad_dict[olymp]
 )
 return html