

def reorder_log_files(logs):
    alpha_logs = []
    num_logs = []

    # 문자로그와 숫자로그를 분리하기
    for log in logs:
        if log.split(' ')[1].isalpha():
            alpha_logs.append(log)
        else:
            num_logs.append(log)

    # 문자 로그 정렬 (숫자 로그는 정렬할 필요 없음)
    alpha_logs.sort(key=lambda x: (x.split(' ')[1:], x.split(' ')[0]))

    return alpha_logs + num_logs

reorder_log_files(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"])
