def mask_phone_number(phone):
    if len(phone) == 10 and phone.isdigit():
        return '******' + phone[-4:] 
    return "Invalid phone number"

print(mask_phone_number("9876543210")) 
print(mask_phone_number("9123456789")) 