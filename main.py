from aiogram import Bot, Dispatcher, F, filters, types
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import asyncio

bot = Bot(token="7209734898:AAFwLYi6kdZK9apbRKLqhAWxEHdVKu2e7hM")
dp = Dispatcher(bot=bot)

class Mystate(StatesGroup):
    first_name = State()
    last_name = State()
    contact = State()
    lang = State()
    credit = State()
    credit_num = State()

language = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="uz"), KeyboardButton(text="ru")]
], resize_keyboard=True)

contact_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📞", request_contact=True)]
], resize_keyboard=True)

basket_uz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Sotib olish"), KeyboardButton(text="Bekor qilish"), KeyboardButton(text="Ortga")]
], resize_keyboard=True)

basket_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Купить"), KeyboardButton(text="отменить"), KeyboardButton(text="назад")]
], resize_keyboard=True)

main_button_uz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Menyu"), KeyboardButton(text="Savatcha"), KeyboardButton(text="Biz haqimizda")],
    [ KeyboardButton(text="Sizning ma'lumotlaringiz"), KeyboardButton(text="Qo'llab-quvvatlash"), KeyboardButton(text="Tilni o'zgartirish")]
], resize_keyboard=True)
main_button_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="меню"), KeyboardButton(text="корзина"), KeyboardButton(text="о нас")],
    [ KeyboardButton(text="ваша информация"), KeyboardButton(text="поддержка"), KeyboardButton(text="Поменять язык")]
], resize_keyboard=True)

foods_uz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Ovqatlar"), KeyboardButton(text="Ichimliklar"), KeyboardButton(text="Ortga")]
], resize_keyboard=True)

foods_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="еда"), KeyboardButton(text="напитки"), KeyboardButton(text="назад")]
], resize_keyboard=True)

food_inline_uz = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Pizza", callback_data="pizza_uz"), InlineKeyboardButton(text="Lavash", callback_data="lavash_uz"), InlineKeyboardButton(text="Kartoshka fri", callback_data="fri_uz")],
    [InlineKeyboardButton(text="Burger", callback_data="burger_uz"), InlineKeyboardButton(text="Hot-dog", callback_data="hotdog_uz"), InlineKeyboardButton(text="KFC", callback_data="kfc_uz")],
    [InlineKeyboardButton(text="❌", callback_data="delete")]
])
food_inline_ru = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="пицца", callback_data="pizza_ru"), InlineKeyboardButton(text="лаваш", callback_data="lavash_ru"), InlineKeyboardButton(text="картофель фри", callback_data="fri_ru")],
    [InlineKeyboardButton(text="бургер", callback_data="burger_ru"), InlineKeyboardButton(text="хот-дог", callback_data="hotdog_ru"), InlineKeyboardButton(text="КФС", callback_data="kfc_ru")],
    [InlineKeyboardButton(text="❌", callback_data="delete")]
])

drinks_uz = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Suv", callback_data="water_uz"), InlineKeyboardButton(text="Pepsi", callback_data="pepsi_uz"), InlineKeyboardButton(text="Cola", callback_data="cola_uz")],
    [InlineKeyboardButton(text="Fanta", callback_data="fanta_uz"), InlineKeyboardButton(text="Olma Sharbati", callback_data="apple_jiuce_uz"), InlineKeyboardButton(text="o'rik sharbati", callback_data="apricot_uz")],
    [InlineKeyboardButton(text="❌", callback_data="delete")]
])
drinks_ru = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="вода", callback_data="water_ru"), InlineKeyboardButton(text="Пепси", callback_data="pepsi_ru"), InlineKeyboardButton(text="Кола", callback_data="cola_ru")],
    [InlineKeyboardButton(text="Фанта", callback_data="fanta_ru"), InlineKeyboardButton(text="яблочный сок", callback_data="apple_jiuce_ru"), InlineKeyboardButton(text="абрикосовый сок", callback_data="apricot_ru")],
    [InlineKeyboardButton(text="❌", callback_data="delete")]
])

