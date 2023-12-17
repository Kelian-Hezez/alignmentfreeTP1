from loading import load_directory
from kmers import stream_kmers, kmer2str
from sampling import sample



def jaccard(fileA,fileB,k,s):

    heapA=sample(fileA,k,s)
    heapB=sample(fileB,k,s)

    taille_I = 0  
    taille_U = 0  

    a=0
    b=0
    lA=len(heapA)
    lB=len(heapB)
    while a<lA and b<lB:
        print(a,b)
        if heapA[a]==heapB[b]:
            taille_I+=1
            taille_U+=1
            a+=1
            b+=1
        else:
            taille_U+=1
            if heapA[a]<heapB[b]:
                a+=1
            else:
                b+=1
    taille_U+=lB-b
    taille_U+=lA-a
    
    return taille_I/taille_U





if __name__ == "__main__":
    # Load all the files in a dictionary
    files = load_directory("data")
    k = 21
    s = 60
    
    filenames = list(files.keys())
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            print(filenames[i],filenames[j])
            J = jaccard(files[filenames[i]], files[filenames[j]], k, s)
            print(filenames[i], filenames[j], J)
