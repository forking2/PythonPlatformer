#Завдання 1

# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
# num3=int(input("Enter thirt nimber:"))
#
# numGenrate1=num1*100
# numGenrate2=num2*10
# numGenrate3=(numGenrate1+numGenrate2+num3)
#
# if num1==100:
#     numGenrate3 = (num1+numGenrate2+num3)
#
# print(numGenrate3)


#завдання 2

# num=int(input("Enter Four-digit number:"))
# num1=print(num//1000)
# num2=print(num//400)
# num3=print(num//662)
# num4=print(num%10)
#
# print(1*3*2*4)



#завдання 3

# metersInSm=int(input("Enter lenght in meter:"))
# metersInDtt=int(input("Enter lenght in meter:"))
# metersInMl=int(input("Enter lenght in meter:"))
# metersInMiles=int(input("Enter lenght in meter:"))
#
# Conwert=print(metersInSm*100)
# Conwert=print(metersInDtt*10)
# Conwert=print(metersInMl*1000)
# Conwert=print(metersInMiles*1609,345)



#завдання 4


# data=int(input("Enter base "))
# data1=int(input("enter height"))
#
# print(data*data1)


#завдання 5

# num=int(input("Enter Four-digit number:"))
# num1=print(num//1128)
# num2=print(num//902.4)
# num3=print(num//4512)
# num4=print(num//2256)
#
# print('-------')
#
# print(num//2256)
# print(num//4512)
# print(num//902.4)
# print(num//1128)











#дз 28.05.2024




#завдання 1

# num1 = int(input('Choose first number: '))
# num2 = int(input('Choose second number: '))
# num3 = int(input('choose third number: '))
# print('you have this operation: + or *')
# op = input('Choose operation: ')
# if op == '+':
#     print(num1 + num2 + num3)
# elif op == '*':
#     print((num1 * num2 * num3))



#завдання 1


# num1 = int(input('Choose first number: '))
# num2 = int(input('Choose second number: '))
# num3 = int(input('choose third number: '))
# print('you have this operation: min max or average ')
# op = input('Choose operation: ')
# if op == 'min':
#     if num1<num2 and num3>num1:
#         print((num2,"-is minemall number",
#           num1,"is midell number",
#           num3,"is other bigest number"))
# if num1>num2 and num2<num3:
#     print(num3, "-is max number",
#           num1, "is mid number",
#           num2, "is min bigest number")
# if num1<num2 and num3<num2 and num3>num1:
#     print(num2, "-is max number",
#           num3, "is mid number",
#           num1, "is min bigest number")

#друге завдання не зміг віконати тому що не знав як задавати умову в умові


#завдання 3

# num1 = int(input('Choose first number in meter: '))
# print('you have this operation: ml inch or yard')
# op = input('Choose operation: ')
# if op == 'ml':
#     print(num1 * 0.000621371)
# elif op == 'inch':
#     print((num1 * 39.3701))
# elif op == 'yard':
#     print((num1 * 1.09361))









#ДЗ 04_06_2024



'''print("Ввиберіть номер від 1 до 7")
op=input("Введіть вибраний номер:")
if op=='1':
    print("Понеділок")
elif op=='2':
    print("Вівторок")
elif op=="3":
    print("Середа")
elif op=='4':
    print("Четверг")
elif op=='5':
    print("П'ятниця")
elif op=='6':
    print("суббота")
elif op=='7':
    print("Неділя")'''



#Завдання 2




'''print("Ввиберіть номер від 1 до 12")
op=input("Введіть вибраний номер:")
if op=='1':
    print("січень")
elif op=='2':
    print("Лютий")
elif op=="3":
    print("Березень")
elif op=='4':
    print("Квітень")
elif op=='5':
    print("Травень")
elif op=='6':
    print("Червень")
elif op=='7':
    print("Липень")
elif op=='8':
    print("Серпень")
elif op=='9':
    print("Вересень")
elif op=='10':
    print("Жовтень")
elif op=='11':
    print("Листопад")
elif op=='12':
    print("Грудень")
'''




#Завдання 3


'''print("Ввиберіть любе число")
op=int(input("Введіть вибраний номер:"))
if op>0:
    print(op,"«Number is positive»")
if op<0:
    print(op,"«Number is negative»")
if op==0:
    print(op,"«Number is equal to zero»")'''






#Завдання 4



'''num1=int(input("Введіть перше число"))
num2=int(input("Введіть друге число"))

if num2>num1:
    print(num2,"-найбільше число",
          num1,"-найменше число")
elif num2<num1:
    print(num1, "-найбільше число",
          num2, "-найменше число")
elif num2==num1:
    print(num1,"=",num2)
'''








