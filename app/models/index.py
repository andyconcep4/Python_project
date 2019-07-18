def getMeme(question1, question2, question3, question4):
    oldermemes = 0
    animalmemes = 0
    gamermemes = 0
    offensivememes = 0
    
    # question1 = input("Do you like older memes?")
    if question1 == "yes":
        oldermemes = oldermemes + 5
        gamermemes = gamermemes + -1
    elif question1 == "no":
        gamermemes = gamermemes + 5
        oldermemes = oldermemes + -1
    else:
        print ("Sorry, that wasn't a valid answer")
        
        
        
        
        
    # question2 = input("Do you like animals memes?")
    if question2 == "yes":
       animalmemes = animalmemes + 10 
    elif question2 == "no":
        offensivememes = offensivememes + 3
        gamermemes = gamermemes + 3
    else:
        print ("Sorry, that wasn't a valid answer")
    # question3 = input("Do you play videogames?")
    if question3 == "yes":
        gamermemes = gamermemes + 10
        offensivememes = offensivememes + 3
        oldermemes = oldermemes + 2
    elif question3 == "no":
        animalmemes = animalmemes + 3
        gamermemes = gamermemes + -1
    else:
        print ("Sorry, that wasn't a valid answer")
        
    # question4 = input("Do you like offensive memes?")
    if question4 == "yes":
        offensivememes = offensivememes + 10
        gamermemes = gamermemes + 4
    elif question4 == "no": 
        offensivememes = offensivememes + -1
    else:
        print ("Sorry, that wasn't a valid answer")
        
    memefolder = 0
    
    if oldermemes >= animalmemes and oldermemes >= gamermemes and oldermemes >= offensivememes:
        memefolder = oldermemes
        winner = "oldermemes"
    #find some way to link each of the folders to the winners of this survey
        
    elif animalmemes >= oldermemes and animalmemes >= gamermemes and animalmemes >= offensivememes:
        memefolder = animalmemes
        winner = "animalmemes"
    
    elif gamermemes >= memefolder and gamermemes >= offensivememes and gamermemes >= oldermemes:
        memefolder = gamermemes
        winner = "gamermemes"
    elif offensivememes >= gamermemes and offensivememes >= animalmemes and offensivememes >= oldermemes:
        memefolder = offensivememes
        winner = "offensivememes "
    else:
        winner="error"
        
    return (winner) 
    
#######################################################################################   
def getPicture(winner):
    if winner == "gamermemes":
        return "/static/VideogameMeme.jpg"
        
    elif winner == "offensivememe":
        return "/static/offensivememe.jpg"
        
    elif winner == "animalmemes":
        return "/static/animalmeme.jpg"
        
    elif winner == "oldermemes":
        return "/static/oldmeme.jpg"

    
    
    
    
    
    #default
    return "/static/offensivememe.jpg"
    
        