def printer_error(s):
    true_char = 'nopqrstuvwxyz'
    count = 0
    for i in s:
        if i in true_char:
            count += 1
    return f'{count}/{len(s)}'



print(printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))