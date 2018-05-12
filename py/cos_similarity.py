#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import sys


def CosSimilarity(list_freq1, list_freq2):
    len1 = len(list_freq1)
    len2 = len(list_freq2)
    if (len1 == 0 or len2 == 0 or len1 != len2):
        return 0.0

    t = 0.0
    b1 = 0.0
    b2 = 0.0

    for i in range(0, len1):
        t += list_freq1[i] * list_freq2[i]
        b1 += list_freq1[i] * list_freq1[i]
        b2 += list_freq2[i] * list_freq2[i]

    b1 = pow(b1, 0.5)
    b2 = pow(b2, 0.5)
    b = b1 * b2

    return t / b


def main(args):
    for i in range(1, argc):
        print(args[i])
    str_file1 = args[1]
    str_file2 = args[2]

    # 单字分词
    list_split_words1 = []  # list()
    list_split_words2 = []
    for c1 in str_file1:
        list_split_words1.append(c1)
    for c2 in str_file2:
        list_split_words2.append(c2)

    # 统计词频及单字并集
    list_word_union = []  # 单字并集，模拟实现 NSMutableOrderedSet
    dict_words_freq1 = {}  # map<word,count>，模拟实现 NSCountedSet
    dict_words_freq2 = dict()  # map<word,count>，模拟实现 NSCountedSet

    for word1 in list_split_words1:
        if (word1 in dict_words_freq1.keys()):
            dict_words_freq1[word1] = dict_words_freq1[word1] + 1
        else:
            dict_words_freq1[word1] = 1
        if (list_word_union.count(word1) == 0):
            list_word_union.append(word1)

    for word2 in list_split_words2:
        if (word2 in dict_words_freq2.keys()):
            dict_words_freq2[word2] = dict_words_freq2[word2] + 1
        else:
            dict_words_freq2[word2] = 1
        if (list_word_union.count(word2) == 0):
            list_word_union.append(word2)

    print('dict_words_freq1 is ', dict_words_freq1)
    print('dict_words_freq2 is ', dict_words_freq2)
    print('list_word_union is ', list_word_union)

    # 分别计算每个文本的单字在并集中的单字个数序列
    list_words_freq1 = []
    list_words_freq2 = []

    for word in list_word_union:
        if (word in dict_words_freq1.keys()):
            list_words_freq1.append(dict_words_freq1[word])
        else:
            list_words_freq1.append(0)

        if (word in dict_words_freq2.keys()):
            list_words_freq2.append(dict_words_freq2[word])
        else:
            list_words_freq2.append(0)

    print('list_words_freq1 is ', list_words_freq1)
    print('list_words_freq2 is ', list_words_freq2)

    score = CosSimilarity(list_words_freq1, list_words_freq2)
    print('CosSimilarity is {}'.format(score))


# main entry
if __name__ == '__main__':
    print('This program is being run by itself')

    # 检测提取参数
    argc = len(sys.argv)
    if (argc != 3):
        print("请输入两个文件名，作为对比参数！")
    else:
        main(sys.argv[1:])
else:
    print('I am being imported from another module')
