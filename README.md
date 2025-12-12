  # Praktikum - Teori Graf - C02
| Name           | NRP        | 
| ---            | ---        | 
| Rafi Attar Maulana | 5025241141 | 
| Denzel Daniels | 5025241228 | 
| Mohammad Najib Bahrudin | 5025241230 | 

### SOAL 1
<img width="665" height="498" alt="Screenshot 2025-12-12 at 21 59 51" src="https://github.com/user-attachments/assets/5162b0f1-af07-403e-b0a5-443fdd1f6914" />


### 1. **knight_open.py** - Open Tour (Animated)
**Tipe Tour:** Open Tour (tidak perlu kembali ke posisi awal)

#### Cara Penggunaan:
```powershell
python knight_open.py
```

#### Input:
- Program berjalan otomatis (tidak ada input user)
- Posisi awal: **(2, 4)** (tetap/hard-coded)

#### Output:
- **Animasi papan catur 8x8** dengan:
  - **Node hijau** = Posisi awal knight
  - **Node biru** = Posisi saat ini saat animasi berjalan
  - **Node merah** = Posisi akhir (langkah ke-64)
  - **Panah merah** menunjukkan jalur pergerakan
- Animasi berjalan otomatis setelah program dimulai

#### Fitur:
- Animasi smooth dengan delay antar langkah (0.1 detik) 
- Warna node memudahkan identifikasi start/end
- 64 langkah dijamin (full Hamiltonian path)

---

### 2. **knight_closed2.py** - Closed Tour (Animated)
**Tipe Tour:** Closed Tour dengan animasi (knight kembali ke awal)

#### Cara Penggunaan:
```powershell
python knight_closed2.py
```

#### Input:
- Program berjalan otomatis (tidak ada input user)
- Posisi awal: **acak** (setiap run berbeda/hard-coded)

#### Output:
- **Animasi papan catur 8x8** dengan:
  - **Node hijau** = Posisi awal knight
  - **Node biru** = Posisi saat animasi berjalan
  - **Node merah** = Posisi akhir yang dapat kembali ke awal
  - **Panah merah** menunjukkan jalur pergerakan
- Animasi berjalan otomatis

## Algoritma: Warnsdorff's Heuristic

Algoritma memilih langkah berikutnya berdasarkan **degree** (jumlah langkah valid tersisa):
- Pilih posisi dengan **degree terendah** (fewest onward moves)
- Ini menghindarkan knight terjebak di area dengan sedikit pilihan

### SOAL 2
<img width="877" height="502" alt="Screenshot 2025-12-12 at 22 00 29" src="https://github.com/user-attachments/assets/5a010e3e-bc23-4aab-a741-0cd0c98e1b4f" />
