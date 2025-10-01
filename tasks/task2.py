# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    q,w,e=map(int,input().split())
    karandash=3
    ruchka=karandash+2
    flomaster=ruchka+7
    itogo=(q*karandash)+(w*ruchka)+(e*flomaster)
    print(itogo)

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()