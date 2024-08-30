
###     Roll# PIAIC59391

name= input("Enter your name:")
numbers:list=[]
first_number= int(input("Enter your first favorite number:"))
numbers.append(first_number)
second_number= int(input("Enter your second favorite number:"))
numbers.append(second_number)
third_number= int(input("Enter your third favorite number:"))
numbers.append(third_number)
print(f"Hello, {name}! Let's explore your favorite numbers:")

info_numbers:list=[]

if first_number%2 ==0:
     info_numbers.append((first_number,"even"))
else:
     info_numbers.append((first_number,"odd"))

print(f"The number {info_numbers[0][0]} is {info_numbers[0][1]}.")


if second_number%2 ==0:
     info_numbers.append((second_number,"even"))
else:
    info_numbers.append((second_number,"odd"))
print(f"The number {info_numbers[1][0]} is {info_numbers[1][1]}.")


if third_number%2 ==0:
    info_numbers.append((third_number,"even"))
else:
    info_numbers.append((third_number,"odd"))
print(f"The number {info_numbers[2][0]} is {info_numbers[2][1]}.")

sum=0
for itr in numbers:
     print(f"The number {itr} and its square: {(itr, itr**2)}")
     sum=sum+itr


print("Amazing! The sum of your favorite numbers is: ",sum)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


checksum=is_prime(sum)

if checksum==True:
    print(f"Wow, {sum} is a prime number!")

