#This is the beggining of the script for the game 3amMilo.

#Characters---------------------
define c = DynamicCharacter("Corie", image = "corie")
define ca = Character("Cara", image = "cara")
define m = Character("Milo", image = "milo")
image side milo nuetral = "milo/nuetral.png"

##Variables (This will determine the ending)------
$ coriepoints = 0
#Script-------------------------
label start:

    scene m room with fade
    $ renpy.set_tag_attributes("milo nuetral")
    "Good ol’ canada."
    "I’ve lived here my entire life, raised in Quebec then moved to Toronto for uni."
    "Brought up by chinese parents, my name is Milo Zhang and I’m in my sophomore year of university."
    "For the 2 years since I’ve been in Toronto, I’ve always stuck to a strict routine."
    "My roommate Cara wakes me up at exactly 6 am, we’ve been bestfriends since the good old days of middle school. "
    "The mechanical pencils, worrying about what binder to use for 8th grade geometry and what colour suited science the best."
    "By the way, green is science."
    show cara nuetral with dissolve
    ca "Psst… Milooooooo… it’s 9 am.."
    m nuetral "Cara, you do this every time, did you think I was gonna fall for it?"
    ca "Worth a try. I wonder why you still need me to wake you up.."
    m "‘Cos it’s convenient, my little alarm clock"
    ca "I am not little! You’re just too damn tall." ##[pouting]
    m "Mhm, keep telling yourself that. You have the opening shift at 8."
    m "You know how long you take to get ready."
    ca "Shut up, I do not take ages."
    m "Uh hello? Spring formal? You spent at least 3 hours getting your dress fitted."
    m "We ended up not going because by the time you decided you liked how you looked, it already ended."
    ca "Fine! Point taken, I’ll take my leave now. À plus tard... dans 1 heure (See you later… in 1 hour)."
    m "Ah mais bien sûr mademoiselle. (Ah but of course miss)."
    hide cara with dissolve
    "And that’s how it is between Cara and I."
    "Nothing has ever been awkward between us in our 10 years of friendship. We’ve always been there for eachother, we’ve shared experiences and related to each other's experiences of being a part of a minority group."
    "Our friendship meant everything to me, especially when I came out as trans."
    "I remember that moment vividly as if it were yesterday, sophomore year of highschool."
    "We were at our favourite cafe, I remember building up the courage, planning out what I was going to say."
    "I remember the dread I felt, worrying about her reaction, already accepting that she’d reject me and stop being friends with me. But I was wrong."
    "I will never forget the way she hugged me, the way she whispered “I’m proud of you” as I started sobbing silently on her shoulder while she held me in her embrace."
    "She was there when I came out to my parents as well, she held my hand as I slowly let the words flow. If it weren’t for Cara.."
    "I don’t think I would have the courage to tell my parents anything. "
    "I remember when people used to think we were dating in highschool, although I do admit, I did have the smallest crush on Cara."
    "But it went away after a week when I realised that we were better off as friends."
    ca "MILOOOOOO!!"
    scene livingroom with fade
    show cara nuetral with dissolve
    $ renpy.set_tag_attributes("milo nuetral")
    m nuetral "Jesus Cara, do you have to scream at 6 am?"
    ca "Yes because do you hear that?"
    ##SOUNDS OF MUFFLED FOOTSTEPS - BOXES DROPPING
    m "Oh, new neighbour perhaps? Or maybe someone from our block is moving out."
    ca "Someone’s definitely moving in!" ##[excited]
    m "...And you know this how?"
    ca "Listen to where the footsteps are leading to! And where the heavy items are being dropped by."
    ca "The walls here suck, we both know that."
    m "Just get changed Cara, I don’t know why you’re so excited over this."
    ca "I am excited because someone’s obviously moving into the luxury apartment!"
    ca "They must have crazy money, and I need me sugar mommy."
    m "Some days, I wonder why you are like this.."
    ca "Oh come onnnnn.. you love me, truly."
    "Cara batted her eyelids at me while she puckered her lips. I scoffed, laughing at the sight of her."
    m "We'll see if your thesis is correct Detective Hoang, after you get changed."
    ca "So do you wanna check it out? Come on Milo I know you want to."
    m "Maybe. "
    "The truth was I was just as curious as Cara to find out who exactly was moving into the luxury apartment."
    "It hadn't been filled since freshman year, and seeing how Toronto prices are, the last owners must have been rich."
    "I wondered what type of personality would be moving in."
    m "Okay fine."
    ca "So it's a date! See you then Mr Zhang.." ##exicted
    "Cara batted her eyelids once more while pointing finger guns at me, she truly was a piece of work."
    scene m room with fade
    $ renpy.set_tag_attributes("milo nuetral")
    "I slowly walked back into my room, stumbling over a few notebooks that I needed for today's classes."
    "In uni, I decided to major in Psychology whilst minoring in biology. It's a rough study, psychology, but I'm used to it." 
    "After all, I am in my sophomore year, in a year's time I'll be graduating."
    "Soon enough we got ready, and headed for classes. "
    "I met Cara by the door and we headed out, and went down to the elevator to make our usual walk to campus. "
    scene recep with fade
    $ renpy.set_tag_attributes("milo nuetral")
    show cara nuetral at better_left with dissolve
    show corie nuetral at better_right with dissolve
    "When suddenly we heard the liveliness coming from the reception that probably shouldn't be due until later this morning.." 
    $ Corie = "???"
    c "I thought I saw on the contract that we could keep pets?"
    "Reception" "I'm sorry, that's not allowed."
    c "What do you mean by that?"
    "I couldn't help but eavesdrop onto the mysterious figure arguing with the receptionist, Miss Margot. "
    "Cara also seemed to be intrigued as she stopped next to me and clung onto my shoulder."
    "Reception" "I'm sorry Mr Rosario, but this complex has strictly no pets allowed."
    "Reception" "Just because your parents have paid a greater amount for our luxury apartment doesn't mean you are exempt from this condition."
    c "Then what do I do with them ?? Are you really going to make me abandon my babies? "
    "Reception" "That's on you now."
    "I looked to my side, making eye contact with Cara. Before I could say anything, I looked back to the frustrated cat lover, who was now looking towards our direction. "
    "Or more so, me."
    "I observed the new person, as they sighed reluctance."
    c "I'll come back soon."
    "Reception" "Thank you for understanding. "
    "But the new person didn't exactly look like they 'understood'."
    hide corie nuetral with dissolve
    show cara nuetral at center with ease
    "They simply stormed out of the building, both hands holding cat carriers, like they were prized luggage."
    ca "So that's the new person moving in. What do you think of them Milo?"

    menu:
        "They're interesting.": 
            m "I think it might add something new here. "
            ca "Well someone has to see the positives in a situation. "

        "I think they might cause some problems.":
            "Cara raised an eyebrow. But simply nodded."

        "They're hot not gonna lie.": 
            "Cara's eyes widened. Her mouth formed into a small pout."
            ca "Oh?"

    m "Either way, we don't have time for this. You have your shift at the cat cafe, I need to pick up my food and quickly get to campus somehow.."
    ca "Yeah yeah, whatever. You're such a killjoy, Milo. "
    "Cara stuck her tongue out and blew a raspberry, she then started to speed walk, leaving me behind. "
    m "You are such a baby carssss wait up !!"
    scene uni with fade
    $ renpy.set_tag_attributes("milo nuetral")
    "We got to the cat cafe and I dropped Cara off, and in exchange I got my usual order, a brownie and an iced coffee, before getting into campus." 
    ca "See ya later at lunch?"
    m "Mhm, get to class in time, I can help you study."
    "I arrived just in time for my first class of the day, rushing into the lecture hall without much grace."
    "The packed lecture hall was less than desired but it was enough. Soon the day rolled past and I met up with Cara again just in time for both of our breaks."
    "I saw her sit at our usual spot at the back of the lunch hall. She gave a insistant wave down."
    ca "Over here!"


label test:
    scene co bed with fade
    show corie nuetral with dissolve
    "The inside of their room smelt like..."
    m nuetral "Cat litter?"
    c "Uh-- shit, I forgot to clean it didn't I?"
    "I tried to stifle my laughter at their use of the word 'shit'. This was not the time for that. But somehow, someway, a chuckle escaped me."
    c "What? Did something happen?"
    m "No! Nothing's happened. Yet."
    "They breathed in a long and frustrated sigh."
    c "Look, I brought you here so we could find how to let the landlords know these guys are in here. Not to..laugh at whatever you're laughing at."
    return
