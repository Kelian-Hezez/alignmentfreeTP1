
def kmer2str(val, k):
    """ Transform a kmer integer into a its string representation
    :param int val: An integer representation of a kmer
    :param int k: The number of nucleotides involved into the kmer.
    :return str: The kmer string formatted
    """
    letters = ['A', 'C', 'T', 'G']
    str_val = []
    for i in range(k):
        str_val.append(letters[val & 0b11])
        val >>= 2

    str_val.reverse()
    return "".join(str_val)


def stream_kmers(sequences, k):
    letters={'A':0, 'C':1, 'T':2, 'G':3}
    mask=(1<<(2*k))-1
    kmer=0
    kmer_comp=0
    count=1
    for j in range(len(sequences)):
        for i in sequences[j]:
            if i in letters:
                nuc=letters[i]
                comp=nuc+2
                comp&=0b11
                comp<<=(2*k-2)
                kmer<<=2
                kmer_comp>>=2
                kmer+=nuc
                kmer_comp+=comp
                kmer&=mask

            if count<k:
                count+=1
            else:
                yield(min(kmer, kmer_comp))
