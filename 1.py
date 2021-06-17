def real_cost(feat: int):
    if feat <= 3:
        return feat
    length = len(f"{feat}")
    if length == 1:
        return feat - 1
    return feat - real_cost(feat - 1 * 10 ** (length - 1))


print(real_cost(10))
