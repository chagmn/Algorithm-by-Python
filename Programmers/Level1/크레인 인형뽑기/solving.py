def solution(board, moves):
    answer = 0
    select = []

    for i in range(len(moves)):
        for j in range(len(board)):

            if board[j][moves[i] - 1] != 0:
                val = board[j][moves[i] - 1]

                if len(select) != 0:
                    if select[len(select) - 1] != val:  # 이전에 선택한거와 동일한가?
                        select.append(val)  # 아니면 추가
                        board[j][moves[i] - 1] = 0
                    else:
                        select.pop()  # 들어있는거 값 삭제
                        answer += 2
                        board[j][moves[i] - 1] = 0
                else:
                    select.append(val)
                    board[j][moves[i] - 1] = 0
                break

    return answer
