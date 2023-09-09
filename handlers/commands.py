# =================================================================================================================
from aiogram import types, Dispatcher
from config import bot, Admins
from keyboards import buttons


# =================================================================================================================

async def start(message: types.Message):
    if message.from_user.id in Admins:
        await bot.send_message(message.from_user.id, "Добро пожаловать в OSOR!\n"
                                                     "Этот бот для управления бизнесом!",
                               reply_markup=buttons.start_admins_markup)
    else:
        await bot.send_message(message.from_user.id, "Добро пожаловать в OSOR!\n"
                                                     "Этот бот для управления бизнесом!",
                               reply_markup=buttons.staff_markup)


async def info(message: types.Message):
    if message.from_user.id in Admins:
        await message.answer(f"Для чего нужен этот бот ?!🤔 :\n"
                             f"=================================\n"
                             f"Этот бот был создан специально для компании OSOR 👕, для управления бизнесом\n"
                             f"=================================\n"
                             f"В этом боте сотрудники могут вводить данные и приходе и уходе товара, также записывать брони\n"
                             f"А управляющие могут как записывать данные, так и выводить их, и этим "
                             f"самым контролировать как сотрудников, так и кассу\n"
                             f"=================================\n"
                             f"Также для удобной навигации по боту, все кнопки на русском и по названиям понятно что за что отвечает!\n"
                             f"=================================\n"
                             f"‼️ Вы админ ‼️",
                             reply_markup=buttons.start_admins_markup)
    else:
        await message.answer(f"Для чего нужен этот бот ?!🤔 :\n"
                             f"=================================\n"
                             f"Этот бот был создан специально для компании OSOR 👕, для управления бизнесом\n"
                             f"=================================\n"
                             f"В этом боте сотрудники могут вводить данные и приходе и уходе товара, также записывать брони\n"
                             f"А управляющие могут как записывать данные, так и выводить их, и этим "
                             f"самым контролировать как сотрудников, так и кассу\n"
                             f"=================================\n"
                             f"Также для удобной навигации по боту, все кнопки на русском и по названиям понятно что за что отвечает!\n"
                             f"=================================\n"
                             f"‼️ Вы сотрудник ‼️",
                             reply_markup=buttons.staff_markup)


async def products_button(message: types.Message):
    if message.from_user.id in Admins:
        await message.answer('Вы зашли в товары!', reply_markup=buttons.products_admins_markup)
    else:
        await message.answer('Вы зашли в товары!', reply_markup=buttons.products_staff_markup)


"""Только для Админов"""


async def finance_button(message: types.Message):
    if message.from_user.id in Admins:
        await message.answer('Вы зашли в финансы!', reply_markup=buttons.ButtonForFinance_markup)
    else:
        await message.answer('Вы не админ!')


async def pull_data_staff(message: types.Message):
    if message.from_user.id in Admins:
        await message.answer("Выберите снизу из кнопок действие ⬇", reply_markup=buttons.staff_pull_data_markup)
    else:
        await message.answer("Вы не админ")


async def pull_data(message: types.Message):
    if message.from_user.id in Admins:
        await message.answer("Вы зашли к выводу данных товаров \n"
                             "(Внутри них есть приход, уход и брони)\n\n"
                             "Выберите действие, из кнопок снизу!\n", reply_markup=buttons.products_pull_data_markup)
    else:
        await message.answer("Вы не админ!")


async def get_bishkek(message: types.Message):
    if message.from_user.id in Admins:
        await message.answer(f"Вы выбрали Бишкек!", reply_markup=buttons.get_bishkek_markup)
    else:
        await message.answer("Вы не админ!")


async def get_osh(message: types.Message):
    if message.from_user.id in Admins:
        await message.answer(f"Вы выбрали Ош!", reply_markup=buttons.get_branches_osh_markup)
    else:
        await message.answer("Вы не админ!")


