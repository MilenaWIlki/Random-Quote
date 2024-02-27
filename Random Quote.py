def generate_random_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "In the midst of winter, I found there was, within me, an invincible summer. - Albert Camus",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "The only thing necessary for the triumph of evil is for good men to do nothing. - Edmund Burke"
    ]
    return random.choice(quotes)

# Example usage:
random_quote = generate_random_quote()
print("Random quote:", random_quote)
