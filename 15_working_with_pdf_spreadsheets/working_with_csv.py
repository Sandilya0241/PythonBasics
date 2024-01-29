import csv

def readCSV():
    # Open a file
    with open("example.csv",encoding='utf-8') as fp:
        # csv.reader
        data_reader = csv.reader(fp)
        try:
            # reformat it into a python object list of lists
            list_data = list(data_reader)
            # for line in list_data[:5]:
            #     print(line)
            # print(list_data[10][3])

            # all_emails = []
            # for data in list_data[1:]:
                # all_emails.append(data[3])
            # print(all_emails)


            # Full name
            full_name_list = []
            for data in list_data[1:]:
                full_name_list.append(data[1]+ " " +data[2])

            print(full_name_list)
        except UnicodeDecodeError as ude:
            print(ude)
        except:
            print("Unknown error")


# Write CSV
def write_CSV():
    with open("to_save_file.csv","w",newline="") as fp:
        csv_writter = csv.writer(fp,delimiter=",")
        csv_writter.writerow(['a','b','c'])
        csv_writter.writerows([[1,2,3],[4,5,6],[7,8,9]])

    with open("to_save_file.csv","a",newline="") as fp:
        csv_writter = csv.writer(fp,delimiter=",")
        csv_writter.writerow([7,8,9])

if __name__ == "__main__":
    # readCSV()
    write_CSV()