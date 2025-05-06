def load_and_create_dict(filepath):
    """
    Loads a file with word-pronunciation pairs and creates a dictionary.

    Args:
        filepath (str): The path to the file.

    Returns:
        dict: A dictionary where keys are words and values are lists of pronunciations.
              Returns an empty dictionary if the file cannot be read.
    """

    word_pronunciations = {}
    try:
        with open(filepath, 'r') as file:
            for line in file:
                parts = line.strip().split()  # Remove leading/trailing whitespace and split by spaces
                if len(parts) > 1:
                    word = parts[0]
                    pronunciation = parts[1:]
                    word_pronunciations[word] = pronunciation
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return word_pronunciations