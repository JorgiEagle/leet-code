def licenseKeyFormatting(s: str, k: int) -> str:
    s = s.replace('-','')
    first_group_length = len(s) % k
    key_list = [s[:first_group_length]] if first_group_length else []
    s = s[first_group_length:]
    for index in range(0, len(s), k):
        key_list.append(s[index:index+k])

    return '-'.join(key_list)

licenseKeyFormatting("5F3Z-2e-9-w", 4)