#Automatic Image Defining Script
init python:
    config.automatic_images = ['_', '/']
    config.automatic_images_strip = ["images"]
    config.side_image_tag = "milo"

##Better ALT------------------------------------------------------------------------------------------------------
transform better_left:
    align (0.2, 1.0)
transform better_less_left:
    align (0.1, 1.0)
transform better_right:
    align (0.65, 1.0)
transform better_less_right:
    align (0.90, 1.0)
transform kinda_middle:
    xalign 0.40 yalign 1.0

