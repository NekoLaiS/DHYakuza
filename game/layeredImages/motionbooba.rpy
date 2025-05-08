
init -200 python:

    class MotionBooba(renpy.Displayable):
        def __init__(self, child, weight_tex, tag=(None, None), weight=1, bounce=0.2, stiff=0.1, dist=2):
            super(MotionBooba, self).__init__()
            self.child = renpy.easy.displayable(child)
            self.wtex = renpy.easy.displayable(weight_tex)

            self.tag, self.tag_layer = tag

            self.weight = weight
            self.bounce = bounce
            self.stiff  = stiff

            self.dist = dist
            
            self.woffset = [0,0]
            self.dwoffset= [0,0]
            self.x, self.y = 0, 0

            self.lastdt = 0.0

        def render(self, width, height, st, at):
            dt = 1/60

            child = renpy.render(self.child, width, height, st, at)
            cw, ch = child.get_size()
            wtex = renpy.render(self.wtex, cw, ch, st, at)
            
            rv = renpy.Render(cw, ch)
            rv.blit(child, (0, 0), focus=True, main=True) 

            if self.tag is None:
                return rv
                
            disp = renpy.display.core.displayable_by_tag(self.tag_layer, self.tag)

            if renpy.easy.displayable_or_none(disp) is None:
                return rv

            # too braindead to deal with this shit
            if disp.state.transform_anchor:
                return rv

            place = renpy.get_placement(disp)

            x = absolute.compute_raw(place.xpos, config.screen_width)
            if type(x) is float: 
                x *= config.screen_width

            y = absolute.compute_raw(place.ypos, config.screen_height)
            if type(y) is float: 
                y *= config.screen_height

            x += absolute.compute_raw(place.xoffset, config.screen_height)
            y += absolute.compute_raw(place.yoffset, config.screen_width)

            # if times are weird, dont bother and reset
            if (st<=1/60 or dt>1/30 or dt<0):
                self.x = x
                self.y = y
            
            dx = (x-self.x)
            dy = (y-self.y)

            self.x, self.y = x, y

            dox = -self.woffset[0] + dx * self.dist
            doy = -self.woffset[1] + dy * self.dist

            dist = min(
                max(math.sqrt(dx**2+dy**2), 1),
                math.sqrt(self.dist**2)
            )

            bx = self.bounce * dox/dist
            by = self.bounce * doy/dist

            self.dwoffset[0] += (-self.stiff * self.dwoffset[0] + bx/self.weight) / self.weight
            self.dwoffset[1] += (-self.stiff * self.dwoffset[1] + by/self.weight) / self.weight

            if abs(self.dwoffset[0]) > self.stiff:
                self.woffset[0] += self.dwoffset[0]
            if abs(self.dwoffset[1]) > self.stiff:
                self.woffset[1] += self.dwoffset[1]

            if abs(self.dwoffset[0]) <= self.stiff: self.dwoffset[0] = 0.0
            if abs(self.dwoffset[1]) <= self.stiff: self.dwoffset[1] = 0.0

            rv.blit(wtex, (0, 0), focus=False, main=False)

            rv.mesh = True
            rv.add_shader("shader.booba")
            rv.add_uniform("u_offset", self.woffset)

            renpy.redraw(self, 0)
            
            self.lastdt = st
            return rv

        def per_interact(self):
            renpy.redraw(self, 0)


transform -200 mbooba(child, wtex, tag, weight, bounce, stiff, dist):
    MotionBooba(child, wtex, tag, weight, bounce, stiff, dist)

transform -200 mbooba_n(child):
    mbooba(child, "images/characters/natsuki/booba/boobaweight_n.png", ("natsuki", "master"),
            1.0, 0.45, 0.25, 20/60)
transform -200 mbooba_s(child):
    mbooba(child, "images/characters/sayori/booba/boobaweight_s.png",  ("sayori", "master"),
            1.25, 0.4, 0.2, 45/60)
transform -200 mbooba_m(child):
    mbooba(child, "images/characters/monika/booba/boobaweight_m.png",  ("monika", "master"),
            1.5, 0.25, 0.18, 100/60)
transform -200 mbooba_y(child):
    mbooba(child, "images/characters/yuri/booba/boobaweight_y.png",    ("yuri", "master"),
            1.8, 0.225, 0.15, 150/60)

image natsuki turned motionbooba = LayeredImageProxy("natsuki", mbooba_n)
image sayori turned motionbooba  = LayeredImageProxy("sayori",  mbooba_s)
image monika forward motionbooba = LayeredImageProxy("monika", mbooba_m)
image yuri turned motionbooba    = LayeredImageProxy("yuri",    mbooba_y)


## lmao

# image natsuki turned ultibooba = LayeredImageProxy("natsuki turned", [booba_n, mbooba_n])
# image sayori turned ultibooba  = LayeredImageProxy("sayori turned",  [booba_s, mbooba_s])
# image monika forward ultibooba = LayeredImageProxy("monika forward", [booba_m, mbooba_m])
# image yuri turned ultibooba    = LayeredImageProxy("yuri turned",    [booba_y, mbooba_y])





label boobatest:

    scene bg class_day
    show layer master

    show sayori  turned booba happ cm oe at t41 zorder 1
    show sayori turned booba happ n6 mowo b1b e1f at t42 zorder 2
    show monika forward booba happ cm oe at t43 zorder 3
    show yuri turned booba happ cm oe at t44 zorder 4

    "cursor booba"

    ""
    show monika at t41 zorder 1
    show sayori at t42 zorder 2
    show sayori  at t43 zorder 3
    show yuri at t44 zorder 4
    ""
    show sayori at t41 zorder 1
    show monika at t42 zorder 2
    show yuri at t43 zorder 3
    show sayori  at t44 zorder 4
    ""
    show sayori at t41 zorder 1
    show sayori  at t42 zorder 2
    show yuri at t43 zorder 3
    show monika at t44 zorder 4
    ""

    hide natsuki
    hide sayori
    hide monika
    hide yuri

    show sayori  turned motionbooba happ cm oe at t41:
        ease 0.2 xoffset -10
        ease 0.2 xoffset 10
        repeat

    show sayori turned motionbooba happ cm oe at t42:
        block:
            easein .15 yoffset -21
            easeout .15 yoffset 0
            repeat 3
        easein_circ .5 yoffset -100
        easeout .15 yoffset 0 
        linear 0.5 xoffset 0 knot -10 knot 10 knot -10 knot 10
        pause 0.5
        repeat

    show monika forward motionbooba happ cm oe at t43:
        xoffset -25
    
        parallel:
            ease 0.4 xoffset 25
            pause 0.5
            ease 0.4 xoffset -25
            pause 0.5
            repeat
        parallel:
            easein 0.2 yoffset -40
            easeout 0.2 yoffset 0
            pause 0.5
            repeat

    show yuri turned motionbooba happ cm oe at t44:
        easein 0.3 yoffset -50
        easeout 0.3 yoffset 0
        0.3
        repeat

    show expression particles_spp.sm

    "motion booba"

    show monika at t41 zorder 1
    show sayori at t42 zorder 2
    show sayori  at t43 zorder 3
    show yuri at t44 zorder 4

    ""

    scene bg sayori_bedroom

    
    show sayori turned motionbooba neut cm oe at t11

    s om "Hello"
    s rup "This is test for uhh booba."
    show sayori at t21
    s "cause Q don't know what the fuck she doin"
    show sayori at thide
    hide sayori

    s "hidden"
    show sayori turned motionbooba happ cm oe at t11
    s "we back"

    show sayori booba -motionbooba
    pause

    return 