pizza_uz_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="pizza_uz_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
lavash_uz_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="lavash_uz_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
frie_uz_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="frie_uz_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
burger_uz_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="burger_uz_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
hotdog_uz_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="hotdog_uz_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
kfc_uz_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="kfc_uz_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
water_uz_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="water_uz_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
pepsi_uz_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="pepsi_uz_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
cola_uz_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="cola_uz_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
fanta_uz_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="fanta_uz_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
apple_uz_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="apple_uz_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
apricot_uz_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="apricot_uz_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
pizza_ru_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="pizza_ru_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
lavash_ru_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="lavash_ru_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
frie_ru_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="frie_ru_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
burger_ru_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="burger_ru_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
hotdog_ru_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="hotdog_ru_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
kfc_ru_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="kfc_ru_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
water_ru_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="water_ru_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
pepsi_ru_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="pepsi_ru_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
cola_ru_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="cola_ru_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
fanta_ru_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="fanta_ru_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
apple_ru_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="apple_ru_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])
apricot_ru_buy_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒", callback_data="apricot_ru_buy"), InlineKeyboardButton(text="❌", callback_data="delete")]
])



credit_card = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Humo"), KeyboardButton(text="Uzcard")]
], resize_keyboard=True)

basket_uzlang = []
basket_rulang = []
total = []

@dp.callback_query(F.data == "buy")
async def buyed(call: CallbackQuery):
    await call.message.answer("Mahsulot savatchaga solindi")

