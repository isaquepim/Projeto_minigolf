#coordenadas da tela
x = 800
y = 600

fase1 = True
fase2 = True
fase3 = True

class Interativos:
    def __init__(self):
        pass

    def obstaculo1(self, px, py, x, y):
        #definir cores ainda
        #ver equações das elipses para ver a tangente
        self.px = px
        self.py = py
        
        fill(242, 141, 53)    
        rect(px, py, x, y)
    
        fill(0)
        ellipse(px + 0.5*x, py + 0.5*y, 1.5*x, 0.5*y)
        #ellipse 1

        fill(242, 141, 53)
        ellipse(px + 0.5*x, py + 0.5*y, x, 0.25*y)
        #ellipse 2
        
        self.a21 = (1.5*x)**2 + (0.5*y)**2
        self.b21 = (0.5*y)**2
        #dados da ellipse 1
        
        self.a22 = (x)**2 + (0.25*y)**2
        self.b22 = (0.25*y)**2
        #dados da ellipse 2
        
    def obstaculo2(self, px, py, x, y):
        #definir cores ainda
        #equações
        self.px = px
        self.py = py
                
        fill(0, 0, 0)
        translate(px, py)
        rotate(PI/7.0)
        ellipse(0, 0, 2*x, y)
        tg1x = x/cos(PI/7.0)
        tg1y = y/sin(PI/7.0)
        self.tg1 = PVector(tg1x, tg1y)
        
        fill(127, 0, 0)
        rotate(PI/7.0)
        ellipse(0, 0, 2*x, y)
        tg2x = x/cos(2*PI/7.0)
        tg2y = y/sin(2*PI/7.0)
        self.tg2 = PVector(tg2x, tg2y)
        
        fill(255, 0, 0)
        rotate(PI/7.0)
        ellipse(0, 0, 2*x, y)
        tg3x = x/cos(3*PI/7.0)
        tg3y = y/sin(3*PI/7.0)
        self.tg3 = PVector(tg3x, tg3y)
        
        fill(0, 127, 0)
        rotate(PI/7.0)
        ellipse(0, 0, 2*x, y)
        tg4x = x/cos(4*PI/7.0)
        tg4y = y/sin(4*PI/7.0)
        self.tg4 = PVector(tg4x, tg4y)
        
        fill(0, 255, 0)
        rotate(PI/7.0)
        ellipse(0, 0, 2*x, y)
        tg5x = x/cos(5*PI/7.0)
        tg5y = y/sin(5*PI/7.0)
        self.tg5 = PVector(tg5x, tg5y)
        
        fill(0, 0, 127)
        rotate(PI/7.0)
        ellipse(0, 0, 2*x, y)
        tg6x = x/cos(6*PI/7.0)
        tg6y = y/sin(6*PI/7.0)
        self.tg6 = PVector(tg6x, tg6y)
        
        fill(0, 0, 255)
        rotate(PI/7.0)
        ellipse(0, 0, 2*x, y)
        tg7x = x/cos(PI)
        tg7y = y/sin(PI)
        self.tg7 = PVector(tg7x, tg7y)
        
    def obstaculo3(self, pxi, pyi, pxo, pyo, x, y):
        #buraco negro
        #entra num ponto e sai em outro com mesma velocidade, aceleração e direção
        self.pxi = pxi
        self.pyi = pyi
        self.pxo = pxo
        self.pyo = pyo
        
        stroke(0, 0, 255)
        fill(0)
        ellipse(pxi, pyi, x, y)
        
        stroke(255, 0, 0)
        fill(0)
        ellipse(pxo, pyo, x, y)

    def obstaculo4(self, px, py, x, y):
        #lago
        #caso a bolinha entre aqui, ela volta para o ponto em que saiu
        self.px = px
        self.py = py

        fill(107, 191, 183)
        noStroke()
        ellipse(px, py, 2*x, y)
        self.a2 = (1.5*x)**2 + (0.5*y)**2
        self.b2 = (0.5*y)**2
        #dados da ellipse

        
    def obstaculo5(self, px, py, x, y):
        #areia
        #aumenta a força necessária para a bolinha se mover
        self.px = px
        self.py = py
        
        fill(242, 188, 121)
        noStroke()
        ellipse(px, py, 3*x/2, y)
        self.a2 = (1.5*x)**2 + (0.5*y)**2
        self.b2 = (0.5*y)**2
        #dados da ellipse
        
    def hole(self, px, py, x, y):
        fill(0, 0, 0)
        noStroke()
        ellipse(px, py, x, y)
        self.px = px
        self.py = py

h = Interativos()

