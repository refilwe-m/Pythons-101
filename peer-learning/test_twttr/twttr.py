vowels = "aeiou"

def main():
    tweet = input("Input: ")
    twt = shorten(tweet)
    print(f"Output: {twt}")


def shorten(word):
    twt = ""
    for i in word:
        if i.lower() not in vowels:
            twt += i
    return twt


if __name__ == "__main__":
    main()
