from core.factor_cache import load_factor
from stock_factor import get_stock_factor


def warmup_factors(codes):

    print("=" * 40)
    print("Factor Warmup")
    print("=" * 40)

    total = len(codes)

    created = 0
    cached = 0


    for i, code in enumerate(codes, 1):

        factor = load_factor(code)


        if factor is not None:

            cached += 1

            continue


        print(
            f"[{i}/{total}] build factor {code}"
        )


        result = get_stock_factor(code)


        if result:

            created += 1



    print("=" * 40)

    print(
        f"Factor Warmup Done "
        f"cached={cached} "
        f"created={created}"
    )

    print("=" * 40)