#Дз 11_06_2024



#завданння 1




# num=int(input("Enter number"))
# numCount=num%3
# numCount2=num%5
#
# if numCount==0 or numCount==0:
#     print(num,"Fizz")
# if numCount!=0:
#     print("Non Fizz")
# if numCount2==0:
#     print(num,"Buzz")
# elif numCount2!=0:
#     print("Non Buzz")
# if numCount==0 and numCount2==0:
#     print(num,"Fizz Brizz")
# elif numCount2!=0 and numCount!=0:
#     print(num)








#завдання 2


#
# num=int(input("Enter number"))
# for i in range(num,8,1):
#     print(num**i)

















#Здання 3

# CostKiyvstar=15
# CostVodafon=20
# CostLifeSell=16
#
# CostKV=10
# CostKL=12
# CostLV=10
#
# num=int(input("як довго ви спілкувалися"))
# num2=input("На який оператор ви звонили:Kiyvstar,Vodafon,LifeSell")
# num3=input("Яким оператором ви користуєтися: Kiyvstar,Vodafon,LifeSell")
#
# if num2=='Kiyvstar' and num3=='Vodafon':
#     reslt=print(
#         num2,"-коштує",CostKiyvstar,'грн','\t',
#         num3,"-коштує",CostVodafon,'грн','\t',
#         "сума розмови становитть",num*CostKV,'грн',)
#
#
# elif num2=='Kiyvstar' and num3=='LifeSell':
#     reslt2=print(
#     num2, "-коштує", CostKiyvstar,'грн','\t',
#     num3, "-коштує", CostLifeSell,'грн','\t',
#     "сума розмови становитть", num * CostKL,'грн')
#
#
# elif num2=='Vodafon' and num3=='LifeSell':
#     reslt3 = print(
#         num2, "-коштує", CostVodafon,'грн','\t',
#         num3, "-коштує", CostLifeSell,'грон','\t',
#         "сума розмови становитть", num * CostLV,'грн')


#Дз 11_06_2024



#завданння 1




# num=int(input("Enter number"))
# numCount=num%3
# numCount2=num%5
#
# if numCount==0 or numCount==0:
#     print(num,"Fizz")
# if numCount!=0:
#     print("Non Fizz")
# if numCount2==0:
#     print(num,"Buzz")
# elif numCount2!=0:
#     print("Non Buzz")
# if numCount==0 and numCount2==0:
#     print(num,"Fizz Brizz")
# elif numCount2!=0 and numCount!=0:
#     print(num)








#завдання 2


#
# num=int(input("Enter number"))
# for i in range(num,8,1):
#     print(num**i)

















#Здання 3

# CostKiyvstar=15
# CostVodafon=20
# CostLifeSell=16
#
# CostKV=10
# CostKL=12
# CostLV=10
#
# num=int(input("як довго ви спілкувалися"))
# num2=input("На який оператор ви звонили:Kiyvstar,Vodafon,LifeSell")
# num3=input("Яким оператором ви користуєтися: Kiyvstar,Vodafon,LifeSell")
#
# if num2=='Kiyvstar' and num3=='Vodafon':
#     reslt=print(
#         num2,"-коштує",CostKiyvstar,'грн','\t',
#         num3,"-коштує",CostVodafon,'грн','\t',
#         "сума розмови становитть",num*CostKV,'грн',)
#
#
# elif num2=='Kiyvstar' and num3=='LifeSell':
#     reslt2=print(
#     num2, "-коштує", CostKiyvstar,'грн','\t',
#     num3, "-коштує", CostLifeSell,'грн','\t',
#     "сума розмови становитть", num * CostKL,'грн')
#
#
# elif num2=='Vodafon' and num3=='LifeSell':
#     reslt3 = print(
#         num2, "-коштує", CostVodafon,'грн','\t',
#         num3, "-коштує", CostLifeSell,'грон','\t',
#         "сума розмови становитть", num * CostLV,'грн')





# дз.20_06_2024




#завдяння 1
# num1=int(input("Enter first number"))
# num2=int(input("Enter second number"))
#
# for i in range(num1,num2,1):
#     if i % 7==0:
#         print(i)
#     elif i%7!=0:
#         print("Не має кратних чисел в діапазоні")





