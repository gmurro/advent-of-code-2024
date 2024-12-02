def read_reports(file_path: str) -> list[list[int]]:
    """
    Read puzzle as array of list of integers
    """
    reports = []
    with open(file_path) as file:
        for line in file:
            reports += [[int(level) for level in line.split()]]
    return reports
