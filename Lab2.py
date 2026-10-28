""" Use temp_list, num_list confusing, I use in the other one eh """

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    user_input = input()
    str_list = user_input.split(",")
    num_list = [float(n) for n in str_list]
    return num_list


def calc_average(temp_list):
    return sum(temp_list) / len(temp_list)


def find_min_max(temp_list):
    return [min(temp_list), max(temp_list)]


def sort_temperature(temp_list):
    return sorted(temp_list)


def calc_median_temperature(temp_list):
    sorted_list = sort_temperature(temp_list)
    n = len(sorted_list)
    mid = n // 2
 
    if n % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        return sorted_list[mid]


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

    average = calc_average(num_list)
    min_max = find_min_max(num_list)
    median = calc_median_temperature(num_list)

    print("Average = " + str(average))
    print("Min/Max = " + str(min_max))
    print("Median =" + str(median))

if __name__ == "__main__":   
    main()