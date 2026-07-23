from strategy import get_top10

def main():

    print("\n🚀 开始A股量化选股...\n")

    top10 = get_top10()

    print("\n📊 A股 Top10：\n")

    for i, (stock, score) in enumerate(top10, 1):
        print(f"{i}. {stock}  score={score:.2f}")

    print("\n✅ 完成")


if __name__ == "__main__":
    main()