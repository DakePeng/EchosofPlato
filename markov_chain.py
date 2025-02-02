import markovify

# Load text file
def load_text(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

text = load_text("Plato_Books_combined.txt")  # Replace with your text file name

# Create Markov model
model = markovify.Text(text, state_size=2)

# Generate 30 sentences
sentences = [model.make_sentence() for _ in range(30)]

# Save to a text file
with open("generated_sentences.txt", "w", encoding="utf-8") as f:
    for sentence in sentences:
        if sentence:  # Avoid None values
            f.write(sentence + "\n")

print("30 generated sentences saved to 'generated_sentences.txt'")
