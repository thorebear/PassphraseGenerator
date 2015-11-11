import numpy
import random as r

import argparse

parser = argparse.ArgumentParser(description='Arguments.')
parser.add_argument('word_count', type=int, help='number of words in passphrase')

args = parser.parse_args()

words = numpy.loadtxt('words', dtype='string')
total_num_words = len(words)
num_words = args.word_count

a = [words[x] for x in [r.randint(0, total_num_words-1)
                        for _ in [0] * num_words]]

print ' '.join(a)
