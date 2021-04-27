#This is the beggining of the script for the game 3amMilo.

#Characters---------------------
define c = Character("Corie", image = "corie")
define ca = Character("Cara", image = "cara")
define m = Character("Milo", image = "milo")
image side milo nuetral = "milo/nuetral.png"
#Script-------------------------
label start:
    
    scene m room
    show cara nuetral 
    ca "Welcome to the Sandbox Development Build of 3amMilo."
    ca "Added 2 new backgrounds and one fullbody sprite for reference."
    m nuetral "As well as this, is a place holder side sprite for Milo."
    ca "You can acess these files via the automatic names given. Cara's room is {b}c bed{/b} , Milo's room is {b}m room{/b}, and Cara's sprites are {b}cara nuetral.{/b}"
    return
