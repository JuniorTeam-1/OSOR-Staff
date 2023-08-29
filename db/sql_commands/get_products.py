# ====================================================================================================================
from aiogram import types, Dispatcher

from db.db_bish.ORM_Bish import cursor_bish
from db.db_osh.ORM_Osh import cursor_osh
from db.db_moscow_1.ORM_Moscow_1 import cursor_moscow_1
from db.db_moscow_2.ORM_Moscow_2 import cursor_moscow_2


# ====================================================================================================================

async def sql_command_products_bish(message: types.Message):
    cursor_bish.execute("SELECT * FROM products")

    batch_size = 5  # Количество записей (людей) для извлечения
    while True:
        products = cursor_bish.fetchmany(batch_size)
        if not products:
            break

        for product in products:
            await message.answer(f"Товар: {product[1]}\n"
                                 f"Дата прихода: {product[2]}\n"
                                 f"Дата ухода: {product[3]}\n"
                                 f"Имя заказчика: {product[4]}\n"
                                 f"Номер тел заказчика: {product[5]}\n"
                                 f"Продавец: {product[6]}\n"
                                 f"Цена(без скидки): {product[7]}\n"
                                 f"Скидка: {product[8]}\n"
                                 f"Итоговая цена: {product[9]}\n"
                                 f"Город: {product[10]}\n")


async def sql_command_products_osh(message: types.Message):
    cursor_osh.execute("SELECT * FROM products")

    batch_size = 5  # Количество записей (людей) для извлечения
    while True:
        products = cursor_osh.fetchmany(batch_size)
        if not products:
            break

        for product in products:
            await message.answer(f"Товар: {product[1]}\n"
                                 f"Дата прихода: {product[2]}\n"
                                 f"Дата ухода: {product[3]}\n"
                                 f"Имя заказчика: {product[4]}\n"
                                 f"Номер тел заказчика: {product[5]}\n"
                                 f"Продавец: {product[6]}\n"
                                 f"Цена(без скидки): {product[7]}\n"
                                 f"Скидка: {product[8]}\n"
                                 f"Итоговая цена: {product[9]}\n"
                                 f"Город: {product[10]}\n")


async def sql_command_products_moscow_1(message: types.Message):
    cursor_moscow_1.execute("SELECT * FROM products")

    batch_size = 5  # Количество записей (людей) для извлечения
    while True:
        products = cursor_moscow_1.fetchmany(batch_size)
        if not products:
            break

        for product in products:
            await message.answer(f"Товар: {product[1]}\n"
                                 f"Дата прихода: {product[2]}\n"
                                 f"Дата ухода: {product[3]}\n"
                                 f"Имя заказчика: {product[4]}\n"
                                 f"Номер тел заказчика: {product[5]}\n"
                                 f"Продавец: {product[6]}\n"
                                 f"Цена(без скидки): {product[7]}\n"
                                 f"Скидка: {product[8]}\n"
                                 f"Итоговая цена: {product[9]}\n"
                                 f"Город: {product[10]}\n")


async def sql_command_products_moscow_2(message: types.Message):
    cursor_moscow_2.execute("SELECT * FROM products")

    batch_size = 5  # Количество записей (людей) для извлечения
    while True:
        products = cursor_moscow_2.fetchmany(batch_size)
        if not products:
            break

        for product in products:
            await message.answer(f"Товар: {product[1]}\n"
                                 f"Дата прихода: {product[2]}\n"
                                 f"Дата ухода: {product[3]}\n"
                                 f"Имя заказчика: {product[4]}\n"
                                 f"Номер тел заказчика: {product[5]}\n"
                                 f"Продавец: {product[6]}\n"
                                 f"Цена(без скидки): {product[7]}\n"
                                 f"Скидка: {product[8]}\n"
                                 f"Итоговая цена: {product[9]}\n"
                                 f"Город: {product[10]}\n")


# ====================================================================================================================

def register_sql_commands(dp: Dispatcher):
    dp.register_message_handler(sql_command_products_bish, commands=['Товары_Бишкек'])
    dp.register_message_handler(sql_command_products_osh, commands=['Товары_Ош'])
    dp.register_message_handler(sql_command_products_moscow_1, commands=['Товары_Москва_1'])
    dp.register_message_handler(sql_command_products_moscow_2, commands=['Товары_Москва_2'])