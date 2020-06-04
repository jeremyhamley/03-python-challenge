# import modules: os , re
import os
import re
#define the path to access the text file
text_file_1 = os.path.join("Resources-PyParagraph_raw_data", "paragraph_1.txt")
text_file_2 = os.path.join("Resources-PyParagraph_raw_data", "paragraph_2.txt")


#open and read paragraph_1
with open(text_file_1,"r") as text_1:
    paragraph_1 = text_1.read()
    #split into sentences
    sentences_1 = re.split("(?<=[.!?]) +",paragraph_1)
    #split into words and count words
    words_1 = paragraph_1.split(" ")
    #calculate average sentence length
    average_setnece_length_1 = (len(words_1)) / (len(sentences_1))

#count the letters in all of the words
letter_count_1 = 0
for word_1 in words_1:
    letter_count_1 = letter_count_1 + (len(word_1))
#calculate the average letter count
average_letter_count_1 = letter_count_1 / (len(words_1))


#open and read paragraph_2
with open(text_file_2,"r") as text_2:
    paragraph_2 = text_2.read()
    #split into sentences
    sentences_2 = paragraph_2.split("\n\n")

    #split into words and count words
    words_2 = paragraph_2.split(" ")
    #calculate average sentence length
    average_setnece_length_2 = (len(words_2)) / (len(sentences_2))

#count the letters in all of the words
letter_count_2 = 0
for word_2 in words_2:
    letter_count_2 = letter_count_2 + (len(word_2))
#calculate the average letter count
average_letter_count_2 = letter_count_2 / (len(words_2))

#open txt file and save paragraph analysis report
pyparagraph_analysis = os.path.join("Analysis-PyParagraph", "PyParagraph_analysis.txt")
with open(pyparagraph_analysis,"w") as text_file:
    text_file.write(f'''
    ----------------------------
    Paragraph Analysis of:
    paragraph_1.txt
    ----------------------------
    Approximate Word Count: {len(words_1)}
    Approximate Sentence Count: {len(sentences_1)}
    Average Letter Count:  {average_letter_count_1}
    Average Sentence Length: {average_setnece_length_1}

    ----------------------------
    Paragraph Analysis of:
    paragraph_2.txt
    ----------------------------
    Approximate Word Count: {len(words_2)}
    Approximate Sentence Count: {len(sentences_2)}
    Average Letter Count:  {average_letter_count_2}
    Average Sentence Length: {average_setnece_length_2}
    ''')
    text_file.close()
#print report in terminal
print(f'''
    ----------------------------
    Paragraph Analysis of:
       paragraph_1.txt
    ----------------------------
    Approximate Word Count: {len(words_1)}
    Approximate Sentence Count: {len(sentences_1)}
    Average Letter Count:  {average_letter_count_1}
    Average Sentence Length: {average_setnece_length_1}

    ----------------------------
    Paragraph Analysis of:
       paragraph_2.txt
    ----------------------------
    Approximate Word Count: {len(words_2)}
    Approximate Sentence Count: {len(sentences_2)}
    Average Letter Count:  {average_letter_count_2}
    Average Sentence Length: {average_setnece_length_2}
    ''')