@dp.callback_query(F.data == "delete")
async def delete_message(call: CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
# https://t.me/Fastfuirousfood_bot - botning linki

# registratrisya boshlandi

@dp.message(filters.CommandStart())
async def start_bot(message: Message, state: FSMContext):
    await state.set_state(Mystate.lang)
    await message.answer("Tilni tanlang\nвыберите язык", reply_markup=language)

@dp.message(Mystate.lang)
async def choose_lang(message: Message, state: FSMContext):
    await state.update_data(lang=message.text)
    await state.set_state(Mystate.first_name)
    data = await state.get_data()
    if data["lang"] == "uz":
        await message.answer(text="Ismingizni kiriting", reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(text="введите ваше имя", reply_markup=ReplyKeyboardRemove())

@dp.message(Mystate.first_name)
async def first_name(message:Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(Mystate.last_name)
    data = await state.get_data()
    if data["lang"] == "uz":
        await message.answer(text="Familiyangizni kiriting")
    else:
        await message.answer("введите свою фамилию")

@dp.message(Mystate.last_name)
async def last_name(message: Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(Mystate.contact)
    data = await state.get_data()
    if data["lang"] == "uz":
        await message.answer("Raqamingizni jo'nating", reply_markup=contact_button)
    else:
        await message.answer("пришлите свой номер", reply_markup=contact_button)

@dp.message(Mystate.contact)
async def contact(message: Message, state: FSMContext):
    await state.update_data(contact=message.contact.phone_number)
    data = await state.get_data()
    await state.clear()
    if data["lang"] == "uz":
        await message.answer(f"Xush kelibsiz {data["first_name"]}", reply_markup=main_button_uz)
    else:
        await message.answer(f"добро пожаловать {data["first_name"]}", reply_markup=main_button_ru)

# registratsiya tugadi

# menyu uzbek tilida boshlangan

@dp.message(F.text == "Menyu")
async def food_uz(message: Message, state: FSMContext):
    await message.answer("Quyidagilardan birini tanlang 👇", reply_markup=foods_uz)

@dp.message(F.text == "Ovqatlar")
async def ovqatlar_uz(message: Message):
    await message.answer("Yoqimli ishtaha 🤗", reply_markup=food_inline_uz)

@dp.callback_query(F.data == "pizza_uz")
async def pizza_uz(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=88bc91b6e0b5c0e43601063dc7c698ec12f22bcc-12413751-images-thumbs&n=13", caption="Pizza - 56000 so'm 💸", reply_markup=pizza_uz_buy_delete)
        

@dp.callback_query(F.data == "pizza_uz_buy")
async def pizza_buy(call: CallbackQuery):
    basket_rulang.append("пицца - 56000 сум")
    basket_uzlang.append("Pizza - 56000 so'm")
    total.append(56000)
    await call.message.answer(text="Mahsulot savatga solindi 🛒")

@dp.callback_query(F.data == "lavash_uz")
async def lavash_uz(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=98c2544a3cb83ffc4ab230f772251ed8ba66ee06-9107157-images-thumbs&n=13", caption="Lavash - 16000 so'm 💸", reply_markup=lavash_uz_buy_delete)
    
        

@dp.callback_query(F.data == "lavash_uz_buy")
async def pizza_buy(call: CallbackQuery):
    basket_rulang.append("лаваш - 16000 сум")
    basket_uzlang.append("Lavash - 16000 so'm")
    total.append(16000)
    await call.message.answer(text="Mahsulot savatga solindi 🛒")

@dp.callback_query(F.data == "fri_uz")
async def fri_uz(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=dd544175da285774b7da963cd552ba75c9f837ce-9181971-images-thumbs&n=13", caption="Kartoshka fri - 9000 so'm 💸", reply_markup=frie_uz_buy_delete)
    
        

@dp.callback_query(F.data == "frie_uz_buy")
async def pizza_buy(call: CallbackQuery):
    basket_rulang.append("картофель фри - 9000 сум")
    basket_uzlang.append("Kartoshka fri - 9000 so'm")
    total.append(9000)
    await call.message.answer(text="Mahsulot savatga solindi 🛒")

@dp.callback_query(F.data == "burger_uz")
async def burger_uz(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=f6f9a8bdecee14b01ddb206647be5df09185add1-12649183-images-thumbs&n=13", caption="Burger - 19000 so'm 💸", reply_markup=burger_uz_buy_delete)
    
        

@dp.callback_query(F.data == "burger_uz_buy")
async def pizza_buy(call: CallbackQuery):
    basket_rulang.append("бургер - 19000 сум")
    basket_uzlang.append("Burger - 19000 so'm")
    total.append(19000)
    await call.message.answer(text="Mahsulot savatga solindi 🛒")

@dp.callback_query(F.data == "hotdog_uz")
async def hotdog_uz(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=1a5a2698b55bf34098d6ebac3248d80c01fd5f97-12911692-images-thumbs&n=13", caption="Hot-dog - 12000 so'm 💸", reply_markup=hotdog_uz_buy_delete)
    
        

@dp.callback_query(F.data == "hotdog_uz_buy")
async def pizza_buy(call: CallbackQuery):
    basket_rulang.append("Hot-dog - 12000 сум")
    basket_uzlang.append("Hot-dog - 12000 so'm")
    total.append(12000)
    await call.message.answer(text="Mahsulot savatga solindi 🛒")

@dp.callback_query(F.data == "kfc_uz")
async def kfc_uz(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=438ff152cb7f4680efd1b8f27fb285e85938f473-9873353-images-thumbs&n=13", caption="KFC - 28000 so'm 💸", reply_markup=kfc_uz_buy_delete)
    
       

@dp.callback_query(F.data == "kfc_uz_buy")
async def pizza_buy(call: CallbackQuery):
    basket_rulang.append("KFC - 28000 сум")
    basket_uzlang.append("KFC - 28000 so'm")
    total.append(28000)
    await call.message.answer(text="Mahsulot savatga solindi 🛒")

@dp.message(F.text == "Ichimliklar")
async def ichimliklar_uz(message: Message):
    await message.answer("Ichishga nima tanlaysiz❓", reply_markup=drinks_uz)

@dp.callback_query(F.data == "water_uz")
async def water_uz(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=b5747b458c42277b7968739ee94ae472856e98fc-4272115-images-thumbs&n=13", caption="Suv - 5000 so'm 💸", reply_markup=water_uz_buy_delete)
    
        

@dp.callback_query(F.data == "water_uz_buy")
async def pizza_buy(call: CallbackQuery):
    basket_rulang.append("вода - 5000 сум")
    basket_uzlang.append("Suv - 5000 so'm")
    total.append(5000)
    await call.message.answer(text="Mahsulot savatga solindi 🛒")

@dp.callback_query(F.data == "pepsi_uz")
async def pepsi_uz(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=a8d0457ecbce9844b3cf138f2ee47fbbec2e3c2f-11378374-images-thumbs&n=13", caption="Pepsi - 15000 so'm 💸", reply_markup=pepsi_uz_buy_delete)
    
        

@dp.callback_query(F.data == "pepsi_uz_buy")
async def pizza_buy(call: CallbackQuery):
    basket_rulang.append("Пепси - 15000 сум")
    basket_uzlang.append("Pepsi - 15000 so'm")
    total.append(15000)
    await call.message.answer(text="Mahsulot savatga solindi 🛒")

@dp.callback_query(F.data == "cola_uz")
async def cola_uz(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=be98e48115bf467c3483432f6e66e746993c88c6-12814900-images-thumbs&n=13", caption="Cola - 15000 so'm 💸", reply_markup=cola_uz_buy_delete)
    
        

@dp.callback_query(F.data == "cola_uz_buy")
async def pizza_buy(call: CallbackQuery):
    basket_rulang.append("Кола - 15000 сум")
    basket_uzlang.append("Cola - 15000 so'm")
    total.append(15000)
    await call.message.answer(text="Mahsulot savatga solindi 🛒")

@dp.callback_query(F.data == "fanta_uz")
async def fanta_uz(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=bc4bf92b54d23caafeffaf103e541c01afed9ad5-10122654-images-thumbs&n=13", caption="Fanta - 15000 so'm 💸", reply_markup=fanta_uz_buy_delete)
    
        

@dp.callback_query(F.data == "fanta_uz_buy")
async def pizza_buy(call: CallbackQuery):
    basket_rulang.append("Фанта - 15000 сум")
    basket_uzlang.append("Fanta - 15000 so'm")
    total.append(15000)
    await call.message.answer(text="Mahsulot savatga solindi 🛒")

@dp.callback_query(F.data == "apple_jiuce_uz")
async def apple_jiuce_uz(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=4ad3acfdddf1b195c1dfe2cf3585facbe1a141e5-12615871-images-thumbs&n=13", caption="Olma sharbati - 12000 so'm 💸", reply_markup=apple_uz_buy_delete)
    
        

@dp.callback_query(F.data == "apple_uz_buy")
async def pizza_buy(call: CallbackQuery):
    basket_rulang.append("яблочный сок - 12000 сум")
    basket_uzlang.append("Olma sharbati - 12000 so'm")
    total.append(12000)
    await call.message.answer(text="Mahsulot savatga solindi 🛒")

@dp.callback_query(F.data == "apricot_uz")
async def apricot_uz(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=994b039c580e1c948b05f74c4e9d5f8709bf0db9-7544543-images-thumbs&ref=rim&n=33&w=250&h=250", caption="O'rik sharbati - 12000 so'm 💸", reply_markup=apricot_uz_buy_delete)
    
        

@dp.callback_query(F.data == "apricot_uz_buy")
async def pizza_buy(call: CallbackQuery):
    basket_rulang.append("абрикосовый сок - 12000 сум")
    basket_uzlang.append("O'rik sharbati - 12000 so'm")
    total.append(12000)
    await call.message.answer(text="Mahsulot savatga solindi 🛒")

@dp.message(F.text == "Ortga")
async def ortga_uz(message: Message):
    await message.answer("Bosh menyuga qaytdingiz", reply_markup=main_button_uz)

# menyu uzbek tilida tugadi

# menyu rus tilida boshlangan

@dp.message(F.text == "меню")
async def food_ru(message: Message, state: FSMContext):
    await message.answer("выберите один из следующих 👇", reply_markup=foods_ru)

@dp.message(F.text == "еда")
async def ovqatlar_ru(message: Message):
    await message.answer("Приятного аппетита 🤗", reply_markup=food_inline_ru)

@dp.callback_query(F.data == "pizza_ru")
async def pizza_uz(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=88bc91b6e0b5c0e43601063dc7c698ec12f22bcc-12413751-images-thumbs&n=13", caption="пицца - 56000 сум 💸", reply_markup=pizza_ru_buy_delete)
    
        

@dp.callback_query(F.data == "pizza_ru_buy")
async def pizza_buy(call: CallbackQuery):
    basket_uzlang.append("Pizza - 56000 so'm")
    basket_rulang.append("пицца - 56000 сум")
    total.append(56000)
    await call.message.answer(text="Продукт был добавлен в корзину 🛒")

@dp.callback_query(F.data == "lavash_ru")
async def lavash_ru(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=98c2544a3cb83ffc4ab230f772251ed8ba66ee06-9107157-images-thumbs&n=13", caption="лаваш - 16000 сум 💸", reply_markup=lavash_ru_buy_delete)
    
        

@dp.callback_query(F.data == "lavash_ru_buy")
async def pizza_buy(call: CallbackQuery):
    basket_uzlang.append("Lavash - 16000 so'm")
    basket_rulang.append("лаваш - 16000 сум")
    total.append(16000)
    await call.message.answer(text="Продукт был добавлен в корзину 🛒")

@dp.callback_query(F.data == "fri_ru")
async def fri_ru(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=dd544175da285774b7da963cd552ba75c9f837ce-9181971-images-thumbs&n=13", caption="картофель фри - 9000 сум 💸", reply_markup=frie_ru_buy_delete)
    
        

@dp.callback_query(F.data == "frie_ru_buy")
async def pizza_buy(call: CallbackQuery):
    basket_uzlang.append("Kartoshka fri - 9000 so'm")
    basket_rulang.append("картофель фри - 9000 сум")
    total.append(9000)
    await call.message.answer(text="Продукт был добавлен в корзину 🛒")

@dp.callback_query(F.data == "burger_ru")
async def burger_ru(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=f6f9a8bdecee14b01ddb206647be5df09185add1-12649183-images-thumbs&n=13", caption="бургер - 19000 сум 💸", reply_markup=burger_ru_buy_delete)
    
        

@dp.callback_query(F.data == "burger_ru_buy")
async def pizza_buy(call: CallbackQuery):
    basket_uzlang.append("Burger - 19000 so'm")
    basket_rulang.append("бургер - 19000 сум")
    total.append(19000)
    await call.message.answer(text="Продукт был добавлен в корзину 🛒")

@dp.callback_query(F.data == "hotdog_ru")
async def hotdog_uz(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=1a5a2698b55bf34098d6ebac3248d80c01fd5f97-12911692-images-thumbs&n=13", caption="Hot-dog - 12000 сум 💸", reply_markup=hotdog_ru_buy_delete)
    
      

@dp.callback_query(F.data == "hotdog_ru_buy")
async def pizza_buy(call: CallbackQuery):
    basket_uzlang.append("Hot-dog - 12000 so'm")
    basket_rulang.append("Hot-dog - 12000 сум")
    total.append(12000)
    await call.message.answer(text="Продукт был добавлен в корзину 🛒")

@dp.callback_query(F.data == "kfc_ru")
async def kfc_uz(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=438ff152cb7f4680efd1b8f27fb285e85938f473-9873353-images-thumbs&n=13", caption="KFC - 28000 сум 💸", reply_markup=kfc_ru_buy_delete)
    
        

@dp.callback_query(F.data == "kfc_ru_buy")
async def pizza_buy(call: CallbackQuery):
    basket_uzlang.append("KFC - 28000 so'm")
    basket_rulang.append("KFC - 28000 сум")
    total.append(28000)
    await call.message.answer(text="Продукт был добавлен в корзину 🛒")

@dp.message(F.text == "напитки")
async def ichimliklar_ru(message: Message):
    await message.answer("Что вы предпочитаете пить❓", reply_markup=drinks_ru)


@dp.callback_query(F.data == "water_ru")
async def water_ru(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=b5747b458c42277b7968739ee94ae472856e98fc-4272115-images-thumbs&n=13", caption="вода - 5000 сум 💸", reply_markup=water_ru_buy_delete)
    
       
@dp.callback_query(F.data == "water_ru_buy")
async def pizza_buy(call: CallbackQuery):
    basket_uzlang.append("Suv - 5000 so'm")
    basket_rulang.append("вода - 5000 сум")
    total.append(5000)
    await call.message.answer(text="Продукт был добавлен в корзину 🛒")


@dp.callback_query(F.data == "pepsi_ru")
async def pepsi_ru(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=a8d0457ecbce9844b3cf138f2ee47fbbec2e3c2f-11378374-images-thumbs&n=13", caption="Пепси - 15000 сум 💸", reply_markup=pepsi_ru_buy_delete)
    
       

@dp.callback_query(F.data == "pepsi_ru_buy")
async def pizza_buy(call: CallbackQuery):
    basket_uzlang.append("Pepsi - 15000 so'm")
    basket_rulang.append("Пепси - 15000 сум")
    total.append(15000)
    await call.message.answer(text="Продукт был добавлен в корзину 🛒")

@dp.callback_query(F.data == "cola_ru")
async def cola_ru(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=be98e48115bf467c3483432f6e66e746993c88c6-12814900-images-thumbs&n=13", caption="Кола - 15000 сум 💸", reply_markup=cola_ru_buy_delete)
    
       

@dp.callback_query(F.data == "cola_ru_buy")
async def pizza_buy(call: CallbackQuery):
    basket_uzlang.append("Cola - 15000 so'm")
    basket_rulang.append("Кола - 15000 сум")
    total.append(15000)
    await call.message.answer(text="Продукт был добавлен в корзину 🛒")

@dp.callback_query(F.data == "fanta_ru")
async def fanta_ru(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=bc4bf92b54d23caafeffaf103e541c01afed9ad5-10122654-images-thumbs&n=13", caption="Фанта - 15000 сум 💸", reply_markup=fanta_ru_buy_delete)
    
        

@dp.callback_query(F.data == "fanta_ru_buy")
async def pizza_buy(call: CallbackQuery):
    basket_uzlang.append("Fanta - 15000 so'm")
    basket_rulang.append("Фанта - 15000 сум")
    total.append(15000)
    await call.message.answer(text="Продукт был добавлен в корзину 🛒")

@dp.callback_query(F.data == "apple_jiuce_ru")
async def apple_jiuce_ru(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=4ad3acfdddf1b195c1dfe2cf3585facbe1a141e5-12615871-images-thumbs&n=13", caption="яблочный сок - 12000 сум 💸", reply_markup=apple_ru_buy_delete)
    
       

@dp.callback_query(F.data == "apple_ru_buy")
async def pizza_buy(call: CallbackQuery):
    basket_uzlang.append("Olma sharbati - 12000 so'm")
    basket_rulang.append("яблочный сок - 12000 сум")
    total.append(12000)
    await call.message.answer(text="Продукт был добавлен в корзину 🛒")

@dp.callback_query(F.data == "apricot_ru")
async def apricot_ru(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=994b039c580e1c948b05f74c4e9d5f8709bf0db9-7544543-images-thumbs&ref=rim&n=33&w=250&h=250", caption="абрикосовый сок - 12000 сум 💸", reply_markup=apricot_ru_buy_delete)
    
@dp.callback_query(F.data == "apricot_ru_buy")
async def pizza_buy(call: CallbackQuery):
    basket_uzlang.append("O'rik sharbati - 12000 so'm")
    basket_rulang.append("абрикосовый сок - 12000 сум")
    total.append(12000)
    await call.message.answer(text="Продукт был добавлен в корзину 🛒")

@dp.message(F.text == "назад")
async def ortga_ru(message: Message):
    await message.answer("вы вернулись в главное меню", reply_markup=main_button_ru)

# menyu rus tilida tugadi

# Savatcha boshlangan

@dp.message(F.text == "Savatcha")
async def Savat_uz(message: Message):
    global basket_uzlang
    text = ""
    cost = 0
    for i in basket_uzlang:
        text += f"{i}\n"
    for i in total:
        cost += i
    if basket_uzlang == []:
        await message.answer("Savatcha bo'sh 😕")
    else:
        await message.answer(f"{text}\n umumiy hisob - {cost} so'm 💰", reply_markup=basket_uz)

@dp.message(F.text == "Sotib olish")
async def sotib_olish(message: Message, state: FSMContext):
    await state.set_state(Mystate.credit)
    await message.answer("qaysi kartadan tolov qilasiz? 🤔", reply_markup=credit_card)

@dp.message(Mystate.credit)
async def credit_cards(message: Message, state: FSMContext):
    await state.update_data(credit=message.text)
    await state.set_state(Mystate.credit_num)
    await message.answer("Karta raqimini kiriting 💳")

@dp.message(Mystate.credit_num)
async def credit_num(message: Message, state: FSMContext):
    text = str(message.text)
    if text.isdigit() and len(text) == 16:
        await state.update_data(credit_num=message.text)
        await state.clear()
        await message.answer("Xaridingiz uchun rahmat! 😊", reply_markup=main_button_uz)
        global basket_uzlang
        global basket_rulang
        global total
        basket_uzlang.clear()
        basket_rulang.clear()
        total.clear()
    else:
        await message.answer(text="Xato")

@dp.message(F.text == "Bekor qilish")
async def bekor_qilish(message: Message):
    global total
    global basket_uzlang
    global basket_rulang
    basket_rulang.clear()
    basket_uzlang.clear()
    total.clear()
    await message.answer(text="Bizning xizmatlarimizdan foydalanganingiz uchun rahmat 😊", reply_markup=main_button_uz)

# savat uzbek tilida tugadi

@dp.message(F.text == "корзина")
async def Savat_ru(message: Message):
    global basket_rulang
    text = ""
    cost = 0
    for i in basket_rulang:
        text += f"{i}\n"
    for i in total:
        cost += i
    if basket_rulang == []:
        await message.answer("Корзина пуста 😕")
    else:
        await message.answer(f"{text}\nОбщая сумма - {cost} сум 💰", reply_markup=basket_ru)

@dp.message(F.text == "Купить")
async def sotib_olish(message: Message, state: FSMContext):
    await state.set_state(Mystate.credit)
    await message.answer("какой картой вы платите? 🤔", reply_markup=credit_card)

@dp.message(Mystate.credit)
async def credit_cards(message: Message, state: FSMContext):
    await state.update_data(credit=message.text)
    await state.set_state(Mystate.credit_num)
    await message.answer("Введите номер карты 💳")

@dp.message(Mystate.credit_num)
async def credit_num(message: Message, state: FSMContext):
    text = str(message.text)
    if text.isdigit() and len(text) == 16:   
        await state.update_data(credit_num=message.text)
        await state.clear()
        await message.answer("Спасибо за покупку! 😊", reply_markup=main_button_ru)
        global basket_uzlang
        global basket_rulang
        global total
        basket_uzlang.clear()
        basket_rulang.clear()
        total.clear()
    else:
        await message.answer(text="ошибка")
    
@dp.message(F.text == "отменить")
async def bekor_qilish_ru(message: Message):
    global basket_rulang
    global total
    basket_uzlang.clear()
    basket_rulang.clear()
    total.clear()
    await message.answer(text="Благодарим вас за использование наших услуг 😊", reply_markup=main_button_ru)

# savat rus tilida tugadi

# about us qismi uzbek tilida

@dp.message(F.text == "Biz haqimizda")
async def about_us_uz(message: Message):
    await message.answer(f"Bizning fast-foodlar tez va sifatli tayyorlanadi. Yuqori sifatli massaliqlar, ziravorlar va o'z ishining ustalari bo'lmish oshpazlar sizni hech qachon och qoldirmaydi. Narxlari bo'lsa hamyonbop!")   

# about us rus tilida 

@dp.message(F.text == "о нас")
async def about_us_ru(message: Message):
    await message.answer(f"Наш фастфуд готовится быстро и качественно. Высококачественное мясо, специи и шеф-повара никогда не оставят вас голодными, а цены доступные!") 

# about us tugadi

# foydalanuvchi ma'lumoti uzbek tilida

@dp.message(F.text == "Sizning ma'lumotlaringiz")
async def your_info_uz(message: Message):
    await message.answer(f"To'liq ism: {message.from_user.full_name}\nUsername: {message.from_user.username}\nsizning IDingzi: {message.from_user.id}")

# foydalanuvchi ma'lumoti rus tilida

@dp.message(F.text == "ваша информация")
async def your_info_ru(message: Message):
    await message.answer(f"полное имя: {message.from_user.full_name}\nимя пользователя: {message.from_user.username}\nВаш ID: {message.from_user.id}")
 
# user info tugadi

# support qismi uzbek tilida

@dp.message(F.text == "Qo'llab-quvvatlash")
async def support_uz(message: Message):
    await message.answer(f"Sizda qandaydir savollar bo'lsa biz bilan bog'laning ❓\nTel 📱: +998885996556\nemail 📧: alimovjavohir677@gmail.com")

# support rus tilida

@dp.message(F.text == "поддержка")
async def support_ru(message: Message):
    await message.answer(f"Свяжитесь с нами если у вас есть какие-либо вопросы ❓\nТел 📱: +998885996556\nэлектронная почта 📧: alimovjavohir677@gmail.com")

# support tugadi

# tilni o'zgaritish uzbek tilida

@dp.message(F.text == "Tilni o'zgartirish")
async def change_lang(message: Message, state: FSMContext):
    await message.answer("Tilni tanlang 👇", reply_markup=language)

# tilni o'zgartirish rus tilida

@dp.message(F.text == "Поменять язык")
async def change_lang_ru(message: Message, state: FSMContext):
    await message.answer("выберите язык 👇", reply_markup=language)

@dp.message(F.text == "uz")
async def lang_uz(message: Message, state: FSMContext):
    data = await state.get_data()
    data["lang"] = "uz"
    await message.answer("Til o'zgartirildi ☺️", reply_markup=main_button_uz)
    await state.clear()

@dp.message(F.text == "ru")
async def lang_ru(message: Message, state: FSMContext):
    data = await state.get_data()
    data["lang"] = "ru"
    await message.answer("язык изменен ☺️", reply_markup=main_button_ru)
    await state.clear()


# tilni o'zgartirish tugadi
# https://t.me/Fastfuirousfood_bot - botning linki

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
