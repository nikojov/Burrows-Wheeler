from unittest import TestCase
import burrows_wheeler

'''
This module contains unit tests for all functions in burrows-wheeler module
'''

def test_calc_char_app():
    text1 = "abcabcabcabc"
    text2 = "abaaba"
    text3 = "agctgcga"
    apps1 = {'a': 4, 'b': 4, 'c': 4}
    apps2 = {'a': 4, 'b': 2}
    apps3 = {'a': 2, 'g': 3, 'c': 2, 't': 1}
    assert burrows_wheeler.calc_char_app(text1) == apps1
    assert burrows_wheeler.calc_char_app(text2) == apps2
    assert burrows_wheeler.calc_char_app(text3) == apps3

def test_create_perm_matrix():
    text1 = "abcabcabcabc"
    text2 = "abaaba"
    text3 = "agctgcga"

    matrix1 = ['$', 'abc$', 'abcabc$', 'abcabcabc$', 'abcabcabcabc$', 'bc$',
           'bcabc$', 'bcabcabc$', 'bcabcabcabc$', 'c$', 'cabc$', 'cabcabc$',
           'cabcabcabc$']
    matrix2 = ['$', 'a$', 'aaba$', 'aba$', 'abaaba$', 'ba$', 'baaba$']
    matrix3 = ['$', 'a$', 'agctgcga$', 'cga$', 'ctgcga$', 'ga$', 'gcga$', 'gctgcga$',
               'tgcga$']

    assert burrows_wheeler.create_perm_matrix(text1) == matrix1
    assert burrows_wheeler.create_perm_matrix(text2) == matrix2
    assert burrows_wheeler.create_perm_matrix(text3) == matrix3

def test_get_first_column():
    matrix1 = ['$', 'abc$', 'abcabc$', 'abcabcabc$', 'abcabcabcabc$', 'bc$',
               'bcabc$', 'bcabcabc$', 'bcabcabcabc$', 'c$', 'cabc$', 'cabcabc$',
               'cabcabcabc$']
    matrix2 = ['$', 'a$', 'aaba$', 'aba$', 'abaaba$', 'ba$', 'baaba$']
    matrix3 = ['$', 'a$', 'agctgcga$', 'cga$', 'ctgcga$', 'ga$', 'gcga$', 'gctgcga$',
           'tgcga$']
    first1 = "$aaaabbbbcccc"
    first2 = "$aaaabb"
    first3 = "$aaccgggt"




    assert first1 == burrows_wheeler.get_first_column(matrix1)
    assert first2 == burrows_wheeler.get_first_column(matrix2)
    assert first3 == burrows_wheeler.get_first_column(matrix3)

def test_get_last_column():
    matrix1 = ['$', 'abc$', 'abcabc$', 'abcabcabc$', 'abcabcabcabc$', 'bc$',
               'bcabc$', 'bcabcabc$', 'bcabcabcabc$', 'c$', 'cabc$', 'cabcabc$',
               'cabcabcabc$']
    matrix2 = ['$', 'a$', 'aaba$', 'aba$', 'abaaba$', 'ba$', 'baaba$']
    matrix3 = ['$', 'a$', 'agctgcga$', 'cga$', 'ctgcga$', 'ga$', 'gcga$', 'gctgcga$',
               'tgcga$']
    text1 = "abcabcabcabc"
    text2 = "abaaba"
    text3 = "agctgcga"


    last1 = "cccc$aaaabbbb"
    last2 = "abba$aa"
    last3 = "ag$ggctac"
    assert last1 == burrows_wheeler.get_last_column(matrix1,text1)
    assert last2 == burrows_wheeler.get_last_column(matrix2,text2)
    assert last3 == burrows_wheeler.get_last_column(matrix3,text3)

