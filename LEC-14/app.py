def find_grades(grades, students): # from lecture
    results = []

    # j = 0 without the in keyword we can use an iterator

    for key in grades:  #{'Ana': 'B', 'Matrin' : 'C'}
        if key in students: # more pythonic

        #if students[j] == key: same result

            results.append(grades[key])
            
            # j+=1

    return results

# print(find_grades({'Ana': 'B', 'Martin' : 'C', 'John' : 'B', 'Katy' : 'A'}, ['Martin', 'Katy']))


# Naive Solution
# def count_matches(d): # from lecture
#     total = 0
#     for key in d:
#        if d[key] == key:
#             total += 1
#     return total
#####################################
# pythonic Solution
def count_matches(d): # from lecture
    total = 0
    for key, value in d.items():
       if value == key:
            total += 1
    return total
# print(count_matches({1:2, 3:4, 5:6})) # should print 0
# print(count_matches({1:3, 'a':'a', 5:5})) #should print 2



# word frequency founder functions solution From lecture
# creating words frequency dict
def generate_words_dict(song):
    song_words = song.lower()
    song_list = song_words.split()
    words_dict = {}
    for w in song_list:
        if w in words_dict:
            words_dict[w] += 1
        else:     
            words_dict[w] = 1
    return words_dict

song = "RAH RAH AH AH AH ROM MAH RO MAH MAH" # sorry for that it was on lecture i swear 😂
print(generate_words_dict(song))

def find_frequent_word(words_dict):
    word_list = []
    biggest_val = max(words_dict.values())
    for k,v in words_dict.items():
        if v == biggest_val:
            word_list.append(k)
    return (word_list, biggest_val)
first_words_dict = generate_words_dict(song)
print(find_frequent_word(first_words_dict))

# find word with freq more than x
def occurs_often(words_dict, x):
    freq_list = []
    freq_words_tuple = find_frequent_word(words_dict)
    while freq_words_tuple[1] > x:
        freq_words_tuple = find_frequent_word(words_dict)
        freq_list.append(freq_words_tuple)
        for w in freq_words_tuple[0]:
            del(words_dict[w])
    return freq_list


words_dict = generate_words_dict(song)
print(occurs_often(words_dict, 2))