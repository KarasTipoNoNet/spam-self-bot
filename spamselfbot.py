import os
from time import sleep
import discord
from discord.ext import commands

instant_start = input('Запустить бота сейчас с стандартными настройками? Да[y]/Нет[n]: ')
if instant_start == 'n':
    os.system('cls' if os.name == 'nt' else 'clear')

    print('''Выберите вариант загрузки токена
1. Вставить токен аккаунта
2. Загрузить из token.txt''')
    token_loader_option = input()

    if token_loader_option == '1':
        token = input('Вставте токен тут: ')
        option = 'Вставка'
        sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif token_loader_option == '2':
        token = open('token.txt', 'r').readline()
        print('Токен загружен!')
        option = 'Загрузка из файла'
        sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print('Неизвестная функция!')
        input()
        quit()    

    sleep(3)
    prefix = input('Введите префикс: ')

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''Предпросмотр опций:

Токен: вариант: {option} / токен: {token}

Префикс: {prefix}
''')
    input('Press ENTER for start main code...')
    os.system('cls' if os.name == 'nt' else 'clear')

elif instant_start == 'y':

    prefix = '.'
    token = open('token.txt', 'r').readline()

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''Предпросмотр опций:

Токен: вариант: skiped / токен: {token}

Префикс: {prefix}
''')
    input('Press ENTER for start main code...')
    os.system('cls' if os.name == 'nt' else 'clear')

client = commands.Bot(command_prefix = prefix, self_bot = True)
client.remove_command('help')

@client.event
async def on_ready():
    print(f'''Спам селф бот работает!
Команды бота: {prefix}help

ВНИМАНИЕ!
У тебя огромный шанс быть забаненым! Продолжай использовать на свой страх и риск!''')

@client.command()
async def help(ctx):
    await ctx.message.delete()
    print(f'''Prefix: {prefix}
{prefix}spam [amount] [message] - начать спам!
{prefix}mur_mur - помурчим?
{prefix}fortnite - фортнайт или пападжи?
{prefix}balgarka - пожалуйста, распели меня балгаркой''')

@client.command()
async def spam(ctx, amount : int = 100, *, message = "Я бог спама! Мухахахаххахахахх @everyone"):
    await ctx.message.delete()
    for a in range(amount):
        try:
            await ctx.send(message)
        except:
            print("Ты был кикнут / забанен / замьючен на сервере где спамил или заблокирован пользователем которому спамил! Спам остановлен...")
            break

@client.command()
async def mur_mur(ctx):
    await ctx.message.delete()
    await ctx.send('Д-д-дай мне свой дискордик')
    sleep(0.5)
    await ctx.send('дис-дискордик')
    sleep(0.5)
    await ctx.send('я хочу тебе помурчать :smiling_face_with_3_hearts:')
    sleep(0.5)
    await ctx.send('так, спокойно...')
    sleep(0.5)
    await ctx.send('м-можно')
    sleep(0.5)
    await ctx.send('можно мы вместе помурчим')
    sleep(0.5)
    await ctx.send('п-помурчим вот так...')
    sleep(0.5)
    await ctx.send('мур мур мур мур мур')
    await ctx.send('мяу мяу')
    sleep(1)
    await ctx.send('МЯЯЯЯЯЯУ الأحمقالأحمقالأحمقالأحمقالأحمقالأ')
    for a in range(3):
        await ctx.send('حمقالأحمقالأحمقالأحمقالأحمقالأحمقالأحمقالأحمقالأحمقالأحمقالأحمقالأحمقالأحمقالأحمقالأحمق')


@client.command()
async def balgarka(ctx):
    await ctx.message.delete()
    await ctx.send('Пожалуйста...')
    sleep(0.5)
    await ctx.send('Распили меня балгаркой')
    sleep(0.5)
    for a in range(4):
        await ctx.send(':sob:')
    await ctx.send('Умоляю')
    sleep(0.1)
    await ctx.send('Распили меня балгаркой')
    await ctx.send('Ну распили')
    for a in range(4):
        await ctx.send(':sob:')

@client.command()
async def fortnite(ctx):
    await ctx.message.delete()
    await ctx.send('Фортнай или пападжи?')
    await ctx.send('пападжи')
    await ctx.send('пападжи или икис бокис сериес икис?')
    await ctx.send('пападжи')
    await ctx.send('пападжи или полистейшн фаааайв?')
    await ctx.send('полистейшн файв')
    await ctx.send('полистейшн файв или лчкт')
    await ctx.send('лчкт')
    await ctx.send('лчкт или хайпер икис икис икис икис')
    await ctx.send('хайпер икис икис икис икис')
    await ctx.send('хайпер икис икис икис икис или грент тзефт авто вайф')
    await ctx.send('грент тзефт авто вайф')




client.run(token, bot = False)