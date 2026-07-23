from stock_factor import get_stock_factor


result = get_stock_factor(
    "000001"
)


print("================")
print("平安银行因子")
print("================")


for k,v in result.items():

    print(
        k,
        ":",
        v
    )