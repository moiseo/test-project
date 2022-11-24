a= int(input())
new = a
count = 0

while(True):
    x = new // 10
    y = new %  10
    result = x + y
    new = (y * 10) + (result % 10)
    count += 1

    if new == a:
        break

print(count)
    
