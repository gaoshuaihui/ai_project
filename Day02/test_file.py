if __name__ == '__main__':
    print(__name__)
    # file = open(file='C:\\Users\\admin\\Desktop\\example.txt', mode='w', encoding='utf-8')
    # file.write('hello')
    # file.close()

    # file = open(file='C:\\Users\\admin\\Desktop\\example.txt', mode='a', encoding='utf-8')
    # file.write('第二次写入')
    # file.close()
    #
    # file = open(file='C:\\Users\\admin\\Desktop\\example.txt', mode='r', encoding='utf-8')
    # print(file.read())
    # file.close()

    # with open(file='C:\\Users\\admin\\Desktop\\example.txt', mode='r', encoding='utf-8') as file:
    #     for line in file:
    #         print(line)
    #     # print(file.readline())

    # with open(file='C:\\Users\\admin\\Desktop\\example.txt', mode='w', encoding='utf-8') as file:
    #     file.write('第一行\n')
    #     file.write('第二行\n')

    lines = ['line1', 'line2', 'line3']
    with open(file='C:\\Users\\admin\\Desktop\\example.txt', mode='w', encoding='utf-8') as file:
        file.writelines(lines)

        # for line in file:
        #     print(line)
        # print(file.readline())