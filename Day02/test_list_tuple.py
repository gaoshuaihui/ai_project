# # 创建一个list
#
my_list = [1, 2, 3, 4, 5,"hello",8.9,[1,23,4]]
print(my_list)

# print(my_list.sort(reverse=True))
#
# print(sorted(my_list,reverse=True))

print(my_list[::-1])

#
# my_list[0] = "改变了"
# print(my_list)
#
# for i in my_list:
#     print(i)



# # 创建一个元组
# my_tuple = (1, 2, 3, 4, 5, 'hello', 8.9, [1, 23, 4])
# print(my_tuple)
#
# # my_tuple[0] = "我也要改变了"
# # print(my_tuple)
#
# for i in my_tuple:
#     print(i)


# # # 创建一个字典
# my_dict = {"name": "张三", "age": 18}
# print(my_dict)
#
#
# for i in my_dict:
#     print(i)
#
# for i in my_dict.keys():
#     print(my_dict[i])
#
# for i in my_dict.values():
#     print(i)
#
# print(my_dict["name"])
# print(my_dict["age"])
#
# my_dict["name"] = "李四"
# print(my_dict)
#
# my_dict.update({"name": "王五"})
# print(my_dict)
#
# my_dict.update({"second_name": "王五"})
# print(my_dict)
#
# my_dict.pop("name")
# print(my_dict)
#
# my_dict.clear()
# print(my_dict)

print("***************************************************")
## 创建一个集合
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
print(list_1)

set_1 = set(list_1)

print(set_1)
for i in set_1:
    print(i)
print("------------------")

print(list(set_1))

print(list(set(list_1)))










