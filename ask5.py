import string

file_in = open("./two_cities_ascii.txt", "r")
file_out = open("myfile.txt", "w")

allowedCharacters = list(string.ascii_lowercase)
characters = ""
for line in file_in:
    lowers = line.lower()
    for character in lowers:
        if character in allowedCharacters:
            characters += character
        else:
            characters += " "

file_in.close()
file_out.write(characters)
file_out.close()


words = characters.split()
words.sort()


def bubble_sort(indices, arr, passes):
    for j in range(passes):
        for i in range(len(indices) - 1 - j):
            if indices[i] > indices[i + 1]:
                indices[i], indices[i + 1] = indices[i + 1], indices[i]
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


def ten_most_famous_words(word_list: list):
    the_most_famous_words = [word_list.pop()]
    frequency = [1]
    while word_list:
        if the_most_famous_words[-1] == word_list[-1]:
            word_list.pop()
            frequency[-1] += 1
        else:
            the_most_famous_words.append(word_list.pop())
            frequency += [1]
    bubble_sort(indices=frequency, arr=the_most_famous_words, passes=10)
    return the_most_famous_words, frequency


def find_the_most_famous_initial_characters(word_list: list, limit: int):
    word = word_list.pop()
    while len(word) < limit:
        word = word_list.pop()
    the_most_famous_initial_characters = [word[:limit]]
    frequency = [1]
    while word_list:
        word = word_list.pop()
        if len(word) < limit:
            continue
        if the_most_famous_initial_characters[-1] == word[:limit]:
            frequency[-1] += 1
        else:
            the_most_famous_initial_characters.append(word[:limit])
            frequency += [1]
    bubble_sort(indices=frequency, arr=the_most_famous_initial_characters, passes=3)
    return the_most_famous_initial_characters, frequency


famous_words, counts = ten_most_famous_words(list(words))
print("The most famous words:")
for word, count in zip(famous_words[-10:], counts[-10:]):
    print(word, count)

the_most_famous_initial_two_characters, counts = find_the_most_famous_initial_characters(list(words), 2)
print("Three most common initial two characters:")
for word, count in zip(the_most_famous_initial_two_characters[-3:], counts[-3:]):
    print(word, count)

the_most_famous_initial_three_characters, counts = find_the_most_famous_initial_characters(list(words), 3)
print("Three most common initial three characters:")
for word, count in zip(the_most_famous_initial_three_characters[-3:], counts[-3:]):
    print(word, count)
