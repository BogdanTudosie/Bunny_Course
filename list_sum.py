def list_sum(a: list, b: list):
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return result

if __name__ == "__main__":
    a = [12, 24, 36, 48]
    b = [14, 28, 42, 56]
    print(list_sum(a, b))