# 좋은수열

# 문자 1, 2, 3으로만 이루어지는 수열이 있다.
# 임의의 길이의 인접한 두 개의 부분 수열이 동일한 것이 있으면,
# 그 수열을 나쁜 수열이라고 부른다. 그렇지 않은 수열은 좋은 수열이다.

# 다음은 나쁜 수열의 예이다.
# 33
# 32121323
# 123123213
# 1

# 다음은 좋은 수열의 예이다.
# 2
# 32
# 32123

# 길이가 N인 좋은 수열들을 N자리의 정수로 보아 그 중 가장 작은 수를 나타내는 수열을 구하는 프로그램을 작성하라.
# 예를 들면, 1213121과 2123212는 모두 좋은 수열이지만, 그 중에서 작은 수를 나타내는 수열은 1213121이다.


def is_good_sequence(seq):
    r = len(seq)
    # 뒤에 2개, 4개, 6개, ... 순으로 조사한다.
    # left right로 나눠 비교한다.
    l = r - 2
    while l >= 0:
        mid = (l + r) // 2
        left = seq[l:mid]
        right = seq[mid:r]
        if left == right: return False
        l -= 2
    return True


# seq : sequence(수열)
def dfs(seq):
    global min_seq
    # backtracking
    if not is_good_sequence(seq): return

    if len(seq) == N:
        seq = int(seq)
        if min_seq == 0:
            min_seq = seq
        return
    for i in range(1, 4):
        dfs(seq + str(i))
        # 중요!!!!!!
        # min_seq 값이 정해지면 더이상 조사하지 않는다.
        #   이유 : 1 2 3 순으로 seq를 만들어 나가기 때문에
        #         숫자가 작은 수열이 우선적으로 생성된다.
        #         그러다가 len(seq) == N이 되면
        #         조건을 만족하는 seq을 찾은 것이다.
        #         (dfs이기 때문에 가능한 것)
        if min_seq: return


N = int(input())

min_seq = 0
dfs('')
print(min_seq)