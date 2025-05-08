
init -200 python:

    renpy.register_shader("shader.booba", variables="""
        uniform sampler2D tex0;
        uniform sampler2D tex1;
        uniform vec2 res0;
        
        uniform vec2 u_offset;

        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        """, vertex_200="""
            v_tex_coord = a_tex_coord;
        """, fragment_300="""
            float weight = texture2D(tex1, v_tex_coord).r;
            gl_FragColor = texture2D(tex0, v_tex_coord+weight*u_offset/res0.xy);
        """)
    
    class Booba(renpy.Displayable):
        def __init__(self, child, weight_tex, weight=1, bounce=0.2, stiff=0.1, dist=20):
            super(Booba, self).__init__()
            self.child = renpy.easy.displayable(child)
            self.wtex = renpy.easy.displayable(weight_tex)

            self.weight = weight
            self.bounce = bounce
            self.stiff = stiff
            self.dist = dist
            
            self.woffset = [0,0]
            self.dwoffset= [0,0]
            self.dmouse =  [0,0]

        def render(self, width, height, st, at):
            mx, my = renpy.get_mouse_pos()
            # if st<=1/60 and self.dwoffset[0]==0.0:self.dmouse[0]=mx
            # if st<=1/60 and self.dwoffset[1]==0.0:self.dmouse[1]=my
            dmx = (self.dmouse[0]-mx)
            dmy = (self.dmouse[1]-my)

            self.dmouse = mx,my

            dox = -self.woffset[0] - dmx * self.dist
            doy = -self.woffset[1] - dmy * self.dist

            dist = max(math.sqrt(dmx**2+dmy**2), 1)

            bx = self.bounce * (dox if dox else 1)/dist
            by = self.bounce * (doy if doy else 1)/dist

            self.dwoffset[0] += (-self.stiff * self.dwoffset[0] + bx/self.weight ) / self.weight
            self.dwoffset[1] += (-self.stiff * self.dwoffset[1] + by/self.weight ) / self.weight
        
            if abs(self.dwoffset[0]) > self.stiff:
                self.woffset[0] += self.dwoffset[0]
            if abs(self.dwoffset[1]) > self.stiff:
                self.woffset[1] += self.dwoffset[1]

            self.woffset = [min(max(i, -self.dist*4), self.dist*4) for i in self.woffset]


            child = renpy.render(self.child, width, height, st, at)
            cw, ch = child.get_size()
            wtex = renpy.render(self.wtex, cw, ch, st, at)
            
            rv = renpy.Render(cw, ch)
            rv.blit(child, (0, 0), focus=True, main=True) 
            rv.blit(wtex,  (0, 0), focus=False, main=False)

            rv.mesh = True
            rv.add_shader("shader.booba")
            rv.add_uniform("u_offset", self.dwoffset)

            renpy.redraw(self, 0)
            return rv


transform -200 booba_n(child):
    Booba(child, "images/characters/natsuki/booba/boobaweight_n.png", 1,   0.5, 0.4,  0.75)
transform -200 booba_s(child):
    Booba(child, "images/characters/sayori/booba/boobaweight_s.png",  2,   0.6, 0.2,  3)
transform -200 booba_m(child):
    Booba(child, "images/characters/monika/booba/boobaweight_m.png",  2.5, 0.5, 0.15, 6.5)
transform -200 booba_y(child):
    Booba(child, "images/characters/yuri/booba/boobaweight_y.png",    3,   0.4, 0.1,  10)

image natsuki booba = LayeredImageProxy("natsuki", booba_n)
image sayori booba  = LayeredImageProxy("sayori",  booba_s)
image monika forward booba = LayeredImageProxy("monika", booba_m)
image yuri booba    = LayeredImageProxy("yuri",    booba_y)
