# =======================================================================================================================
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from keyboards import buttons

from db.db_bish.ORM_Bish import bish_sql_product_care_insert
from db.db_osh.ORM_Osh import osh_sql_product_care_insert
from db.db_moscow_1.ORM_Moscow_1 import moscow_1_sql_product_care_insert
from db.db_moscow_2.ORM_Moscow_2 import moscow_2_sql_product_care_insert
from datetime import datetime


# =======================================================================================================================

class FsmCareProducts(StatesGroup):
    name = State()  # Название товара
    info_product = State()
    date_care = State()  # Дата где будут записаны уходы
    name_customer = State()
    phone_customer = State()
    name_salesman = State()
    phone_salesman = State()
    price = State()
    discount = State()
    city = State()
    care_photo_product = State()
    submit = State()


async def fsm_start(message: types.Message):
    await FsmCareProducts.name.set()
    await message.answer('Название товара?', reply_markup=buttons.cancel_markup)


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FsmCareProducts.next()
    await message.answer('Информация о товаре!?')


async def load_info_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['info'] = message.text
    await FsmCareProducts.next()
    await message.answer('Дата ухода?')


async def load_date_care(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date_care'] = message.text
    await FsmCareProducts.next()
    await message.answer('Имя заказчика?')


async def load_name_customer(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_customer'] = message.text
    await FsmCareProducts.next()
    await message.answer('Номер телефона заказчика? \n'
                         '+996 или +7')


async def load_phone_customer(message: types.Message, state: FSMContext):
    if message.text.find("+"):
        await message.answer('Начните с +')
    else:
        async with state.proxy() as data:
            data['phone_customer'] = message.text
        await FsmCareProducts.next()
        await message.answer('Имя продавца?')


async def load_name_salesman(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_salesman'] = message.text
    await FsmCareProducts.next()
    await message.answer('Номер телефона продавца? \n'
                         '+996 или +7')


async def load_phone_salesman(message: types.Message, state: FSMContext):
    if message.text.find("+"):
        await message.answer('Начните с +')
    else:
        async with state.proxy() as data:
            data['phone_salesman'] = message.text
        await FsmCareProducts.next()
        await message.answer('Цена?')


async def load_price(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['price'] = message.text
        await FsmCareProducts.next()
        await message.answer('Скидка?\n'
                             '(Сумму скидки!)')
    else:
        await message.answer('Укажите цифрами!')


async def load_discount(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['discount'] = message.text
            data['calculation'] = int(data['price']) - int(data['discount'])

        await FsmCareProducts.next()
        await message.answer('Город?\n'
                             'Если Москва, то указать какой филиал!\n'
                             'Выберите снизу по кнопкам, какой город!',
                             reply_markup=buttons.city_markup)
    else:
        await message.answer('Укажите цифрами!')


async def load_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
    await FsmCareProducts.next()
    await message.answer('Фотография товара?')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id
        data['date'] = datetime.now()
        await message.answer_photo(
            data["photo"],
            caption=f"Данные товара: \n"
                    f"Название товара: {data['name']}\n"
                    f"Информация о товаре: {data['info']}\n"
                    f"Дата ухода товара: {data['date_care']}\n"
                    f"Заказчик: {data['name_customer']}\n"
                    f"Номер телефона заказчика: {data['phone_customer']}\n"
                    f"Продацев: {data['name_salesman']}\n"
                    f"Цена: {data['price']}\n"
                    f"Скидка: {data['discount']}\n"
                    f"Итоговая цена: {data['calculation']}\n"
                    f"Город: {data['city']}")
    await FsmCareProducts.next()
    await message.answer("Все верно?", reply_markup=buttons.submit_markup)


async def load_submit(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == 'да':
            if data['city'] == 'Бишкек':
                await bish_sql_product_care_insert(state)
                await message.answer('Готово!', reply_markup=buttons.data_recording_markup)
                await state.finish()

            elif data['city'] == 'ОШ':
                await osh_sql_product_care_insert(state)
                await message.answer('Готово!', reply_markup=buttons.data_recording_markup)
                await state.finish()

            elif data['city'] == 'Москва 1-филиал':
                await moscow_1_sql_product_care_insert(state)
                await message.answer('Готово!', reply_markup=buttons.data_recording_markup)
                await state.finish()

            elif data['city'] == 'Москва 2-филиал':
                await moscow_2_sql_product_care_insert(state)
                await message.answer('Готово!', reply_markup=buttons.data_recording_markup)
                await state.finish()

        elif message.text.lower() == 'нет':
            await message.answer('Хорошо, отменено', reply_markup=buttons.data_recording_markup)
            await state.finish()


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=buttons.data_recording_markup)


# =======================================================================================================================

def register_products(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals='Отмена', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['записать_уход_товара'])

    dp.register_message_handler(load_name, state=FsmCareProducts.name)
    dp.register_message_handler(load_info_product, state=FsmCareProducts.info_product)
    dp.register_message_handler(load_date_care, state=FsmCareProducts.date_care)
    dp.register_message_handler(load_name_customer, state=FsmCareProducts.name_customer)
    dp.register_message_handler(load_phone_customer, state=FsmCareProducts.phone_customer)
    dp.register_message_handler(load_name_salesman, state=FsmCareProducts.name_salesman)
    dp.register_message_handler(load_phone_salesman, state=FsmCareProducts.phone_salesman)
    dp.register_message_handler(load_price, state=FsmCareProducts.price)
    dp.register_message_handler(load_discount, state=FsmCareProducts.discount)
    dp.register_message_handler(load_city, state=FsmCareProducts.city)
    dp.register_message_handler(load_photo, state=FsmCareProducts.care_photo_product, content_types=['photo'])
    dp.register_message_handler(load_submit, state=FsmCareProducts.submit)