import requests
def getrandomjoke():
    url="https://evilinsult.com/generate_insult.php?lang=en&type=json"
    response = requests.get(url)
    if response.status_code==200:
        print(f"full json response: {response.json()}")
        joke_data=response.json()
        return f"{joke_data['setup']}-{joke_data['qpunchline']}"
    else:
        return "failed to retrieve joke"
def notmain():
    print("Welcome to random joke generator")
    while True:
        user_input=input("press enter to get a new joke or type q to quit:").lower()
        if user_input=="q":
            print("badbye it wasnt nice meeting you hope you dont come back... PLEASE DONT")
            break
        joke=getrandomjoke()
        print(joke)
notmain()