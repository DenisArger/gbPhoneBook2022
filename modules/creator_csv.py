def create_csv(filename="new_export"):
    with open('database.csv', "rb") as data:
        with open(f"export/{filename}.csv", "wb") as new_file:
            new_file.writelines(data.readlines())
