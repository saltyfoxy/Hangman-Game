from pickle import DICT
import random


dictionnary = {
    "afforest": "establish a forest on previously unforested land",
    "aftermath": "the consequences of an event, especially a catastrophic one",
    "becalm": "make still, steady, or tranquil",
    "blithesome": "carefree and happy and lighthearted",
    "broadsheet": "an advertisement intended for wide distribution",
    "buffoonish": "like a clown",
    "caprice": "a sudden desire",
    "capricious": "determined by chance or impulse rather than by necessity",
    "causerie": "light informal conversation for social occasions",
    "chivalrous": "attentive and honorable like an ideal knight",
    "congratulatory": "expressive of sympathetic pleasure or joy on account of someone's success or good fortune",
    "dapper": "marked by up-to-dateness in dress and manners",
    "debonaire": "having a sophisticated charm",
    "emblazon": "decorate with heraldic arms",
    "eudaemonia": "a contented state of being happy and healthy and prosperous",
    "extremum": "the point located farthest from the middle of something",
    "exultant": "joyful and proud especially because of triumph or success",
    "featherbrained": "lacking seriousness; given to frivolity",
    "felicity": "pleasing and appropriate manner or style",
    "gabble": "speak (about unimportant matters) rapidly and incessantly",
    "gallant": "having or displaying great dignity or nobility",
    "gilt": "having the deep slightly brownish color of gold",
    "gleeful": "full of high-spirited delight",
    "halycon": "a mythical bird said to breed at the winter solstice",
    "heyday": "the period of greatest prosperity or productivity",
    "hotheaded": "characterized by undue haste and lack of thought or deliberation",
    "madcap": "characterized by impulsiveness or recklessness",
    "majestic": "having or displaying great dignity or nobility",
    "natty": "marked by up-to-dateness in dress and manners",
    "nuance": "a subtle difference in meaning or opinion or attitude",
    "phantasy": "imagination unrestricted by reality",
    "pollyannaish": "pleasantly (even unrealistically) optimistic",
    "prate": "speak about unimportant matters rapidly and incessantly",
    "sappy": "very sentimental or emotional",
    "snappy": "quick and energetic",
    "spiffy": "marked by up-to-dateness in dress and manners",
    "stunner": "a very attractive or seductive looking woman",
    "timberland": "land that is covered with trees and shrubs",
    "timbre" : "the distinctive property of a complex sound",
    "twaddle": "pretentious or silly talk or writing",
    "vividness": "interest and variety and intensity",
    "wearisome": "so lacking in interest as to cause mental fatigue",
    "whismical": "determined by chance or impulse rather than by necessity",
    "whismy": "an odd or fanciful or capricious idea",
    "zippy": "quick and energetic"
}


pattern = ("  -----------   \n" 
           "  |             \n"
           "  |             \n"
           "  |             \n"
           "  |             \n"
           "  |             \n"
           "  |             \n"
           "  |             \n"
           "__|__ \n")

pattern1 = pattern[:29] + "|" + pattern[29:]
pattern2 = pattern1[:47] + "|" + pattern1[47:]
pattern3 = pattern2[:65] + "|" + pattern2[65:]
pattern4 = pattern3[:83] + "|" + pattern3[83:]
pattern5 = pattern4[:101] + "o" + pattern4[101:]
pattern6 = pattern5[:118] + "/" + pattern5[118:]
pattern7 = pattern6[:119] + "|" + pattern6[119:]
pattern8 = pattern7[:120] + "\\" + pattern7[120:]
pattern9 = pattern8[:138] + "/" + pattern8[138:]
pattern10 = pattern9[:140] + "\\" + pattern9[140:]

print(pattern1)
print(pattern2)
print(pattern3)
print(pattern4)
print(pattern5)

play = True

def randomWord(level): 
    word = "               "
    easyWords = []
    mediumWords = []
    hardWords = []
    for word in dictionnary.keys(): 
        if len(word) <= 7:
            easyWords.append(word)
        elif len(word) > 7 and len(word) <= 9:
            mediumWords.append(word)
        elif len(word) > 9:
            hardWords.append(word)
            
    if level == 1:
        word = random.choice(easyWords)
        # print(f"Easy Word : {word} . Lenght : {len(word)} \n")
        return word     
    elif level == 2:
        word = random.choice(mediumWords)
        # print(f"Medium Word : {word} . Lenght : {len(word)} \n")
        return word
    elif level == 3:
        word = random.choice(hardWords)
        # print(f"Hard Word : {word} . Lenght : {len(word)} \n ")
        return(word)
    elif level == "r" or level == "random": 
        word = random.choice(list(dictionnary.keys()))
        # print(f"Random Word : {word} . Lenght : {len(word)} \n")
        return word
            

