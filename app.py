from flask import Flask, request, jsonify, \
render_template, json, redirect, redirect, \
url_for, session, make_response, flash
from models import MModel
from time import sleep
import pdfkit

application = Flask(__name__)
application.config['SECRET_KEY'] = 'sfh7^erw9*(%sadHGw%R'

model = MModel()
html_source = ''
 
app = Flask(__name__)

# ======================================================================================================= 
# # Index
@application.route('/')
def index():
	if 'data_nama' in session:
		data_nama = session['data_nama']
		return render_template('index_sistem.html', data_nama=data_nama)
	return render_template('form_login.html')

@application.route('/jual')
def jual():
	if 'data_nama' in session:
		data_nama = session['data_nama']
		return render_template('jual.html', data_nama=data_nama)
	return render_template('form_login.html')

# login	
@application.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if model.authenticate(username, password):
			data_nama = model.getUserForSession(username)
			session['data_nama'] = data_nama
			return redirect(url_for('index'))
		msg = 'Username / Password Salah.'
		return render_template('form_login.html', msg=msg)
	return render_template('form_login.html')

# Logout  
@application.route('/logout')
def logout():
	session.pop('data_nama', '')
	return redirect(url_for('login'))



# ============================ Data pegawai ===================================================
# Menampilkan Data pegawai
@application.route('/pegawai')
def pegawai():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        nama = data_nama[1]
        container_pegawai = [] 
        container_pegawai = model.selectPegawai()
        return render_template('pegawai.html', container_pegawai=container_pegawai, data_nama=data_nama)
    return render_template('form_login.html')

# Tambah Data Pegawai
@application.route('/insert_pegawai', methods=['GET', 'POST'])
def insert_pegawai():
	if 'data_nama' in session:
		if request.method == 'POST':
			id_pegawai = request.form['id_pegawai']
			nik = request.form['nik']
			nama = request.form['nama']
			username = request.form['username']
			password = request.form['password']
			jenis_kelamin = request.form['jenis_kelamin']
			jabatan = request.form['jabatan']
			tanggal_masuk = request.form['tanggal_masuk']
			status = request.form['status']
			hak_akses = request.form['hak_akses']
			data_p = (id_pegawai, nik, nama, username, password, jenis_kelamin, jabatan, tanggal_masuk, status, hak_akses)
			model.insertPegawai(data_p)
			flash("Data Berhasil Ditambahkan")
			return redirect(url_for('pegawai'))
		else:
			data_nama = session['data_nama']
			return render_template('insert_pegawai.html', data_nama=data_nama)
	return render_template('form_login.html')

# Update Data Pengguna
@application.route('/update_pegawai/<id_pegawai>')
def update_pegawai(id_pegawai):
	if 'data_nama' in session:
		data_pg = model.getPegawaibyNo(id_pegawai)
		data_nama = session['data_nama']
		return render_template('edit_pegawai.html', data_pg=data_pg, data_nama=data_nama)
	return redirect(url_for('login')) 
    
@application.route('/update_pg', methods=['GET', 'POST'])
def update_pg():
    if 'data_nama' in session:
        id_pegawai = request.form['id_pegawai']
        nik = request.form['nik']
        nama = request.form['nama']
        username = request.form['username']
        password = request.form['password']
        jenis_kelamin = request.form['jenis_kelamin']
        jabatan = request.form['jabatan']
        tanggal_masuk = request.form['tanggal_masuk']
        status = request.form['status']
        hak_akses = request.form['hak_akses']
        data_pg = (id_pegawai, nik, nama, username, password, jenis_kelamin, jabatan, tanggal_masuk, status, hak_akses)
        model.updatePegawai(data_pg)
        flash("Data Berhasil Diupdate")
        return redirect(url_for('pegawai'))
    return render_template('form_login.html')

# Menghapus Data Pengguna
@application.route('/delete_pegawai/<id_pegawai>')
def delete_pegawai(id_pegawai):
    if 'data_nama' in session:
        model.deletePegawai(id_pegawai)
        flash("Data Berhasil Dihapus")
        return redirect(url_for('pegawai'))
    return render_template('form_login.html')

# ============================ Data Jabatan ===================================================
# Menampilkan Data Jabatan
@application.route('/jabatan')
def jabatan():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        nama = data_nama[1]
        container_jabatan = [] 
        container_jabatan = model.selectJabatan()
        return render_template('jabatan.html', container_jabatan=container_jabatan, data_nama=data_nama)
    return render_template('form_login.html')

# Tambah Data Jabatan
@application.route('/insert_jabatan', methods=['GET', 'POST'])
def insert_jabatan():
	if 'data_nama' in session:
		if request.method == 'POST':
			id_jabatan = request.form['id_jabatan']
			nama_jabatan = request.form['nama_jabatan']
			gaji_pokok = request.form['gaji_pokok']
			tj_transport = request.form['tj_transport']
			uang_makan = request.form['uang_makan']
			data_j = (id_jabatan, nama_jabatan, gaji_pokok, tj_transport, uang_makan)
			model.insertJabatan(data_j)
			flash("Data Berhasil Ditambahkan")
			return redirect(url_for('jabatan'))
		else:
			data_nama = session['data_nama']
			return render_template('insert_jabatan.html', data_nama=data_nama)
	return render_template('form_login.html')

