## Copyright 2019-2024 Azariel Del Carmen (bronya_rand). All rights reserved.

# gallery.rpy
# This file contains the code for the gallery menu that shows backgrounds and 
# sprites from your mod.

default persistent.gallery_imgs = {}

init -2 python in gallery:
    from store import Transform, persistent, config, Hide, Composite
    import os
    import renpy.display.image as imgcore
    galleryList = {} 

    # This class declares the code to make a image for the gallery menu.
    # Syntax:
    #   image - This variable contains the path or image tag (sayori 1a) of the 
    #       image.
    #   small_size - This variable contain the path or image tag of a shorten version
    #       of the image in the gallery.
    #   name - This variable contains the human-readable name of the image in the
    #       gallery.
    #   artist - This variable contains the human-readable author name of the image.
    #   sprite - This variable checks if the image declared is a character sprite.
    #   already_unlocked - This variable makes sure the image is unlocked already when 
    #       the game is launched.
    #
    # To unlock an image, simply do `$ X.unlock()` (without the `'s where X is your gallery image' variable name).
    class GalleryImage:

        def __init__(self, image, small_size=None, name=None, artist=None, sprite=False, already_unlocked=False):
            # The image variable name in-game
            self.file = image

            # The human readable name of the image
            if name: self.name = name
            else: self.name = image

            if self.name not in persistent.gallery_imgs:
                persistent.gallery_imgs[self.name] = {
                    "unlocked": True if already_unlocked else False
                }

            # The human readable author of the image
            self.artist = artist

            # This condition sees if the image given is a sprite
            self.sprite = sprite

            self.unlocked = persistent.gallery_imgs[self.name]['unlocked']

            if sprite:
                self.image = Composite(
                    (config.screen_width, config.screen_height), (0, 0), 
                    "black", (0.2 * (config.screen_width / 1280.0), 0), 
                    Transform(image, zoom=0.75*0.95)
                )

                # A descaled version of the main image.
                if small_size:
                    self.small_size = small_size 
                else:               
                    self.small_size = Composite(
                        (234, 132), (0, 0), 
                        "black", (0.2, 0), 
                        Transform(image, zoom=0.137)
                    )
            else:
                self.image = Transform(image, size=(config.screen_width, config.screen_height-40))

                if small_size:
                    self.small_size = small_size 
                else:     
                    self.small_size = Transform(image, size=(234, 132))

            galleryList[self.name] = self
        
        def unlock(self):
            self.unlocked = True
            persistent.gallery_imgs[self.name]['unlocked'] = True

        # This function exports the selected image to the players' computer.
        def export(self):
            if renpy.android:
                try: os.mkdir(os.environ['ANDROID_PUBLIC'] + "/gallery")
                except: pass
            else:
                try: os.mkdir(config.basedir + "/gallery")
                except: pass

            if self.sprite: renpy.show_screen("dialog", message="Sprites cannot be exported to the gallery folder. Please try another image.", ok_action=Hide("dialog"))
            else:
                try: 
                    renpy.file(self.file)
                    export = self.file
                except:
                    export = self.get_registered_image().filename
                    
                if renpy.android:
                    with open(os.path.join(os.environ['ANDROID_PUBLIC'], "gallery", os.path.splitext(export)[0].split("/")[-1] + os.path.splitext(export)[-1]), "wb") as p:
                        p.write(renpy.file(export).read())
                else:
                    with open(os.path.join(config.basedir, "gallery", os.path.splitext(export)[0].split("/")[-1] + os.path.splitext(export)[-1]).replace("\\", "/"), "wb") as p:
                        p.write(renpy.file(export).read())

                    renpy.show_screen("dialog", message='Exported "%s" to the gallery folder.' % self.name, ok_action=Hide("dialog"))
        
        # For Ren'Py 6 compatibility. This function gets the image displayed in the
        # gallery from from 'renpy.display.image'.
        def get_registered_image(self): 

            if not isinstance(self.name, tuple):
                name = tuple(self.name.split())

            return imgcore.images.get(name)

init python:
    current_img_name = None
    # This function advances to the next/previous image in the gallery.
    def next_image(back=False):
        global current_img_name

        # Create a new list from the keys
        all_keys = [k for k, v in galleryList.items() if v.unlocked]

        # Get the current key as index
        current_index = all_keys.index(current_img_name)

        # Get the next key as index
        next_index = current_index - 1 if back else current_index + 1

        try: 
            all_keys[next_index]
            current_img_name = all_keys[next_index]
        except IndexError: current_img_name = all_keys[0]

    # This section declares the images to be shown in the gallery. See the
    # 'GalleryMenu' class syntax to declare a image to the gallery.
    residential = gallery.GalleryImage("bg residential_day", already_unlocked=True)
    s1a = gallery.GalleryImage("sayori 1", sprite=True, already_unlocked=True)
    m1a = gallery.GalleryImage("monika 1", name="Monika", artist="Satchely", sprite=True)

    # Fast Sort (DO NOT REMOVE)
    gallery.galleryList = {k: gallery.galleryList[k] for k in sorted(gallery.galleryList)}




