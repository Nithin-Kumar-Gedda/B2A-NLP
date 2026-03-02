def levenshtein_distance(txt1, txt2):
    len_of_txt1 = len(txt1)
    len_of_txt2 = len(txt2)

    matrix = [[0] * (len_of_txt2 + 1) for _ in range(len_of_txt1 + 1)] # create of matrix

    for i in range(len_of_txt1 + 1):  # initialize of row and column of matrix
        matrix[i][0] = i
    for j in range(len_of_txt2 + 1):
        matrix[0][j] = j

    for i in range(1, len_of_txt1 + 1):
        for j in range(1, len_of_txt2 + 1):
            cost = 0 if txt1[i-1] == txt2[j-1] else 1
            matrix[i][j] = min(matrix[i-1][j] + 1, # deletion
                               matrix[i][j-1] +1, #insertion
                               matrix[i-1][j-1] + cost ) #substitution 
    return matrix[len_of_txt1][len_of_txt2]

text1 = "transformation"
text2 = "transaction"
distance = levenshtein_distance(text1,text2)
print("Levenshtein distance between '{}' and '{}' is {}.".format(text1,text2,distance))