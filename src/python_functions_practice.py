def return_10():
    return 10 

def add(first_number, second_number):
    return first_number + second_number
    return sum

def subtract(number_10, number_05):
    return number_10 - number_05
    return sum

def multiply(number_4, number_2):
    return number_4 * number_2
    return sum

def divide(number_10, number_02):
    return number_10 / number_02
    return sum

def length_of_string(string_length):
    return len(string_length)

def join_string(string_1, string_2):
    return add(string_1,string_2)

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

months_of_the_year = ["January", "February", "March", "April", "May", "June", "July", "August", "September"]

def number_to_full_month_name(number_of_month):
    position_in_list_index = number_of_month - 1
    return months_of_the_year[position_in_list_index]

def number_to_short_month_name(month_num):
    month_dict = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    return month_dict[month_num]


