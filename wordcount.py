# put your code here.


def word_count(file_name):

    poem = open(file_name)
    word_in_poems = {}

    for line in poem:
        line = line.rstrip()
        poem_line = line.split(" ")
#        print poem_line


        for word in poem_line:
            if word in word_in_poems:
                word_in_poems[word] += 1

            else:
                word_in_poems[word] = 1

    item_as_tuple = word_in_poems.iteritems()

    for key, value in item_as_tuple:
        print "{} {}".format(key, value)



    poem.close()

word_count("twain.txt")