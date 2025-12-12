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

## Deskripsi Program
Program ini menyelesaikan masalah Largest Monotonically Increasing Subsequence (LMIS) menggunakan algoritma Dynamic Programming.

LMIS adalah subsequence terpanjang dari sebuah urutan bilangan dimana setiap elemen lebih besar dari elemen sebelumnya (monoton naik).

## Cara Penggunaan

### 1. Menjalankan Program
- Buka program dalam browser
- Interface akan menampilkan form input

### 2. Input
- **Format Input**: Bilangan bulat dipisahkan dengan koma
- **Contoh**: 4, 1, 13, 7, 0, 2, 8, 11, 3
- Masukkan urutan bilangan pada kotak input
- Klik tombol "Cari LMIS"

### 3. Output
Program akan menampilkan:
- **Urutan Input**: Array bilangan yang dimasukkan
- **LMIS**: Subsequence terpanjang yang monoton naik
- **Panjang LMIS**: Jumlah elemen dalam LMIS
- **Array DP**: Visualisasi panjang LMIS di setiap posisi
- **Semua Solusi**: Jika ada lebih dari satu LMIS dengan panjang maksimal

## Contoh

### Input:
```
4, 1, 13, 7, 0, 2, 8, 11, 3
```

### Output:
```
Urutan Input: [4, 1, 13, 7, 0, 2, 8, 11, 3]
LMIS: [1, 2, 8, 11]
Panjang: 4
```

### Penjelasan:
Dari urutan tersebut, subsequence [1, 2, 8, 11] adalah yang terpanjang dimana:
- 1 < 2 < 8 < 11 (monoton naik)
- Tidak ada subsequence lain yang lebih panjang dari 4 elemen

## Algoritma
- **Metode**: Dynamic Programming
- **Time Complexity**: O(n²)
- **Space Complexity**: O(n)

## Struktur Data
- **dp[i]**: Menyimpan panjang LMIS yang berakhir di index i
- **parent[i]**: Menyimpan index elemen sebelumnya untuk rekonstruksi

## Aplikasi
Program ini berguna untuk:
- Analisis data sekuensial
- Optimasi urutan
- Pemecahan masalah teori graf
- Studi kasus algoritma Dynamic Programming
