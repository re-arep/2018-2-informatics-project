from vpython import *
from random import *

scene = canvas(title='Informatics Project-firecracker', width=800, height=600, center=vector(0, 90, 155), autoscale=False)


floor = box(length=40, width=30, height=2, pos=vector(0, 0, 0))  # 바닥

T1 = label(xoffset=-30, yoffset=50, height=30, pos=vector(-10, 1, 11), color=color.black, background=color.white)  # 왼쪽라벨
T2 = label(xoffset=30, yoffset=50, height=30, pos=vector(10, 1, 11), color=color.black, background=color.white)  # 오른쪽라벨
text1 = text(text='Element', align='center', pos=vector(-10, 1, 11))  # 왼쪽 전구 이름(Element)
text2 = text(text='number', align='center', pos=vector(10, 1, 11))  # 오른쪽 전구 이름(Shape)

lamp1 = sphere(pos=vector(-10, 1, 11), radius=2, opacity=0.4)  # 왼쪽전구
lamp2 = sphere(pos=vector(10, 1, 11), radius=2, opacity=0.4)  # 오른쪽전구

body = cylinder(pos=vector(1, -0.5, 0), axis=vector(7, 0, 0), radius=1, color=color.red)  # 로켓 몸체(원기둥)
body.rotate (angle=1.58, axis=vector(0, 0, 1), origin=vector(0, 0, 0))  # 로켓 몸체 방향설정
head = cone(pos=vector(8, -0.5, 0), axis=vector(2.5, 0, 0), radius=1.2, color=color.red)  # 로켓 머리(원뿔)
head.rotate (angle=1.58, axis=vector(0, 0, 1), origin=vector(0, 0, 0))  # 로켓 머리 방향설정

roket = compound([body, head])  # 로켓 몸체&머리 이음
roket.pos = vector(0, 5, 0)  # 로켓 위치
roket.velocity = vector(0, 9.9, 0)  # 로켓 속도


def keyInput(evt):  # 키보드 입력 받는 함수
    ele = evt.key
    if ele == 'k':  # 칼륨
        lamp1.color = color.purple
        T1.text = 'K'
        col[0] = color.purple
    elif ele == 'c':  # 칼슘
        lamp1.color = color.orange
        T1.text = 'Ca'
        col[0] = color.orange
    elif ele == 's':  # 스트론튬
        lamp1.color = color.red
        T1.text = 'Sr'
        col[0] = color.red
    elif ele == 'l':  # 리튬
        lamp1.color = color.red
        T1.text = 'Li'
        col[0] = color.red
    elif ele == 'n':  # 나트륨
        lamp1.color = color.yellow
        T1.text = 'Na'
        col[0] = color.yellow

    elif ele == '0':  # 연쇄 폭발 불꽃 0개
        lamp2.color = color.red
        T2.text = '0'
        numb[0] = 0
    elif ele == '1':  # 연쇄 폭발 불꽃 1개
        lamp2.color = color.magenta
        T2.text = '1'
        numb[0] = 1
    elif ele == '2':  # 연쇄 폭발 불꽃 2개
        lamp2.color = color.cyan
        T2.text = '2'
        numb[0] = 2
    elif ele == '3':  # 연쇄 폭발 불꽃 3개
        lamp2.color = color.green
        T2.text = '3'
        numb[0] = 3


def launch(t):  # 로켓 발사 키 함수
    launcht = t.key
    if launcht == 't':
        for i in range(50):
            if roket.pos.y >= 130:  # 로켓이 일정 위치 이상 올라가면 사라지는 부분
                roket.visible = False
                break
            roket.pos.y = roket.pos.y + roket.velocity.y * dt - 9.8*dt  # 중력 적용


def object(N):  # 불꽃 구슬 생성 함수
    for i in range(N):

        x1 = randint(-10, 10)
        y1 = randint(120, 140)
        z1 = randint(-10, 10)

        if x1 == 0 and y1 == 130 and z1 == 0:  # 폭발지점에 불꽃이 있을경우 힘을 주지 못하는 오류 해결 코드
            x1 = 1
            y1 = 131
            z1 = 1

        k = 10/((x1 ** 2 + (y1-130) ** 2 + z1 ** 2) ** (1 / 2))  # 스칼라 10 - 폭발 힘   벡터 비례 상수

        ball.append(sphere(pos=vector(x1, y1, z1), radius=0.5, color=col[0]))
        ballvec.append([x1*k, (y1-130)*k, z1*k])


