#숫자 카드 게임 : n x m 행렬에 임의의 행에서 가장 낮은 숫자만 선택할 수 있을 때 선택할 수 있는 가장 높은 숫자
#
input time

n, m = map(int, input().split())

for i in m:
    data = list(map(int, input().split()))
    min = min(data)
    