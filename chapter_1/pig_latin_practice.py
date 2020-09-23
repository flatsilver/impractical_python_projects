"""単語をピッグラテンに変換する"""

def main():
    vowels = 'aiueo'

    while True:
        word = input("Type a word and get its pig Latin translation: ")
        if word[0] in vowels:
            pig_latin = word + 'way'
        else:
            pig_latin = word[1:] + word[0] + 'ay'

        print(pig_latin)

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n")
        if try_again.lower() == "n":
            break


if __name__ == '__main__':
    main()
