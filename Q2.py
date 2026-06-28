def analyze_string(s):

    if s == "":
        print("Empty string entered.")
        return

    print("\nLength:", len(s))

    print("Reverse String:", s[::-1])

    vowels = "aeiouAEIOU"
    count = 0

    for ch in s:
        if ch in vowels:
            count += 1

    print("Total vowels in string:", count)

    print("\n<<<>>> Character with Indexes <<<>>>")

    for i in range(len(s)):
        print("Positive Index:", i," " ,"Negative Index:", i-len(s)," ","Character:", s[i])
             

a = input("\nEnter a string:- ")

analyze_string(a)