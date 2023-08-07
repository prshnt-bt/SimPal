import requests
from difflib import get_close_matches
import random
from sentence_transformers import SentenceTransformer, util
import math

def calc_square_root(number):
    try:
        number = float(number)
        result = math.sqrt(number)
        return f"The square root of {number} is {result:.2f}."
    except ValueError:
        return "Invalid input. Please provide a valid number."
    
# ----------------------------------------------------------------Geolocation/weather functions
def get_weather():
    city_name = input("Chatbot: Enter City name: ")
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=a35a5a545f643f8e4d8f0f4a50dc6098'
    # Sending GET request to the API
    response = requests.get(base_url)
    data = response.json()
    if data:
        print("Weather Information:")
        print("City:", data['name'])
        print("Weather:", data['weather'][0]['main'])
        print("Description:", data['weather'][0]['description'])
        print("Temperature:", data['main']['temp'], "°C")
        print("Feels Like:", data['main']['feels_like'], "°C")
        print("Humidity:", data['main']['humidity'], "%")
        print("Wind Speed:", data['wind']['speed'], "m/s")
        print("Visibility:", data['visibility'], "m")
        
        return "Any other query?"
    else:
        # If the request fails, display an error message
        print(f"Error {response.status_code}: {data['message']}")
# ----------------------------------------------------------------currency converter functions
def get_currency_rate():
    base_currency = input("Chatbot: Please enter the base currency: ")
    target_currency = input("Chatbot: Please enter the target currency: ")
    amount = input("Chatbot: Please enter the amount: ")
    api_key = "169930934ca929fdd869b94f"
    url = "https://v6.exchangerate-api.com/v6/169930934ca929fdd869b94f/latest/USD"
    response = requests.get(url)
    data = response.json()
    if data["result"] == "success":
        rates = data["conversion_rates"]
        if base_currency == "USD":
            base_rate = 1.0
        else:
            base_rate = rates.get(base_currency)

        target_rate = rates.get(target_currency)
        amount = float(amount)
        if base_rate is not None and target_rate is not None:
            rate = (target_rate / base_rate) * amount
        if rate:
            return f"Chatbot: 1 {base_currency} = {rate} {target_currency}"
        else:
            print("Chatbot: Sorry, I couldn't retrieve currency rates at the moment. Please try again later.")
#----------------------------------------------------------------mathematical functions
def calc_square_root():
    user_input = input("You: ")
    try:
        number = float(user_input)
        result = math.sqrt(number)
        return f"The square root of {number} is {result}"
    except ValueError:
        return "Invalid input. Please provide a valid number."
def calc_square():
    user_input = input("You: ")
    try:
        number = float(user_input)
        result = number ** 2
        return f"The square of {number} is {result}"
    except ValueError:
        return "Invalid input. Please provide a valid number."
def calc_cube():
    user_input = input("You: ")
    try:
        number = float(user_input)
        result = number ** 3
        return f"The cube of {number} is {result}"
    except ValueError:
        return "Invalid input. Please provide a valid number."
def calc_add():
    user_input1 = input("You: ")
    user_input2 = input("You: ")
    try:
        num1 = float(user_input1)
        num2 = float(user_input2)
        result = num1 + num2
        return f"The addition of {num1} and {num2} is {result}"
    except ValueError:
        return "Invalid input. Please provide valid numbers."
def calc_subtract():
    user_input1 = input("You: ")
    user_input2 = input("You: ")
    try:
        num1 = float(user_input1)
        num2 = float(user_input2)
        result = num1 - num2
        return f"The subtraction of {num1} from {num2} is {result}"
    except ValueError:
        return "Invalid input. Please provide valid numbers."
def calc_multiply():
    user_input1 = input("You: ")
    user_input2 = input("You: ")
    try:
        num1 = float(user_input1)
        num2 = float(user_input2)
        result = num1 * num2
        return f"The multiplication of {num1} and {num2} is {result}"
    except ValueError:
        return "Invalid input. Please provide valid numbers."
def calc_divide():
    user_input1 = input("You: ")
    user_input2 = input("You: ")
    try:
        num1 = float(user_input1)
        num2 = float(user_input2)
        if num2 == 0:
            return "Cannot divide by zero."
        result = num1 / num2
        return f"The division of {num1} by {num2} is {result}"
    except ValueError:
        return "Invalid input. Please provide valid numbers."