def test_create_tally():
    last1 = "cccc$aaaabbbb"
    last2 = "abba$aa"
    last3 = "ag$ggctac"
    apps1 = {'a': 4, 'b': 4, 'c': 4}
    apps2 = {'a': 4, 'b': 2}
    apps3 = {'a': 2, 'g': 3, 'c': 2, 't': 1}
    keys1 = list(apps1.keys())
    keys1.sort()

    keys2 = list(apps2.keys())
    keys2.sort()

    keys3 = list(apps3.keys())
    keys3.sort()
    tally1 = {'c': [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 'a': [0, 0, 0, 0, 0, 1, 2, 3, 4, 4, 4, 4, 4],
              'b': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4]}

    tally1_2 = {'c': [1, 3, 4, 4, 4, 4, 4], 'a': [0, 0, 0, 2, 4, 4, 4], 'b': [0, 0, 0, 0, 0, 2, 4]}
    tally1_4 = {'c': [1, 4, 4, 4], 'a': [0, 0, 4, 4], 'b': [0, 0, 0, 4]}
    tally2 = {'a': [1, 1, 1, 2, 2, 3, 4], 'b': [0, 1, 2, 2, 2, 2, 2]}
    tally2_2 = {'a': [1, 1, 2, 4], 'b': [0, 2, 2, 2]}
    tally2_4 = {'a': [1, 2], 'b': [0, 2]}
    tally3 = {'a': [1, 1, 1, 1, 1, 1, 1, 2, 2], 'g': [0, 1, 1, 2, 3, 3, 3, 3, 3], 'c': [0, 0, 0, 0, 0, 1, 1, 1, 2],
              't': [0, 0, 0, 0, 0, 0, 1, 1, 1]}
    tally3_2 = {'a': [1, 1, 1, 1, 2], 'g': [0, 1, 3, 3, 3], 'c': [0, 0, 0, 1, 2], 't': [0, 0, 0, 1, 1]}
    tally3_4 = {'a': [1, 1, 2], 'g': [0, 3, 3], 'c': [0, 0, 2], 't': [0, 0, 1]}
    assert tally1_2 == burrows_wheeler.create_tally(last1, keys1, 2)
    assert tally1_4 == burrows_wheeler.create_tally(last1, keys1, 4)

    assert tally2_2 == burrows_wheeler.create_tally(last2, keys2, 2)
    assert tally2_4 == burrows_wheeler.create_tally(last2, keys2, 4)

    assert tally3_2 == burrows_wheeler.create_tally(last3, keys3, 2)
    assert tally3_4 == burrows_wheeler.create_tally(last3, keys3, 4)



def test_create_suf_array():
    text1 = "abcabcabcabc"
    text2 = "abaaba"
    text3 = "agctgcga"
    matrix1 = ['$', 'abc$', 'abcabc$', 'abcabcabc$', 'abcabcabcabc$', 'bc$',
               'bcabc$', 'bcabcabc$', 'bcabcabcabc$', 'c$', 'cabc$', 'cabcabc$',
               'cabcabcabc$']
    matrix2 = ['$', 'a$', 'aaba$', 'aba$', 'abaaba$', 'ba$', 'baaba$']
    matrix3 = ['$', 'a$', 'agctgcga$', 'cga$', 'ctgcga$', 'ga$', 'gcga$', 'gctgcga$',
               'tgcga$']
    suf1 = [12, 9, 6, 3, 0, 10, 7, 4, 1, 11, 8, 5, 2]
    suf1_2 = [12, 6, 0, 7, 1, 8, 2]
    suf1_4 = [12, 0, 1, 2]

    suf2 = [6, 5, 2, 3, 0, 4, 1]
    suf2_2 = [6, 2, 0, 1]
    suf2_4 = [6, 0]

    suf3 = [8, 7, 0, 5, 2, 6, 4, 1, 3]
    suf3_2 = [8, 0, 2, 4, 3]
    suf3_4 = [8, 2, 3]
    assert suf1 == burrows_wheeler.create_suf_array(matrix1, 1)
    assert suf1_2 == burrows_wheeler.create_suf_array(matrix1, 2)
    assert suf1_4 == burrows_wheeler.create_suf_array(matrix1, 4)

    assert suf2 == burrows_wheeler.create_suf_array(matrix2,1)
    assert suf2_2 == burrows_wheeler.create_suf_array(matrix2, 2)
    assert suf2_4 == burrows_wheeler.create_suf_array(matrix2, 4)

    assert suf3 == burrows_wheeler.create_suf_array(matrix3, 1)
    assert suf3_2 == burrows_wheeler.create_suf_array(matrix3, 2)
    assert suf3_4 == burrows_wheeler.create_suf_array(matrix3, 4)

