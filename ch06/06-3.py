class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        alpha_logs = []
        num_logs = []

        # 문자로그와 숫자로그를 분리하기
        # 8 / art
        for log in logs:
            if log.split(' ')[1].isalpha():
                alpha_logs.append(log)
            else:
                num_logs.append(log)

        # 문자 로그 정렬 (숫자 로그는 정렬할 필요 없음)
        alpha_logs.sort(key=lambda x: (x.split(' ')[1:], x.split(' ')[0]))

        return alpha_logs + num_logs