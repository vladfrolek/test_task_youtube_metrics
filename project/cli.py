import argparse
from .reader import read_files
from .renderer import render_report
from .report_registry import available_reports,get_report

def main():
    parser = argparse.ArgumentParser(
        description='Parser for file destinations, and name of report'
    )
    parser.add_argument(
        '--files',
        nargs='+',
        required=True,
        help = 'Files destinations'
    )
    parser.add_argument(
        '--report',type=str,
        required=True,
        help='Name of report'
    )
    args = parser.parse_args()
    file_paths = args.files
    report_name = args.report
    report_function=get_report(report_name)
    if report_function:
        try:
            videos = read_files(file_paths)
        except FileNotFoundError as error:
            print(error)
            return 
        report_data = report_function(videos)
        print(render_report(report_data))
    else:
        print(f'Отчет {report_name} не найден\nДоступные отчеты: {", ".join(available_reports())}')
    
if __name__ == '__main__':
    main()