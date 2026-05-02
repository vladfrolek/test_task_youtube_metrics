from project.renderer import render_report


def test_render_report_returns_table_with_expected_data():
    report_data = [
        {
            "title": "Video 1",
            "ctr": 20.0,
            "retention_rate": 30.0,
        }
    ]

    result = render_report(report_data)

    assert "title" in result
    assert "ctr" in result
    assert "retention_rate" in result
    assert "Video 1" in result
    assert "20.0" in result or "20" in result
    assert "30.0" in result or "30" in result