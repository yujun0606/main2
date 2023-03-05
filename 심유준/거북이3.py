# 반복 기능으로 도형을 그리는 프로그램
# import turtle as t

'''t.shape("turtle")
a = 50
b = 90
t.color("green")
t.begin_fill()
t.speed(0)
for x in range(4):
    t.forward(a)
    t.left(b)
t.end_fill()
c = 50
d = 120
t.color("red")
for x in range(3):
    t.forward(c)
    t.left(d)
e= 50
f = 60
t.color("gray")
for x in range(6):
    t.forward(e)
    t.left(f)'''
'''n = 50
t.bgcolor("black")
t.color("green")
t.speed(0)
for x in range(n):
    t.circle(80)
    t.left(360/n)'''

'''angle = 89
t.bgcolor("black")
t.color("yellow")
t.speed(0)
for x in range(200):
    t.forward(x)
    t.left(angle)'''
import time

input("엔터를 누르고 20초를 셉니다")
start = time.time()

input("20초 후에 다시 엔터를 누릅니다")
end = time.time()

et = end - start
print("실제 시간 : ", et, "초")
    





