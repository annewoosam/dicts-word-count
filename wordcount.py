def count_words(filename):
# python3 wordcount.py anyfilename.txt 
# python3 wordcount.py test.txt 
# python3 wordcount.py twain.txt 
#New
    import sys
#New
    filename = sys.argv[1]

    word_counts = {}

    for line in open(filename): #<=-New open(filename)

        line = line.rstrip()

        words = line.split(' ')

        for word in words:

            word_counts[word] = word_counts.get(word, 0) + 1

    word_counts.items()

    for word,number in word_counts.items():
    	print(f'{word} {number}')

print(count_words(str)) # had to write str for string to pass a variable file name


# def count_words_twain(file):

#     text_file = open(file)

#     word_counts = {}

#     for line in text_file:

#         line = line.rstrip()

#         words = line.split(' ')

#         for word in words:

#             word_counts[word] = word_counts.get(word, 0) + 1

#     word_counts.items()

#     for word,number in word_counts.items():
#     	print(f'{word} {number}')


# print(count_words_twain('twain.txt'))