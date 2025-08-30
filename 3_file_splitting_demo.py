def split_small_file(filename):
    """Load entire file into memory and split"""
    
    with open(filename, 'rb') as f:
        data = f.read()  # Load ALL data into memory
    
    chunk_size = 1024
    chunks = []
    for i in range(0, len(data), chunk_size):
        chunks.append(data[i:i + chunk_size])
    
    print(f"Small file approach: Loaded {len(data)} bytes")
    return chunks

def split_large_file(filename):
    """Stream file chunk by chunk without loading everything"""
    
    chunks = []
    chunk_size = 1024
    
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)  # Read only small chunks
            if not chunk:
                break
            chunks.append(chunk)
    
    print(f"Large file approach: Streamed in {chunk_size} byte chunks")
    return chunks

# Create test files
with open('small_test.txt', 'w') as f:
    f.write('Hello World! ' * 100)  # Small file (~1.3KB)

with open('large_test.txt', 'w') as f:
    f.write('Big Data! ' * 1000000)   # Large file (~10MB)

print("=== DEMO ===")
print("Small file splitting:")
small_chunks = split_small_file('small_test.txt')

print("\nLarge file splitting:")
large_chunks = split_large_file('large_test.txt')

print(f"\nBoth produced {len(small_chunks)} and {len(large_chunks)} chunks")

print("\n=== KEY DIFFERENCES ===")
print("Small file approach:")
print("  • Loads ENTIRE file into memory at once")
print("  • Memory usage = file size")

print("\nLarge file approach:")
print("  • Reads file piece by piece (streaming)")
print("  • Memory usage = constant (chunk size)")