#завдання 2
# num1=int(input("Enter first number"))
# num2=int(input("Enter second number"))
# count=0
# print("Всі числа діапазону")
# for i in range(num1,num2,1):
#     print(i)
# # print("Числа діапазону за спаданням")
# # for i in range(num1,num2,-1):
# #     print(i)
#
# print("Числа кратні семи")
# for i in range(num1,num2):
#     if i%7==0:
#         print(i)
#     elif i%7!=0:
#         print("Не кратне семи")
#
# for i in range(num1,num2):
#     if i%5==0:
#         count+=1
#         print(i,'\n',count,"-кратних п'яти ")
#
#     elif i%5!=0:
#         print("Не кратне п'яти")









#завдання 3
# num1=int(input("Enter first number"))
# num2=int(input("Enter second number"))
# for i in range(num1,num2,1):
#     if i%3==0:
#         print('Fizz')
#     elif i%3!=0:
#         print('no Fizz')
#
#
# for i in range(num1,num2,1):
#     if i%5==0:
#         print('Buzz')
#     elif i%5!=0:
#         print('no Buzz')
#
#
# for i in range(num1,num2,1):
#     if i%3==0 and i%5==0:
#         print('Fizz Buzz')
#     elif i%3!=0 and i%5!=0:
#         print('no Fizz Buzz')

#проблема в тому що кожне число діапазону підписується кратне чи ні тобто на одне число по 2-3 підписи кратне чи ні,підкажіть будь ласка як це прибрати













# Завдання 1
# num1=int(input('Enter first number'))
# num2=int(input('Enter second number'))
#
# sum=0
# sum2=0
# sum3=0
# sum4=0
# sum6=0
# sum5=0
# SumaChisel1=0
# SumaChisel2=0
# SumaChisel3=0
#
# for i in range(num1,num2+1):
#     if i%2==0:
#         SumaChisel1+=1
#         sum+=i
#         sum2+=1
#         print("Сума праних чисел:",sum)
#
#
#
#     elif i%2!=0:
#         SumaChisel2+=1
#         sum3+=i
#         sum4+=1
#         print("Сума не парних чисел:", sum3)
# print('Середнэ арефметичне суми парних чесел',sum//SumaChisel1,'\n',
#       'Середнэ арефметичне суми не парних чесел',sum3//SumaChisel2)
#
#
#
#
# print('сума чисел кратних 9')
# for i in range(num1,num2+1):
#     if i % 9 == 0:
#         SumaChisel3+=1
#         sum6+= i
#         sum5+= 1
# print("Сума чисел, кратних 9:",sum6)
# print('Середнє арефметичне суми скратних 9',sum6//SumaChisel3)





# Завдання 2
# num=int(input("Enter number"))
# SimVol=input("So..choose symbol")
#
# for i in range(num):
#     print(SimVol)


# Завдання 3
#
# num=int(input("Enter number"))
#
# while num-7:
#
#    if num>0: print('Number is positive')
#
#    elif num==0: print('Number is equal to zero')
#
#    else: print('Number is negative')
#
#    num=int(input())
#
# print('Good bye!')






# Завдання 4
# num=int(input("Enter number"))
# num2=int(input("Enter second number"))


# Count=0
# for i in range(num,num2,1):
#     MaxCount=max(int(Count+1))
#     MinCount=min(int(Count+1))
# print(MaxCount,MinCount)

#не вдалося виконати,скажіть будь ласка як треба це зробити








#02_07_2024



#завдання 1
# numX=int(input("Enter first nuber"))
# numY=int(input("Enter second number"))
#
# count=(numX**numY)
# print(count)
# for i in range(numX,count,1):
#     print(i)





#завдання 2
# count=0
# for i in range(100,1000,1):
#     num_str=str(i)
#     if num_str[0]==num_str[1] or num_str[0]==num_str[2] or num_str[1]==num_str[2]:
#         count+=1
# print(count,'-кількість чисел які повторюються')







#завдання 3
# count=0
# for i in range(100,10000,1):
#     num_str=str(i)
#     if num_str[0]!=num_str[1] or num_str[0]!=num_str[2] or num_str[1]!=num_str[2]:
#         count+=1
# print(count,'-кількість чисел які не повторюються')






#завдання 4
# num=int(input("Enter number"))
# for i in range(1,num+1,1):
#     print(i)
#     num_str=str(i)
#     Count=(num_str and i)!=3

    # def Filt():
#     Count=(num_str and i)!=3 and (num_str and i)!=6
# print()










