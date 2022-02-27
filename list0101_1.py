from cProfile import label
import tkinter


def key_down(e):
    key_s = e.keysym
    label2["text"] = "keysym " + key_s


def mouse_function(e):
    label3["text"] = "마우스가 클릭됐습니다."


root = tkinter.Tk()  # 윈도우 객체 생성
root.geometry("480x300")  # 윈도우 크기 지정
root.title("test-game")  # 윈도우 타이틀 지정
root.bind("<KeyPress>", key_down)
root.bind("<Button-1>", mouse_function)

label = tkinter.Label(root, text="test단계")  # 라벨 컴포넌트 생성 (창 안의 내용 지정)
fnt = ("Times New Roman", 20)

label2 = tkinter.Label(text="keysym", font=fnt)
label2.place(x=0, y=0)

label3 = tkinter.Label(font=fnt)
label3.place(x=0, y=80)

label.place(x=80, y=60)  # 라벨 배치
root.mainloop()
