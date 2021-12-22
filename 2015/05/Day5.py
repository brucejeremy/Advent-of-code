

word_list = []
with open('word_list.txt', 'r') as words:
    for word in words.readlines():
        word_list.append(word.strip())

# A nice string is one with all of the following properties:

# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

bad_pairs = ['ab', 'cd', 'pq', 'xy']
vowels = 'aeiou'

nice_strings = 0

for word in word_list:
    vowel_count = 0
    size = len(word)
    bad_pair_found = False
    consecutive_letter = False
    for idx, letter in enumerate(word):
        if letter in vowels:
            vowel_count += 1
        if idx < size - 1:
            if word[idx:idx+2] in bad_pairs:
                bad_pair_found = True
                break
            if not consecutive_letter and letter == word[idx+1]:
                consecutive_letter = True
    if vowel_count >= 3 and consecutive_letter and not bad_pair_found:
        nice_strings += 1

print('Part one:')
print(f'Nice strings: {nice_strings}')

#------------------------------------------------------------------------

# Now, a nice string is one with all of the following properties:

# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

nice_strings = 0

for word in word_list:
    vowel_count = 0
    size = len(word)
    repeat_pair_found = False
    repeat_letter = False
    for idx, letter in enumerate(word):
        if idx < size - 1:
            if not repeat_pair_found:
                if word.count(word[idx:idx+2]) > 1:
                    repeat_pair_found = True
        if idx < size - 2:
            if not repeat_letter and letter == word[idx+2]:
                repeat_letter = True
    if repeat_pair_found and repeat_letter:
        nice_strings += 1

print('\nPart two:')
print(f'Nice strings: {nice_strings}')