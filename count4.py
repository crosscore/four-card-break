from itertools import permutations, product
import random
import operator

# トランプの数値のリストを生成（ジョーカーを除く）
cards_values = list(range(1, 14)) * 4

# 4枚のカードと1枚のカードをランダムに選択
selected_cards = random.sample(cards_values, 5)
four_cards = selected_cards[:4]
target_card = selected_cards[4]

# 四則演算の関数を定義
operations = [operator.add, operator.sub, operator.mul, operator.truediv]
operations_symbols = ['+', '-', '*', '/']

# すべてのカードの順列と演算の組み合わせを試す
def find_combinations(cards, target, ops):
    combinations = set()
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
                    # 演算子のシンボルを取得
                    op_symbols = [operations_symbols[ops.index(op)] for op in op_combinations]
                    # 組み合わせを保存
                    combination_str = ''.join(str(e) for sublist in zip(numbers, op_symbols) for e in sublist) + str(numbers[-1])
                    combinations.add(combination_str)
            except ZeroDivisionError:
                # 0での除算を無視
                continue
    return combinations

combinations = find_combinations(four_cards, target_card, operations)

print(f"4枚のカード: {four_cards}")
print(f"目的のカード: {target_card}")
print(f"組み合わせの数: {len(combinations)}")
for i, combination_str in enumerate(combinations, 1):
    print(f"組み合わせ{i}: {combination_str}")