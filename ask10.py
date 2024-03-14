def divisible_numbers(number_list, divisor):
    total = len(number_list)
    count = 0
    for number in number_list:
        if number % divisor == 0:
            count += 1
    percent = count / total * 100
    return percent


file_in = open("./two_cities_ascii.txt", "r")
text = ""
for line in file_in:
    text += str(line)
file_in.close()
bit4_list = ""
for char in text:
    decimal = ord(char)
    binary = bin(decimal)[2:]
    binary = (7 - len(binary))*"0" + binary
    bit4_list += binary[:2] + binary[-2:]

bit16_list = [bit4_list[i: i + 16] for i in range(0, len(bit4_list), 16)]
if len(bit16_list[-1]) != 16:
    bit16_list.pop()
numbers = [int(bit16, 2) for bit16 in bit16_list]
for i in [2, 3, 5, 7]:
    print("Percent of numbers divisible by %d = %.5f" % (i, divisible_numbers(numbers, i)) + "%")
