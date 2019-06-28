def quiz1results(answer1, answer2):
    freqexp = ""
    selfw = ""
    level = ""
    text = ""
    ## Tree that determines level and text
    if int(answer1) == 4:
        level = 0
        text = "Great job!"
        image = "https://media2.giphy.com/media/cEODGfeOYMRxK/giphy.gif"
    elif int(answer1) + int(answer2) <= 14 and int(answer1) + int(answer2) >= 10:
        level = 1
        text = "It will be pretty easy for you to convert to vegetariansism."
        image = "https://ecommerceinsiders.com/wp-content/uploads/2014/12/press-the-easy-button.jpg"
    elif int(answer1) + int(answer2) <= 9 and int(answer1) + int(answer2) >= 5:
        level = 2
        text = "It will be somewhat easy for you to convert to vegetariansism, but you will face some difficulties."
        image = "https://static01.nyt.com/images/2019/06/13/dining/aw-large-mushroom-shawarma/aw-large-mushroom-shawarma-articleLarge.jpg"
    elif int(answer1) + int(answer2) <= 4:
        level = 3
        text = "It will be pretty difficult for you to convert to vegetariansism."
        image = "https://media0.giphy.com/media/3o7WIpD2wiA4qNyqMU/giphy.gif"
    if int(answer1) == 4:
        freqexp = "You are already vegetarian!"
    elif int(answer1) == 1:
        freqexp = "Your current meat consumption is where you will struggle. You eat meat very frequently and are attached to it, which will make much more difficult to remove yourself from it."
    elif int(answer1) == 2:
        freqexp = "You eat meat somewhat frequently, which will make it more difficult to remove yourself from meat, but this obstacle is manageable."
    elif int(answer1) == 3:
        freqexp = "You barely eat meat, which will make very easy for you te eliminate it from your diet completely."
    if int(answer1) == 4:
        selfw = "Just continue to exercize strong self will to retain your current virtue!"
    elif int(answer2) >=8:
        selfw = "You have very strong self will, which will allow you to pull yourself aay from meat if your passion to do so is strong enough (take our our other quiz to find out!) despite how much you love it."
    elif int(answer2) >=4 and int(answer2) <=7:
        selfw = "You have moderately strong self will, which will definitely help you eliminate meat from your diet, but you will probably have to try to exercize even stronger self will to be successful in your vegetarianism."
    elif int(answer2) <=3:
        selfw = "You don't have strong self control, which will make it pretty difficult to move away from meat. But if your passion is strong enough you can overcome this obstacle. "
    ## tree that determines 
    return [level, text, freqexp, selfw, image]