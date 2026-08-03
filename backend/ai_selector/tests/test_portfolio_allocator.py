from core.portfolio.allocator import PortfolioAllocator


def test_allocator():

    allocator = PortfolioAllocator()


    result = allocator.allocate(

        score=0.9,

        confidence=0.8,

        cash=100000,

        price=10
    )


    assert result["allocation"] > 0


    assert result["qty"] > 0


    assert result["amount"] <= 20000