def patternError(numError):
    global pattern
    pattern1 = pattern[:29] + "|" + pattern[29:]
    pattern2 = pattern[:47] + "|" + pattern[47:]
    pattern3 = pattern[:65] + "|" + pattern[65:]
    pattern4 = pattern[:83] + "|" + pattern[83:]
    pattern5 = pattern[:101] + "o" + pattern[101:]
    pattern6 = pattern[:118] + "/" + pattern[118:]
    pattern7 = pattern[:119] + "|" + pattern[119:]
    pattern8 = pattern[:120] + "\\" + pattern[120:]
    pattern9 = pattern[:138] + "/" + pattern[138:]
    pattern10 = pattern[:140] + "\\" + pattern[140:]
    
    match numError:
        case 1:
            return pattern1
        case 2: 
            return pattern2
        case 3:
            return pattern3
        case 4:
            return pattern4
        case 5:
            return pattern5
        case 6:
            return pattern6
        case 7:
            return pattern7
        case 8:
            return pattern8
        case 9: 
            return pattern9
        case 10:
            return pattern10



def deleteCharAtPos(s, *args):
    count = 0 # count how many occurence of the character have been found found
    indexOfChar = 0
    i = 0
    for val in s:
        indexOfChar += 1
        print(f"val : {val} , args : {args[i]}")
        if val == args[i] and args[i] and type(args[i]) == 'str':
            print(f"val et égal à index de args")
            i += 1
            print(f"val : {val}")
            count += 1
            print(count)
            if args[i] == count:
                print(f"we're in mofo")
                s = s[:indexOfChar-1] + ' ' + s[(indexOfChar):]
    return s
            
while True:
        try:
            difficulty = int(input("Choose the level of difficulty you'd like to play the game \n \n 1 : EASY : Small size words \n 2 : MEDIUM : Medium size words \n 3 : HARD : Long size words \n R : RANDOM \n \n Your answer :  "))
        except ValueError:
            print("Sorry, that is not the expected answer.")
            continue
        if difficulty < 1 or difficulty > 3 :
            print("Answer must be either 1, 2 or 3.")
        if difficulty == "R" or difficulty == "random":
            break
        else:
            break

found = False
hanged = False
counterOfErrors = 0
wordToFind = randomWord(difficulty)
answer = "_ " * len(wordToFind)
print(wordToFind)
    
while play:
    
    while found == False or hanged == False:
        try:
            print("                        "  + pattern.splitlines()[0])
            print("                        "  + pattern.splitlines()[1])
            print("                        "  + pattern.splitlines()[2])    
            print("                        "  + pattern.splitlines()[3]    + "                           " + answer  )
            print("                        "  + pattern.splitlines()[4])
            print("                        "  + pattern.splitlines()[5])   
            print("                        "  + pattern.splitlines()[6])
            print("                        "  + pattern.splitlines()[7]   + "                                                                 " + dictionnary.get(wordToFind))
            print("                        "  + pattern.splitlines()[8])
            
            playerAnswer = str(input(" \n                                         Let's find the word! Write a letter :  " )).lower()
            if playerAnswer in wordToFind:
                letter = wordToFind.find(playerAnswer)
                print(answer[letter], wordToFind[letter])
                listAnswer = list(answer)
                if letter == 0:
                    listAnswer[letter] = wordToFind[letter].upper()
                else:
                    listAnswer[letter * 2] = wordToFind[letter]
                print(listAnswer)
                print(answer)  
                               
                answer = ''.join(listAnswer)
                print(answer)
                
            elif playerAnswer not in wordToFind and len(playerAnswer) == 1:
                counterOfErrors += 1
                pattern = patternError(counterOfErrors)
                print(pattern)
                
            if "_" not in answer:               #OVER
                found == True
                break
            if counterOfErrors == 10:           #OVER, LOST
                hanged == True
                break
           
            
        except ValueError:
            print("Error : Sorry, only accepted characters are letters.")
            continue
        if (len(playerAnswer)) > 1:
            print("Error : Only one letter at a time.")
            continue
        else:
            break

    
        
    
    

    
    # finalPattern = ("  -----------\n" 
    #        "  |         | \n"
    #        "  |         | \n"
    #        "  |         | \n"
    #        "  |         | \n"
    #        "  |         o \n"
    #        "  |        /|\  \n"
    #        "  |        / \ \n"
    #        "__|__\n")

