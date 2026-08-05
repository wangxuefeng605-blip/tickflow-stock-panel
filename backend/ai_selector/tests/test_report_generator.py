from core.report_generator import generate_report



def test_report_import():

    assert callable(
        generate_report
    )