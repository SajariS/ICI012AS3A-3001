def evaluate_string(data: bytes) -> float:
    frequency_table = {
        101: 12.02,  # e
        116: 9.10,   # t
        97: 8.12,    # a
        111: 7.68,   # o
        105: 7.31,   # i
        110: 6.95,   # n
        115: 6.28,   # s
        114: 6.02,   # r
        104: 5.92,   # h
        100: 4.32,   # d
        108: 3.98,   # l
        117: 2.88,   # u
        99: 2.71,    # c
        109: 2.61,   # m
        102: 2.30,   # f
        121: 2.11,   # y
        119: 2.09,   # w
        103: 2.03,   # g
        112: 1.82,   # p
        98: 1.49,    # b
        118: 1.11,   # v
        107: 0.69,   # k
        120: 0.17,   # x
        113: 0.11,   # q
        106: 0.10,   # j
        122: 0.07,   # z
    }
    score = 0.0
    for byte in data:
        if byte in frequency_table:
            score += frequency_table[byte]
    return score