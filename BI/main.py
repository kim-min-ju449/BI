import tkinter
from tkinter import *

import os

def btncall():
    global new
    new = Toplevel()
    
def main():
    win = Tk()  # 창 생성
    win.geometry("1000x600")
    win.title("연습")
    win.option_add("*Font", "궁서 25")
    btn = Button(win, command=btncall)
    btn.config(width=10, height=2, bg="lightyellow", font=('koverwatch', 30), )  # 버튼 가로 세로 크기 변경
    btn.config(text="연습1")  # 현재 시각
    btn.pack(side=LEFT, padx=70)  # 버튼 배
    btn2 = Button(win)
    btn2.config(width=10, height=2, bg="lightyellow", font=('koverwatch', 30), )  # 버튼 가로 세로 크기 변경
    btn2.config(text="연습2")  # 현재 시각
    btn2.pack(side=LEFT, padx=70)  # 버튼 배
    btn3 = Button(win)
    btn3.config(width=10, height=2, bg="lightyellow", font=('koverwatch', 30), )  # 버튼 가로 세로 크기 변경
    btn3.config(text="연습2")  # 현재 시각
    btn3.pack(side=LEFT, padx=70)  # 버튼 배
    win.mainloop()  # 창 실행

    # py_Img = tkinter.PhotoImage(file="m.gif")
    # label_Img = tkinter.Label(win, text="이미지가 표시되는 부분입니다.", image=py_Img)
    # label_Img.pack()


# def btncall():
#     btn["text"]="click"


main()