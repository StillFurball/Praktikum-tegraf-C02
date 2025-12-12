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

# Largest Monotonically Increasing Subsequence (LMIS) Solver

## Deskripsi
Program ini menyelesaikan permasalahan mencari **Largest Monotonically Increasing Subsequence** dari sebuah urutan bilangan menggunakan pendekatan tree.<br><br>
# Apa itu Largest Monotonically Increasing Subsequence (LMIS)?<br>
Largest Monotonically Increasing Subsequence (LMIS) adalah subsequence terpanjang yang dapat diambil dari suatu urutan bilangan tanpa mengubah urutannya, di mana setiap elemen dalam subsequence tersebut harus bernilai lebih besar daripada elemen sebelumnya sehingga membentuk urutan yang naik secara monoton.<br><br>
Subsequence = ambil beberapa angka dari urutan asli, TANPA mengubah urutannya<br>
Monotonically Increasing = setiap angka harus lebih besar dari angka sebelumnya<br>
Largest = cari yang paling panjang

## Cara Penggunaan

### 1. Menjalankan Program
```bash
python lmis.py
```

### 2. Input
- Program akan meminta input berupa urutan bilangan
- Bilangan dapat dipisahkan dengan **spasi** atau **koma**
- Contoh input yang valid:
  ```
  4, 1, 13, 7, 0, 2, 8, 11, 3
  ```
  atau
  ```
  4 1 13 7 0 2 8 11 3
  ```

### 3. Output
Program akan menampilkan:
- Urutan bilangan yang diinput
- Panjang subsequence terpanjang yang ditemukan
- Jumlah solusi yang ditemukan
- Semua solusi LMIS yang memiliki panjang maksimal

### 4. Opsi Tambahan
- Setelah hasil ditampilkan, program menawarkan untuk menampilkan struktur tree
- Ketik `y` untuk melihat struktur tree, atau `n` untuk skip

## Contoh Penggunaan

### Input:
```
4, 1, 13, 7, 0, 2, 8, 11, 3
```

### Output:
```
============================================================
LARGEST MONOTONICALLY INCREASING SUBSEQUENCE SOLVER
============================================================

Masukkan urutan bilangan (pisahkan dengan spasi atau koma):
> 4, 1, 13, 7, 0, 2, 8, 11, 3

Urutan bilangan: [4, 1, 13, 7, 0, 2, 8, 11, 3]

============================================================
HASIL:
============================================================
Panjang subsequence terpanjang: 4

Jumlah solusi yang ditemukan: 4

Solusi 1: [4, 7, 8, 11]
Solusi 2: [1, 7, 8, 11]
Solusi 3: [1, 2, 8, 11]
Solusi 4: [0, 2, 8, 11]

============================================================
```

## Penjelasan Algoritma

1. **Build Tree**: Program membangun tree di mana setiap node merepresentasikan elemen dalam subsequence
2. **Eksplorasi**: Untuk setiap elemen, ada 2 pilihan:
   - Masukkan ke subsequence (jika nilainya lebih besar dari elemen terakhir)
   - Skip elemen tersebut
3. **Pencarian**: Program mencari semua path dari root ke leaf
4. **Hasil**: Path dengan panjang maksimal adalah solusi LMIS

## Catatan
- Subsequence harus **monotonically increasing** (setiap elemen lebih besar dari elemen sebelumnya)
- Bukan strictly increasing, jadi tidak boleh ada elemen yang sama atau lebih kecil
- Program menemukan **semua** solusi yang memiliki panjang maksimal
