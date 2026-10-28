"""打印九九乘法表。

用法:
    python multiplication_table.py        # 默认 9 阶（经典下三角）
    python multiplication_table.py -n 5   # 自定义阶数
"""

import argparse

DEFAULT_SIZE = 9


def build_table(size: int = DEFAULT_SIZE) -> str:
    """生成 size 阶乘法表文本，第 row 行输出 1..row 列。"""
    lines = []
    for row in range(1, size + 1):
        cells = [f"{col}×{row}={col * row}" for col in range(1, row + 1)]
        lines.append(" ".join(cells))
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="打印九九乘法表")
    parser.add_argument(
        "-n", "--size", type=int, default=DEFAULT_SIZE, help="乘法表阶数（默认 9）"
    )
    args = parser.parse_args()
    if args.size < 1:
        parser.error("阶数必须为正整数")
    print(build_table(args.size))


if __name__ == "__main__":
    main()