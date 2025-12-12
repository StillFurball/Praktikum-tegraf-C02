class Node:
    def __init__(self, value, level=0):
        self.value = value
        self.level = level
        self.children = []
        self.path = [value]
    
    def add_child(self, child_node):
        self.children.append(child_node)

def build_tree(sequence):
    """
    Membangun tree untuk menemukan Largest Monotonically Increasing Subsequence
    """
    if not sequence:
        return None
    
    # Root node (kosong, level 0)
    root = Node(None, 0)
    root.path = []
    
    # Queue untuk BFS: (current_node, index_in_sequence)
    queue = [(root, 0)]
    
    while queue:
        current_node, seq_index = queue.pop(0)
        
        # Jika sudah mencapai akhir sequence
        if seq_index >= len(sequence):
            continue
        
        current_value = sequence[seq_index]
        
        # Cek apakah bisa menambahkan nilai ini ke path
        # (nilai harus lebih besar dari nilai terakhir di path)
        if current_node.value is None or current_value > current_node.value:
            # Buat child node dengan nilai ini
            child_node = Node(current_value, current_node.level + 1)
            child_node.path = current_node.path + [current_value]
            current_node.add_child(child_node)
            
            # Lanjutkan eksplorasi dari child ini
            queue.append((child_node, seq_index + 1))
        
        # Selalu coba skip elemen ini (tidak dimasukkan ke subsequence)
        queue.append((current_node, seq_index + 1))
    
    return root

def find_all_paths(node, all_paths):
    """
    Mencari semua path dari root ke leaf
    """
    if not node.children:  # Leaf node
        if node.path:  # Hanya tambahkan jika path tidak kosong
            all_paths.append(node.path)
        return
    
    for child in node.children:
        find_all_paths(child, all_paths)

def find_lmis(sequence):
    """
    Menemukan Largest Monotonically Increasing Subsequence
    """
    # Build tree
    root = build_tree(sequence)
    
    # Temukan semua path
    all_paths = []
    find_all_paths(root, all_paths)
    
    # Temukan path terpanjang
    if not all_paths:
        return []
    
    max_length = max(len(path) for path in all_paths)
    longest_paths = [path for path in all_paths if len(path) == max_length]
    
    return longest_paths

def print_tree(node, prefix="", is_last=True):
    """
    Mencetak tree structure
    """
    if node.value is not None:
        connector = "└── " if is_last else "├── "
        print(prefix + connector + str(node.value))
        prefix += "    " if is_last else "│   "
    else:
        print("Root")
    
    for i, child in enumerate(node.children):
        print_tree(child, prefix, i == len(node.children) - 1)

def main():
    print("=" * 60)
    print("LARGEST MONOTONICALLY INCREASING SUBSEQUENCE SOLVER")
    print("=" * 60)
    print()
    
    # Input dari user
    print("Masukkan urutan bilangan (pisahkan dengan spasi atau koma):")
    user_input = input("> ")
    
    # Parse input
    sequence = []
    try:
        # Coba parse dengan koma atau spasi
        if ',' in user_input:
            sequence = [int(x.strip()) for x in user_input.split(',')]
        else:
            sequence = [int(x.strip()) for x in user_input.split()]
    except ValueError:
        print("Error: Input tidak valid. Masukkan angka yang dipisahkan spasi atau koma.")
        return
    
    print(f"\nUrutan bilangan: {sequence}")
    print()
    
    # Cari LMIS
    longest_paths = find_lmis(sequence)
    
    # Tampilkan hasil
    print("=" * 60)
    print("HASIL:")
    print("=" * 60)
    
    if not longest_paths:
        print("Tidak ada subsequence yang meningkat secara monoton.")
    else:
        print(f"Panjang subsequence terpanjang: {len(longest_paths[0])}")
        print(f"\nJumlah solusi yang ditemukan: {len(longest_paths)}")
        print()
        
        for i, path in enumerate(longest_paths, 1):
            print(f"Solusi {i}: {path}")
    
    print()
    print("=" * 60)
    
    # Optional: tampilkan tree
    show_tree = input("\nTampilkan struktur tree? (y/n): ").lower()
    if show_tree == 'y':
        print("\nStruktur Tree:")
        print("-" * 60)
        root = build_tree(sequence)
        print_tree(root)

if __name__ == "__main__":
    main()