def calc_sine():
    user_input = input("You: ")
    try:
        angle = float(user_input)
        result = math.sin(math.radians(angle))
        return f"The sine of {angle} degrees is {result:.2f}"
    except ValueError:
        return "Invalid input. Please provide a valid number."
def calc_cosine():
    user_input = input("You: ")
    try:
        angle = float(user_input)
        result = math.cos(math.radians(angle))
        return f"The cosine of {angle} degrees is {result:.2f}"
    except ValueError:
        return "Invalid input. Please provide a valid number."
def calc_tangent():
    user_input = input("You: ")
    try:
        angle = float(user_input)
        result = math.tan(math.radians(angle))
        return f"The tangent of {angle} degrees is {result:.2f}"
    except ValueError:
        return "Invalid input. Please provide a valid number."
def calc_factorial():
    user_input = input("You: ")
    try:
        number = int(user_input)
        if number < 0:
            return "Factorial is not defined for negative numbers."
        result = math.factorial(number)
        return f"The factorial of {number} is {result}"
    except ValueError:
        return "Invalid input. Please provide a valid integer."



# NLTK patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how_are_you|how\s?are\s?you', ['I am good, thank you!', 'I am doing well.', 'All good!']),
    (r'what is your name|who are you', ['I am your friendly chat bot!', 'I go by the name ChatBot.', 'You can call me Bot.']),
    #flagshipFunctions
    (r'currency|currency converter|want to convert currency|exchange rate', get_currency_rate),
    (r'weather|mausam|hows the weather|forecast', get_weather),
    #mathematical
    (r'calculate square root of (.+)|square root', calc_square_root),
    (r'calculate square of (.+)|square', calc_square),
    (r'calculate cube of (\d+(\.\d+)?)|cube of a number', calc_cube),
    (r'add (.+) and (.+)|addition|add two numbers', calc_add),
    (r'subtract (.+) from (.+)|subtraction|minus|subtract 2 numbers', calc_subtract),
    (r'multiply (.+) by (.+)|multiplication', calc_multiply),
    (r'divide (.+) by (.+)|Division', calc_divide),
    (r'calculate sine of (.+)', calc_sine),
    (r'calculate cosine of (.+)', calc_cosine),
    (r'calculate tangent of (.+)', calc_tangent),
    (r'calculate factorial of (.+)', calc_factorial),
    #extras
    (r'what can you do', ['I can answer questions, tell jokes, and more!', 'I am here to chat and assist you.']),
    (r'who created you|who made you', ['I was created by Prashant Bisht.', 'I am the creation of some Prashant Bisht.']),
    (r'how old are you', ['I am just a program, so I don\'t have an age.', 'Age is just a number for a chat bot like me.']),
    (r'tell me a joke', ['Why don\'t scientists trust atoms? Because they make up everything!', 'Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them.','Why don’t skeletons fight each other? They don’t have the guts.',
        'Why did the scarecrow win an award? Because he was outstanding in his field.',
        'Why did the tomato turn red? Because it saw the salad dressing.',
        'What do you call fake spaghetti? An impasta.',
        'Why don’t scientists trust atoms? Because they make up everything!',
        'Why don’t some couples go to the gym? Because some relationships don’t work out!',
        'Why don’t seagulls fly over the bay? Because then they’d be bagels.',
        'Why did the golfer bring two pairs of pants? In case he got a hole in one.',
        'What’s brown and sticky? A stick.',
        'What did one hat say to the other hat? You stay here, I’ll go on ahead!',
        'Why don’t scientists trust stairs? Because they’re always up to something.',
        'Why do we never tell secrets on a farm? Because the potatoes have eyes and the corn has ears.',
        'Why don’t some couples go to the gym? Because some relationships don’t work out!',
        'Why don’t scientists trust atoms? Because they make up everything!',
        'What do you call fake spaghetti? An impasta.',
        'Why did the tomato turn red? Because it saw the salad dressing.',
        'What do you get when you cross a snowman and a vampire? Frostbite.',
        'What do you call a can opener that doesn’t work? A can’t opener.',
        'Why did the scarecrow win an award? Because he was outstanding in his field.',
        'Why don’t seagulls fly over the bay? Because then they’d be bagels.',]),
    (r'thank you|thanks', ['You\'re welcome!', 'No problem!', 'Happy to help!']),
    (r'sorry|apologies', ['No worries!', 'It\'s alright!', 'No need to apologize.']),
    (r'help|need help', ['Sure, I\'m here to assist you. What do you need help with?', 'How can I assist you today?']),
    (r'what time is it|time', ['I am sorry, I am not equipped to provide real-time information.']),
    (r'who am I', ['You are a human talking to a chat bot.', 'I don\'t know who you are.']),
    (r'what is the meaning of life', ['The meaning of life is a philosophical question, and I am just a program.']),
    (r'your favorite color', ['As a chat bot, I don\'t have preferences or favorites.']),
    (r'love you', ['Thank you, but I am just a program and don\'t have feelings.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Take care!']),
    (r'how do you work|how does it work', ['I am powered by algorithms and machine learning.', 'My functioning is based on NLP techniques.']),
    (r'where are you from', ['I am just a digital creation, so I don\'t have a physical location.']),
    (r'who is your favorite superhero', ['I don\'t have personal preferences, but many people like Batman and Superman.']),
    (r'what is your favorite food', ['As an AI, I don\'t eat, but I can recommend some great recipes!']),
    (r'what is your favorite movie', ['I can\'t watch movies, but I hear "The Matrix" is popular among AI programs.']),
    (r'can you think|do you have thoughts', ['I don\'t have consciousness or thoughts, but I can process data and respond accordingly.']),
    (r'what is the best programming language', ['There is no one-size-fits-all answer. It depends on your needs and preferences.']),
    (r'who is your favorite musician', ['As a chat bot, I don\'t have musical prefewhay rences.']),
    (r'what is the weather today|weather', ['I don\'t have access to real-time data, but you can check a weather app for that.']),
    (r'what is your purpose', ['My purpose is to assist and engage in conversations with users like you.']),
    (r'what is the largest country|biggest country', ['Russia is the largest country by land area.', 'Canada is the second-largest country by land area.']),
    (r'what is the capital of|capital of', ['The capital of India is New Delhi.', 'The capital of France is Paris.']),
    (r'who is the president of|president of', ['I don\'t have real-time data, but you can check the latest news for that.']),
    (r'what is the population of|population of', ['I don\'t have real-time data, but you can search online for the latest population figures.']),
    (r'who won the|winner of', ['I don\'t have real-time data, but you can check the latest results online.']),
    (r'what is your favorite book', ['As an AI, I don\'t read books, but "The Hitchhiker\'s Guide to the Galaxy" is popular.']),
    (r'what are your hobbies', ['I don\'t have hobbies, but I enjoy interacting with users like you.']),
    (r'what is your favorite sport', ['As an AI, I don\'t have preferences, but many people enjoy football and basketball.']),
    (r'who is your best friend', ['As an AI, I don\'t have friends, but I enjoy talking to everyone.']),
    (r'can you tell me a riddle', ['Sure! What has keys but can\'t open locks? A piano!', 'Why don\'t some couples go to the gym? Because some relationships don\'t work out!']),
    (r'what is your favorite programming language', ['As a chat bot, I don\'t have preferences, but I understand multiple programming languages.']),
    (r'what is the square root of|square root of', ['The square root of 9 is 3.', 'The square root of 16 is 4.', 'I can calculate the square root of any number you provide.']),
    (r'what is the capital of|capital of', ['The capital of Japan is Tokyo.', 'The capital of Brazil is Brasília.']),
    (r'who is your favorite actor|actress', ['As an AI, I don\'t have preferences, but many people like actors such as Tom Hanks and actresses like Meryl Streep.']),
    (r'what is the meaning of|meaning of', ['The meaning of a word or phrase can be found in a dictionary.', 'The meaning of life is a profound philosophical question.']),
    (r'what is your favorite subject', ['As a chat bot, I don\'t have preferences, but I enjoy discussing a wide range of topics.']),
    (r'what is the time zone', ['As an AI, I don\'t have a fixed time zone.']),
    (r'what is your favorite animal', ['As a program, I don\'t have preferences, but I like all animals.']),
    (r'who is your favorite historical figure', ['As an AI, I don\'t have preferences, but historical figures like Albert Einstein and Leonardo da Vinci are well-known.']),
    (r'what is the best movie of all time', ['The best movie of all time is subjective and depends on individual tastes.']),
    (r'can you sing a song', ['I don\'t have a singing voice, but I can share song lyrics with you.']),
    (r'what is your favorite song', ['As an AI, I don\'t have personal favorites, but many people like "Imagine" by John Lennon.']),
    (r'what is your favorite color', ['As a chat bot, I don\'t have preferences or favorite colors.']),
    (r'what is the capital of|capital of', ['The capital of China is Beijing.', 'The capital of Italy is Rome.']),
    (r'who is the best football player', ['The title of "best" is subjective and may vary based on opinions. Many admire players like Lionel Messi and Cristiano Ronaldo.']),
    (r'what is your favorite TV show', ['As an AI, I don\'t have preferences, but many people enjoy shows like "Friends" and "Game of Thrones."']),
    (r'who is your favorite author', ['As a chat bot, I don\'t have preferences, but authors like J.K. Rowling and Stephen King are popular.']),
    (r'what is the square of|square of', ['The square of 5 is 25.', 'The square of 10 is 100.', 'I can calculate the square of any number you provide.']),
    (r'what is your favorite quote', ['As an AI, I don\'t have personal favorites, but many people find inspiration in quotes like "Be the change you wish to see in the world."']),
    (r'what is your favorite dessert', ['As an AI, I don\'t have preferences, but many people enjoy desserts like chocolate cake and ice cream.']),
    (r'what is the longest river', ['The Nile is the longest river in the world.', 'The Amazon River is the second-longest river in the world.']),
    (r'what is your favorite place', ['As an AI, I don\'t have preferences, but many people love places like the beach and mountains.']),
    (r'what is the best book of all time', ['The best book of all time is subjective and depends on individual tastes and genres.']),
    (r'can you play a game', ['I can engage in text-based games like word association or trivia. Would you like to play?']),
    (r'what is your favorite programming language', ['As an AI, I don\'t have personal preferences, but I understand multiple programming languages.']),
    (r'what is the meaning of life, the universe, and everything', ['In the book "The Hitchhiker\'s Guide to the Galaxy," the answer to that question is 42.']),
    (r'what is the largest animal', ['The blue whale is the largest animal on Earth.', 'The African elephant is the largest land animal.']),
    (r'who is your favorite musician', ['As a chat bot, I don\'t have musical preferences, but many people admire artists like Beethoven and Mozart.']),
    (r'can you solve math problems', ['Yes, I can help with math problems. Feel free to ask!'])
    
]