def Menu():
    global estado
    
    background(0)
    rectMode(CENTER)
    
    textAlign(CENTER)
    textSize(30)
    text('MINIGOLF',width/2,100)
    
    textSize(20)
    noFill()
    stroke(255)
    
    text('New Game', width/2, 200)
    if mouseX <= width/2 + 90 and mouseX >= width/2 - 90 and mouseY <= 200+45 and mouseY >= 200-45:
        rect(width/2, 200,180,90)
        if mousePressed == True:
            estado = Minigolf
            restart = True
            
    text('Credits', width/2, 400)
    if mouseX <= width/2 + 90 and mouseX >= width/2 - 90 and mouseY <= 400+45 and mouseY >= 400-45:
        rect(width/2, 400,180,90)
        if mousePressed == True:
            estado = Creditos

class Bola:
    def __init__(self,p,v,r):
        self.v = v
        self.p = p
        self.r = r
        p0 = p
        v0 = v
    def move(self,dt,h2o = False):
        if h2o == False:
            self.p.add(self.v*dt)
        else:
            self.p = p0
            self.v = v0
    
    def xlr8(self,dt,at=False):
        v = self.v.copy()
        if at == False:
            if v.mag() < 0.01:
                self.v.add(v.mult(-1))
            elif v.mag() < 0.1:
                mi = -0.3*v.mag()
                v.mult(mi)
                self.v.add(v)
            else:
                mi = -0.3*v.mag()**2
                v.mult(mi)
                self.v.add(v)
        else:
            if v.mag() < 0.09:
                self.v.add(v.mult(-1))
            elif v.mag() < 0.2:
                mi = -0.5*v.mag()
                v.mult(mi)
                self.v.add(v)
            else:
                mi = -0.5*v.mag()**2
                v.mult(mi)
                self.v.add(v)            

#definicao da bola
v = PVector(0,0)
p = PVector(300,200)
r = 2

#incrementos e verfificadores de movimento    
inc = PVector(0,0)     
ver = False

b = Bola(p,v,r)

def colide(b, s):
    s.normalize()
    vy = s*(b.v.dot(s))
    vx = b.v - vy

    
    vy = vy* (-1)
    b.p.add(2*vy)
    b.v = vx + vy


t = millis()

r2 = b.r**2

#pa = PVector(0,0)
restart = True
hole = False

