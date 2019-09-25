import io_handler

file_1_path = raw_input("Enter the file path of data set 1: ")
file_2_path = raw_input("Enter the file path of data set 2: ")

data_set_1 = io_handler.read_csv(file_1_path)
data_set_2 = io_handler.read_csv(file_2_path)