def objectother1(xx, N):  # 연쇄폭발 불꽃 생성 함수 1
    x2 = int(ball[xx].pos.x)-randint(0, 50)  # 랜덤으로 선택된 메인 불꽃의 위치를 기준으로 연쇄 폭발 지점 설정
    y2 = int(ball[xx].pos.y)-randint(0, 50)
    z2 = int(ball[xx].pos.z)

    for i in range(N):
        x3 = randint(x2 - 10, x2 + 10)
        y3 = randint(y2 - 10, y2 + 10)
        z3 = randint(z2 - 10, z2 + 10)

        if x3-x2 == 0 and y3-y2 == 0 and z3-z2 == 0:
            x3 = x2+1
            y3 = y2+1
            z3 = z2+1

        k = 8/(((x3-x2) ** 2 + (y3-y2) ** 2 + (z3-z2) ** 2) ** (1 / 2))  # 스칼라 8 - 폭발 힘   벡터 비례 상수

        ball2.append(sphere(pos=vector(x3, y3, z3), radius=0.5, color=color.red))
        ballvec2.append([(x3-x2) * k, (y3-y2) * k, (z3-z2) * k])


def objectother2(xx, N):  # 연쇄폭발 불꽃 생성 함수 2
    x2 = int(ball[xx].pos.x)+randint(0, 50)
    y2 = int(ball[xx].pos.y)-randint(0, 50)
    z2 = int(ball[xx].pos.z)

    for i in range(N):
        x3 = randint(x2 - 10, x2 + 10)
        y3 = randint(y2 - 10, y2 + 10)
        z3 = randint(z2 - 10, z2 + 10)

        if x3-x2 == 0 and y3-y2 == 0 and z3-z2 == 0:
            x3 = x2+1
            y3 = y2+1
            z3 = z2+1

        k = 8/(((x3-x2) ** 2 + (y3-y2) ** 2 + (z3-z2) ** 2) ** (1 / 2))  # 스칼라 8 - 폭발 힘   벡터 비례 상수

        ball3.append(sphere(pos=vector(x3, y3, z3), radius=0.5, color=color.red))
        ballvec3.append([(x3-x2) * k, (y3-y2) * k, (z3-z2) * k])


def objectother3(xx, N):  # 연쇄폭발 불꽃 생성 함수 3
    x2 = int(ball[xx].pos.x)+randint(0, 50)
    y2 = int(ball[xx].pos.y)+randint(0, 50)
    z2 = int(ball[xx].pos.z)

    for i in range(N):
        x3 = randint(x2 - 10, x2 + 10)
        y3 = randint(y2 - 10, y2 + 10)
        z3 = randint(z2 - 10, z2 + 10)

        if x3-x2 == 0 and y3-y2 == 0 and z3-z2 == 0:
            x3 = x2+1
            y3 = y2+1
            z3 = z2+1

        k = 8/(((x3-x2) ** 2 + (y3-y2) ** 2 + (z3-z2) ** 2) ** (1 / 2))  # 스칼라 8 - 폭발 힘   벡터 비례 상수

        ball4.append(sphere(pos=vector(x3, y3, z3), radius=0.5, color=color.red))
        ballvec4.append([(x3-x2) * k, (y3-y2) * k, (z3-z2) * k])


scene.bind('keydown', keyInput)  # 키보드 입력 활성화

dt = 0.01  # 단위시간
tt = 0  # 누적 시간

col = [color.black]  # 불꽃 색
colcol = [color.purple, color.orange, color.red, color.yellow]  # 전체 불꼿 색
colcolnum = 0  # 연쇄 폭발의 색깔 다양성을 위한 정의
numb = [0]  # 연쇄 폭발 개수


ball = []  # 불꽃의 정보를 포함하는 리스트
ballvec = []  # 불꽃이 받는 힘 벡터 정보를 포함하는 리스트
ball2 = []
ballvec2 = []
ball3 = []
ballvec3 = []
ball4 = []
ballvec4 = []

