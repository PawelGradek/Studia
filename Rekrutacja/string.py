def rev_string(string):
    word = ''
    listWords = []
    for i in string:
        word += i
        if i == ' ' :
            listWords.append(word)
            word = ''
        if i == string[-1]:
            listWords.append(word+' ')

    newText = ''
    listWords.reverse()
    for j in listWords:
        newText +=j

    return newText


string = "When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars."

x = rev_string(string)
print(x)