import requests
import random

# Load the dataset of words from the file
def load_word_dataset(file_path):
    with open(file_path, "r") as file:
        return [word.strip().upper() for word in file.readlines()]

# Filter words based on API feedback
def filter_words(words, feedback):
    new_word_list = words[:]
    for item in feedback:
        letter = item["guess"].upper()
        slot = item["slot"]
        result = item["result"]
        
        if result == "absent":
            # Remove words containing this letter
            new_word_list = [word for word in new_word_list if letter not in word]
        elif result == "present":
            # Keep words containing the letter but not in this position
            new_word_list = [
                word for word in new_word_list if letter in word and word[slot] != letter
            ]
        elif result == "correct":
            # Keep words with this letter in the correct position
            new_word_list = [word for word in new_word_list if word[slot] == letter]
    
    return new_word_list

# Make an API call with the guessed word
def make_api_call(guess, size):
    url = f"https://wordle.votee.dev:8000/daily?guess={guess}&size={size}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error if the request fails
    return response.json()

# Main function to solve the puzzle
def solve_wordle(api_url, word_file_path, word_size):
    word_list = load_word_dataset(word_file_path)
    attempts = 0
    max_attempts = 6  # Limit to 6 attempts as per typical Wordle rules
    
    while attempts < max_attempts and word_list:
        # Choose a random word from the remaining list
        guess = random.choice(word_list)
        print(f"Attempt {attempts + 1}: Guessing {guess}")
        
        # Make an API call
        feedback = make_api_call(guess, word_size)
        print("API Feedback:", feedback)
        
        # Check if the word is fully correct
        if all(item["result"] == "correct" for item in feedback):
            print(f"Solved! The correct word is {guess}")
            return guess
        
        # Filter the word list based on feedback
        word_list = filter_words(word_list, feedback)
        attempts += 1
    
    print("Failed to solve the puzzle within the allowed attempts.")
    return None

# Usage
if __name__ == "__main__":
    word_file_path = "word_dataset.txt"  # Path to your dataset file
    word_size = 5  # Word length
    solve_wordle("https://wordle.votee.dev:8000/daily", word_file_path, word_size)