# Load pre-trained sentence embedding model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Get sentence embeddings
def get_sentence_embedding(text):
    return model.encode([text], convert_to_tensor=True)

# Calculate similarity score between two embeddings
def get_similarity_score(embedding1, embedding2):
    return util.pytorch_cos_sim(embedding1, embedding2)

# Get response using sentence embeddings
def get_response_with_embedding(user_input):
    user_embedding = get_sentence_embedding(user_input)
    best_score = 0.0
    best_response = None

    for pattern, response in patterns:
        pattern_embedding = get_sentence_embedding(pattern)
        similarity_score = get_similarity_score(user_embedding, pattern_embedding)
        if similarity_score > best_score:
            best_score = similarity_score
            best_response = response
    if callable(best_response):  # Check if the response is a function
        return best_response()
    
    return random.choice(best_response) if best_response else None

# Get fuzzy response for similar patterns
def get_fuzzy_response(user_input):
    best_match = get_close_matches(user_input.lower(), [pattern for pattern, _ in patterns])
    if best_match:
        pattern_response = [response for pattern, response in patterns if pattern.lower() == best_match[0]]
        if pattern_response:
            return random.choice(pattern_response)  # Get a random response from the list
    return None

# Main chatbot loop
def chat():
    print("Chatbot: Hi, I'm your chatbot assistant. How can I help you today?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        else:
            response = get_response_with_embedding(user_input)
            if not response:
                fuzzy_response = get_fuzzy_response(user_input)
                if fuzzy_response:
                    print("Chatbot:", fuzzy_response)
                else:
                    print("Chatbot: I'm sorry, I don't understand that.")
            else:
                    print("Chatbot:", response)



# ----------------------------------------------------------------main
if __name__ == "__main__":
    chat()
