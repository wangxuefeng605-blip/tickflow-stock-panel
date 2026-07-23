from alpha_model import alpha_score


# 模拟 stock_factor.py 输出
factor = {

    "momentum": 0.9771,

    "volume_factor": 1.143,

    "trend": 1,

    "value": 0.65,

    "quality": 0.72

}


# 因子权重
weights = {

    "momentum": 0.25,

    "volume_factor": 0.15,

    "trend": 0.10,

    "value": 0.20,

    "quality": 0.30

}


# 计算 Alpha

score = alpha_score(
    factor,
    weights
)


print("====================")
print("测试 Alpha Model")
print("====================")


print(
    "输入因子:"
)

print(factor)


print(
    "\n权重:"
)

print(weights)


print(
    "\nAlpha Score:"
)

print(score)