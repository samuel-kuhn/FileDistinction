def find_string_difference(str1, str2):
    start = end = difference1 = difference2 = ""
    delta = abs(len(str1)-len(str2))
    for i in range (min(len(str1), len(str2))):
        if str1[i] == str2[i]:
            start += str1[i]
        else: 
            break
    for i in range (min(len(str1), len(str2))):
        if (str1[::-1][i] == str2[::-1][i]):
            end = str1[::-1][i] + end
        else:
            break
    difference1 = str1[len(start):len(str1)-len(end)]
            
    return(start + difference1 + end)

# Example usage:
str1 = "123345"
str2 = "12745"



print(find_string_difference(str1, str2))