object(1000)  # 메인 불꽃 1000개 생성
for i in range(1000):  # 생성 후 보이지 않게 처리
    ball[i].visible = False

c2 = randint(0, 999)  # 연쇄 폭발 불꽃 생성
objectother1(c2, 1000)
c3 = randint(0, 999)
objectother2(c3, 1000)
c4 = randint(0, 999)
objectother3(c4, 1000)

for i in range(1000):  # 연쇄 폭발 불꽃 생성 후 보이지 않게 처리
    ball2[i].visible = False
    ball3[i].visible = False
    ball4[i].visible = False


while True:
    rate(100)
    scene.bind('keydown', launch)  # 로켓 발사 키보드 입력 활성화

    if col[0] == color.purple:  # 사용자가 선택한 색깔 정보 받기
        colcolnum = 0
    elif col[0] == color.orange:
        colcolnum = -1
    elif col[0] == color.red:
        colcolnum = -2
    elif col[0] == color.yellow:
        colcolnum = -3

    if roket.pos.y >= 130:  # 로켓이 임의의 지점 도달시 실행
        if len(ball) == 1000:
            for i in range(1000):  # 메인 불꽃 가시화
                ball[i].visible = True
            for i in range(1000):  # 폭발 에너지에 따른 움직임 적용 및 중력 적용
                ball[i].color = col[0]  # 사용자가 선택한 색깔로 지정
                ball[i].pos.x = ball[i].pos.x + ballvec[i][0]*dt
                ball[i].pos.y = ball[i].pos.y + ballvec[i][1]*dt - 9.8*dt
                ball[i].pos.z = ball[i].pos.z + ballvec[i][2]*dt

        tt = tt + dt  # 시간 누적

        if tt >= 3.8:

            for j in range(1000):  # 사용자가 선택한 연쇄 폭발의 개수에 따른 활성화
                if numb[0] == 0:
                    break
                if numb[0] >= 1:
                    ball2[j].visible = True
                if numb[0] >= 2:
                    ball3[j].visible = True
                if numb[0] >= 3:
                    ball4[j].visible = True

            for j in range(1000):  # 사용자가 선택한 연쇄 폭발의 개수에 따른 폭발 활성화
                if numb[0] == 0:
                    break
                if numb[0] >= 1:
                    ball2[j].color = colcol[colcolnum+1]  # 색의 다양성을 위해 사용자가 선택한 색깔을 제외한 색깔 출력
                    ball2[j].pos.x = ball2[j].pos.x + ballvec2[j][0] * dt
                    ball2[j].pos.y = ball2[j].pos.y + ballvec2[j][1] * dt - 9.8 * dt
                    ball2[j].pos.z = ball2[j].pos.z + ballvec2[j][2] * dt
                if numb[0] >= 2:
                    ball3[j].color = colcol[colcolnum+2]
                    ball3[j].pos.x = ball3[j].pos.x + ballvec3[j][0] * dt
                    ball3[j].pos.y = ball3[j].pos.y + ballvec3[j][1] * dt - 9.8 * dt
                    ball3[j].pos.z = ball3[j].pos.z + ballvec3[j][2] * dt
                if numb[0] >= 3:
                    ball4[j].color = colcol[colcolnum+3]
                    ball4[j].pos.x = ball4[j].pos.x + ballvec4[j][0] * dt
                    ball4[j].pos.y = ball4[j].pos.y + ballvec4[j][1] * dt - 9.8 * dt
                    ball4[j].pos.z = ball4[j].pos.z + ballvec4[j][2] * dt

                if tt >= 7:
                    for j in range(1000):  # 연쇄 폭발 불꽃 비가시화
                        ball2[j].visible = False
                        ball3[j].visible = False
                        ball4[j].visible = False

        if tt >= 5.2:  # 메인 불꽃 비가시화 및 연산량 감소를 위한 삭제
            if len(ball) == 1000:  # while 문의 특성으로 인해 이미 삭제된 것을 또 삭제하려는 오류 해결 코드
                for i in range(1000):
                    ball[0].visible = False
                    del ball[0]
