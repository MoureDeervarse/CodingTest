def solution(phone_book):
    answer = True
    check_number = ''
    
    sorted_numbers = sorted(phone_book);
    for number in sorted_numbers:
        if check_number == '':
            check_number = number
            continue
        
        if number.startswith(check_number):
            answer = False
            break;
        else:
            check_number = number
    
    return answer