import string

# Step 1: Creating a sample file with some content 
def create_sample_file():
    with open("task.txt", "w") as file:
        file.write("my name is my madhu is the name")
    print("File 'task.txt' has been created with task text.\n")

# Step 2: Reads file and count word occurrences
def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()

        text = text.translate(str.maketrans('', '', string.punctuation)).lower()

        words = text.split()

        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        # Sort and display the word counts
        print("Word Frequencies (Alphabetical Order):")
        for word in sorted(word_count):
            print(f"{word}: {word_count[word]}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

create_sample_file()
count_words_in_file("task.txt")
