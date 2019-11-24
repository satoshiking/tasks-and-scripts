import os
import sys

import pandas as pd

INPUT_FILE = 'input.csv'


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


def display_grouped(column):
    df_grouped = df.groupby(column).count()
    i = 1
    for row in list(df_grouped.index):
        print('  ', i, row, ':', df_grouped.loc[row][0])
        i += 1
    print()


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
    print("[12] Quit.")

    return input("What would you like to do? ")


def get_case_choice():
    print("  1. Title case")
    print("  2. lower case")
    print("  3. UPPER case")
    print("  4. Sentense case")
    choice = input("Enter number to choose function to execute: ")
    while choice not in '1234':
        choice = input("Please enter valid number: ")
    return choice


def show_csv():
    print("Our data from CSV:")
    print(df, "\n")


def show_csv_as_dict():
    df2 = df.to_dict('records')
    i = 0
    for row in df2:
        print(i, ":", row)
        i += 1


def check_duplicates():
    global df

    is_duplicats = False
    df_grouped = df.groupby(list(df.columns))
    for group in df_grouped.indices:
        duplicates = list(df_grouped.indices[group])
        if len(duplicates) > 1:
            print("rows: {} are the same".format(duplicates))
            is_duplicats = True
    if not is_duplicats:
        print("There is no duplicated rows")
    print()
    show_csv_as_dict()


def remove_spaces_and_feed():
    global df

    df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
    print("All leading and trailing characters were removed")
    print('Transformed data ...')
    show_csv_as_dict()


def change_case_all_columns():
    global df, df_obj

    choice = get_case_choice()
    if choice == '1':
        df[df_obj.columns] = df_obj.apply(lambda x: x.str.title())
    elif choice == '2':
        df[df_obj.columns] = df_obj.apply(lambda x: x.str.lower())
    elif choice == '3':
        df[df_obj.columns] = df_obj.apply(lambda x: x.str.upper())
    elif choice == '4':
        if len(list(df_obj.columns)) > 0:
            df[df_obj.columns] = df_obj.apply(lambda x: x.str.lower())
            df[df_obj.columns[0]] = df_obj.apply(lambda x: x.str.title())

    print('Transformed data ...')
    show_csv_as_dict()


def change_case_column():
    global df

    # Find all columns with string type
    correct_columns = list(df.select_dtypes(include=['object']).columns)
    if correct_columns:
        column = get_column(correct_columns)
        choice = get_case_choice()
        if choice == '1':
            df[column] = df[column].str.title()
        elif choice == '2':
            df[column] = df[column].str.lower()
        elif choice == '3':
            df[column] = df[column].str.upper()
        elif choice == '4':
            df[column] = df[column].str.title()

        print('Transformed data ...')
        show_csv_as_dict()
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
    df = df.drop(row).reset_index(drop=True)
    print("\nRow %s was deleted" % row)
    print('Transformed data ...')
    show_csv_as_dict()


def update_cell():
    global df

    row, column = get_row(), get_column(list(df.columns))
    value = input("Please enter new cell value: ")
    df.loc[row, column] = value
    print("\n Cell [{}, {}] was updated".format(row, column))
    print('Transformed data ...')
    show_csv_as_dict()


def sort_rows_by_column():
    global df

    column = get_column(list(df.columns))
    df_sorted = df.sort_values(by=column)
    print('Sorted data ...')
    df2 = df_sorted.to_dict('records')
    i = 0
    for row in df2:
        print(i, ":", row)
        i += 1


def check_column_values():
    global df

    column = get_column(list(df.columns))
    display_grouped(column)

    if input("Want to change some value ('y' for yes and otherwise no)? ") == 'y':
        more = 'y'
        while more == 'y':
            old = input("Enter the value in the column to change: ")
            while old not in list(df.groupby(column).count().index):
                old = input("Please enter a valid column value: ")

            new = input("Enter the new value: ")
            df[column] = df.apply(lambda x: new if x[column] == old else x[column], axis=1)
            display_grouped(column)
            more = input("Need more changes ('y' for yes and otherwise for no)? ")


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

        # Set up a loop where users can choose what they'd like to do.
        choice = ''
        while choice != '12':
            choice = get_user_choice()

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
                check_column_values()
            elif choice == '11':
                save_csv()
            elif choice == '12':
                quit()
            else:
                print("\nI didn't understand that choice.\n")
