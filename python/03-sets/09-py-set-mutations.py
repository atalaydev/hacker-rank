if __name__ == '__main__':
    _ = input()
    a = set(map(int, input().split()))

    actions = {
        'intersection_update': 
            (lambda b: a.intersection_update(b)),
        'update': 
            (lambda b: a.update(b)),
        'symmetric_difference_update': 
            (lambda b: a.symmetric_difference_update(b)),
        'difference_update': 
            (lambda b: a.difference_update(b)),
    }

    action_length = int(input())
    for i in range(action_length):
        action, _ = list(map(str, input().split()))
        func = actions.get(action)(set(map(int, input().split())))

    print(sum(a))