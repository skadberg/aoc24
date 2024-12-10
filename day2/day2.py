
reports_list = []
with open('input.txt', 'r') as file:
    for line in file:
        report = list(map(int, line.split()))
        reports_list.append(report)

def is_increasing(list):
    return all(i < j for i, j in zip(list, list[1:]))

def is_decreasing(list):
    return all(i > j for i, j in zip(list, list[1:]))

def is_increase_le_3(list):
    for i in range(len(list)-1):
        if abs(list[i] - list[i+1]) > 3 or abs(list[i] - list[i+1]) < 1:
            return False
    return True

def is_safe(report, damp=False):
    if is_increase_le_3(report) and (is_increasing(report) or is_decreasing(report)):
        return True

    if damp:
        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            if is_increase_le_3(modified_report) and (is_increasing(modified_report) or is_decreasing(modified_report)):
                return True
    return False

safe_reports = []
for report in reports_list:
    if is_safe(report):
        safe_reports.append(report)
print(len(safe_reports))

safe_reports = []
for report in reports_list:
    if is_safe(report, damp=True):
        safe_reports.append(report)
print(len(safe_reports))

