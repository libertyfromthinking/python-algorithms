def solution(phone_book):
    phone_book.sort()
    
    for i,j in phone_book, phone_book[1:]:
        if i in j:
            return False

    return True
        
