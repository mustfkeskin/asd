from gensim.models import KeyedVectors

# Load back with memory-mapping = read-only, shared across processes.
wv = KeyedVectors.load("Model/product.vectors", mmap='r')