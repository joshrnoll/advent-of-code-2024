from my_lib import get_input

#TODO - Find bug. Code appears to work correctly but produces an answer that is too low.
def main():
    input = get_input()
    reports = input.split("\n")
    safe_reports = 0
    for report in reports:
        if is_safe(report):
            safe_reports += 1
        elif problem_dampener(report):
            safe_reports += 1
    print(safe_reports)
                    

def is_safe(str):
    items = str.split()
    increasing = False
    decreasing = False
    for i in range(len(items)):  
        if i == 0:
            continue
        elif int(items[i]) > int(items[i - 1]):
            increasing = True
            if increasing == True and decreasing == True:
                print(f"Report {str} is unsafe!")
                return False
            elif (int(items[i]) - int(items[i - 1])) > 3:
                print(f"Report {str} is unsafe!")
                return False
        elif int(items[i]) < int(items[i - 1]):
            decreasing = True
            if increasing == True and decreasing == True:
                print(f"Report {str} is unsafe!")
                return False
            elif (int(items[i - 1]) - int(items[i])) > 3:
                print(f"Report {str} is unsafe!")
                return False
        elif int(items[i]) == int(items[i - 1]):
            print(f"Report {str} is unsafe!")
            return False
    if increasing == True or decreasing == True:
        return True
    else:
        print(f"Report {str} is unsafe!")
        return False


def problem_dampener(str):
    items = str.split()
    for i in items:
        items = str.split()
        items.remove(i)
        items = ' '.join(items)
        if is_safe(items):
            # print(f"Report {str} is safe via dampener!")
            return True


if __name__ == "__main__":
    main()