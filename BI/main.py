import tkinter
from tkinter import *
#import avoidgame
from pygame.rect import *
import os
import random
import pygame
#from Pgame import *



def btncall():
    global new
    new = Toplevel()
    new.geometry("320x200+820+100")
    canvas = Canvas(new, bg='Yellow')
    canvas.pack(expand=YES, fill=BOTH)
    img=PhotoImage(file="bananaleaf.png")
    canvas.create_image(10, 10, anchor=NW, image=img)
    new.mainloop()



def btncall2():
    global new
    new = Toplevel()
    btn = Button(new, command=btncall)
    img = PhotoImage(file="bananaleaf.png")

    btn.config(width=10, height=2, bg="lightyellow", font=('koverwatch', 30),)  # 버튼 가로 세로 크기 변경
    btn.config(text="연습1")  # 현재 시각
    btn.pack(side=LEFT, padx=70)  # 버튼 배
    btn2 = Button(new, command=btncall2)
    btn2.config(width=10, height=2, bg="lightyellow", font=('koverwatch', 30), )  # 버튼 가로 세로 크기 변경
    btn2.config(text="연습2")  # 현재 시각
    btn2.pack(side=LEFT, padx=70)  # 버튼 배
    btn3 = Button(new, command=btncall3)
    btn3.config(width=10, height=2, bg="lightyellow", font=('koverwatch', 30), )  # 버튼 가로 세로 크기 변경
    btn3.config(text="연습2")  # 현재 시각
    btn3.pack(side=LEFT, padx=70)  # 버튼 배
def btncall3():
    pygame.init()  # 초기화 (반드시 필요) init 호출

    # 화면 크기 설정
    screen_width = 480  # 가로 크기
    screen_height = 640  # 세로 크기
    screen = pygame.display.set_mode((screen_width, screen_height))

    # 화면 타이틀 설정
    pygame.display.set_caption("QUIZ")  # 게임 이름

    # FPS
    clock = pygame.time.Clock()
    ###############################################################

    # 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
    # 배경 만들기
    background = pygame.image.load("bananaleaf.png")

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

    # 똥 만들기
    ddong = pygame.image.load("orange1.png")
    ddong_size = ddong.get_rect().size
    ddong_width = ddong_size[0]
    ddong_height = ddong_size[1]
    ddong_x_pos = random.randint(0, screen_width - ddong_width)  # 0 ~ 480 - 캐릭터
    ddong_y_pos = 0
    ddong_speed = 10

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

        # 4. 충돌 처리
        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        ddong_rect = ddong.get_rect()
        ddong_rect.left = ddong_x_pos
        ddong_rect.top = ddong_y_pos

        if character_rect.colliderect(ddong_rect):
            print("충돌")
            running = False

        # 5. 화면에 그리기
        screen.blit(background, (0, 0))
        screen.blit(character, (character_x_pos, character_y_pos))
        screen.blit(ddong, (ddong_x_pos, ddong_y_pos))

        pygame.display.update()  # 게임 화면을 다시 그리기 ! (반드시 계속 호출되어야함)

    # 잠시 대기
    pygame.time.delay(2000)  # 2초 정도 대기 (ms) 하고 게임 꺼짐

    # pygame 종료
    pygame.quit()



def main():
    win = Tk()  # 창 생성
    win.geometry("1000x600")
    win.title("연습")
    win.option_add("*Font", "궁서 25")
    btn = Button(win, command=btncall)
    btn.config(width=10, height=2, bg="lightyellow", font=('koverwatch', 30), )  # 버튼 가로 세로 크기 변경
    btn.config(text="연습1")  # 현재 시각
    btn.pack(side=LEFT, padx=70)  # 버튼 배
    btn2 = Button(win, command=btncall2)
    btn2.config(width=10, height=2, bg="lightyellow", font=('koverwatch', 30), )  # 버튼 가로 세로 크기 변경
    btn2.config(text="연습2")  # 현재 시각
    btn2.pack(side=LEFT, padx=70)  # 버튼 배
    btn3 = Button(win, command=btncall3)
    btn3.config(width=10, height=2, bg="lightyellow", font=('koverwatch', 30), )  # 버튼 가로 세로 크기 변경
    btn3.config(text="연습2")  # 현재 시각
    btn3.pack(side=LEFT, padx=70)  # 버튼 배
    # canvas = Canvas(win, bg='Yellow')
    # canvas.pack(expand=YES, fill=BOTH)
    win.mainloop()  # 창 실행




main()