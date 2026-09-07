def pallindrome(text):
    if len(text) <= 1:
        print("Pallindrome")
    else:
        if text[0] == text[-1]:
            pallindrome(text[1:-1])
        else:
            print("Not a pallindrome")

(pallindrome("madam"))
(pallindrome("malayalam"))
(pallindrome("abba"))