def test_get_positions():
    first1 = "$aaaabbbbcccc"
    first2 = "$aaaabb"
    first3 = "$aaccgggt"
    last1 = "cccc$aaaabbbb"
    last2 = "abba$aa"
    last3 = "ag$ggctac"
    apps1 = {'a': 4, 'b': 4, 'c': 4}
    apps2 = {'a': 4, 'b': 2}
    apps3 = {'a': 2, 'g': 3, 'c': 2, 't': 1}
    keys1 = list(apps1.keys())
    keys1.sort()

    keys2 = list(apps2.keys())
    keys2.sort()

    keys3 = list(apps3.keys())
    keys3.sort()
    tally1 = {'c': [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 'a': [0, 0, 0, 0, 0, 1, 2, 3, 4, 4, 4, 4, 4],
              'b': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4]}

    tally1_2 = {'c': [1, 3, 4, 4, 4, 4, 4], 'a': [0, 0, 0, 2, 4, 4, 4], 'b': [0, 0, 0, 0, 0, 2, 4]}
    tally1_4 = {'c': [1, 4, 4, 4], 'a': [0, 0, 4, 4], 'b': [0, 0, 0, 4]}
    tally2 = {'a': [1, 1, 1, 2, 2, 3, 4], 'b': [0, 1, 2, 2, 2, 2, 2]}
    tally2_2 = {'a': [1, 1, 2, 4], 'b': [0, 2, 2, 2]}
    tally2_4 = {'a': [1, 2], 'b': [0, 2]}
    tally3 = {'a': [1, 1, 1, 1, 1, 1, 1, 2, 2], 'g': [0, 1, 1, 2, 3, 3, 3, 3, 3], 'c': [0, 0, 0, 0, 0, 1, 1, 1, 2],
              't': [0, 0, 0, 0, 0, 0, 1, 1, 1]}
    tally3_2 = {'a': [1, 1, 1, 1, 2], 'g': [0, 1, 3, 3, 3], 'c': [0, 0, 0, 1, 2], 't': [0, 0, 0, 1, 1]}
    tally3_4 = {'a': [1, 1, 2], 'g': [0, 3, 3], 'c': [0, 0, 2], 't': [0, 0, 1]}
    suf1 = [12, 9, 6, 3, 0, 10, 7, 4, 1, 11, 8, 5, 2]
    suf1_2 = [12, 6, 0, 7, 1, 8, 2]
    suf1_4 = [12, 0, 1, 2]

    suf2 = [6, 5, 2, 3, 0, 4, 1]
    suf2_2 = [6, 2, 0, 1]
    suf2_4 = [6, 0]

    suf3 = [8, 7, 0, 5, 2, 6, 4, 1, 3]
    suf3_2 = [8, 0, 2, 4, 3]
    suf3_4 = [8, 2, 3]
    par_p = [1,2,4]
    par_q=[1,2,4]

    tallies = [[tally1, tally1_2, tally1_4], [tally2, tally2_2, tally2_4], [tally3, tally3_2, tally3_4]]

    sufs = [[suf1, suf1_2, suf1_4], [suf2, suf2_2, suf2_4], [suf3, suf3_2, suf3_4]]
    for p,tally in enumerate(tallies[0]):
        for q, suf in enumerate(sufs[0]):
            assert burrows_wheeler.get_positons(keys1, apps1, tally, first1, last1, [1, 2, 3], suf, par_p[p], par_q[q]) == [9, 6, 3]



    for p,tally in enumerate(tallies[1]):
        for q, suf in enumerate(sufs[1]):
            assert burrows_wheeler.get_positons(keys2, apps2, tally, first2, last2, [1, 5, 6], suf, par_p[p], par_q[q]) == [5, 4, 1]


    for p,tally in enumerate(tallies[2]):
        for q, suf in enumerate(sufs[2]):
            assert burrows_wheeler.get_positons(keys3, apps3, tally, first3, last3, [2, 0, 6], suf, par_p[p], par_q[q]) == [0, 8, 4]

