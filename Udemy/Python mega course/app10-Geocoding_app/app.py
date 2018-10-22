from flask import Flask, render_template, request, Markup, send_file
from werkzeug import secure_filename
import pandas
from geopy.geocoders import Nominatim

app = Flask(__name__)
nom = Nominatim(scheme="http")

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
	global csv
	csv = request.files['file']
	if csv.filename[-3:]!='csv':
		return render_template('index.html', warning = Markup('<h3 style="color:#d60007"> Arquivo não está no formato desejado!</h3>'))
	try:
		csv.save(secure_filename('uploaded'+csv.filename))
		data = pandas.read_csv('uploaded'+csv.filename)
		data.set_index('ID')
		data['Address'] = data['Address'] + ", " + data['City'] + ", " + data['State'] + ", " + data['Country']
		data['Coordinates'] = data['Address'].apply(nom.geocode)
		data['Latitude'] = data['Coordinates'].apply(lambda x: x.latitude if x != None else 'N/A')
		data['Longitude'] = data['Coordinates'].apply(lambda x: x.longitude if x != None else 'N/A')
		del data['City']
		del data['State']
		del data['Country']
		del data['Coordinates']
		data.to_csv('processed'+csv.filename, index=None)
		return render_template('index.html', tabela = 'tabela.html', tb = data.to_html())
	except:
		return render_template('index.html', warning = Markup('<h3 style="color:#d60007"> Arquivo não está no formato desejado!</h3>'))

@app.route('/download')
def download():
	return send_file('processed'+csv.filename, attachment_filename="yourfile.csv", as_attachment=True)

if __name__=='__main__':
	app.debug = True
	app.run()