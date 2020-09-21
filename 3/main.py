import os
import requests
import sys

while(True):
    print("Welcome to IsItDown.py!")
    print("Please write a URL or URLs you want to check. (separeated by comma)")
    input_URL = map(str.strip, sys.stdin.readline().split(','))

    for URL in input_URL:
        if ".com" not in URL:
            print(f"{URL} is not valid url")
            continue
        if "http://" not in URL:
            URL = "http://" + URL
        try:
            res = requests.get(URL)
            if res.status_code == requests.codes.ok:
                print(f"{URL} is up!")
            else:
                print(f"{URL} is down!")
        except:
            print(f"{URL} is down!")

    restart = None

    while(True):
        restart = input("Do You Want to start over? y/n")
        if restart == "y" or restart == "n":
            break
        else:
            print("is not valid answer")

    if restart == "n":
        break
    elif restart == "y":
        os.system('clear')

print("bye!")