# Update Data Jabatan
@application.route('/update_jabatan/<id_jabatan>')
def update_jabatan(id_jabatan):
	if 'data_nama' in session:
		data_jb = model.getJabatanbyNo(id_jabatan)
		data_nama = session['data_nama']
		return render_template('edit_jabatan.html', data_jb=data_jb, data_nama=data_nama)
	return redirect(url_for('login')) 
    
@application.route('/update_jb', methods=['GET', 'POST'])
def update_jb():
    if 'data_nama' in session:
        id_jabatan = request.form['id_jabatan']
        nama_jabatan = request.form['nama_jabatan']
        gaji_pokok = request.form['gaji_pokok']
        tj_transport = request.form['tj_transport']
        uang_makan = request.form['uang_makan']
        data_jb = (id_jabatan, nama_jabatan, gaji_pokok, tj_transport, uang_makan)
        model.updateJabatan(data_jb)
        flash("Data Berhasil Diupdate")
        return redirect(url_for('jabatan'))
    return render_template('form_login.html')

# Menghapus Data Jabatan
@application.route('/delete_jabatan/<id_jabatan>')
def delete_jabatan(id_jabatan):
    if 'data_nama' in session:
        model.deleteJabatan(id_jabatan)
        flash("Data Berhasil Dihapus")
        return redirect(url_for('jabatan'))
    return render_template('form_login.html')

# ============================ Data Potongan ===================================================
# Menampilkan Data Potongan
@application.route('/potongan')
def potongan():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        nama = data_nama[1]
        container_potongan = [] 
        container_potongan = model.selectPotongan()
        return render_template('setting_potongan.html', container_potongan=container_potongan, data_nama=data_nama)
    return render_template('form_login.html')

# Tambah Data Potongan
@application.route('/insert_potongan', methods=['GET', 'POST'])
def insert_potongan():
	if 'data_nama' in session:
		if request.method == 'POST':
			id_potongan = request.form['id_potongan']
			jenis_potongan = request.form['jenis_potongan']
			jumlah_potongan = request.form['jumlah_potongan']
			data_pt = (id_potongan, jenis_potongan, jumlah_potongan)
			model.insertPotongan(data_pt)
			flash("Data Berhasil Ditambahkan")
			return redirect(url_for('potongan'))
		else:
			data_nama = session['data_nama']
			return render_template('insert_setting_potongan.html', data_nama=data_nama)
	return render_template('form_login.html')

# Update Data Potongan
@application.route('/update_potongan/<id_potongan>')
def update_potongan(id_potongan):
	if 'data_nama' in session:
		data_ptg = model.getPotonganbyNo(id_potongan)
		data_nama = session['data_nama']
		return render_template('edit_potongan.html', data_ptg=data_ptg, data_nama=data_nama)
	return redirect(url_for('login')) 
    
@application.route('/update_ptg', methods=['GET', 'POST'])
def update_ptg():
    if 'data_nama' in session:
        id_potongan = request.form['id_potongan']
        jenis_potongan = request.form['jenis_potongan']
        jumlah_potongan = request.form['jenis_potongan']
        data_ptg = (id_potongan, jenis_potongan, jumlah_potongan)
        model.updatePotongan(data_ptg)
        flash("Data Berhasil Diupdate")
        return redirect(url_for('potongan'))
    return render_template('form_login.html')

# Menghapus Data Potongan
@application.route('/delete_potongan/<id_potongan>')
def delete_potongan(id_potongan):
    if 'data_nama' in session:
        model.deletePotongan(id_potongan)
        flash("Data Berhasil Dihapus")
        return redirect(url_for('potongan'))
    return render_template('form_login.html')

# ================= GAJI ====================
    # Menampilkan Data Gaji
@application.route('/gaji')
def gaji():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        nama = data_nama[1]
        container_gaji = [] 
        container_gaji = model.selectGaji()
        return render_template('gaji.html', container_gaji=container_gaji, data_nama=data_nama)
    return render_template('form_login.html')

# Tambah Data Gaji
@application.route('/insert_gaji', methods=['GET', 'POST'])
def insert_gaji():
	if 'data_nama' in session:
		if request.method == 'POST':
			id_gaji = request.form['id_gaji']
			id_pegawai = request.form['id_pegawai']
			id_jabatan = request.form['id_jabatan']
			id_potongan = request.form['id_potongan']
			date = request.form['date']
			status_gaji = '-'
			data_g = (id_gaji, id_pegawai, id_jabatan, date, status_gaji, id_potongan)
			model.insertGaji(data_g)
			flash("Data Berhasil Ditambahkan")
			return redirect(url_for('gaji'))
		else:
			data_nama = session['data_nama']
			return render_template('insert_gaji.html', data_nama=data_nama)
	return render_template('form_login.html')

