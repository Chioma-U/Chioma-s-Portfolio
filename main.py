#APIs
import webbrowser
import JarvisAI
import pyttsx3
import random
import time
import pyjokes
import os
import playsound as ps


a=5
bot_name="Chimto"




obj = JarvisAI.JarvisAssistant()




#Code and functions :)
while a>0:
    #Playing Songs
    def sound():
        import os
        os.startfile("C:\\Users\\gugwunze\\Music\\Playlists\\MosesMusic.mp3")
        ps.playsound("C:\\Users\\gugwunze\\Music\\Playlists\\MosesMusic.mp3")

    #Game
    def game():
        while True:
            choices = ["rock", "paper", "scissors"]
            engine.say(choices)
            engine.runAndWait()
            engine.stop()

            computer = random.choice(choices)
            player = None

            while player not in choices:
                player = input("rock, paper, or scissors?: ").lower()
                engine.say("rock paper or scissors")
                engine.runAndWait()
                engine.stop()

            if player == computer:
                print("computer: ", computer)
                print("player: ", player)
                print("Tie!")
                engine.say("tie")
                engine.runAndWait()
                engine.stop()


            elif player == "rock":
                if computer == "paper":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("You lose!")
                    engine.say("you lose")
                    engine.runAndWait()
                    engine.stop()

                if computer == "scissors":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("You win!")
                    engine.say("you win")
                    engine.runAndWait()
                    engine.stop()


            elif player == "scissors":
                if computer == "rock":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("You lose!")
                    engine.say("you lose")
                    engine.runAndWait()
                    engine.stop()

                if computer == "paper":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("You win!")
                    engine.say("you win")
                    engine.runAndWait()
                    engine.stop()


            elif player == "paper":
                if computer == "scissors":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("You lose!")
                    engine.say("you lose")
                    engine.runAndWait()
                    engine.stop()

                if computer == "rock":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("You win!")
                    engine.say("you win")
                    engine.runAndWait()
                    engine.stop()

            engine.say("do you want to play again?")
            engine.runAndWait()
            engine.stop()
            play_again = input("(yes/no):").lower()

            if play_again != "yes":
                break

        engine.say("bye")
        engine.runAndWait()
        engine.stop()


    def open():
        if "powerpoint" in q:
            os.startfile(r"C:\ProgramData\Microsoft\Windows\StartMenu\Programs\Microsoft Office 2013\Powerpoint 2013.EXE")

        if "chrome" in q:
            os.startfile("C:\Program Files (x86)\Google\Chrome\Application")


    response = obj.mic_input()
    answer = response
    string = answer
    engine = pyttsx3.init()




    # responses

    greetings = ["Hi there!", "How can I be of help?", "Hello!","What can I do for you?"]
    age = ["I am 14 years old", "I have existed for fourteen years surprisingly",
           "I may not be older than you, I am 14 years old"]
    name = ["My name is Chioma", "You can call me Chioma", "I go by Chioma",
            "My friends call me Chiomy, but my name is Chioma"]
    gender = ["I am female","I identify as a female, but.. you know.. I am a bot!"]
    goodbye = ["talk to you later", "bye", "It was fun talking to you, see you later!"]
    reason = ["I am your virtual assistant", "I can do a lot of things like tell you the date and time, tell you a joke, sing you a song, open an application for you, google something, and also play rock paper scissors with you!",]




    # input dictionary
    response_g = ["hi", "hello", "hey", "what's up", "whats up","sup","hey Chioma"]
    response_a = ["how old are you", "what is your age", "how long have you existed",]
    response_s = ["what is your gender", "what is your sex", "are you a female","are you a male","what do you identify as"]
    response_reason = ["why were you built", "what do you do", "what can you do","what do you know how to do"]
    response_b = ["it was fun talking to you, bye"]




    # Actual Conditions
    if string in response_g:
        meh = (random.choice(greetings))
        engine.say(meh)
        engine.runAndWait()
        engine.stop()
        print ("Bot:", meh,)



    elif string in response_a:
        meh_two = (random.choice(age))
        engine.say(meh_two)
        engine.runAndWait()
        engine.stop()
        print("Bot:" ,meh_two,)



    if  "name" in string:
        meh_three =(random.choice(name))
        engine.say(meh_three)
        engine.runAndWait()
        engine.stop()
        print("Bot:", meh_three, )


    elif string in response_s:
        meh_four = (random.choice(gender))
        engine.say(meh_four)
        engine.runAndWait()
        engine.stop()
        print("Bot:", meh_four, )



    elif "bye" in string:
        meh_five = (random.choice(goodbye))
        engine.say(meh_five)
        engine.runAndWait()
        engine.stop()
        print("Bot:", meh_five, )


    if string in response_reason:
        meh_six = (random.choice(reason))
        engine.say(meh_six)
        engine.runAndWait()
        engine.stop()
        print("Bot:", meh_six, )

    if "time" in string:
        meh_se = (time.asctime())
        engine.say(meh_se)
        engine.runAndWait()
        engine.stop()
        print("Bot:", meh_se, )


    if "joke" in string:
        jokes = pyjokes.get_joke()
        engine.say(jokes)
        engine.runAndWait()
        engine.stop()
        print("Bot:",jokes, )

    if "play" in string:
        sound()

    if "open" in string:
        so =input("Sorry what app should I open again")
        engine.say(so)
        engine.runAndWait()
        engine.stop()
        q=input("Type here:")
        open()



    if "search" in string:
        sea=("what do you wan to search for?")
        engine.say(sea)
        engine.runAndWait()
        engine.stop()
        sea = ("Sorry I couldn't get that please could you type it in")
        engine.say(sea)
        engine.runAndWait()
        engine.stop()
        se = input ("type here:")
        webbrowser.open('https://www.bing.com/search?q='+se)

        mah = ("here is what I found")
        engine.say(mah)
        engine.runAndWait()
        engine.stop()


    if "game" in string:
        game()


    if "science teacher" in string:
        te =(" its miss anne.. and mister baankoohlayh..  by the way. hi mister baankoohlayh .. i see you out there")
        engine.say(te)
        engine.runAndWait()
        engine.stop()
        print("Bot:Ms. ane and Mr. Bankole" )


    if "school" in string:
        te =("The name my school is. Meadowlands Canadian School ")
        engine.say(te)
        engine.runAndWait()
        engine.stop()
        print("Bot:Ms. ane and Mr. Bankole" )

    if "favourite food" in string:
        lo =("ohfen sala and pounded yam is by far my favourite food")
        engine.say(lo)
        engine.runAndWait()
        engine.stop()
        print("Bot:",lo, )

    if "recite" in string:
        ko =(" I am strong in the lord and in the power of his might. I put on the whole armour of God that I am able to stand against the wiles of the enemy, I put on the whole armour of God so that I'm able to stand in the evil days, and having done all to stand.  Amen ")
        engine.say(ko)
        engine.runAndWait()
        engine.stop()
        print("Bot:",ko, )


    if "slogan" in string:
        do =(" What God cannot do! Those not What.   Exist !")
        engine.say(do)
        engine.runAndWait()
        engine.stop()
        print("Bot:",do, )



    else:
        if (a == 2):
            break
        print("")

        if "anything to say" in string:
            po = ("Bye everyone. Its been a pleasure talking to you all")
            engine.say(po)
            engine.runAndWait()
            engine.stop()
            print("Bot:", po, )
            break
