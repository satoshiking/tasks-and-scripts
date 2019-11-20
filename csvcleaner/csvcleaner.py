import os
import sys

import pandas as pd


def get_row():
    print("There are {} rows in your csv file in range [0, {}]:".
          format(df.shape[0], df.shape[0]-1))
    row = None
    while True:
        if row:
            if row.isdigit():
                row = int(row)
                if 0 <= row <= df.shape[0]-1:
                    break
                else:
                    print("Type correct number in range:[0-{}]".
                          format(df.shape[0]-1))
            else:
                print("...Only numbers are supported")
        row = input("Type row number: ")
    return row


def get_column(correct_columns):
    print("There are next available columns in your csv file:")
    print(correct_columns)
    column = None
    while column not in correct_columns:
        if column:
            print("There is no column=", column)
        column = input("Type column name: ")
    return column


def display_title_bar():
    os.system('clear')
    print("\t**********************************************")
    print("\t***   application to clean data in CSV     ***")
    print("\t**********************************************")
    print()


def get_user_choice():
    # Let users know what they can do.
    print()
    print("[0] Show CSV as it is now.")
    print("[1] Show CSV in dictionary format.")
    print("[2] Remove leading and trailing characters as spaces and /n /t")
    print("[3] Change text case (for all columns)")
    print("[4] Change text case for a specified column")
    print("[5] Check for duplicated rows")
    print("[6] Delete a row")
    print("[7] Delete a column")
    print("[8] Update a cell")
    print("[9] Sort rows by column value")
    print("[10] Check (and optionally change) column value(s)")
    print("[11] Save cleaned data to CSV file.")
    print("[q] Quit.")

    return input("What would you like to do? ")


def show_csv():
    print("Our data from CSV:")
    print(df, "\n")


def show_csv_as_dict():
    columns = list(df.columns)
    df_sorted = df.sort_values(by=columns)
    print('Data in dictionary format ...\n', df_sorted)


def check_duplicates():
    global df

    duplicates = df.duplicated().sum()
    print("%s duplicate(s) have found." % duplicates)

    if duplicates > 0:
        choice = 'q'
        while choice not in 'yYnN':
            choice = input("Drop duplicates (y/n)? ")
            if choice in 'yY':
                df = df.drop_duplicates().reset_index(drop=True)
                dupicates_new = df.duplicated().sum()
                print("{} duplicate(s) were droped.".
                      format(duplicates-dupicates_new))


def remove_spaces_and_feed():
    global df

    df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
    print("All leading and trailing characters were removed")
    print('Transformed data ...\n', df)


def change_case_all_columns():
    global df, df_obj

    df[df_obj.columns] = df_obj.apply(lambda x: x.str.upper())
    print('Transformed data ...\n', df)


def change_case_column():
    global df

    # Find all columns with string type
    correct_columns = list(df.select_dtypes(include=['object']).columns)
    if correct_columns:
        column = get_column(correct_columns)
        df[column] = df[column].str.upper()
        print('Transformed data ...\n', df)
    else:
        print('There is no columns with string values to change text case')


def delete_column():
    global df

    column = get_column(list(df.columns))
    df = df.drop(columns=column)
    print("\nColumn %s was deleted" % column)
    print('Transformed data ...\n', df)


def delete_row():
    global df
    row = get_row()
    df = df.drop(row)
    print("\nRow %s was deleted" % row)
    print('Transformed data ...\n', df)


def update_cell():
    global df

    row, column = get_row(), get_column(list(df.columns))
    value = input("Please enter new cell value: ")
    df.loc[row, column] = value
    print("\n Cell [{}, {}] was updated".format(row, column))
    print('Transformed data ...\n', df)


def sort_rows_by_column():
    global df

    column = get_column(list(df.columns))
    df_sorted = df.sort_values(by=column)
    print('Sorted data ...\n', df_sorted)


def save_csv():
    OUTPUT_FILE = input("Type the name of new csv file: ")
    try:
        df.to_csv(OUTPUT_FILE, index=False, encoding='utf8')
        print("\nCleaned CSV is saved as", OUTPUT_FILE)
    except Exception as e:
        print("\nCleaned CSV is not saved")
        print(e)


def quit():
    print("\nBye - Bye")


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Exactly one argument is needed ...")
        print("Usage: python csvcleaner.py \"filename.csv\"")
        sys.exit()
    else:
        INPUT_FILE = sys.argv[1]

        try:
            df = pd.read_csv(INPUT_FILE)
        except Exception as e:
            print("Couldn't open file", INPUT_FILE)
            print(e)
            sys.exit()

        df_obj = df.select_dtypes(['object'])
        display_title_bar()
        show_csv()

        # Set up a loop where users can choose what they'd like to do.
        choice = ''
        while choice != 'q':
            choice = get_user_choice()
            display_title_bar()

            if choice == '0':
                show_csv()
            elif choice == '1':
                show_csv_as_dict()
            elif choice == '2':
                remove_spaces_and_feed()
            elif choice == '3':
                change_case_all_columns()
            elif choice == '4':
                change_case_column()
            elif choice == '5':
                check_duplicates()
            elif choice == '6':
                delete_row()
            elif choice == '7':
                delete_column()
            elif choice == '8':
                update_cell()
            elif choice == '9':
                sort_rows_by_column()
            elif choice == '10':
                print("don't know")
            elif choice == '11':
                save_csv()
            elif choice == 'q':
                quit()
            else:
                print("\nI didn't understand that choice.\n")
