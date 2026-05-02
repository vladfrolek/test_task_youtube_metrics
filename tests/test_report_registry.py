from project.report import generate_clickbait_report
from project.report_registry import available_reports, get_report


def test_get_report_returns_clickbait_report_function():
    report_function = get_report("clickbait")

    assert report_function == generate_clickbait_report


def test_get_report_returns_none_for_unknown_report():
    report_function = get_report("unknown_report")

    assert report_function is None


def test_available_reports_contains_clickbait():
    reports = available_reports()

    assert "clickbait" in reports