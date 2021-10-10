# This program checks a password created by a user and validates it according to the requirements of the program




print("Create a strong password that you can easily remember. Consider using special symbols(!,@,#,$,%,&and*), "
      "numbers, uppercase and lowercase characters to make your password stronger.")


def pr_red(skk):
    print("\033[91m {}\33[00m" .format(skk))


def password_validation(password):
    spe_sym = ['!', '@', '#', '$', '%', '&', '*']
    passwd = "Strong password"
    if len(password) < 7:
        pr_red("Password should have a minimum of 7 characters")
        passwd = "Weak password"
    elif len(password) > 14:
        pr_red("Password should have a maximum of 14 characters")
        passwd = "Weak password"
    elif not any(char.isdigit() for char in password):
        passwd = "Weak password"
    elif not any(char in spe_sym for char in password):
        passwd = "Weak password"
    d_s_l = {"digits": 0, "spe_sym": 0, "lowercase": 0, "uppercase": 0}
    for x in password:
        if x.isdigit():
            d_s_l["digits"] += 1
        elif x.islower():
            d_s_l["lowercase"] += 1
        elif x.isupper():
            d_s_l["uppercase"] += 1
        else:
            d_s_l["spe_sym"] += 1
    while d_s_l["digits"] < 2:
        pr_red("Password should have at least two digits")
        passwd = "Weak password"
        break
    while d_s_l["lowercase"] < 2:
        pr_red("Password should have at least two lowercase characters")
        passwd = "Weak password"
        break
    while d_s_l["uppercase"] < 1:
        pr_red("Password should have at least one uppercase character")
        passwd = "Weak password"
        break
    while d_s_l["spe_sym"] < 2:
        pr_red("Password should have at least two special characters")
        passwd = "Weak password"
        break
    if passwd:
        return passwd


print(password_validation(input("Create password: ")))
