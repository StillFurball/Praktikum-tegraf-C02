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
