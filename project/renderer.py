from tabulate import tabulate

def render_report(data):
    return tabulate(data,headers="keys")