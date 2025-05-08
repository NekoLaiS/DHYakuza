
layeredimage natsuki:
    
    group outfit:
        attribute uniform default null
        attribute casual null
    
    
    
    group mood:

        attribute neut default null 
        attribute angr null 
        attribute anno null 
        attribute cry null  
        attribute curi null 
        attribute dist null
        attribute doub null
        attribute flus null 
        attribute happ null
        attribute laug null 
        attribute lsur null 
        attribute nerv null 
        attribute pani null 
        attribute pout null
        attribute sad null 
        attribute sedu null 
        attribute shoc null 
        attribute vang null 
        attribute vsur null 
        attribute worr null 
        attribute yand null 
       
    
    
    
    group blush:
        attribute nobl default null
        attribute awkw null
        attribute blus null
        attribute blaw null 
        attribute bful null 
    
    
    
    group left: 
        anchor (0,0) subpixel (True)
        yoffset (-0.5)
        attribute ldown default if_any(["uniform"]):
            paths.natsuki("bases", "turned", "uniform_left_down")
        attribute ldown default if_any(["casual"]):
            paths.natsuki("bases", "turned", "casual_left_down")
        attribute lhip if_any(["uniform"]):
            paths.natsuki("bases", "turned", "uniform_left_hip")
        attribute lhip if_any(["casual"]):
            paths.natsuki("bases", "turned", "casual_left_hip")
        attribute lpoint if_any(["uniform"]):
            paths.natsuki("bases", "turned", "uniform_left_point")
        attribute lpoint if_any(["casual"]):
            paths.natsuki("bases", "turned", "casual_left_point")
    
    
    
    group right:
        anchor (0,0) subpixel (True)
        yoffset (-0.5)
        attribute rdown default if_any(["uniform"]):
            paths.natsuki("bases", "turned", "uniform_right_down")
        attribute rdown default if_any(["casual"]):
            paths.natsuki("bases", "turned", "casual_right_down")
        attribute rhip if_any(["uniform"]):
            paths.natsuki("bases", "turned", "uniform_right_hip")
        attribute rhip if_any(["casual"]):
            paths.natsuki("bases", "turned", "casual_right_hip")
    
    
    
    group head: 
        
        anchor (0,0) subpixel (True)
        
        attribute ff default:
            paths.natsuki("bases", "face_forward")
        
        attribute fs:
            paths.natsuki("bases", "face_sad")
        
        attribute fta:
            paths.natsuki("bases", "face_turnedaway")
    
    
    
    
    
    group nose if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        
    
        attribute nose default if_any(["nobl"]):
            "nat_ff_n1"
        attribute nose if_any(["awkw"]):
            "nat_ff_n2"
        attribute nose if_any(["blus"]):
            "nat_ff_n3"
        attribute nose if_any(["blaw"]):
            "nat_ff_n4"
        
        
        
    
        attribute n1:
            "nat_ff_n1"
        attribute n2:
            "nat_ff_n2"
        attribute n3:
            "nat_ff_n3"
        attribute n4:
            "nat_ff_n4"
    
    
    
    
    group mouth if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        
    
        attribute cm default if_any(["happ","sedu","nerv"]):
            "nat_ff_ma"
        attribute cm default if_any(["neut","anno","worr","lsur"]):
            "nat_ff_md"
        attribute cm default if_any(["pout","curi"]):
            "nat_ff_me"
        attribute cm default if_any(["flus","shoc"]):
            "nat_ff_mg"
        attribute cm default if_any(["sad","angr","vsur","dist","doub"]):
            "nat_ff_mj"
        attribute cm default if_any(["vang","pani","cry"]):
            "nat_ff_mm"
        attribute cm default if_any(["yand"]):
            "nat_ff_mn"
        attribute cm default if_any(["laug"]):
            "nat_ff_mo"
        
    
        attribute om if_any(["sedu","nerv","yand"]):
            "nat_ff_mb"
        attribute om if_any(["happ","laug"]):
            "nat_ff_mc"
        attribute om if_any(["sad","anno","worr","lsur","dist","pout"]):
            "nat_ff_mg"
        attribute om if_any(["neut","curi"]):
            "nat_ff_mh"
        attribute om if_any(["doub","angr","vsur"]):
            "nat_ff_mi"
        attribute om if_any(["flus","shoc"]):
            "nat_ff_ml"
        attribute om if_any(["cry","vang","pani"]):
            "nat_ff_mq"
        
        

        attribute ma:
            "nat_ff_ma"
        attribute mb:
            "nat_ff_mb"
        attribute mc:
            "nat_ff_mc"
        attribute md:
            "nat_ff_md"
        attribute me:
            "nat_ff_me"
        attribute mf:
            "nat_ff_mf"
        attribute mg:
            "nat_ff_mg"
        attribute mh:
            "nat_ff_mh"
        attribute mi:
            "nat_ff_mi"
        attribute mj:
            "nat_ff_mj"
        attribute mk:
            "nat_ff_mk"
        attribute ml:
            "nat_ff_ml"
        attribute mm:
            "nat_ff_mm"
        attribute mn:
            "nat_ff_mn"
        attribute mo:
            "nat_ff_mo"
        attribute mp:
            "nat_ff_mp"
        attribute mq:
            "nat_ff_mq"
        attribute mr:
            "nat_ff_mr"
    
    
    
    group eyes if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        

        attribute oe default if_any(["neut","happ","laug","pout","curi"]):
            "nat_ff_e1a"
        attribute oe default if_any(["sad","worr","flus","dist"]):
            "nat_ff_e1b"
        attribute oe default if_any(["anno","sedu","doub"]):
            "nat_ff_e1d"
        attribute oe default if_any(["cry"]):
            "nat_ff_e1g"
        attribute oe default if_any(["angr","lsur","nerv"]):
            "nat_ff_e2a"
        attribute oe default if_any(["vang","vsur","pani","shoc"]):
            "nat_ff_e2d"
        attribute oe default if_any(["yand"]):
            "nat_ff_e3a"
        
    
        attribute ce if_any(["sad","worr","anno","angr","vang","vsur","flus","dist","sedu","nerv","doub"]):
            "nat_ff_e4a"
        attribute ce if_any(["neut","happ","laug","lsur","yand","pout","curi"]):
            "nat_ff_e4b"
        attribute ce if_any(["shoc","pani"]):
            "nat_ff_e4c"
        attribute ce if_any(["cry"]):
            "nat_ff_e4e"
        

        attribute e1a:
            "nat_ff_e1a"
        attribute e1b:
            "nat_ff_e1b"
        attribute e1c:
            "nat_ff_e1c"
        attribute e1d:
            "nat_ff_e1d"
        attribute e1e:
            "nat_ff_e1e"
        attribute e1f:
            "nat_ff_e1f"
        attribute e1g:
            "nat_ff_e1g"
        attribute e1h:
            "nat_ff_e1h"
        attribute e2a:
            "nat_ff_e2a"
        attribute e2b:
            "nat_ff_e2b"
        attribute e2c:
            "nat_ff_e2c"
        attribute e2d:
            "nat_ff_e2d"
        attribute e3a:
            "nat_ff_e3a"
        attribute e3b:
            "nat_ff_e3b"
        attribute e4a:
            "nat_ff_e4a"
        attribute e4b:
            "nat_ff_e4b"
        attribute e4c:
            "nat_ff_e4c"
        attribute e4d:
            "nat_ff_e4d"
        attribute e4e:
            "nat_ff_e4e"
        attribute e0a:
            "nat_ff_e0a"
        attribute e0b:
            "nat_ff_e0b"
    
    
    
    group brows if_all(["ff"]) if_not(["fta","fs"]): 
        
        anchor (0,0) subpixel (True)
        
        attribute brow default if_any(["neut","dist","sedu"]):
            "nat_ff_b1a"
        attribute brow default if_any(["sad","pani","flus","pout","nerv"]):
            "nat_ff_b1b"
        attribute brow default if_any(["happ","worr","shoc"]):
            "nat_ff_b1c"
        attribute brow default if_any(["curi","doub"]):
            "nat_ff_b1f"
        attribute brow default if_any(["lsur"]):
            "nat_ff_b2a"
        attribute brow default if_any(["cry","vsur"]):
            "nat_ff_b2c"
        
        
        
    
    group brows:
        
        anchor (0,0) subpixel (True)
        
        attribute brow default if_any(["vang"]) if_all(["ff","oe"]) if_not(["fta","fs","ce"]):
            "nat_ff_b1d"
        attribute brow default if_any(["vang"]) if_all(["ce","ff"]) if_not(["fta","fs","oe"]):
            "nat_ff_b3a"
        attribute brow default if_any(["laug"]) if_all(["ff","oe"]) if_not(["fta","fs","ce"]):
            "nat_ff_b1b"
        attribute brow default if_any(["laug"]) if_all(["ce","ff"]) if_not(["fta","fs","oe"]):
            "nat_ff_b3a"
        attribute brow default if_any(["yand"]) if_all(["ff","oe"]) if_not(["fta","fs","ce"]):
            "nat_ff_b2a"
        attribute brow default if_any(["yand"]) if_all(["ce","ff"]) if_not(["fta","fs"]):
            "nat_ff_b3c"
        attribute brow default if_any(["anno","angr"]) if_all(["ff","oe"]) if_not(["fta","fs","ce"]):
            "nat_ff_b1d"
        attribute brow default if_any(["anno","angr"]) if_all(["ce","ff"]) if_not(["fta","fs"]):
            "nat_ff_b3b"
    
    
    
    group brows:
        
        anchor (0,0) subpixel (True)
        

        attribute b1a if_all(["ff"]) if_not(["fta","fs"]):
            "nat_ff_b1a"
        attribute b1b if_all(["ff"]) if_not(["fta","fs"]):
            "nat_ff_b1b"
        attribute b1c if_all(["ff"]) if_not(["fta","fs",]):
            "nat_ff_b1c"
        attribute b1d if_all(["ff"]) if_not(["fta","fs"]):
            "nat_ff_b1d"
        attribute b1e if_all(["ff"]) if_not(["fta","fs"]):
            "nat_ff_b1e"
        attribute b1f if_all(["ff"]) if_not(["fta","fs"]):
            "nat_ff_b1f"
        attribute b2a if_all(["ff"]) if_not(["fta","fs"]):
            "nat_ff_b2a"
        attribute b2b if_all(["ff"]) if_not(["fta","fs"]):
            "nat_ff_b2b"
        attribute b2c if_all(["ff"]) if_not(["fta","fs"]):
            "nat_ff_b2c"
        attribute b3a if_all(["ff"]) if_not(["fta","fs"]) if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "nat_ff_b3a"
        attribute b3b if_all(["ff"]) if_not(["fta","fs"]) if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "nat_ff_b3b"
        attribute b3c if_all(["ff"]) if_not(["fta","fs"]) if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "nat_ff_b3c"
        attribute b3a if_all(["ff"]) if_not(["fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "nat_ff_b1e"
        attribute b3b if_all(["ff"]) if_not(["fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "nat_ff_b1d"
        attribute b3c if_all(["ff"]) if_not(["fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "nat_ff_b1c"
    
    
    
    group special if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        
        attribute s_scream:
            paths.natsuki("bases", "face_special_scream")
    
    

    
    
    group nose if_all(["fs"]) if_not(["ff","fta"]):
        
        anchor (0,0) subpixel (True)
        

        attribute nose default if_any(["nobl"]):
            "nat_fs_n1"
        attribute nose default if_any(["awkw"]):
            "nat_fs_n2"
        attribute nose default if_any(["blus"]):
            "nat_fs_n3"
        attribute nose default if_any(["blaw"]):
            "nat_fs_n4"
        attribute nose default if_any(["bful"]):
            "nat_fs_n5"
        
        
        
        attribute n1:
            "nat_fs_n1"
        attribute n2:
            "nat_fs_n2"
        attribute n3:
            "nat_fs_n3"
        attribute n4:
            "nat_fs_n4"
        attribute n5:
            "nat_fs_n5"
    
    
    
    group mouth if_all(["fs"]) if_not(["ff","fta"]):
        
        anchor (0,0) subpixel (True)
        
    
        attribute cm default if_any(["neut"]):
            "nat_fs_m1"
        attribute cm default if_any(["sad","cry"]):
            "nat_fs_m2"
        

        attribute om if_any(["sad","cry","neut"]):
            "nat_fs_m3"
        
        

        attribute m1:
            "nat_fs_m1"
        attribute m2:
            "nat_fs_m2"
        attribute m3:
            "nat_fs_m3"
        attribute m4:
            "nat_fs_m4"
    
    
    
    group eyes if_all(["fs"]) if_not(["ff","fta","n5","bful"]):
        
        anchor (0,0) subpixel (True)
    
        attribute oe default if_any(["neut"]):
            "nat_fs_e1"
        attribute oe default if_any(["sad"]):
            "nat_fs_e2"
        attribute oe default if_any(["cry"]):
            "nat_fs_e3"
        
        attribute ce if_any(["neut"]):
            "nat_fs_e4"
        attribute ce if_any(["sad"]):
            "nat_fs_e5"
        attribute ce if_any(["cry"]):
            "nat_fs_e6"
        
        
        attribute e1:
            "nat_fs_e1"
        attribute e2:
            "nat_fs_e2"
        attribute e3:
            "nat_fs_e3"
        attribute e4:
            "nat_fs_e4"
        attribute e5:
            "nat_fs_e5"
        attribute e6:
            "nat_fs_e6"
    
    
    
    group brows if_all(["fs"]) if_not(["ff","fta","n5","bful"]):
        
        anchor (0,0) subpixel (True)
        
    
        attribute brow default if_any(["neut"]):
            "nat_fs_b1"
        attribute brow default if_any(["sad"]):
            "nat_fs_b3"
    
    
    
    group brows:
        
        anchor (0,0) subpixel (True)
        
        attribute brow default if_any(["cry"]) if_all(["fs","oe"]) if_not(["ff","fta","n5","bful","ce"]):
            "nat_fs_b3"
        attribute brow default if_any(["cry"]) if_all(["fs","ce"]) if_not(["ff","fta","n5","bful","oe"]):
            "nat_fs_b2"
    
    
    
    group brows if_all(["fs"]) if_not(["ff","fta","n5","bful"]): 
        
        anchor (0,0) subpixel (True)
        
    
        attribute b1:
            "nat_fs_b1"
        attribute b2:
            "nat_fs_b2"
        attribute b3:
            "nat_fs_b3"



layeredimage natsuki cross:
    

    
    group outfit:
        attribute uniform default null
        attribute casual null
    
    
    
    group mood: 
        
        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute cry null  #crying
        attribute curi null #curious
        attribute dist null #distant
        attribute doub null #doubtful
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute lsur null #surprised (lightly)
        attribute nerv null #nervous
        attribute pani null #panicked
        attribute pout null #pouting
        attribute sad null  #sad
        attribute sedu null #seductive
        attribute shoc null #shocked
        attribute vang null #VERY angry
        attribute vsur null #surprised (very)
        attribute worr null #worried
        attribute yand null #yandere
    
    
    
    
    group blush: #state of her nose/blush.
        attribute nobl default null #no blush or tear drop.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing AND awkward.  defaults for n
        attribute bful null #full face blush.  Currently only works on the side face.
    
    
    
    group head: #This needs to render below her body for her "cross" pose.
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        attribute ff default:
            paths.natsuki("bases", "face_forward")
        
        attribute fs:
            paths.natsuki("bases", "face_sad")
        
        attribute fta:
            paths.natsuki("bases", "face_turnedaway")
    
    
    
    #Body definitions.  There are two variations on both types, since one of the bodies provided in the MPT specifically works better with the "fs" head than the other.
    always:
        paths.natsuki("bases", "crossed", "ff_uniform") if_all(["uniform","ff"])
    always:
        paths.natsuki("bases", "crossed", "fs_uniform") if_all(["uniform"]) if_any(["fs","fta"])
    always:
        paths.natsuki("bases", "crossed", "ff_casual") if_all(["casual","ff"])
    always:
        paths.natsuki("bases", "crossed", "fs_casual") if_all(["casual"]) if_any(["fs","fta"])
    
    
    
    group nose if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        ###Default nose/blush
        attribute nose default if_any(["nobl"]):
            "nat_ff_n1"
        attribute nose if_any(["awkw"]):
            "nat_ff_n2"
        attribute nose if_any(["blus"]):
            "nat_ff_n3"
        attribute nose if_any(["blaw"]):
            "nat_ff_n4"
        
        
        
        ###All noses - truncated tags:
        attribute n1:
            "nat_ff_n1"
        attribute n2:
            "nat_ff_n2"
        attribute n3:
            "nat_ff_n3"
        attribute n4:
            "nat_ff_n4"
    
    
    
    
    group mouth if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        ###Default Closed Mouths:
        attribute cm default if_any(["happ","sedu","nerv"]):
            "nat_ff_ma"
        attribute cm default if_any(["neut","anno","worr","lsur"]):
            "nat_ff_md"
        attribute cm default if_any(["pout","curi"]):
            "nat_ff_me"
        attribute cm default if_any(["flus","shoc"]):
            "nat_ff_mg"
        attribute cm default if_any(["sad","angr","vsur","dist","doub"]):
            "nat_ff_mj"
        attribute cm default if_any(["vang","pani","cry"]):
            "nat_ff_mm"
        attribute cm default if_any(["yand"]):
            "nat_ff_mn"
        attribute cm default if_any(["laug"]):
            "nat_ff_mo"
        
        ###Default Open Mouths:
        attribute om if_any(["sedu","nerv","yand"]):
            "nat_ff_mb"
        attribute om if_any(["happ","laug"]):
            "nat_ff_mc"
        attribute om if_any(["sad","anno","worr","lsur","dist","pout"]):
            "nat_ff_mg"
        attribute om if_any(["neut","curi"]):
            "nat_ff_mh"
        attribute om if_any(["doub","angr","vsur"]):
            "nat_ff_mi"
        attribute om if_any(["flus","shoc"]):
            "nat_ff_ml"
        attribute om if_any(["cry","vang","pani"]):
            "nat_ff_mq"
        
        
        ###All mouths - truncated tags:
        attribute ma: 
            "nat_ff_ma"
        attribute mb:
            "nat_ff_mb"
        attribute mc:
            "nat_ff_mc"
        attribute md:
            "nat_ff_md"
        attribute me:
            "nat_ff_me"
        attribute mf:
            "nat_ff_mf"
        attribute mg:
            "nat_ff_mg"
        attribute mh:
            "nat_ff_mh"
        attribute mi:
            "nat_ff_mi"
        attribute mj:
            "nat_ff_mj"
        attribute mk:
            "nat_ff_mk"
        attribute ml:
            "nat_ff_ml"
        attribute mm:
            "nat_ff_mm"
        attribute mn:
            "nat_ff_mn"
        attribute mo:
            "nat_ff_mo"
        attribute mp:
            "nat_ff_mp"
        attribute mq:
            "nat_ff_mq"
        attribute mr:
            "nat_ff_mr"
    
    
    
    group eyes if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        ###Default Opened eyes:
        attribute oe default if_any(["neut","happ","laug","pout","curi"]):
            "nat_ff_e1a"
        attribute oe default if_any(["sad","worr","flus","dist"]):
            "nat_ff_e1b"
        attribute oe default if_any(["anno","sedu","doub"]):
            "nat_ff_e1d"
        attribute oe default if_any(["cry"]):
            "nat_ff_e1g"
        attribute oe default if_any(["angr","lsur","nerv"]):
            "nat_ff_e2a"
        attribute oe default if_any(["vang","vsur","pani","shoc"]):
            "nat_ff_e2d"
        attribute oe default if_any(["yand"]):
            "nat_ff_e3a"
        
        ###Default Closed eyes:
        attribute ce if_any(["sad","worr","anno","angr","vang","vsur","flus","dist","sedu","nerv","doub"]):
            "nat_ff_e4a"
        attribute ce if_any(["neut","happ","laug","lsur","yand","pout","curi"]):
            "nat_ff_e4b"
        attribute ce if_any(["shoc","pani"]):
            "nat_ff_e4c"
        attribute ce if_any(["cry"]):
            "nat_ff_e4e"
        
        
        ###All eyes - truncated tags:
        attribute e1a:
            "nat_ff_e1a"
        attribute e1b:
            "nat_ff_e1b"
        attribute e1c:
            "nat_ff_e1c"
        attribute e1d:
            "nat_ff_e1d"
        attribute e1e:
            "nat_ff_e1e"
        attribute e1f:
            "nat_ff_e1f"
        attribute e1g:
            "nat_ff_e1g"
        attribute e1h:
            "nat_ff_e1h"
        attribute e2a:
            "nat_ff_e2a"
        attribute e2b:
            "nat_ff_e2b"
        attribute e2c:
            "nat_ff_e2c"
        attribute e2d:
            "nat_ff_e2d"
        attribute e3a:
            "nat_ff_e3a"
        attribute e3b:
            "nat_ff_e3b"
        attribute e4a:
            "nat_ff_e4a"
        attribute e4b:
            "nat_ff_e4b"
        attribute e4c:
            "nat_ff_e4c"
        attribute e4d:
            "nat_ff_e4d"
        attribute e4e:
            "nat_ff_e4e"
        attribute e0a:
            "nat_ff_e0a"
        attribute e0b:
            "nat_ff_e0b"
    
    
    
    group brows if_all(["ff"]) if_not(["fta","fs"]): #eyebrows.
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        #Default Eyebrows:
        attribute brow default if_any(["neut","dist","sedu"]):
            "nat_ff_b1a"
        attribute brow default if_any(["sad","pani","flus","pout","nerv"]):
            "nat_ff_b1b"
        attribute brow default if_any(["happ","worr","shoc"]):
            "nat_ff_b1c"
        attribute brow default if_any(["curi","doub"]):
            "nat_ff_b1f"
        attribute brow default if_any(["lsur"]):
            "nat_ff_b2a"
        attribute brow default if_any(["cry","vsur"]):
            "nat_ff_b2c"
    
    
    
    #Some of Natsuki's eyebrows can only be used with closed eye expressions: the following moods take advantage of this, and thus need logic to check whether the eyes are open or not.
    group brows:#In case you're wondering why there's no if_all or if_not logic on this group line, it's because the attributes below explicitly use the same logic - and if you have a group and an attribute both using the same logic tag, the attribute one will COMPLETELY overwrite and ignore the group logic.  It took me way too long to figure this out.
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        attribute brow default if_any(["vang"]) if_all(["ff","oe"]) if_not(["fta","fs","ce"]):
            "nat_ff_b1d"
        attribute brow default if_any(["vang"]) if_all(["ce","ff"]) if_not(["fta","fs","oe"]):
            "nat_ff_b3a"
        attribute brow default if_any(["laug"]) if_all(["ff","oe"]) if_not(["fta","fs","ce"]):
            "nat_ff_b1b"
        attribute brow default if_any(["laug"]) if_all(["ce","ff"]) if_not(["fta","fs","oe"]):
            "nat_ff_b3a"
        attribute brow default if_any(["yand"]) if_all(["ff","oe"]) if_not(["fta","fs","ce"]):
            "nat_ff_b2a"
        attribute brow default if_any(["yand"]) if_all(["ce","ff"]) if_not(["fta","fs"]):
            "nat_ff_b3c"
        attribute brow default if_any(["anno","angr"]) if_all(["ff","oe"]) if_not(["fta","fs","ce"]):
            "nat_ff_b1d"
        attribute brow default if_any(["anno","angr"]) if_all(["ce","ff"]) if_not(["fta","fs"]):
            "nat_ff_b3b"
    
    
    
    group brows:
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        ###All eyebrows - truncated tags:
        attribute b1a if_all(["ff"]) if_not(["fta","fs"]):
            "nat_ff_b1a"
        attribute b1b if_all(["ff"]) if_not(["fta","fs"]):
            "nat_ff_b1b"
        attribute b1c if_all(["ff"]) if_not(["fta","fs",]):
            "nat_ff_b1c"
        attribute b1d if_all(["ff"]) if_not(["fta","fs"]):
            "nat_ff_b1d"
        attribute b1e if_all(["ff"]) if_not(["fta","fs"]):
            "nat_ff_b1e"
        attribute b1f if_all(["ff"]) if_not(["fta","fs"]):
            "nat_ff_b1f"
        attribute b2a if_all(["ff"]) if_not(["fta","fs"]):
            "nat_ff_b2a"
        attribute b2b if_all(["ff"]) if_not(["fta","fs"]):
            "nat_ff_b2b"
        attribute b2c if_all(["ff"]) if_not(["fta","fs"]):
            "nat_ff_b2c"
        attribute b3a if_all(["ff"]) if_not(["fta","fs"]) if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "nat_ff_b3a"
        attribute b3b if_all(["ff"]) if_not(["fta","fs"]) if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "nat_ff_b3b"
        attribute b3c if_all(["ff"]) if_not(["fta","fs"]) if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "nat_ff_b3c"
        #If the user tries to specifically use a closed-eyebrow variant with open eyes, we intentionally replace the eyebrow graphic in use with an appropriate - but not identical - replacement from the regular eyebrows:
        attribute b3a if_all(["ff"]) if_not(["fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "nat_ff_b1e"
        attribute b3b if_all(["ff"]) if_not(["fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "nat_ff_b1d"
        attribute b3c if_all(["ff"]) if_not(["fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "nat_ff_b1c"
    
    
    
    #This group is intentionally last on this list, so it will render over top of every other thing on the face.
    group special if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        attribute s_scream:
            paths.natsuki("bases", "face_special_scream")
    
    
    
####################The "sad, turned away" face, and the few expressions it has.
    
    
    
    group nose if_all(["fs"]) if_not(["ff","fta"]):
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):
            "nat_fs_n1"
        attribute nose default if_any(["awkw"]):
            "nat_fs_n2"
        attribute nose default if_any(["blus"]):
            "nat_fs_n3"
        attribute nose default if_any(["blaw"]):
            "nat_fs_n4"
        attribute nose default if_any(["bful"]):
            "nat_fs_n5"
        
        
        
        #All noses - truncated tags:
        attribute n1:
            "nat_fs_n1"
        attribute n2:
            "nat_fs_n2"
        attribute n3:
            "nat_fs_n3"
        attribute n4:
            "nat_fs_n4"
        attribute n5:
            "nat_fs_n5"
    
    
    
    group mouth if_all(["fs"]) if_not(["ff","fta"]):
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        #Closed mouths
        attribute cm default if_any(["neut"]):
            "nat_fs_m1"
        attribute cm default if_any(["sad","cry"]):
            "nat_fs_m2"
        
        #Open mouths.  Note that there's only one at this time.
        attribute om if_any(["sad","cry","neut"]):
            "nat_fs_m3"
        
        
        #sad mouths - truncated tags:
        attribute m1:
            "nat_fs_m1"
        attribute m2:
            "nat_fs_m2"
        attribute m3:
            "nat_fs_m3"
        attribute m4:
            "nat_fs_m4"
    
    
    
    group eyes if_all(["fs"]) if_not(["ff","fta","n5","bful"]): #Cannot show if full-face blush is present.
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        #Open eyes
        attribute oe default if_any(["neut"]):
            "nat_fs_e1"
        attribute oe default if_any(["sad"]):
            "nat_fs_e2"
        attribute oe default if_any(["cry"]):
            "nat_fs_e3"
        
        #Closed eyes
        attribute ce if_any(["neut"]):
            "nat_fs_e4"
        attribute ce if_any(["sad"]):
            "nat_fs_e5"
        attribute ce if_any(["cry"]):
            "nat_fs_e6"
        
        
        #All eyes - truncated tags:
        attribute e1:
            "nat_fs_e1"
        attribute e2:
            "nat_fs_e2"
        attribute e3:
            "nat_fs_e3"
        attribute e4:
            "nat_fs_e4"
        attribute e5:
            "nat_fs_e5"
        attribute e6:
            "nat_fs_e6"
    
    
    
    group eyebrows if_all(["fs"]) if_not(["ff","fta","n5","bful"]): #Cannot show if full-face blush is present.
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        #default brows
        attribute brow default if_any(["neut"]):
            "nat_fs_b1"
        attribute brow default if_any(["sad"]):
            "nat_fs_b3"
    
    
    
    group brows:#Required separate group definition because of additional logic for showing these particular eyebrows.
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        attribute brow default if_any(["cry"]) if_all(["fs","oe"]) if_not(["ff","fta","n5","bful","ce"]):
            "nat_fs_b3"
        attribute brow default if_any(["cry"]) if_all(["fs","ce"]) if_not(["ff","fta","n5","bful","oe"]):
            "nat_fs_b2"
    
    
    
    group eyebrows if_all(["fs"]) if_not(["ff","fta","n5","bful"]): #Cannot show if full-face blush is present.
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        attribute b1:
            "nat_fs_b1"
        attribute b2:
            "nat_fs_b2"
        attribute b3:
            "nat_fs_b3"