def test_get_from_last_to_first():
    first1 = "$aaaabbbbcccc"
    first2 = "$aaaabb"
    first3 = "$aaccgggt"

    last1 = "cccc$aaaabbbb"
    last2 = "abba$aa"
    last3 = "ag$ggctac"
    apps1 = {'a': 4, 'b': 4, 'c': 4}
    apps2 = {'a': 4, 'b': 2}
    apps3 = {'a': 2, 'g': 3, 'c': 2, 't': 1}
    keys1 = list(apps1.keys())
    keys1.sort()

    keys2 = list(apps2.keys())
    keys2.sort()

    keys3 = list(apps3.keys())
    keys3.sort()
    tally1 = {'c': [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 'a': [0, 0, 0, 0, 0, 1, 2, 3, 4, 4, 4, 4, 4],
              'b': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4]}

    tally1_2 = {'c': [1, 3, 4, 4, 4, 4, 4], 'a': [0, 0, 0, 2, 4, 4, 4], 'b': [0, 0, 0, 0, 0, 2, 4]}
    tally1_4 = {'c': [1, 4, 4, 4], 'a': [0, 0, 4, 4], 'b': [0, 0, 0, 4]}
    tally2 = {'a': [1, 1, 1, 2, 2, 3, 4], 'b': [0, 1, 2, 2, 2, 2, 2]}
    tally2_2 = {'a': [1, 1, 2, 4], 'b': [0, 2, 2, 2]}
    tally2_4 = {'a': [1, 2], 'b': [0, 2]}
    tally3 = {'a': [1, 1, 1, 1, 1, 1, 1, 2, 2], 'g': [0, 1, 1, 2, 3, 3, 3, 3, 3], 'c': [0, 0, 0, 0, 0, 1, 1, 1, 2],
              't': [0, 0, 0, 0, 0, 0, 1, 1, 1]}
    tally3_2 = {'a': [1, 1, 1, 1, 2], 'g': [0, 1, 3, 3, 3], 'c': [0, 0, 0, 1, 2], 't': [0, 0, 0, 1, 1]}
    tally3_4 = {'a': [1, 1, 2], 'g': [0, 3, 3], 'c': [0, 0, 2], 't': [0, 0, 1]}

    par_p = [1,2,4]


    tallies = [[tally1, tally1_2, tally1_4], [tally2, tally2_2, tally2_4], [tally3, tally3_2, tally3_4]]
    front_num=[11,1,3]
    for front_index, index in enumerate([2,5,7]):
        for p, tally in enumerate(tallies[0]):
            assert burrows_wheeler.get_from_last_to_first(index, keys1, apps1, tally, first1, last1, par_p[p]) == front_num[front_index]


    front_num=[6,3,4]
    for front_index, index in enumerate([2,5,6]):
        for p, tally in enumerate(tallies[1]):
            assert burrows_wheeler.get_from_last_to_first(index, keys2, apps2, tally, first2, last2, par_p[p]) == front_num[front_index]



    front_num=[6,3,4]
    for front_index, index in enumerate([3,5,8]):
        for p, tally in enumerate(tallies[2]):
            assert burrows_wheeler.get_from_last_to_first(index, keys3, apps3, tally, first3, last3, par_p[p]) == front_num[front_index]



