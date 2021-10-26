from tkinter import *
win = Tk() # 창 생성
win.geometry("1000x500")
win.title("바나나설명서")
win.option_add("*Font","궁서 25")
btn = Button(win)
btn.config(width=10, height=2) # 버튼 가로 세로 크기 변경
btn.config(text="연습1") # 현재 시각
btn.pack() # 버튼 배치
win.mainloop() # 창 실행




