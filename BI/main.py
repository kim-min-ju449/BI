import tkinter
from tkinter import *
from PyQt5.QtCore import QDateTime
import datetime as dt
from pygame.rect import *
import os
import datetime
import random
import pygame
global score
def juice():
    global new
    new = Toplevel()
    new.geometry("800x600")
    canvas = Canvas(new, bg='#FEEBB6')
    new.title("주스")
    canvas.pack(expand=YES, fill=BOTH)
    img = PhotoImage(file="bananajuice.png")
    canvas.create_image(10, 10, anchor=NW, image=img)
    new.mainloop()
def bread():
    global new
    new = Toplevel()
    new.geometry("800x600")
    canvas = Canvas(new, bg='#FEEBB6')
    new.title("빵")
    canvas.pack(expand=YES, fill=BOTH)
    img = PhotoImage(file="bananabread.png")
    canvas.create_image(10, 10, anchor=NW, image=img)
    new.mainloop()
def dessert():
    global new
    new = Toplevel()
    new.geometry("800x600")
    canvas = Canvas(new, bg='#FEEBB6')
    new.title("디저트")
    canvas.pack(expand=YES, fill=BOTH)
    img = PhotoImage(file="bananadessert.png")
    canvas.create_image(10, 10, anchor=NW, image=img)
    new.mainloop()

def btncall():
    global new
    new = Toplevel()
    new.geometry("800x600")
    canvas = Canvas(new, bg='White')
    canvas.pack(expand=YES, fill=BOTH)
    img=PhotoImage(file="bananaI.png")
    canvas.create_image(10, 10, anchor=NW, image=img)
    new.mainloop()

def btncall2():
    global new
    new = Toplevel()
    btn = Button(new, command=juice)
    btn.config(width=5, height=2, bg="#FAAC58", font=('koverwatch', 30),)  # 버튼 가로 세로 크기 변경
    btn.config(text="주스")  # 현재 시각
    btn.pack(side=LEFT, padx=70)  # 버튼 배
    btn2 = Button(new, command=bread)
    btn2.config(width=5, height=2, bg="#99681A", font=('koverwatch', 30), )  # 버튼 가로 세로 크기 변경
    btn2.config(text="빵")  # 현재 시각
    btn2.pack(side=LEFT, padx=70)  # 버튼 배
    btn3 = Button(new, command=dessert)
    btn3.config(width=5, height=2, bg="lightyellow", font=('koverwatch', 30), )  # 버튼 가로 세로 크기 변경
    btn3.config(text="디저트")  # 현재 시각
    btn3.pack(side=LEFT, padx=70)  # 버튼 배
def today():
    datetime = QDateTime.currentDateTime()
    return datetime
def btncall3():

    BLACK = (0, 0, 0)
    i=0
    score =0
    count=0
    pygame.init()  # 초기화 (반드시 필요) init 호출

    # 화면 크기 설정
    screen_width = 480  # 가로 크기
    screen_height = 640  # 세로 크기
    screen = pygame.display.set_mode((screen_width, screen_height))

    # 화면 타이틀 설정
    pygame.display.set_caption("바나나게임")  # 게임 이름

    # FPS
    clock = pygame.time.Clock()


    # 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
    # 배경 만들기
    background = pygame.image.load("bananaleaf.png")
    back = BLACK

    # 캐릭터 만들기
    character = pygame.image.load("doll1.png")
    character_size = character.get_rect().size
    character_width = character_size[0]
    character_height = character_size[1]
    character_x_pos = (screen_width / 2) - (character_width / 2)
    character_y_pos = screen_height - character_height

    # 이동 위치
    to_x = 0
    character_speed = 10

    # 장애물 만들기
    ddong = pygame.image.load("orange1.png")
    ddong_size = ddong.get_rect().size
    ddong_width = ddong_size[0]
    ddong_height = ddong_size[1]
    ddong_x_pos = random.randint(0, screen_width - ddong_width)  # 0 ~ 480 - 캐릭터
    ddong_y_pos = 0
    ddong_speed = 10

    #바나나만들기
    don = pygame.image.load("banana.png")
    don_size = don.get_rect().size
    don_width = don_size[0]
    don_height = don_size[1]
    don_x_pos = random.randint(0, screen_width - ddong_width)  # 0 ~ 480 - 캐릭터
    don_y_pos = 0
    don_speed = 10

    # 이벤트 루프
    running = True
    while running:
        dt = clock.tick(60)

        # 2. 이벤트 처리 (키보드, 마우스 등)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_x -= character_speed
                elif event.key == pygame.K_RIGHT:
                    to_x += character_speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0

        # 3. 게임 캐릭터 위치 정의
        character_x_pos += to_x

        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width

        ddong_y_pos += ddong_speed

        if ddong_y_pos > screen_height:
            ddong_y_pos = 0
            ddong_x_pos = random.randint(0, screen_width - ddong_width)

        don_y_pos += don_speed

        if don_y_pos > screen_height:
            don_y_pos = 1
            don_x_pos = random.randint(0, screen_width - don_width)*2

        # 4. 충돌 처리
        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        ddong_rect = ddong.get_rect()
        ddong_rect.left = ddong_x_pos
        ddong_rect.top = ddong_y_pos

        don_rect = don.get_rect()
        don_rect.left = don_x_pos
        don_rect.top = don_y_pos

        if character_rect.colliderect(ddong_rect):
            #print("충돌")
            print("점수" + str(score))
            print(today())


            running = False

            #return score

        if character_rect.colliderect(don_rect):

            running = True
            score +=1

        # 5. 화면에 그리기
        screen.blit(background, (0, 0))
        screen.blit(character, (character_x_pos, character_y_pos))
        screen.blit(ddong, (ddong_x_pos, ddong_y_pos))
        screen.blit(ddong, (ddong_x_pos, ddong_y_pos))
        screen.blit(don, (don_x_pos, don_y_pos))
        font_01 = pygame.font.SysFont("FixedSsy", 30, True, False)
        text_score = font_01.render("Score : " + str(score), True, BLACK)
        screen.blit(text_score, [15, 15])
        pygame.display.update()  # 게임 화면을 다시 그리기 ! (반드시 계속 호출되어야함)

    # 잠시 대기
    pygame.time.delay(2000)  # 2초 정도 대기 (ms) 하고 게임 꺼짐

    pygame.quit()

    with open('score.txt', 'a') as f:
        f.write(f'{score}\t{datetime.datetime.now()}\n')


