def main():
    left_list = get_list('input.txt', 'left')
    right_list = get_list('input.txt', 'right')

    similarity = get_similarity(left_list, right_list)
    print(f"The similarity score is: {similarity}")

    total = get_distances_total(left_list, right_list)
    print(f"The total distance is: {total}")
        

def get_list(filename, leftorright):
    if leftorright == 'right':
        leftorright = 0
    if leftorright == 'left':
        leftorright = 1
    list = []
    
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.split()
            list.append(line[leftorright])
    return list


def get_smallest(list):
    smallest = int(list[0])
    for i in list:
        if int(i) < smallest:
            smallest = int(i)
    return smallest


def calculate_total(list):
    total = 0
    for i in list:
        total += int(i)
    return total


def get_distances_total(list1, list2):
    if len(list1) == len(list2):
        distances = []
        for i in range(len(list1)):
            left_smallest = get_smallest(list1)
            right_smallest = get_smallest(list2)
            if left_smallest > right_smallest:
                distance = left_smallest - right_smallest
            else:
                distance = right_smallest - left_smallest
            distances.append(distance)
            list1.remove(str(left_smallest))
            list2.remove(str(right_smallest))
    else:
        raise Exception("ERR: Lists are not the same length")

    try:
        total = calculate_total(distances)
        return total
    except NameError:
        print("ERR: Could not calculate total. Was distances defined?")


def get_similarity(list1, list2):
    similarity = 0
    for i in list1:
        multiplier = 0
        for j in list2:
            if i == j:
                multiplier += 1
        product = int(i) * multiplier
        similarity += product
    return similarity


if __name__ == "__main__":
    main()

