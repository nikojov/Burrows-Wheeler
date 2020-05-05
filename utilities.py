from Bio import SeqIO
import burrows_wheeler as bw


def search_fasta_file(file,pattern,p,q,N):
    '''
    This function search for a pattern in fasta input file, N serves as upper bound for
    size of text that is being searched for at once, because this algorithm uses
    O(n^2) space.
    :param file:  fasta file in which we search for pattern
    :param pattern: pattern that is searched
    :param p: tally factor for algorithm
    :param q: suffix array factor for algorithm
    :param N: the upper limit for chunk of string that is searched at once
    :return: list of list of pattern positions , in all reads in a input file
    '''
    positions_list=[]
    for record in SeqIO.parse(file, "fasta"):
        text=str(record.seq).replace("\n","")

        if len(text) < N:
            positions_list.append(bw.burrows_wheeler(text,pattern,(p,q)))
        else:
            positions_list.append(search_large_text(text,pattern,p,q,N))
    return positions_list


def search_large_text(text,pattern,p,q,N):
    '''
    This is just a wrapper for burrows-wheeler algorithm, it uses upper bound for size of text
    that is searched at once because burrows-wheleer has O(n^2) space consumption.
    :param text: input text
    :param pattern: pattern that is searched
    :param p: tally matrix factor
    :param q: suffix array factor
    :param N:  the upper limit for chunk of string that is searched at once
    :return: list of positions of pattern in text
    '''
    pattern_len=len(pattern)
    text_len=len(text)
    positions=[]
    begin_index=0
    end_index=N
    while end_index < text_len:
        positions.extend(bw.burrows_wheeler(text[begin_index:end_index],pattern,(p,q)))
        begin_index=end_index-pattern_len+1
        end_index=begin_index+N


    if begin_index < text_len and (text_len-begin_index) > pattern_len:
        positions.extend(bw.burrows_wheeler(text[begin_index:],pattern,(p,q)))

    return positions


