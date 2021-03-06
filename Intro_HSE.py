#!/usr/bin/env python
# coding: utf-8

# ## Лекция 1

# **Развлекаемся с функциями `input()` и `print()`**

# In[2]:


name = input()
print('GL HF, ' + name + 'Больше изменений богу изменений')


# In[4]:


name = input('Введите Ваше имя: ')
print('Добро пожаловать в DH, ' + name)


# In[22]:


print('Добро пожаловать в DH, ' + input('Введите Ваше имя: ')) ## одной строкой, в угоду readability


# **Внезапно, числа!**
# 
# `int()`
# `type()`

# In[5]:


a = int(input('Введите число: '))
print(a * 2)


# **Длина строки:**
# 
# `len()`

# In[7]:


user_name = input('Введите Ваше имя: ')
print(len(user_name))


# In[36]:


user_name = input('Введите Ваше имя: ')
print('Количество букв в Вашем имени:', len(user_name))


# In[38]:


user_name = input('Введите Ваше имя: ')  ## альтернативное решение через конкатенацию
l = str(len(user_name))
print('Количество букв в Вашем имени: ' + l)


# **Методы `str()`**
# 
# `.upper()`
# `.lower()`

# In[33]:


print(name.upper())


# In[39]:


pres_born = input('Укажите фамилию президента, который был у власти при Вашем рождении: ')
pres_living = input('Укажите фамилию нынешнего президента: ')
print(pres_born == pres_living)


# **Строки**

# In[26]:


num = int(input('Введите число: '))
num_1 = str(num + 1)
num_2 = str(num - 1)
num_str = str(num)
print('За числом ' + num_str + ' следует число ' + num_1)
print('Числу ' + num_str + ' предшествует число ' + num_2)


# ### Домашнее задание:
# 
# "Нужно написать программу, которая демонстрирует один простой математический фокус. 
# 
# В начале работы программа должна объявить пользователю, что какое бы число он ни ввёл, ряд арифметических операций превратит в конце это число в 4. Затем нужно запросить у пользователя число, умножить его на 2, прибавить к результату 8, разделить результат на 2, отнять задуманное число. 
# 
# Каждый этап нужно выводить на экран так, чтобы они были прозрачны для пользователя (напр, “Число 5 умноженное на 4 равно 20”).
# 
# Разумеется, финальный результат тоже нужно показать на экране."

# **Решим задачу**, опираясь исключительно на рассмотренные на лекции инструменты: функции `input(), print()`, типы переменных, и конкатенацию строк:

# In[31]:


m = int(input('Код превратит введённое число в 4! Введите любое целое число: '))
m_str = str(m)
m_1 = str(m * 2)
print('Умножим число ' + m_str + ' на 2, получим ' + m_1)
m_2 = str(m * 2 + 8)
print('К числу ' + m_1 + ' прибавим 8, получим ' + m_2)
m_3 = str((m * 2 + 8) // 2)
print('Разделим число ' + m_2 + ' пополам, получим ' + m_3)
m_4 = str((m * 2 + 8) // 2 - m)
print('Вычтем из числа ' + m_3 + ' введённое число, получим ' + m_4)


#  **Код ревью:**
#  
#  * в коде лишь одна числовая переменная m, введённая пользователем -> мы можем использовать только её для вычеслений
#      * подозреваю, что это плохо, поскольку делает код более ресурсоёмким
#      * код выполняет лишние повторные вычесления 
#  * остальные переменные переведены в строки для конкатенации в выводе
#  * если бы не было условия выводить результат каждой операции, то все операции можно было бы оформить одной строкой: 
#         m = int(input('Код превратит введённое число в 4! Введите любое целое число: '))
#         m = (m * 2 + 8) // 2 - m
#         print(m)

# **Что делать?** 
# 
# Поиграем с методом .format()

# In[32]:


m = int(input('Код превратит введённое число в 4! Введите любое целое число: '))
m_1 = m * 2
print('Умножим {} на 2, получим {}'.format(m,m_1))
m_2 = m_1 + 8
print('К числу {} прибавим 8, получим {}'.format(m_1,m_2))
m_3 = m_2 // 2
print('Разделим {} на 2, получим {}'.format(m_2,m_3))
m_4 = m_3 - m
print('Вычтем из {} введённое число, получим {}'.format(m_3,m_4))


# Обошлись без строковых переменных, но выполнили условия пошагового вывода.

# Прочитал про **f-strings**, давай попробуем!

# In[17]:


m = int(input('Код превратит введённое число в 4! Введите любое целое число: '))
print(f'Умножим {m} на 2, получим {m * 2}') ## более читаемо и элегантно чем .format()
print(f'К числу {m} прибавим 8, получим {m + 8}')


# Но если задуматься, нам ведь не нужны все промежуточные переменные (m_1, m_2, etc.) - можем ли мы обновлять значение в одной переменной?
