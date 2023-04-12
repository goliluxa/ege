def max_subseq_sum(n, l, c, seq):
    left = right = sum_ = max_sum = max_idx = 0
    neg_count = 0
    for i in range(n):
        if seq[i] < 0:
            neg_count += 1
        sum_ += seq[i]
        while neg_count > c:
            if seq[left] < 0:
                neg_count -= 1
            sum_ -= seq[left]
            left += 1
        if i - left + 1 == l:
            if sum_ > max_sum:
                max_sum = sum_
                max_idx = left
            if seq[left] < 0:
                neg_count -= 1
            sum_ -= seq[left]
            left += 1
    return max_sum, max_idx

# читаем входные данные из файла A
with open('A.txt', 'r') as f:
    n, l, c = map(int, f.readline().split())
    seq = [int(f.readline()) for _ in range(n)]
# находим максимальную сумму и её индекс
max_sum_A, max_idx_A = max_subseq_sum(n, l, c, seq)

# читаем входные данные из файла B
with open('B.txt', 'r') as f:
    n, l, c = map(int, f.readline().split())
    seq = [int(f.readline()) for _ in range(n)]
# находим максимальную сумму и её индекс
max_sum_B, max_idx_B = max_subseq_sum(n, l, c, seq)

# выводим ответ
print(max_sum_A, max_sum_B)
