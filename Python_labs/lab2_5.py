#Введите  с  клавиатуры  текст.  Программно  найдите  в  нем  и  выведите 
#отдельно  все  слова,  которые  начинаются  с  большого  латинского 
#символа  (от  A  до  Z)  и  заканчиваются  2  или  4  цифрами,  например 
#«Petr93»,  «Johnny70»,  «Service2002».  Используйте  регулярные 
#выражения.
import re
text = input("Write your text:")
print(text)
pattern = re.compile(r'\b([A-Z][a-z]*\d{2}|[A-Z][a-z]*\d{4})\b')
result = re.findall(pattern,text)
print(result)