# TRANSAKSI ==================================================================
# Menampilkan Data Transaksi
@application.route('/transaksi')
def transaksi():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        nama = data_nama[1]
        container_transaksi = [] 
        container_transaksi = model.selectTransaksi()
        return render_template('transaksi.html', container_transaksi=container_transaksi, data_nama=data_nama)
    return render_template('form_login.html')

@application.route('/tahun2021')
def tahun2021():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        nama = data_nama[1]
        container_transaksi_2021 = [] 
        container_transaksi_2021 = model.select2021()
        return render_template('transaksi2021.html', container_transaksi_2021=container_transaksi_2021, data_nama=data_nama)
    return render_template('form_login.html')

@application.route('/tahun2022')
def tahun2022():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        nama = data_nama[1]
        container_transaksi_2022 = [] 
        container_transaksi_2022 = model.select2022()
        return render_template('transaksi2022.html', container_transaksi_2022=container_transaksi_2022, data_nama=data_nama)
    return render_template('form_login.html')
# END TRANSAKSI ==================================================================

# Detail Gaji
@application.route('/detail_gaji/<id_gaji>')
def detail_gaji(id_gaji):
	if 'data_nama' in session:
		data_gj = model.getGajibyNo(id_gaji)
		data_nama = session['data_nama']
		return render_template('detail_transaksi.html', data_gj=data_gj, data_nama=data_nama)
	return redirect(url_for('login')) 
    
@application.route('/detail_gj', methods=['GET', 'POST'])
def detail_gj():
    if 'data_nama' in session:
        id_gaji = request.form['id_gaji']
        id_pegawai = request.form['id_pegawai']
        id_jabatan = request.form['id_jabatan']
        id_potongan = request.form['id_potongan']
        date = request.form['date']
        status_gaji = request.form['status_gaji']
        data_gj = (id_gaji, id_pegawai, id_jabatan, date, status_gaji, id_potongan)
        model.detailGaji(data_gj)
        return redirect(url_for('gaji'))
    return render_template('form_login.html')

# Menghapus Data Gaji
@application.route('/delete_gaji/<id_gaji>')
def delete_gaji(id_gaji):
    if 'data_nama' in session:
        model.deleteGaji(id_gaji)
        flash("Data Berhasil Dihapus")
        return redirect(url_for('gaji'))
    return render_template('form_login.html')


#  LAPORAN ===========================================================================================
# Menampilkan Data Transaksi
@application.route('/laporan')
def laporan():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        nama = data_nama[1]
        container_laporan = [] 
        container_laporan = model.selectLaporan()
        return render_template('laporan_gaji.html', container_laporan=container_laporan, data_nama=data_nama)
    return render_template('form_login.html')

# CETAK laporan
@application.route('/laporan_gaji')
def laporan_gaji():
	if 'data_nama' in session:
		data_nama = session['data_nama']
		container_transaksi = []
		container_transaksi = model.selectTransaksi()
		html = render_template('pdf.html', container_transaksi=container_transaksi, data_nama=data_nama)
		config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files (x86)\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
		pdf = pdfkit.from_string(html, False, configuration=config)
		respons = make_response(pdf)
		respons.headers['Content-Type'] = 'application/pdf'
		respons.headers['Content-Desposition'] = 'inline: filename=laporan.pdf'
		return respons
	return render_template('form_login.html')

# CETAK laporan
@application.route('/laporan_gaji_2021')
def laporan_gaji_2021():
	if 'data_nama' in session:
		data_nama = session['data_nama']
		container_transaksi_2021 = []
		container_transaksi_2021 = model.select2021()
		html = render_template('pdf2021.html', container_transaksi_2021=container_transaksi_2021, data_nama=data_nama)
		config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files (x86)\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
		pdf = pdfkit.from_string(html, False, configuration=config)
		respons = make_response(pdf)
		respons.headers['Content-Type'] = 'application/pdf'
		respons.headers['Content-Desposition'] = 'inline: filename=laporan.pdf'
		return respons
	return render_template('form_login.html')

# CETAK laporan
@application.route('/laporan_gaji_2022')
def laporan_gaji_2022():
	if 'data_nama' in session:
		data_nama = session['data_nama']
		container_transaksi_2022 = []
		container_transaksi_2022 = model.select2022()
		html = render_template('pdf2022.html', container_transaksi_2022=container_transaksi_2022, data_nama=data_nama)
		config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files (x86)\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
		pdf = pdfkit.from_string(html, False, configuration=config)
		respons = make_response(pdf)
		respons.headers['Content-Type'] = 'application/pdf'
		respons.headers['Content-Desposition'] = 'inline: filename=laporan.pdf'
		return respons
	return render_template('form_login.html')


if __name__ == '__main__':
    application.run(debug=True)