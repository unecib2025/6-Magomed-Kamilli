#1
users=["admin","operator"]
new=input("Enter new user: ")
users.append(new)
print(users)
#2
list1=["root","security"]
list1.insert(0,input("Enter administrator's name: "))
print(list1)
#3
user=["bob","charlie","alice"]
user.remove(input("Enter user's name: "))
print(list)
#4
mylist=["Access granted", "Login failed","Connection Lost"]
print("Last log:",mylist.pop(len(mylist)-1))
print("Remaining logs:",mylist)
#5
logins=['ok', 'error', 'ok', 'error', 'error']
print("Number of login errors:",logins.count("error"))
#6
log_list=["Access ok", "Breach detected", "System reboot", "Breach detected"]
print("First detection of intrusion on positions: ",log_list.index("Breach detected"))
#7
numbers=[3, 1, 2, 3, 1, 2]
print(numbers.sort())
#8
reports=["2025-10-01", "2025-10-02", "2025-10-03"]
reports.reverse()
print(reports)
#9
messages_list=["alert", "spam", "login", "error", "spam", "alert"]
while "spam" in messages_list:
    messages_list.remove("spam")
messages_list.append("END_LOG")
messages_list.reverse()
print("Log after cleaning: ",messages_list)
print("'alert' count: ", messages_list.count("alert"))
#10
whitelist=[]
whitelist.append("192.168.0.1")
whitelist.append("192.168.0.2")
whitelist.append("192.168.0.3")
whitelist.append("192.168.0.4")
whitelist.append("192.168.0.5")
whitelist.remove(input("Enter IP for deletion: "))
new_IP=input("Enter new IP: ")
whitelist.insert(2,new_IP)
whitelist.sort()
print("Updated whitelist: ",whitelist)
print("New IP's index",whitelist.index(new_IP))
#11
logins_list=["ok", "fail", "fail", "ok", "fail"]
print("Failed Logins: ",logins_list.count("fail"))
while "fail" in logins_list:
    logins_list.remove("fail")
logins_list.append("audit_completed")
logins_list.reverse()
print("Final login list: ",logins_list)
print("First 'ok' index: ",logins_list.index("ok"))
#Вопросы
#1 append() добавляет элемент в конец списка, а insert() добавляет элемент в указанную позицию, сдвигая остальные элементы.
#2 удаляет последний элемент списка и возвращает его.
#3 Нельзя, remove() удаляет лишь первое вхождение элемента, чтобы удалить несколько, надо вызывать remove() несколько раз.
#4 Разворачивает список на месте, но не возвращает его, а меняет исходный.
#5 count() возвращает сколько раз элемент встречается в списке, а index() возвращает первый индекс вхождения элемента.
#6 Изменяющие исходный список это: append(), insert(), remove(), pop(), sort(), reverse(), а возвращают новое значение sorted() и reversed().
#7 программа выдаст следующую ошибку: ValueError: <элемент> is not in list
#8 упрощает поиск аномалий, повторов и закономерностей, а так же после сортировки легко применять алгоритмы анализа или визуализации.