import re
import math
from collections import Counter

def get_cosine(vec1, vec2):
    common = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in common])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    words = re.compile(r'\w+').findall(text)
    return Counter(words)

def check_plagiarism(text1, text2, threshold):
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)

    similarity = get_cosine(vector1, vector2)
    if similarity > threshold:
        return "PLAGIARIZED"
    else:
        return "NOT PLAGIARIZED"

# Example usage
ab = input("Enter First Text ")
bc = input("Enter Second Text ")
text1 = ab
text2 = bc

print(check_plagiarism(text1, text2, 0.5)) # NOT PLAGIARIZED
