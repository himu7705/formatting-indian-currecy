def format_indian_currency(number):
    num_str = str(number)
    if '.' in num_str:
        whole, decimal = num_str.split('.')
        decimal = '.' + decimal
    else:
        whole = num_str
        decimal = ''
    if len(whole) > 3:
        last_three = whole[-3:]
        rest = whole[:-3]
        parts = []
        while len(rest) > 2:
            parts.insert(0, rest[-2:])
            rest = rest[:-2]
        if rest:
            parts.insert(0, rest)
        formatted =','.join(parts) + ',' + last_three
    else:
        formatted = whole
    return formatted + decimal
