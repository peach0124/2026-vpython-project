Web VPython 3.2

box(size=vec (2.7,3.3,1), pos=vec(0.2,0,0), color=color.red)
box(pos=vec(-1.4,0.5,0),size=vec(0.5,0.5,0.5),color=color.red)
sphere(pos=vec(-1.7,1.3,0),radius=0.4,color=color.red)
sphere(pos=vec(-1.7,-0.7,0),radius=0.4,color=color.red)
box(pos=vec(-1.65,0.25,0),size=vec(0.35,2.1,0.6),color=color.red)

sphere(pos=vec(-0.4,0.3,0.6),radius=0.17)
sphere(pos=vec(0.2,0.3,0.6),radius=0.17)
sphere(pos=vec(0.8,0.3,0.6),radius=0.17)
sphere(pos=vec(-0.4,-0.15,0.6),radius=0.17)
sphere(pos=vec(0.2,-0.15,0.6),radius=0.17)
sphere(pos=vec(0.8,-0.15,0.6),radius=0.17)
sphere(pos=vec(-0.4,-0.6,0.6),radius=0.17)
sphere(pos=vec(0.2,-0.6,0.6),radius=0.17)
sphere(pos=vec(0.8,-0.6,0.6),radius=0.17)
sphere(pos=vec(-0.4,-1.05,0.6),radius=0.17)
sphere(pos=vec(0.2,-1.05,0.6),radius=0.17)
sphere(pos=vec(0.8,-1.05,0.6),radius=0.17)

b1 = box(pos=vec(-0.4,0.3,0.6), size=vec(0.2,0.2,0.34), texture="https://i.postimg.cc/mrjKNrhg/1.png")
b2 = box(pos=vec(0.2,0.3,0.6), size=vec(0.2,0.2,0.34), texture="https://i.postimg.cc/fbWMhp9V/2.png")
b3 = box(pos=vec(0.8,0.3,0.6), size=vec(0.2,0.2,0.34), texture="https://i.postimg.cc/26MYh5XR/3.png")
box(pos=vec(-0.4,-0.15,0.6), size=vec(0.2,0.2,0.34), texture="https://i.postimg.cc/1XFQHZLg/4.png")
box(pos=vec(0.2,-0.15,0.6), size=vec(0.2,0.2,0.34), texture="https://i.postimg.cc/7hzkVypB/5.png")
box(pos=vec(0.8,-0.15,0.6), size=vec(0.2,0.2,0.34), texture="https://i.postimg.cc/02gxNbSx/6.png")
box(pos=vec(-0.4,-0.6,0.6), size=vec(0.2,0.2,0.34), texture="https://i.postimg.cc/52bVwTpG/7.png")
box(pos=vec(0.2,-0.6,0.6), size=vec(0.2,0.2,0.34), texture="https://i.postimg.cc/sgmRKmN2/8.png")
box(pos=vec(0.8,-0.6,0.6), size=vec(0.2,0.2,0.34), texture="https://i.postimg.cc/R0bxxFmD/9.png")
box(pos=vec(-0.4,-1.05,0.6), size=vec(0.2,0.2,0.34), texture="https://i.postimg.cc/Zn9vydgh/quf.png")
box(pos=vec(0.2,-1.05,0.6), size=vec(0.2,0.2,0.34), texture="https://i.postimg.cc/HnNg0kZX/image.png")
box(pos=vec(0.8,-1.05,0.6), size=vec(0.2,0.2,0.34), texture="https://i.postimg.cc/76vXz8nY/image.png")

box(size=vec (1.8,0.5,1.1), pos=vec(0.2,1,0))

l = label(text = "" ,pos=vec(0.2,1.2,0))
while True :
    rate(6)
    k = keysdown()
    l.text = l.text + k
    if scene.mouse.pick == b1 : 
        l.text = l.text + '1'
