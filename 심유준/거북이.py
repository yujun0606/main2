# 모듈 : 파이썬에서 이미 정해 놓은 틀
# 모듈을 불러올 떄 : import 명령어
# 모듈 종류 : tutle, random, time
# as : 별명 

import turtle as t
t.shape("turtle")
t.speed(0)
# 정사각형 그리기
t.color("blue")
t.pensize(5)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

#정삼각형 그리기
t.color("red")
t.begin_fill() #색깔채우기 
t.pensize(7)
t.forward(50)
t.left(120)
t.forward(50)
t.left(120)
t.forward(50)
t.end_fill()

#정오각형 그리기

t.color("green")
t.pensize(10)
t.forward(50)
t.left(72)
t.forward(50)
t.left(72)
t.forward(50)
t.left(72)
t.forward(50)
t.left(72)
t.forward(50)
t.left(72)
t.forward(50)
t.left(72)

#정육각형 그리기

t.color("gray")
t.pensize(15)
t.forward(50)
t.left(60)
t.forward(50)
t.left(60)
t.forward(50)
t.left(60)
t.forward(50)
t.left(60)
t.forward(50)
t.left(60)
t.forward(50)
t.left(60)

#별

t.color("yellow")
t.pensize(20)
t.forward(50)
t.left(144)
t.forward(50)
t.left(144)
t.forward(50)
t.left(144)
t.forward(50)
t.left(144)
t.forward(50)
t.left(144)

# 거북이 모듈 함수
'''
forward, backward, left, right, color, pensize, begin_fill,
end_fill, speed ->가장빠른 속도 : 0
'''
















