import sys
sys.stdin = open('1873.상호의 배틀필드.txt')

move_symbol = ["^", "v", "<", ">"]
move_command = ["U", "D", "L", "R", "S"]
move_dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

T= int(input())

H,W = map(int, input().split())
Map = [[''] * W for _ in range(H)]
N = int(input())
text_arr = input()


