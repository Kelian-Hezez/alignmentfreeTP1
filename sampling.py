import heapq as hp
from kmers import stream_kmers


def xorshift(state):
    x = state[0]
    x ^= x << 13
    x ^= x >> 7
    x ^= x << 17
    state[0] = x
    return x

def sample(f, k, s):
    sketch = [-float('inf')]*s
    hp.heapify(sketch)
    state=[123456789]
    for kmer in stream_kmers(f, k):
        #kmer=xorshift(state)^kmer
        if -kmer>sketch[0]:
            hp.heappushpop(sketch,-kmer)
    return sketch
