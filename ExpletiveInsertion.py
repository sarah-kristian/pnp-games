# Description: This file contains the code for inserting expletives into words in English
# This is variably called Expletive Insertion, Expletive Infixation, or Tmesis

import nltk
nltk.download('cmudict')
# nltk.download('cmudict')
# from nltk.corpus import cmudict
# d = cmudict.dict()

# def get_phonetic_transcr(word):
#     phonemes = d.get(word.lower())
#     if phonemes:
#         for pron in phonemes:
#             stress_pattern = [int(phoneme[-1]) for phoneme in pron if phoneme[-1].isdigit()]
#             main_stress_index = stress_pattern.index(1) if 1 in stress_pattern else None
#             print(f"Phonetic transcription: {pron}")
#             print(f"Stress pattern: {stress_pattern}")
#             print(f"Main stress is on syllable: {main_stress_index + 1}" if main_stress_index is not None else "No primary stress found")
#     else:
#         print("Word not found in CMU dictionary.")




# def expletive_insertion():

#     word = 'banana'

#     get_phonetic_transcr(word)
# #    swear_word = input("Enter a swear word: ").lower().strip()
# #    carrier_word = input("Enter a carrier word: ").lower().strip()


#     print("Expletive Insertion")



# if __name__ == "__main__":
#     expletive_insertion()