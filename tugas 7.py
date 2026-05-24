# Data mahasiswa dalam bentuk array (list of dictionaries)
mahasiswa = [
    {"Nama": "Rewinur", "Kehadiran": "Tinggi", "Tugas": "Lengkap"},
    {"Nama": "Naila", "Kehadiran": "Rendah", "Tugas": "Tidak Lengkap"},
    {"Nama": "Mawar", "Kehadiran": "Tinggi", "Tugas": "Lengkap"},
    {"Nama": "Melda", "Kehadiran": "Rendah", "Tugas": "Tidak Lengkap"},
]

def status_mahasiswa(kehadiran, tugas):
    if kehadiran == "Tinggi":
        status = "Aktif"
        if tugas == "Lengkap":
            keterangan = "Mahasiswa Disiplin"
        else:
            keterangan = ""
    else:  # Kehadiran Rendah
        status = "Tidak Aktif"
        keterangan = ""
    return status, keterangan

# Tampilkan hasil status untuk seluruh data mahasiswa
for mhs in mahasiswa:
    status, keterangan = status_mahasiswa(mhs["Kehadiran"], mhs["Tugas"])
    print(f"Nama: {mhs['Nama']}")
    print(f"Kehadiran: {mhs['Kehadiran']}")
    print(f"Tugas: {mhs['Tugas']}")
    print(f"Status: {status}")
    if keterangan:
        print(f"Keterangan: {keterangan}")
    print("-" * 30)

# Tambahkan 1 data mahasiswa baru (fitur tambahan)
nama_baru = input("Masukkan nama mahasiswa baru: ")
kehadiran_baru = input("Masukkan kehadiran (Tinggi/Rendah): ")
tugas_baru = input("Masukkan status tugas (Lengkap/Tidak Lengkap): ")

status_baru, keterangan_baru = status_mahasiswa(kehadiran_baru, tugas_baru)
print("\nData Mahasiswa Baru:")
print(f"Nama: {nama_baru}")
print(f"Kehadiran: {kehadiran_baru}")
print(f"Tugas: {tugas_baru}")
print(f"Status: {status_baru}")
if keterangan_baru:
    print(f"Keterangan: {keterangan_baru}")