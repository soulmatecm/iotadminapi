import random


def generate_random_string(length):
    """生成随机字符串
    """
    raw = ''
    range1 = range(58, 65)  # between 0~9 and A~Z
    range2 = range(91, 97)  # between A~Z and a~z
    i = 0
    while i < length:
        seed = random.randint(48, 122)
        if seed in range1 or seed in range2:
            continue
        raw += chr(seed)
        i += 1
    return raw
