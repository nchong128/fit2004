def naiveFib(N):
    if N == 0 or N == 1:
        return N
    else:
        return naiveFib(N-1) + naiveFib(N-2)

def fibTopDown(N):
    memo = [0] * (N + 1)

    if N == 0:
        return 0
    elif N == 1:
        return 1

    memo[0] = 0
    memo[1] = 1

    for i in range(2, N + 1):
        memo[i] = -1

    return fibTopDownAux(memo, N)

def fibTopDownAux(memo, N):
    if memo[N] != -1:
        return memo[N]
    else:
        memo[N] = fibTopDownAux(memo, N-1) + fibTopDownAux(memo, N-2)
        return memo[N]

def fibBottomUp(N):
    # Make array
    memo = [0]* (N+1)

    if N == 0:
        return 0
    elif N == 1:
        return 1

    memo[0] = 0
    memo[1] = 1

    for i in range(2, N + 1):
        memo[i] = memo[i-1] + memo[i - 2]

    return memo[-1]

def main():
    N = 9

    answer = fibBottomUp(N)

    assert fibTopDown(N) == naiveFib(N) == fibBottomUp(N), print("Wrong")

    print(answer)

if __name__ == '__main__':
    main()