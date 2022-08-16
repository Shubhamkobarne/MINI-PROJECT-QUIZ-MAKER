#------------------------------------------------------------------------------------
def python_quiz():
    guess = []
    correct_guess = 0
    question_n = 1

    for i in question:
        print("----------------------------------------------------------------------")
        print(i)
        for y in options[question_n-1]:
            print(y)
        gues = input("Enter (A,B,C,OR D): ")
        gues = gues.upper()
        guess.append(gues)
        correct_guess += check_answer(question.get(i),gues)
        question_n +=1

    display_score(correct_guess, guess)
#---------------------------------------------------------------------------------------
def check_answer(answer, gues):
    if answer == gues:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0 

#---------------------------------------------------------------------------------------
def display_score(correct_guess, guess):
    print("----------------------------------------------------------------------")
    print("RESULT")
    print("----------------------------------------------------------------------")
    
    print("Answers: ", end="")
    for i in guess:
        print(i,end="")
    print()

    score = int((correct_guess/len(question))*100)
    print("Your score is: "+str(score)+"%")
        
    
#---------------------------------------------------------------------------------------

question = {
"What is output for raining'. find('z') ?: ":"C",
"What is output for following code,y = [4, 5,1j],y.sort(): ":"D",
"Syntax error in python is detected by _________at _______: ":"B",
"Which of the following is more accurate for the following declaration?,x = Circle(): ":"B",
"Which among them is correct(s) about Recursive Function?: ":"B",
"Select the correct function among them which can be used to write the data to perform for a binary output?: ":"C",
"Select the valid option for the following Output,Hello Canvas: ":"B",
"Best part is you can display images in various options in Python. Select the option where you can display an image: ":"D"
}

options = [["A - Type error","B - ' '","C - -1","D - Not found"],
           ["A - [1j,4,5]","B - [5,4,1j]","C - [4,5,1j]","D - Type Error"],
           ["A - compiler/ compile time","B - interpreter/ run time","C - compiler/ run time","D - interpreter/ compile time"],
           ["A - Now you can assign int value to x","B - x contains a reference to a Circle object","C - x actually contains an object of type Circle","D - x contains an int value"],
           ["A - They are much faster than the normal functions","B - They take more space then the non-recursive functions"],
           ["A - Write","B - Output.binary","C - Dump","D - Binary.output"],
           ["A - Canvas.Create_text(text= ''Hello! '')","B - Canvas.Create_text(30 , 40, text= ''Hello! '' ,filled= ''green '')","C - Canvas.Create_text(text= ''Hello! '' ,textcolor= ''Green'')","D - Canvas.Create_text(30 , 40, text= ''Hello!'')"],
           ["A - Only A label","B - Only A button and A label","C - Only A checkbox","D - A label, a check box , a button and a radio button"]]
python_quiz()
