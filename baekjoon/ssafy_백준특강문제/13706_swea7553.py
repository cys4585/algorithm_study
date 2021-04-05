# 제곱근

def square(left, right, n):
    while True:
        mid = (left + right)//2
        if mid*mid == n:
            return mid
        else:
            if mid*mid > n:
                right = mid
            else:
                left = mid


N = int(input())
square_root = square(1, N, N)
print(square_root)