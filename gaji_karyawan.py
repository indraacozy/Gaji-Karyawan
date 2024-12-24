# Program menghitung gaji karyawan

def hitung_gaji(jam_kerja, tarif_per_jam):
    # Batas kerja normal
    batas_jam_normal = 40
    tarif_lembur = 1.5 * tarif_per_jam

    if jam_kerja > batas_jam_normal:
        jam_lembur = jam_kerja - batas_jam_normal
        gaji = (batas_jam_normal * tarif_per_jam) + (jam_lembur * tarif_lembur)
    else:
        gaji = jam_kerja * tarif_per_jam

    return gaji

# Meminta input dari pengguna
try:
    jam_kerja = float(input("Masukkan jumlah jam kerja dalam seminggu: "))
    tarif_per_jam = float(input("Masukkan tarif per jam: "))

    # Menghitung gaji
    gaji = hitung_gaji(jam_kerja, tarif_per_jam)

    # Menampilkan hasil
    print(f"Gaji total karyawan adalah: Rp{gaji:,.2f}")

except ValueError:
    print("Input tidak valid. Harap masukkan angka yang benar.")
