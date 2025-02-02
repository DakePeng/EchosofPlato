import spacy
import random

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Function to replace noun with n+7 substitution
def n_plus_7_replacement(text):
    # Process the text with spaCy
    doc = nlp(text)
    
    # Build a list of nouns (tokens) and their positions
    noun_dict = [token for token in doc if token.pos_ == "NOUN"]

    # Replace nouns with the n+7 substitution
    new_text = []
    for word in text.split():
        # Check if the word is a noun in the noun_dict
        matched_noun = None
        for noun in noun_dict:
            if word.lower() == noun.text.lower():
                matched_noun = noun
                break
        
        if matched_noun:
            # Get the word's vector and find the word 7 positions ahead in the word vector space
            similar_words = list(nlp.vocab.vectors.most_similar(matched_noun.vector, n=8))  # Get the 8 most similar
            replacement_word = nlp.vocab.strings[similar_words[7][0]]  # The 7th most similar word (n+7)
            new_text.append(replacement_word)
        else:
            new_text.append(word)

    return ' '.join(new_text)

# Load your text file
file_path = 'The_Republic_Cleaned.txt'
with open(file_path, 'r') as file:
    text = file.read()

# Apply the n+7 replacement
new_text = n_plus_7_replacement(text)

# Output the modified text
with open('modified_file.txt', 'w') as output_file:
    output_file.write(new_text)

print("N+7 replacement complete. Check the modified_file.txt.")