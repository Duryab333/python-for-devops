import requests
import os
import json

def save_to_file(data, filename="demo.txt"): 
    """Save processed data to a JSON file."""
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    except (OSError, IOError) as e:
        print(f"can not write to file: {e}")


def fetch_joke(joke_url):
    headers = {"Accept" : "application/json"}
    try:
        response = requests.get(url=joke_url, headers=headers)
        response.raise_for_status() # catch http error
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API request fails: {e}")
        return None

def process_joke(data, mood):

    if data is None:
        return "No joke avaliable due to api error"
    try:
        if mood.lower()=="dad":
            #print((data["joke"]))
            return data["joke"]
        else:
            return data["setup"] + data["punchline"]
    except KeyError:
        return "Joke formate unexpected. Could not extract joke text"
    
def main():
    try:
        mood  =input("Which joke would you like to hear eg. (DAD, PJ): ") 
    except Exception as e:
        print(f"Invalid input:{e}")
        return
    
    if mood.lower()== "dad":
        joke_url  = "https://icanhazdadjoke.com/"
    else:
        joke_url  = "https://official-joke-api.appspot.com/random_joke"

    raw_data = fetch_joke(joke_url)
    final_joke= process_joke(raw_data,mood)
    print("\nYour joke :")
    print(final_joke)

    save_to_file({"joke": final_joke}, "demo.txt")


if __name__== "__main__":
    main()
