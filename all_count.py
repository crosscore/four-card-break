from itertools import permutations, product, combinations
import random
import operator

# トランプの数値のリストを生成（ジョーカーを除く）
cards_values = list(range(1, 14)) * 4

# 四則演算の関数を定義
operations = [operator.add, operator.sub, operator.mul, operator.truediv]
operations_symbols = ['+', '-', '*', '/']

# すべてのカードの順列と演算の組み合わせを試す
def find_combinations(cards, target, ops):
    count = 0
    for numbers in permutations(cards):
        for op_combinations in product(ops, repeat=3):
            try:
                # 最初の2枚のカードに対して演算を適用
                result = op_combinations[0](numbers[0], numbers[1])
                # 2番目と3番目の演算を適用
                result = op_combinations[1](result, numbers[2])
                # 最後の演算を適用
                result = op_combinations[2](result, numbers[3])
                
                # 結果が目的のカードの数値と一致するかチェック
                if result == target:
                    count += 1
            except ZeroDivisionError:
                # 0での除算を無視
                continue
    return count

# 全ての可能な5枚のカードの組み合わせに対してfind_combinations関数を適用
total_count = 0
for selected_cards in combinations(cards_values, 5):
    four_cards = selected_cards[:4]
    target_card = selected_cards[4]
    total_count += find_combinations(four_cards, target_card, operations)

print(f"全ての可能な組み合わせの総数: {total_count}")