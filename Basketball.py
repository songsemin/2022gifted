Web VPython 3.2

ring(pos=vector(45,25,0),
        axis=vector(0,1,0),
        radius=3, thickness=1)
box(size = vec(1,25,1), pos = vec(50,13,0))
box(size = vec(1,5,5), pos = vec(50,28,0))
box(size = vec(100,1,20))
a3 = arrow(pos = vec(-50,2,0))
ball = sphere(make_trail = True, color = color.magenta, pos = vec(-50,2,0))

p = label()
s = False
while True :
    p.text = ball.pos
    p.pos = ball.pos + vec(3,3,0)
    rate(100)
    k = keysdown()
    if 'right' in k :
        a3.axis.x += 0.1
    if 'left' in k :
        a3.axis.x -= 0.1
    if 'up' in k :
        a3.axis.y += 0.1
    if 'down' in k :
        a3.axis.y -= 0.1
        
    if ' ' in k :
        s = True
    if s == True :         
        ball.v = a3.axis
        ball.pos = ball.pos + ball.v * 0.01
        if mag(ball.pos - vector(45,25,0)) < 2 :
            label(text = 'winner!!')
            ball.color = vec(1,1,1)
        else :
            ball.v.y = ball.v.y + -9.8 * 0.01
