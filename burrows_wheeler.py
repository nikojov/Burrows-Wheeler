def print_matrix(matrix):
    for row in matrix:
        print(row)


def calc_char_app(text):
    '''
    Calculates  appearances of all chars in string
    :param text:  input String
    :return:  Dictionary, where keys are characters that appear in input text and values are number of their
    appearance
    '''
    hash_table = {}
    for c in text:

        if c not in hash_table:
            hash_table[c] = 1
        else:
            hash_table[c] += 1

    return hash_table


def create_perm_matrix(text):
    '''
    Creates all permutations of input string, puts them in a matrix and than sorts that matrix.
    Each row contains it's permutation, but only up to $ sign that marks the end.
    So this is technically sorted upper triangle matrix of all suffixes of input text.
    It contains all useful info as whole matrix but requires half the space.
    :param text: input string
    :return: sorted matrix
    '''
    iter_range = len(text)

    if iter_range < 1:
        print("Text  must have lenght greater than zero")
        exit(1)

    perm_matrix = []
    text += '$'

    for i in range(len(text)):
        perm_matrix.append(text[i:])

    perm_matrix.sort()
    return perm_matrix


def get_first_column(matrix):
    '''

   :param matrix:
   :return: first column of a input matrix
    '''

    first = []
    for row in matrix:
        c = row[0]
        first.append(c)
    return ''.join(first)


def get_last_column(matrix, text):
    '''

    :param matrix:
    :param text:
    :return: returns last column of matrix
    '''
    last = []
    lenght = len(matrix)
    for row in matrix:
        if lenght == len(row):
            last.append('$')
            continue
        c = text[lenght - len(row) - 1]

        last.append(c)
    return ''.join(last)


def create_tally(last, keys, p):
    '''
    Creates tally matrix, in a form of dictionary.
    For every char that appears in input, it creates list of number  of char appearances,
     up to some index,in last column.
     Tally factor determines what portion of tally is actually stored in tally matrix.
    :param last: last column of matrix
    :param keys: all chars that appear in input text
    :param p: tally factor
    :return: tally matrix
    '''
    max_iterations = (len(last) - 1) // p + 1

    tally = {}
    for key in keys:
        tally[key] = []

    for index, c in enumerate(last):
        if index == 0:
            for key in keys:
                tally[key].append(0)

        if c != '$':
            tally[c][-1] += 1

        if index % p == 0: # p is used for optimised algorithm, determines when to add new row to tally matrix,
                            # in basic algorithm it is 1
            if len(tally[keys[0]]) >= max_iterations:
                break
            for key in keys:
                tally[key].append(tally[key][-1])

    return tally


def get_from_last_to_first(index, keys, apps, tally, first, last, p):
    '''
    Gets index of char in last column, and returns index of same char in first column
    :param index: index of a char
    :param keys: all chars that appear in input text
    :param apps: appearance dict.
    :param tally: tally matrix
    :param first: first column
    :param last:  last column
    :param p:  tally factor
    :return: position in first column
    '''
    my_key = last[index]
    if my_key == '$':
        return 0
    ord_num = 0
    if index % p == 0:
        ord_num = tally[my_key][index // p]
    else:
        changed_index = index // p
        ord_num = tally[my_key][changed_index]
        for i in range(changed_index * p + 1, index + 1):
            if last[i] == my_key:
                ord_num += 1
    new_index = 0
    for key in keys:
        if key == my_key:
            new_index += ord_num
            break
        else:
            new_index += apps[key]

    return new_index


def create_suf_array(matrix, q):
    '''
    Creates suffix index of input text, suffix index determines how much of suffix index is actually stored in suff_array
    :param matrix: matrix of input text
    :param q: suffix index factor
    :return: returns suffix index
    '''
    suff_array = []
    for i in range(0, len(matrix), q): #step q is used for optimised algorithm, with basic alg it is 1
        suff_array.append(len(matrix) - len(matrix[i]))
    return suff_array


def search_for_pattern(pattern, first, last, keys, apps, tally, p):
    '''
    This function is the core of the algorithm, it searches for pattern in text using last and first column of matrix,
    tally matrix and returns positions of found pattern in suffix array.
    :param pattern: pattern that is searched for
    :param first: first column
    :param last: last column
    :param keys: chars that appear in text
    :param apps:  appearances dict.
    :param tally: tally matrix
    :param p: tally factor
    :return:  returns list of positions of searched pattern in suffix array
    '''
    if len(pattern) < 1:
        print("Pattern must have lenght greater than zero")
        exit(1)

    my_key = pattern[-1]
    if my_key not in keys:
        return []
    begin_index = 0
    last_index = 0
    for key in keys:
        if key == my_key:
            begin_index += 1
            break
        else:
            begin_index += apps[key]

    last_index = begin_index + apps[my_key]
    if len(pattern) == 1:
        return list(range(begin_index, last_index))
    found = True
    for c in reversed(pattern[:-1]):

        if c not in keys:
            return []
        new_last_index = 0
        new_begin_index = len(first) + 1
        for i in range(begin_index, last_index):
            if last[i] == c:
                new_index = get_from_last_to_first(i, keys, apps, tally, first, last, p)
                if new_index < new_begin_index: new_begin_index = new_index
                if new_index >= new_last_index: new_last_index = new_index + 1

        if new_last_index == 0 and new_begin_index == (len(first) + 1):
            found = False
            break
        else:
            last_index = new_last_index
            begin_index = new_begin_index
    if found:
        return list(range(begin_index, last_index))
    else:
        return []


def get_positons(keys, apps, tally, first, last, pattern_rows, suffix_array, p, q):
    '''
    This function takes positions of suffixes in suffix array, and returns positions of this suffixes in input text
    :param keys:  chars that appear in text
    :param apps: appearances dict.
    :param tally: tally matrix
    :param first: first column
    :param last:  last column
    :param pattern_rows: rows in suffix array where pattern is found
    :param suffix_array: suffix array
    :param p: tally matrix factors
    :param q: suffix array factors
    :return: list of positions of suffixes in input text
    '''
    pos = []
    for row in pattern_rows:
        if row % q == 0:
            pos.append(suffix_array[row // q])
        else:
            steps = 0
            changed_row = row
            while changed_row % q != 0:
                steps += 1
                changed_row = get_from_last_to_first(changed_row, keys, apps, tally, first, last, p)
            pos.append((suffix_array[changed_row // q] + steps) % len(last))

    return pos


def burrows_wheeler(text, pattern, parameters_tuple=(1, 1)):
    '''
    This function returns positions of pattern in input text using Burrows-Wheeler algorithm.
    If no parameters_tuple is provided then this works as non-optimised algorithm.
    Parameters tuple determines tally and suffix array factors and it serves as
    optimization for basic algorithm.
    The higher factors means that this algorithm uses less space.
    :param text: input text
    :param pattern: searched pattern
    :param parameters_tuple: tuple( tally matrix factor, suffix array factor), default(1,1)
    :return: positions of pattern in text
    '''
    pattern = pattern.lower()
    text = text.lower()
    p = parameters_tuple[0]
    q = parameters_tuple[1]
    apps = calc_char_app(text)
    matrix = create_perm_matrix(text)
    suf_array = create_suf_array(matrix, q)
    first = get_first_column(matrix)
    last = get_last_column(matrix, text)

    keys = list(apps.keys())
    keys.sort()
    tally = create_tally(last, keys, p)
    pattern_rows = search_for_pattern(pattern, first, last, keys, apps, tally, p)
    positions = get_positons(keys, apps, tally, first, last, pattern_rows, suf_array, p, q)
    positions.sort()
    return positions