# # 10_07_2024
# # Завдання 2
# num1=int(input("Enter first number"))
# num2=int(input("Enter second number"))
# count=0
# sum=0
# for i in range(num1,num2,1):
#     if i%num1==0:
#         print(i,"-просте число")
#     elif i%num1!=0:
#         print(i,'-Не просте число')
#
#
#
#
#
# # Завдання 2
# for i in range(1,11,1):
#     count=(i*1)
#     print('\n',i,"*",1,'=',count)
#
#     count2=(i*2)
#     print(i,"*",2,'=',count2)
#
#     count3=(i*3)
#     print(i,"*",3,'=',count3)
#
#     count4=(i*4)
#     print(i,"*",4,'=',count4)
#
#     count5=(i*5)
#     print(i,"*",5,'=',count5)
#
#     count6=(i*6)
#     print(i,"*",6,'=',count6)
#
#     count7=(i*7)
#     print(i,"*",7,'=',count7)
#
#     count8=(i*8)
#     print(i,"*",8,'=',count8)
#
#     count9=(i*9)
#     print(i,"*",9,'=',count9)
#
#     count10 = (i * 10)
#     print(i, "*", 10, '=', count10)
#
#
#
# # Завдання 2
# # # Завдання 3
# nun=print("Choose number")
# count=input('enter number')
# if count=='1':
#     for i in range(1, 11, 1):
#         count = (i * 1)
#         print(i,"*",1,'=',count)
#
# elif count == '2':
#     for i in range(1, 11, 1):
#         count2=(i*2)
#         print(i,"*",2,'=',count2)
#
#
# elif count == '3':
#     for i in range(1, 11, 1):
#         count3 = (i * 3)
#         print(i,"*",3,'=',count3)
#
# elif count == '4':
#             for i in range(1, 11, 1):
#                 count4 = (i * 4)
#                 print(i,"*",4,'=',count4)
#
# elif count == '5':
#                 for i in range(1, 11, 1):
#                     count5 = (i * 5)
#                     print(i,"*",5,'=',count5)
# elif count == '6':
#     for i in range(1, 11, 1):
#         count6 = (i * 6)
#         print(i,"*",6,'=',count6)
#
# elif count == '7':
#             for i in range(1, 11, 1):
#                 count7 = (i * 7)
#                 print(i,"*",7,'=',count7)
#
# elif count == '9':
#     for i in range(1, 11, 1):
#         count9 = (i * 9)
#         print(i,"*",9,'=',count9)
#
#
# elif count == '10':
#     for i in range(1, 11, 1):
#         count9 = (i * 10)
#         print(i,"*",10,'=',count9)

#
#
#
#



import asyncio,logging,sys
from aiogram import Bot,Dispatcher,html,F
from aiogram.client.default import DefaultBotProperties
from  aiogram.enums import  ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.types import  Message,KeyboardButton,ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder,InlineKeyboardMarkup,InlineKeyboardButton

Token='7109297067:AAF8vmLZtBby6WEwzMOJyXOyqH-7pK5ENFY'
dp=Dispatcher()

@dp.message(CommandStart())  # /start
async def command_start(message: Message):
    await  message.answer(f'Hi,{html.bold(message.from_user.full_name)}!')





@dp.message(Command('url'))
async  def command_url(message:Message,bot:Bot):
    builder=InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Game',url='https://media.npr.org/assets/img/2014/08/07/monkey-selfie_custom-6624e8356a07d872997e801d7a04aa8cdc8fbaac.jpg?s=1100&c=50&f=jpeg'))
    builder.row(InlineKeyboardButton(text='Author1',url='https://www.instagram.com/bobrickcs22/'))
    builder.row(InlineKeyboardButton(text='Author2',url='https://www.instagram.com/marian.sal_/'))


    userId = message.from_user.id
    chatInfo = await bot.get_chat(userId)
    if not chatInfo.has_private_forwards:
        # builder.row(InlineKeyboardButton(text='User', url=f'tg://user?id={userId}'))
        await message.answer('Oберіть питання:', reply_markup=builder.as_markup())



# @dp.message(Command('button'))
# async def cmd_button(message:Message):
#     klava=[
#         [KeyboardButton(text='Game')],
#         [KeyboardButton(text='Virus')],
#
#     ]
#     keyboard = ReplyKeyboardMarkup(keyboard=klava, resize_keyboard=True, input_field_placeholder='оберіть команду')
#     await message.answer("Наші команди", reply_markup=keyboard)





# @dp.message(Command('Author'))
# async def command_Author(message:Message):
#     await message.answer('Bobrick and Marian')







async def main():
    bot = Bot(token=Token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await  dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())












