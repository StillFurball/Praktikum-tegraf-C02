# Praktikum-tegraf-C02
| Name           | NRP        | 
| ---            | ---        | 
| Rafi Attar Maulana | 5025241141 | 
| Denzel Daniels | 5025241228 | 
| Mohammad Najib Bahrudin | 5025241230 | 


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
