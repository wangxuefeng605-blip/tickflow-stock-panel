from core.portfolio.capital_allocator import CapitalAllocator


def test_capital_allocator():

    allocator = CapitalAllocator()


    result = allocator.allocate(
        {
            "000001":0.8,
            "000002":0.4
        },
        100000
    )


    assert result["000001"] == 66666.67

    assert result["000002"] == 33333.33