# Largest Monotonically Increasing Subsequence (LMIS) Solver

## Deskripsi
Program ini menyelesaikan permasalahan mencari **Largest Monotonically Increasing Subsequence** dari sebuah urutan bilangan menggunakan pendekatan tree.

---

## Pengertian LMIS

### Apa itu LMIS?

**Subsequence** = ambil beberapa angka dari urutan asli, **TANPA mengubah urutannya**

**Monotonically Increasing** = setiap angka harus **lebih besar** dari angka sebelumnya

**Largest** = cari yang **paling panjang**

### Contoh Sederhana

Urutan: **[4, 1, 13, 7, 0, 2, 8, 11, 3]**

**Subsequence yang valid:**
- [1, 7, 8, 11] ✓ (panjang 4) → 1 < 7 < 8 < 11
- [1, 2, 8, 11] ✓ (panjang 4) → 1 < 2 < 8 < 11
- [4, 13] ✓ (panjang 2) → 4 < 13
- [0, 2, 3] ✓ (panjang 3) → 0 < 2 < 3

**Subsequence yang TIDAK valid:**
- [4, 1, 13] ✗ → karena 4 > 1 (turun!)
- [13, 7, 8] ✗ → karena 13 > 7 (turun!)

**Jawaban:** [1, 7, 8, 11] atau [1, 2, 8, 11] → panjang **4** (yang terpanjang)

---

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

---

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

Jumlah solusi yang ditemukan: 3

Solusi 1: [1, 7, 8, 11]
Solusi 2: [1, 2, 8, 11]
Solusi 3: [0, 2, 8, 11]

============================================================
```

---

## Penjelasan Algoritma

### Mengapa Menggunakan Tree?

Tree digunakan sebagai **pohon keputusan** untuk mengeksplorasi semua kemungkinan subsequence. Setiap kali bertemu angka baru, ada **2 pilihan**:

1. **Ambil angka** (jika lebih besar dari angka terakhir di path)
2. **Skip angka** (lewati angka tersebut)

### Visualisasi Tree

```
Urutan: [4, 1, 13, 7, 0, 2, 8, 11, 3]

Root (kosong)
├─ Ambil 4 → [4]
│  ├─ Skip 1 → [4]
│  ├─ Ambil 13 → [4, 13] ← panjang 2
│  └─ ...
│
└─ Skip 4 → []
   ├─ Ambil 1 → [1]
   │  ├─ Ambil 7 → [1, 7]
   │  │  ├─ Ambil 8 → [1, 7, 8]
   │  │  │  └─ Ambil 11 → [1, 7, 8, 11] ← panjang 4! ✓
   │  │  └─ ...
   │  └─ ...
   └─ ...
```

### Langkah-langkah Algoritma

1. **Build Tree**: Membangun tree dengan mengeksplorasi semua kemungkinan
   - Mulai dari root (kosong)
   - Untuk setiap angka: ambil atau skip
   - Pastikan monotonically increasing

2. **Eksplorasi**: Menggunakan BFS (Breadth-First Search)
   - Queue untuk menyimpan node yang akan dieksplorasi
   - Setiap node punya 2 cabang (ambil/skip)

3. **Pencarian Path**: Mencari semua path dari root ke leaf
   - Leaf = node tanpa anak (ujung tree)
   - Setiap path = satu subsequence

4. **Hasil**: Memilih path dengan panjang maksimal
   - Cari panjang terbesar
   - Ambil semua path yang panjangnya maksimal

---

## Penjelasan Kode

### 1. Class Node
```python
class Node:
    def __init__(self, value, level=0):
        self.value = value          # Angka di node ini
        self.level = level          # Kedalaman di tree
        self.children = []          # Cabang/anak dari node
        self.path = [value]         # Jejak dari root ke node ini
```

**Fungsi:** Merepresentasikan setiap titik dalam tree
- `value`: Angka yang disimpan
- `level`: Kedalaman node (root=0, anak=1, dst)
- `children`: Daftar node anak
- `path`: Urutan angka dari awal sampai node ini

### 2. Function build_tree()
```python
def build_tree(sequence):
    root = Node(None, 0)  # Buat root kosong
    queue = [(root, 0)]   # Antrian eksplorasi
    
    while queue:
        current_node, seq_index = queue.pop(0)
        current_value = sequence[seq_index]
        
        # PILIHAN 1: Ambil angka (jika > nilai terakhir)
        if current_node.value is None or current_value > current_node.value:
            child_node = Node(current_value, current_node.level + 1)
            child_node.path = current_node.path + [current_value]
            current_node.add_child(child_node)
            queue.append((child_node, seq_index + 1))
        
        # PILIHAN 2: Skip angka
        queue.append((current_node, seq_index + 1))
```

**Fungsi:** Membangun tree dengan mengeksplorasi semua kemungkinan
- Gunakan **BFS** (antrian/queue)
- Setiap angka punya 2 pilihan: ambil atau skip
- Ambil hanya jika lebih besar dari angka terakhir

### 3. Function find_all_paths()
```python
def find_all_paths(node, all_paths):
    if not node.children:  # Jika leaf (ujung)
        if node.path:
            all_paths.append(node.path)
        return
    
    for child in node.children:
        find_all_paths(child, all_paths)  # Rekursif
```

**Fungsi:** Mencari semua jalur dari root ke leaf
- Gunakan **rekursif**
- Simpan path jika sudah sampai leaf
- Terus eksplorasi sampai ujung tree

### 4. Function find_lmis()
```python
def find_lmis(sequence):
    root = build_tree(sequence)           # Bangun tree
    all_paths = []
    find_all_paths(root, all_paths)       # Kumpulkan semua path
    
    max_length = max(len(path) for path in all_paths)
    longest_paths = [path for path in all_paths 
                     if len(path) == max_length]
    
    return longest_paths
```

**Fungsi:** Mencari subsequence terpanjang
- Bangun tree
- Kumpulkan semua path
- Filter hanya yang paling panjang

### 5. Function main()
```python
def main():
    # Input dari user
    user_input = input("> ")
    
    # Parse input (pisahkan dengan koma/spasi)
    if ',' in user_input:
        sequence = [int(x.strip()) for x in user_input.split(',')]
    else:
        sequence = [int(x.strip()) for x in user_input.split()]
    
    # Cari LMIS
    longest_paths = find_lmis(sequence)
    
    # Tampilkan hasil
    for path in longest_paths:
        print(f"Solusi: {path}")
```

**Fungsi:** Program utama
- Terima input dari user
- Parse input menjadi list integer
- Panggil find_lmis()
- Tampilkan semua solusi

---

## Kompleksitas

- **Time Complexity**: O(2^n) - karena setiap elemen punya 2 pilihan (ambil/skip)
- **Space Complexity**: O(n) - untuk menyimpan path dan queue

---

## Catatan Penting

- Subsequence harus **monotonically increasing** (setiap elemen lebih besar dari sebelumnya)
- Bukan **strictly increasing**, jadi tidak boleh ada elemen yang sama atau lebih kecil
- Program menemukan **semua** solusi yang memiliki panjang maksimal
- Tree memvisualisasikan semua kemungkinan eksplorasi