def Minigolf():
    global estado, Menu, t, restart, p, r, v, b, h, hole, fase1, fase2, fase3, b, r2
    
    if fase1:
        la = PVector(100,255)
        lb = PVector(400,255)
        lc = PVector(400,155)
        ld = PVector(490,155)
        le = PVector(490,255)
        lf = PVector(590,255)
        lg = PVector(617.5,255-55/2*3**(1/2))
        lh = PVector(672.5,255-55/2*3**(1/2))
        li = PVector(700,255)
        lj = PVector(700,345)
        lk = PVector(672.5,345+55/2*3**(1/2))
        ll = PVector(617.5,345+55/2*3**(1/2))
        lm = PVector(590,345)
        ln = PVector(490,345)
        lo = PVector(490,445)
        lp = PVector(400,445)
        lq = PVector(400,345)
        lr = PVector(100,345)
        t1a = PVector(410,270)
        t1b = PVector(410,310)
        t1c = PVector(480,270)
        t2a = PVector(410,330)
        t2b = PVector(480,330)
        t2c = PVector(480,290)
        lados = [(la,lb),(lb,lc),(lc,ld),(ld,le),(le,lf),(lf,lg),(lg,lh),(lh,li),(li,lj),(lj,lk),(lk,ll),(ll,lm),(lm,ln),(ln,lo),(lo,lp),(lp,lq),(lq,lr),(lr,la),(t1a,t1b),(t1b,t1c),(t1c,t1a),(t2a,t2b),(t2b,t2c),(t2c,t2a)]
        
    elif fase2:
        la = PVector(150,255)
        lb = PVector(150,345)
        lc = PVector(650,345)
        ld = PVector(650,255)
        lados = [(la,lb),(lb,lc),(lc,ld),(ld,la)]
        
    elif fase3:
        la = PVector(260,155)
        lb = PVector(260,355)
        lc = PVector(320,455)
        ld = PVector(480,455)
        le = PVector(540,355)
        lf = PVector(540,155)
        lg = PVector(450,155)
        lh = PVector(450,355)
        li = PVector(350,355)
        lj = PVector(350,155)
        lados = [(la,lb),(lb,lc),(lc,ld),(ld,le),(le,lf),(lf,lg),(lg,lh),(lh,li),(li,lj),(lj,la)]

    def detecta_colisao():
        for l in lados:
            p1 = l[0].copy()
            p2 = l[1].copy()
            p = p2-p1
            ball = b.p.copy()
            v1 = p.dot(ball-p1)
            v2 = p.dot(ball-p2)
            
            if v1 > 0 and v2 < 0:
                a_ = (ball-p1) - (v1/(v1-v2))*p
                if a_.x**2 + a_.y**2 <= r2:
                    colide(b,a_)
        
    background(122, 166, 56)
    oldt = t
    t = millis()
    dt = t-oldt
    r = 2
    
    rectMode(CORNERS)
    
    fill(0,0,0)
    stroke(0)
    rectMode(CENTER)
    text('Exit', 0.11*width, 50)
    if mouseX <= 0.11*width + 0.1*width and mouseX >= 0.11*width - 0.1*width and mouseY <= 50+30 and mouseY >= 50-30:
        noFill()
        rect(0.11*width, 50, 0.2*width, 60)
        if mousePressed == True:
            estado = Menu
            restart = True
            fase1 = True
            fase2 = True
            fase3 = True
            
    text('Restart', 0.11*width, 120)
    if mouseX <= 0.11*width + 0.1*width and mouseX >= 0.11*width - 0.1*width and mouseY <= 120+30 and mouseY >= 120-30:
        noFill()
        rect(0.11*width, 120, 0.2*width, 60)
        if mousePressed == True:
            restart = True
    
    if fase1:
        if restart:
            v = PVector(0,0)
            p = PVector(120,300)
            b = Bola(p,v,r)
            restart = False
            hole = False
        
        h.hole(680, 300, 2*r+3, 2*r+3)
    
        fill(255,0,0)
        triangle(410,270,410,310,480,270)
        triangle(410,330,480,330,480,290)
    
        #BURACO
        if (p.x-h.px)**2 + (p.y-h.py)**2 <= (r+3)**2 and v.mag() <= 15:
            v = PVector(0,0)
            p = PVector(h.px, h.py)
            b = Bola(p,v,r)
            hole = True
            restart = True
            fase1 = False
            
    elif fase2:
        if restart:
            v = PVector(0,0)
            p = PVector(170,300)
            b = Bola(p,v,r)
            restart = False
            hole = False
        
        h.hole(630, 300, 2*r+3, 2*r+3)
        
        #BURACO
        if (p.x-h.px)**2 + (p.y-h.py)**2 <= (r+3)**2 and v.mag() <= 15:
            v = PVector(0,0)
            p = PVector(h.px, h.py)
            b = Bola(p,v,r)
            hole = True
            restart = True
            fase2 = False
            
    elif fase3:
        if restart:
            v = PVector(0,0)
            p = PVector(305,175)
            b = Bola(p,v,r)
            restart = False
            hole = False
        
        h.hole(495, 175, 2*r+3, 2*r+3)
        
        #BURACO
        if (p.x-h.px)**2 + (p.y-h.py)**2 <= (r+3)**2 and v.mag() <= 15:
            v = PVector(0,0)
            p = PVector(h.px, h.py)
            b = Bola(p,v,r)
            hole = True
            
    b.move(dt)
    b.xlr8(dt)
    
    detecta_colisao()
    
    fill(255)
    stroke(255)
    ellipse(b.p.x,b.p.y, 2*b.r, 2*b.r)
    
    stroke(0)
    for i in lados:
        line(i[0].x,i[0].y,i[1].x,i[1].y)

posy = y-50

def Creditos():
    global posy, Menu, estado
    background(0)
    posx = width/2
    v = -3
    posy += v
    text("Minigolf: \n Isaque Vieira Machado Pim \n Igor Patricio Michels  \n \n Agradecimentos: \n Paulo Cesar \n Asla de Sa \n Coffee Machine do 14", posx, posy)
    if posy < -400:
        estado = Menu
        posy = y-50
    
estado = Menu

def setup():
    size(x, y)
    
def draw():
    global estado
    estado()
    
def mouseDragged():
    global inc, ver, hole
    
    if b.v.mag() == 0 and hole == False: #condição para não aceitar tacadas se a bola estiver se movendo
        if sqrt((mouseX - b.p.x)**2 + (mouseY-b.p.y)**2) <= r+10:
            ver = True
    
    if ver:
        inc.x = b.p.x - mouseX
        inc.y = b.p.y - mouseY
        stroke(255,0,0)
        line(b.p.x,b.p.y,mouseX,mouseY)
        #colocar um contador de jogadas no canto superior direito

def mouseReleased():
    global inc, ver
    if ver:
        b.v.add(inc/500)
        inc = PVector(0,0) 
        ver = False
