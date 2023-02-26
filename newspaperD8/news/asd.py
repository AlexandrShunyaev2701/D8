
a = 'ахуел xyёв xyй xyя xуе xуй xую'
b = 'он совсем хуй ахуел в конец'
for i in b:
    if i in a:
        print(b.replace(i,'***'))       