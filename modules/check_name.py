def check_name(name):
    abbadonned_symbols = [",", "\\", "/", ":", "*",
                          "?", "\"", "<", ">", "|", "+", "%", "!", " "]
    for i in abbadonned_symbols:
        if i in name:
            print("Проверьте ввод")
            return False
    return name
