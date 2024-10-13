import random

# User input for number of symbols per row/column (total fields = ilosc * ilosc)
ilosc = int(input("Podaj liczbę symboli w wierszu (2-10 i musi być tak, żeby liczba pól była parzysta): "))
total_fields = ilosc * ilosc

# Ensure the total number of fields is even
while total_fields % 2 != 0:
    print("Liczba pól musi być parzysta. Spróbuj ponownie.")
    ilosc = int(input("Podaj liczbę symboli w wierszu (2-10): "))
    total_fields = ilosc * ilosc

# List of emojis and other variables
emojis = ['😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '🥲', '🥹', '😊', '😇', '👽', '🙃', '😉',
          '😌', '😍', '🥰', '😘', '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪', '🤨', '🧐', '🤓',
          '😎', '🥸', '🤩', '🥳', '👾', '😏', '😒', '😞', '😔', '😟', '😕', '🙁', '☹️', '😣', '😖',
          '😫', '😩', '🥺', '😈', '🤔']

# Select enough emojis and double them to make pairs
emojiArr = random.sample(emojis, total_fields // 2) * 2  # Use half emojis, double them to make pairs
random.shuffle(emojiArr)  # Shuffle for gameplay

# Grid setup
revealed = [False] * total_fields  # Keeps track of which cards are revealed

# Display the hidden grid (in rows and columns)
def display_grid():
    print("\nAktualna plansza:")
    for i in range(total_fields):
        if revealed[i]:
            print(f"| {emojiArr[i]} |", end=" ")
        else:
            print("| # |", end=" ")
        if (i + 1) % ilosc == 0:  # New line after each row
            print()

# Handle player input for card selection
def get_coordinates():
    while True:
        try:
            pos = int(input(f"Podaj numer karty (1-{total_fields}): ")) - 1
            if 0 <= pos < total_fields and not revealed[pos]:
                return pos
            else:
                print("Nieprawidłowy wybór lub karta już odkryta. Spróbuj ponownie.")
        except ValueError:
            print("Nieprawidłowy wybór. Wprowadź prawidłowy numer.")

# Main memory game logic for 2 players
def memory_game_2players():
    attempts = 0
    pairs_found = 0
    player_scores = [0, 0]  # player_scores[0] for Player 1, player_scores[1] for Player 2
    current_player = 0  # Starts with Player 1
    
    while pairs_found < total_fields // 2:
        display_grid()
        print(f"\nGracz {current_player + 1}'s tura")
        
        # Player selects first and second card
        print("Wybierz pierwszą kartę:")
        first = get_coordinates()
        
        display_grid()
        print("Wybierz drugą kartę:")
        second = get_coordinates()
        
        # Reveal the cards
        revealed[first] = True
        revealed[second] = True
        display_grid()
        
        if emojiArr[first] == emojiArr[second]:
            print(f"Gracz {current_player + 1} znalazł parę: {emojiArr[first]}!")
            player_scores[current_player] += 1
            pairs_found += 1
        else:
            print(f"Karty nie pasują: {emojiArr[first]} i {emojiArr[second]}")
            revealed[first] = False
            revealed[second] = False
            # Switch to the other player if no match
            current_player = 1 - current_player  # Switch between 0 and 1 (Player 1 and Player 2)
        
        attempts += 1
    
    # Game over, determine the winner
    print("\nKoniec gry!")
    print(f"Wynik Gracz 1: {player_scores[0]}")
    print(f"Wynik Gracz 2: {player_scores[1]}")
    
    if player_scores[0] > player_scores[1]:
        print("Gracz 1 wygrywa!")
    elif player_scores[1] > player_scores[0]:
        print("Gracz 2 wygrywa!")
    else:
        print("Gra kończy się remisem!")

# Start the 2-player memory game
memory_game_2players()
