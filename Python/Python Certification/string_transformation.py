# Python: String Transformation
import os


def transformSentence(sentence):
    new_sentence = ""
    words_list = sentence.split(" ")
    for word in words_list:
        new_sentence += word[0]
        for i in range(1, len(word)):
            if word[i-1].lower() < word[i].lower():
                new_sentence += word[i].upper()
            elif word[i-1].lower() > word[i].lower():
                new_sentence += word[i].lower()
            else:
                new_sentence += word[i]
        new_sentence += " "

    return new_sentence


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + '\n')

    fptr.close()
