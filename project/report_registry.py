from .report import generate_clickbait_report
REPORTS = {
    'clickbait':generate_clickbait_report,
    'some_report':'some_report_func',
    'another_report':'another_report_func'
}


def get_report(report_name):
    
    if report_name in REPORTS:
        return REPORTS[report_name]
    else:
        return None

def available_reports():
    return list(REPORTS.keys())


