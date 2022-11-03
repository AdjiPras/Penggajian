import pymysql
import config2

db = cursor = None

class MModel:
	def __init__ (self, no=None, nama=None, no_telp=None):
		self.no = no
		self.nama = nama
		self.no_telp = no_telp
		
	def openDB(self):
		global db, cursor
		db = pymysql.connect(
			host=config2.DB_HOST,
			user=config2.DB_USER,
			password=config2.DB_PASSWORD,
			database=config2.DB_NAME)
		cursor = db.cursor()

	def closeDB(self):
		global db, cursor
		db.close()

	# validasi login dengan table data_pegawai.
	def authenticate(self, username=None, password=None):
		self.openDB()
		cursor.execute("SELECT COUNT(*) FROM data_pegawai WHERE username = '%s' AND password = '%s'" % (username, password))
		count_account = (cursor.fetchone())[0]
		self.closeDB()
		return True if count_account>0 else False

# ========================= DATA PEGAWAI ================================
	# Menampilkan Data Pegawai Dari DB
	def selectPegawai(self):
		self.openDB()
		cursor.execute("SELECT id_pegawai, nik, nama, username, password, jenis_kelamin, jabatan, tanggal_masuk, status, hak_akses FROM `data_pegawai` ORDER BY nama ASC")
		container_pegawai = []
		for id_pegawai, nik, nama, username, password, jenis_kelamin, jabatan, tanggal_masuk, status, hak_akses in cursor.fetchall():
			container_pegawai.append((id_pegawai, nik, nama, username, password, jenis_kelamin, jabatan, tanggal_masuk, status, hak_akses))
		self.closeDB()
		return container_pegawai

	# Untuk Hak Akses
	def getUserForSession(self, username):
		self.openDB()
		cursor.execute("SELECT username, nama, hak_akses FROM data_pegawai WHERE username='%s'" % username)
		data_nama = cursor.fetchone()
		return data_nama

	# Menambah Data Pegawai
	def insertPegawai(self, data_p):
		self.openDB()
		cursor.execute("INSERT INTO data_pegawai (id_pegawai, nik, nama, username, password, jenis_kelamin, jabatan, tanggal_masuk, status, hak_akses) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % data_p)
		db.commit()
		self.closeDB()

	# Update Data Pegaawai
	def updatePegawai(self, data_pg):
		self.openDB()
		cursor.execute("UPDATE data_pegawai SET nik='%s', nama='%s', username='%s', password='%s', jenis_kelamin='%s', jabatan='%s', tanggal_masuk='%s', status='%s', hak_akses='%s' WHERE id_pegawai='%s'" % data_pg)
		db.commit()
		self.closeDB()

	def getPegawaibyNo(self, id_pegawai):
		self.openDB()
		cursor.execute("SELECT id_pegawai, nik, nama, username, password, jenis_kelamin, jabatan, tanggal_masuk, status, hak_akses FROM data_pegawai WHERE id_pegawai='%s'" % id_pegawai)
		data_pg = cursor.fetchone()
		return data_pg

	# Menghapus Data Pegawai
	def deletePegawai(self, id_pegawai):
		self.openDB()
		cursor.execute("DELETE FROM data_pegawai WHERE id_pegawai='%s'" % id_pegawai)
		db.commit()
		self.closeDB()

# ========================= DATA JABATAN ================================
	# Menampilkan Data Jabatan Dari DB
	def selectJabatan(self):
		self.openDB()
		cursor.execute("SELECT id_jabatan, nama_jabatan, CONCAT('Rp. ',FORMAT(gaji_pokok,2)), \
			CONCAT('Rp. ',FORMAT(tj_transport,2)), CONCAT('Rp. ',FORMAT(uang_makan,2)) FROM `data_jabatan` ORDER BY nama_jabatan ASC")
		container_jabatan = []
		for id_jabatan, nama_jabatan, gaji_pokok, tj_transport, uang_makan in cursor.fetchall():
			container_jabatan.append((id_jabatan, nama_jabatan, gaji_pokok, tj_transport, uang_makan))
		self.closeDB()
		return container_jabatan

	# Menambah Data Jabatan
	def insertJabatan(self, data_j):
		self.openDB()
		cursor.execute("INSERT INTO data_jabatan (id_jabatan, nama_jabatan, gaji_pokok, tj_transport, uang_makan) VALUES('%s', '%s', '%s', '%s', '%s')" % data_j)
		db.commit()
		self.closeDB()

	# Update Data Jabatan
	def updateJabatan(self, data_jb):
		self.openDB()
		cursor.execute("UPDATE data_jabatan SET nama_jabatan='%s', gaji_pokok='%s', tj_transport='%s', uang_makan='%s' WHERE id_jabatan='%s'" % data_jb)
		db.commit()
		self.closeDB()

	def getJabatanbyNo(self, id_jabatan):
		self.openDB()
		cursor.execute("SELECT id_jabatan, nama_jabatan, gaji_pokok, tj_transport, uang_makan FROM data_jabatan WHERE id_jabatan='%s'" % id_jabatan)
		data_jb = cursor.fetchone()
		return data_jb

	# Menghapus Data Jabatan
	def deleteJabatan(self, id_jabatan):
		self.openDB()
		cursor.execute("DELETE FROM data_jabatan WHERE id_jabatan='%s'" % id_jabatan)
		db.commit()
		self.closeDB()

# ========================= DATA POTONGAN ================================
	# Menampilkan Data Potongan Dari DB
	def selectPotongan(self):
		self.openDB()
		cursor.execute("SELECT id_potongan, jenis_potongan, CONCAT('Rp. ',FORMAT(jumlah_potongan,2)) FROM `data_potongan` ORDER BY jenis_potongan ASC")
		container_potongan = []
		for id_potongan, jenis_potongan, jumlah_potongan in cursor.fetchall():
			container_potongan.append((id_potongan, jenis_potongan, jumlah_potongan))
		self.closeDB()
		return container_potongan

		# Menambah Data Potongan
	def insertPotongan(self, data_pt):
		self.openDB()
		cursor.execute("INSERT INTO data_potongan (id_potongan, jenis_potongan, jumlah_potongan) VALUES('%s', '%s', '%s')" % data_pt)
		db.commit()
		self.closeDB()

		# Update Data Potongan
	def updatePotongan(self, data_ptg):
		self.openDB()
		cursor.execute("UPDATE data_potongan SET jenis_potongan='%s', jumlah_potongan='%s' WHERE id_potongan='%s'" % data_ptg)
		db.commit()
		self.closeDB()

	def getPotonganbyNo(self, id_potongan):
		self.openDB()
		cursor.execute("SELECT id_potongan, jenis_potongan, jumlah_potongan FROM data_potongan WHERE id_potongan='%s'" % id_potongan)
		data_ptg = cursor.fetchone()
		return data_ptg

	# Menghapus Data Potongan
	def deletePotongan(self, id_potongan):
		self.openDB()
		cursor.execute("DELETE FROM data_potongan WHERE id_potongan='%s'" % id_potongan)
		db.commit()
		self.closeDB()

# ========================= Data Gaji ================================
	# Menampilkan Data Gaji
	def selectGaji(self):
		self.openDB()
		cursor.execute("SELECT g.id_gaji, g.date, p.nik, p.nama, p.jenis_kelamin, j.nama_jabatan, \
			CONCAT('Rp. ',FORMAT(j.gaji_pokok,2)), CONCAT('Rp. ',FORMAT(j.tj_transport,2)), \
			CONCAT('Rp. ',FORMAT(j.uang_makan,2)), CONCAT('Rp. ',FORMAT(pt.jumlah_potongan,2)), \
			CONCAT('Rp. ',FORMAT(j.gaji_pokok+j.tj_transport+j.uang_makan-pt.jumlah_potongan,2)) AS Total, g.status_gaji \
			FROM data_gaji g \
			JOIN data_pegawai p ON g.id_pegawai=p.id_pegawai \
			JOIN data_jabatan j ON g.id_jabatan=j.id_jabatan \
			JOIN data_potongan pt ON g.id_potongan=pt.id_potongan \
			WHERE g.date ORDER BY g.date DESC")
		container_gaji = []
		for id_gaji,date,nik,nama_pegawai,jenis_kelamin,nama_jabatan,gaji_pokok,tj_transport,uang_makan,jumlah_potongan,total_gaji,status_gaji in cursor.fetchall():
			container_gaji.append((id_gaji,date,nik,nama_pegawai,jenis_kelamin,nama_jabatan,gaji_pokok,tj_transport,uang_makan,jumlah_potongan,total_gaji,status_gaji))
		self.closeDB()
		return container_gaji

		# Menambah Data Potongan
	def insertGaji(self, data_g):
		self.openDB()
		cursor.execute("INSERT INTO data_gaji (id_gaji, id_pegawai, id_jabatan, date, status_gaji, id_potongan) VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % data_g)
		db.commit()
		self.closeDB()

	# Menampilkan Data Transaksi
	def selectTransaksi(self):
		self.openDB()
		cursor.execute("SELECT g.id_gaji, g.date, p.nik, p.nama, p.jenis_kelamin, j.nama_jabatan, \
			CONCAT('Rp. ',FORMAT(j.gaji_pokok,2)), CONCAT('Rp. ',FORMAT(j.tj_transport,2)), \
			CONCAT('Rp. ',FORMAT(j.uang_makan,2)), CONCAT('Rp. ',FORMAT(pt.jumlah_potongan,2)), \
			CONCAT('Rp. ',FORMAT(g.total_gaji,2)) AS Total, g.status_gaji \
			FROM data_gaji g \
			JOIN data_pegawai p ON g.id_pegawai=p.id_pegawai \
			JOIN data_jabatan j ON g.id_jabatan=j.id_jabatan \
			JOIN data_potongan pt ON g.id_potongan=pt.id_potongan\
			WHERE g.date ORDER BY g.date DESC")
		container_transaksi = []
		for id_gaji,date,nik,nama_pegawai,jenis_kelamin,nama_jabatan,gaji_pokok,tj_transport,uang_makan,jumlah_potongan,total_gaji,status_gaji in cursor.fetchall():
			container_transaksi.append((id_gaji,date,nik,nama_pegawai,jenis_kelamin,nama_jabatan,gaji_pokok,tj_transport,uang_makan,jumlah_potongan,total_gaji,status_gaji))
		self.closeDB()
		return container_transaksi

	# Menampilkan Data Transaksi Borongan
	def select2021(self):
		self.openDB()
		cursor.execute("SELECT g.id_gaji, g.date, p.nik, p.nama, p.jenis_kelamin, j.nama_jabatan, \
			CONCAT('Rp. ',FORMAT(j.gaji_pokok,2)), CONCAT('Rp. ',FORMAT(j.tj_transport,2)), \
			CONCAT('Rp. ',FORMAT(j.uang_makan,2)), CONCAT('Rp. ',FORMAT(pt.jumlah_potongan,2)), \
			CONCAT('Rp. ',FORMAT(g.total_gaji,2)) AS Total, g.status_gaji \
			FROM data_gaji g \
			JOIN data_pegawai p ON g.id_pegawai=p.id_pegawai \
			JOIN data_jabatan j ON g.id_jabatan=j.id_jabatan \
			JOIN data_potongan pt ON g.id_potongan=pt.id_potongan\
			WHERE g.date BETWEEN '2021-0-00' AND '2021-12-12' \
			ORDER BY g.date DESC")
		container_transaksi_2021 = []
		for id_gaji,date,nik,nama_pegawai,jenis_kelamin,nama_jabatan,gaji_pokok,tj_transport,uang_makan,jumlah_potongan,total_gaji,status_gaji in cursor.fetchall():
			container_transaksi_2021.append((id_gaji,date,nik,nama_pegawai,jenis_kelamin,nama_jabatan,gaji_pokok,tj_transport,uang_makan,jumlah_potongan,total_gaji,status_gaji))
		self.closeDB()
		return container_transaksi_2021

	# Menampilkan Data Transaksi 2022
	def select2022(self):
		self.openDB()
		cursor.execute("SELECT g.id_gaji, g.date, p.nik, p.nama, p.jenis_kelamin, j.nama_jabatan, \
			CONCAT('Rp. ',FORMAT(j.gaji_pokok,2)), CONCAT('Rp. ',FORMAT(j.tj_transport,2)), \
			CONCAT('Rp. ',FORMAT(j.uang_makan,2)), CONCAT('Rp. ',FORMAT(pt.jumlah_potongan,2)), \
			CONCAT('Rp. ',FORMAT(g.total_gaji,2)) AS Total, g.status_gaji \
			FROM data_gaji g \
			JOIN data_pegawai p ON g.id_pegawai=p.id_pegawai \
			JOIN data_jabatan j ON g.id_jabatan=j.id_jabatan \
			JOIN data_potongan pt ON g.id_potongan=pt.id_potongan\
			WHERE g.date BETWEEN '2022-0-00' AND '2022-12-12' \
			ORDER BY g.date DESC")
		container_transaksi_2022 = []
		for id_gaji,date,nik,nama_pegawai,jenis_kelamin,nama_jabatan,gaji_pokok,tj_transport,uang_makan,jumlah_potongan,total_gaji,status_gaji in cursor.fetchall():
			container_transaksi_2022.append((id_gaji,date,nik,nama_pegawai,jenis_kelamin,nama_jabatan,gaji_pokok,tj_transport,uang_makan,jumlah_potongan,total_gaji,status_gaji))
		self.closeDB()
		return container_transaksi_2022

	def getGajibyNo(self, id_gaji):
		self.openDB()
		cursor.execute("SELECT g.id_gaji, g.date, p.nik, p.nama, p.jenis_kelamin, j.nama_jabatan, \
			CONCAT('Rp. ',FORMAT(j.gaji_pokok,2)), CONCAT('Rp. ',FORMAT(j.tj_transport,2)), \
			CONCAT('Rp. ',FORMAT(j.uang_makan,2)), CONCAT('Rp. ',FORMAT(pt.jumlah_potongan,2)), \
			CONCAT('Rp. ',FORMAT(g.total_gaji,2)) AS Total, g.status_gaji \
			FROM data_gaji g \
			JOIN data_pegawai p ON g.id_pegawai=p.id_pegawai \
			JOIN data_jabatan j ON g.id_jabatan=j.id_jabatan \
			JOIN data_potongan pt ON g.id_potongan=pt.id_potongan \
			WHERE id_gaji='%s'" % id_gaji)
		data_gj = cursor.fetchone()
		return data_gj

# LAPORAN =============================================================================================
	# Menampilkan Data Laporan Gaji
	def selectLaporan(self):
		self.openDB()
		cursor.execute("SELECT g.id_gaji, g.date, p.nik, p.nama, p.jenis_kelamin, j.nama_jabatan, \
			CONCAT('Rp. ',FORMAT(j.gaji_pokok,2)), CONCAT('Rp. ',FORMAT(j.tj_transport,2)), \
			CONCAT('Rp. ',FORMAT(j.uang_makan,2)), CONCAT('Rp. ',FORMAT(pt.jumlah_potongan,2)), \
			CONCAT('Rp. ',FORMAT(g.total_gaji,2)) AS Total, g.status_gaji \
			FROM data_gaji g \
			JOIN data_pegawai p ON g.id_pegawai=p.id_pegawai \
			JOIN data_jabatan j ON g.id_jabatan=j.id_jabatan \
			JOIN data_potongan pt ON g.id_potongan=pt.id_potongan\
			WHERE g.date ORDER BY g.date DESC")
		container_laporan = []
		for id_gaji,date,nik,nama_pegawai,jenis_kelamin,nama_jabatan,gaji_pokok,tj_transport,uang_makan,jumlah_potongan,total_gaji,status_gaji in cursor.fetchall():
			container_laporan.append((id_gaji,date,nik,nama_pegawai,jenis_kelamin,nama_jabatan,gaji_pokok,tj_transport,uang_makan,jumlah_potongan,total_gaji,status_gaji))
		self.closeDB()
		return container_laporan

	# Menghapus Data Gaji
	def deleteGaji(self, id_gaji):
		self.openDB()
		cursor.execute("DELETE FROM data_gaji WHERE id_gaji='%s'" % id_gaji)
		db.commit()
		self.closeDB()
	