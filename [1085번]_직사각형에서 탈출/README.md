## 백준 1085번_직사각형 탈출하기

### 풀이
1. 입력하는 (x, y)을 기준으로 가장 가까운 직사각형의 경계선은 (위, 아래, 좌, 우) 수직으로 내린 것 중에서 가장 작은 것이다.
2. (x, y) 기준으로 위, 아래, 좌, 우 값을 구해서 리스트에 넣은 다음, min() 함수를 통해서 가장 작은 값을 출력하면 끝이다.
