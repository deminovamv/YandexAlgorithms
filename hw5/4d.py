def correct_parenthesis_sequence(sequence:str):
    if not sequence:
        return 'NO'
    else:
        pars_sum = 0
        for el in sequence:
            if el == '(':
                pars_sum += 1
            else:
                pars_sum -= 1
                if pars_sum < 0:
                    return 'NO'
        if pars_sum == 0:
            return 'YES'
        return 'NO'

print(correct_parenthesis_sequence(input()))