def data():
    f = open('score.txt', 'w', encoding='utf-8')

    f.write('\n')
    f.write('월드')
    f.write('\n')
    f.write(str(score))

    f.close()

    print('with')


# def btncall4():
#     global new
#     new = Toplevel()
#     new.geometry("800x600")
#     #datetime = QDateTime.currentDateTime()
#     x = dt.datetime.now()
#     x
#     label = tkinter.Label(new, text=x, width=50, height=5, fg="BLACK", relief="solid")
#     #label2 = tkinter.Label(new, text=score, width=50, height=5, fg="BLACK", relief="solid")
#     label.pack()
#     #label2.pack()
#
#     #new.config("text")
#     # canvas = Canvas(new, bg='Yellow')
#     # canvas.pack(expand=YES, fill=BOTH)
#     # img=PhotoImage(file="bananaI.png")
#     # canvas.create_image(10, 10, anchor=NW, image=img)+
#     #print(str(score))
#     new.mainloop()
#

def main():
    win = Tk()  # 창 생성
    win.geometry("1000x600")
    win.title("BI")
    win.configure(bg='white')
    lbl = Label(win, text="BI" ,font = ("궁서체",70), bg='white')
    lbl.pack(pady=50)
    # canvas = Canvas(win, bg='Yellow')
    # canvas.pack(expand=YES, fill=BOTH)
    # img = PhotoImage(file="bananaleaf.png")
    # canvas.create_image(10, 10, anchor=NW, image=img)
    win.option_add("*Font", "궁서 25")
    btn = Button(win, command=btncall)
    btn.config(width=10, height=2, bg="#ffcc33", font=('koverwatch', 30), )  # 버튼 가로 세로 크기 변경
    btn.config(text="바나나정보")  # 현재 시각
    btn.pack(side=LEFT, padx=40)  # 버튼 배
    btn2 = Button(win, command=btncall2)
    btn2.config(width=10, height=2, bg="lightyellow", font=('koverwatch', 30), )  # 버튼 가로 세로 크기 변경
    btn2.config(text="바나나요리")  # 현재 시각
    btn2.pack(side=LEFT, padx=40)  # 버튼 배
    btn3 = Button(win, command=btncall3)
    btn3.config(width=10, height=2, bg="#81BEF7", font=('koverwatch', 30), )  # 버튼 가로 세로 크기 변경
    btn3.config(text="게임하기")  # 현재 시각
    btn3.pack(side=LEFT, padx=40)  # 버튼 배
    # btn4 = Button(win, command=btncall4)
    # btn4.config(width=10, height=2, bg="#81BEF7", font=('koverwatch', 30), )  # 버튼 가로 세로 크기 변경
    # btn4.config(text="게임기록")  # 현재 시각
    # btn4.pack(side=LEFT, padx=40)  # 버튼 배
    # canvas = Canvas(win, bg='Yellow')
    # canvas.pack(expand=YES, fill=BOTH)
    win.mainloop()  # 창 실행

main()