async def get_moscow_1(message: types.Message):
    if message.from_user.id in Admins:
        await message.answer(f"Вы выбрали Москву! (Первый филиал)", reply_markup=buttons.get_branches_moscow_1_markup)
    else:
        await message.answer("Вы не админ!")


async def get_moscow_2(message: types.Message):
    if message.from_user.id in Admins:
        await message.answer(f"Вы выбрали Москву! (Второй филиал)", reply_markup=buttons.get_branches_moscow_2_markup)
    else:
        await message.answer("Вы не админ!")


async def ButtonForFinance(message: types.Message):
    if message.from_user.id in Admins:
        await message.answer(f"Выберите снизу из кнопок, что вы хотите получить! ⬇",
                             reply_markup=buttons.ButtonForFinance_markup)
    else:
        await message.answer("Вы не админ!")


async def SalaryButton(message: types.Message):
    if message.from_user.id in Admins:
        await message.answer(f"Выберите с какого филиала! ⬇", reply_markup=buttons.SalaryStaff_markup)
    else:
        await message.answer("Вы не админ!")


async def RegularСustomerButton(message: types.Message):
    if message.from_user.id in Admins:
        await message.answer("Вы зашли с постоянным клиентам!\n"
                             "Выберите из какого города(филиала) хотите вывести!"
                             "Из какого филиала ?! ⬇", reply_markup=buttons.RegularСustomer_markup)
    else:
        await message.answer("Вы не админ!")


async def controlchecout(message: types.Message):
    await message.answer(f"Вы зашли в контроль кассы!\n"
                         f"Снизу расписаны отчеты за дни и месяца!", reply_markup=buttons.control_markup)
# --------------------------------------------------

async def staff_button(message: types.Message):
    if message.from_user.id in Admins:
        await message.answer('Вы зашли к сотрудникам!', reply_markup=buttons.staff_admins_markup)
    else:
        await message.answer("Вы не админ!")


async def get_staff_buttons(message: types.Message):
    if message.from_user.id in Admins:
        await message.answer("Выберите снизу из кнопок ⬇", reply_markup=buttons.data_recording_staff_markup)
    else:
        await message.answer("Вы не админ!")


# --------------------------------------------------

async def back_for_admins(message: types.Message):
    await message.answer('Вы возвратились назад!', reply_markup=buttons.start_admins_markup)


"""----------"""


async def back_for_staff(message: types.Message):
    if message.from_user.id in Admins:
        await message.answer('Вы возвратились назад!', reply_markup=buttons.start_admins_markup)
    else:
        await message.answer('Вы возвратились назад!', reply_markup=buttons.staff_markup)


async def data_recording(message: types.Message):
    await message.answer('Выберите действие, из кнопок снизу!', reply_markup=buttons.data_recording_markup)


# =================================================================================================================

def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])

    dp.register_message_handler(info, commands=['Информация'])

    dp.register_message_handler(data_recording, commands=['запись_данных_товара'])
    dp.register_message_handler(pull_data, commands=['вывести_данные_товара'])

    dp.register_message_handler(get_staff_buttons, commands=['запись_данных_сотрудников'])
    dp.register_message_handler(pull_data_staff, commands=['вывести_данные_сотрудников'])

    dp.register_message_handler(products_button, commands=['Товары'])
    dp.register_message_handler(staff_button, commands=['Сотрудники'])
    dp.register_message_handler(finance_button, commands=['Финансы'])


    dp.register_message_handler(SalaryButton, commands=['Зарплаты'])
    dp.register_message_handler(RegularСustomerButton, commands=['Постоянные_клиенты'])
    dp.register_message_handler(controlchecout, commands=['Контроль_кассы'])

    dp.register_message_handler(get_bishkek, commands=['Бишкек'])
    dp.register_message_handler(get_osh, commands=['Ош'])
    dp.register_message_handler(get_moscow_1, commands=['Москва_1'])
    dp.register_message_handler(get_moscow_2, commands=['Москва_2'])

    dp.register_message_handler(back_for_staff, commands=['<-назад'])
    dp.register_message_handler(back_for_admins, commands=['<назад'])
