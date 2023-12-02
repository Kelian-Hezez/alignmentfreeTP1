from loading import load_directory
from kmers import stream_kmers, kmer2str



def jaccard(fileA, fileB, k, genomeA):
    dico ={}

    taille_I = 0  
    taille_U = 0  
    for kmer in stream_kmers(fileA,k):   
        dico[kmer] = 1 if kmer not in dico else dico[kmer]+1 
        taille_U+=1
    
    for kmer in stream_kmers(fileB, k):  
        if kmer in dico:             
            taille_I+=1
            dico[kmer] -= 1
            if dico[kmer] ==0:
                del dico[kmer]
        
        else:
            taille_U+=1
    return taille_I/taille_U





if __name__ == "__main__":
    # Load all the files in a dictionary
    files = load_directory("data")
    k = 21
    
    filenames = list(files.keys())
    for i in range(len(files)):
        for j in range(i+1, len(files)):

            J = jaccard(files[filenames[i]], files[filenames[j]], k)
            print(filenames[i], filenames[j], J)
