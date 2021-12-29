def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True


solution(["123", "456", "789"])


# def solution3(phone_book):
#     len_0 = len(phone_book[0])
#     for i in range(1, len(phone_book)):
#         for j in range(len(phone_book[0])):
#             if phone_book[i][j] != phone_book[0][j]:
#                 break
#         if phone_book[i][0:len_0] == phone_book[0]:
#             return False
#     return True