def test_search_for_pattern():
    first1 = "$aaaabbbbcccc"
    first2 = "$aaaabb"
    first3 = "$aaccgggt"

    last1 = "cccc$aaaabbbb"
    last2 = "abba$aa"
    last3 = "ag$ggctac"
    apps1 = {'a': 4, 'b': 4, 'c': 4}
    apps2 = {'a': 4, 'b': 2}
    apps3 = {'a': 2, 'g': 3, 'c': 2, 't': 1}
    keys1 = list(apps1.keys())
    keys1.sort()

    keys2 = list(apps2.keys())
    keys2.sort()

    keys3 = list(apps3.keys())
    keys3.sort()
    tally1 = {'c': [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 'a': [0, 0, 0, 0, 0, 1, 2, 3, 4, 4, 4, 4, 4],
              'b': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4]}

    tally1_2 = {'c': [1, 3, 4, 4, 4, 4, 4], 'a': [0, 0, 0, 2, 4, 4, 4], 'b': [0, 0, 0, 0, 0, 2, 4]}
    tally1_4 = {'c': [1, 4, 4, 4], 'a': [0, 0, 4, 4], 'b': [0, 0, 0, 4]}
    tally2 = {'a': [1, 1, 1, 2, 2, 3, 4], 'b': [0, 1, 2, 2, 2, 2, 2]}
    tally2_2 = {'a': [1, 1, 2, 4], 'b': [0, 2, 2, 2]}
    tally2_4 = {'a': [1, 2], 'b': [0, 2]}
    tally3 = {'a': [1, 1, 1, 1, 1, 1, 1, 2, 2], 'g': [0, 1, 1, 2, 3, 3, 3, 3, 3], 'c': [0, 0, 0, 0, 0, 1, 1, 1, 2],
              't': [0, 0, 0, 0, 0, 0, 1, 1, 1]}
    tally3_2 = {'a': [1, 1, 1, 1, 2], 'g': [0, 1, 3, 3, 3], 'c': [0, 0, 0, 1, 2], 't': [0, 0, 0, 1, 1]}
    tally3_4 = {'a': [1, 1, 2], 'g': [0, 3, 3], 'c': [0, 0, 2], 't': [0, 0, 1]}

    par_p = [1,2,4]


    tallies = [[tally1, tally1_2, tally1_4], [tally2, tally2_2, tally2_4], [tally3, tally3_2, tally3_4]]

    pattern_ranges=[[],list(range(1,5)),list(range(5,9))]
    patterns=['abcgd','abc','b']
    for index, pattern in enumerate(patterns):
        for p,tally in enumerate(tallies[0]):
            assert burrows_wheeler.search_for_pattern(patterns[index], first1, last1, keys1, apps1, tally, par_p[p]) == pattern_ranges[index]




    pattern_ranges=[[],list(range(3,5)),list(range(2,3))]
    patterns=['abcgd','aba','aa']
    for index, pattern in enumerate(patterns):
        for p,tally in enumerate(tallies[1]):
            assert burrows_wheeler.search_for_pattern(patterns[index], first2, last2, keys2, apps2, tally, par_p[p]) == pattern_ranges[index]


    pattern_ranges=[[],list(range(2,3)),list(range(6,8))]
    patterns=['abcgd','ag','gc']
    for index, pattern in enumerate(patterns):
        for p,tally in enumerate(tallies[2]):
            assert burrows_wheeler.search_for_pattern(patterns[index], first3, last3, keys3, apps3, tally, par_p[p]) == pattern_ranges[index]


def test_burrows_wheeler():
    test_list = [0,3]
    for i in range(1, 100):
        for j in range(1, 100):
            assert test_list == burrows_wheeler.burrows_wheeler("AbaAba", "ABA", (i, j))





def test_all():
    '''
    This function is called when this module is run. It runs all of unit tests.
    :return: None
    '''
    test_create_perm_matrix()
    test_create_suf_array()
    test_calc_char_app()
    test_get_first_column()
    test_get_last_column()
    test_get_from_last_to_first()
    test_create_tally()
    test_get_positions()
    test_search_for_pattern()
    test_burrows_wheeler()


if __name__ == "__main__":
    from importlib import  reload
    reload(burrows_wheeler)
    test_all()