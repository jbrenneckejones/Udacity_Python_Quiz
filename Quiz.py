
Difficulties = [ "Easy", "Medium", "Hard" ]

SentencePlace = [ "___1___" , "___2___" , "___3___" , "___4___" ]

SentencesList = [ 
          "I meant what I ___1___ And I said what I ___2___ An ___3___ s faithful One hundred per ___4___ ! " 
        , "I do ___1___ like them, Sam-I-am. I do not ___2___ green ___3___ and ___4___ . " 
        , "Don't ___1___ because it's ___2___. Smile because it ___3___ . - Dr. ___4___"]

AnswersList = [
          [ "said" , "meant" , "elephant", "cent" ]
        , [ "not" , "like" , "eggs" , "ham" ] 
        , [ "cry" , "over" , "happened" , "Suess" ] ]

def GetDifficulty():
    """ Asks the user for input then returns the index number of 
        that difficulty in the difficulty list, if it doesn't find
        it then it repeats the process. 
        Argument : void
        return : Difficulty index number """

    Input = raw_input("What difficulty? Easy, Medium, or Hard \n")

    CurrentDifficulty = 0
    while not Input in Difficulties:
            Input = raw_input("I'm sorry I didn't get that difficulty, can you try again? \n")

    return CurrentDifficulty

def Quiz():
    """ Asks the user for input for their difficulty then uses that index to
        get the type of answers and sentence to use. Then it prints the SentencePlace
        to the screen and asks the user to fill in each blank. When the index is less
        than the answers length and it equals one of our sentence place then we prompt
        for input. After the program ends we prompt one more time to play again then 
        we call this function.
        Argument : void
        return : void """

    Difficulty = GetDifficulty()
    Answers = AnswersList[Difficulty]
    Sentence = SentencesList[Difficulty]

    SplitSentence = Sentence.split()

    Index = 0

    print(Sentence)

    for Word in SplitSentence:
        if Index < len(SentencePlace) and Word == SentencePlace[Index]:
            Input = raw_input("What goes at " + SentencePlace[Index] + " \n")
            while Input != Answers[Index]:
                Input = raw_input("Try again \n")
            Sentence = Sentence.replace(Word, Answers[Index])
            Index += 1
            print("\n\n" + Sentence)

    print("\n\nCongratulations!!!")

    Input = raw_input("\nTry again? y or n \n")

    if Input == "y":
        Quiz()
    else:
        return

Quiz()