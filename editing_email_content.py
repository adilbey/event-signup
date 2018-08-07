import pandas

#for path, enter the location of your CSV file
input = pandas.read_csv("PATH")

input['edited_email'] = input['Email'].astype(str) + ";"

list_of_edited_emails=''.join(input['edited_email'].tolist())

print(list_of_edited_emails)