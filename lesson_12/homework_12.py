import requests
"""
Написати 50 XPath локаторів для обраного сайту 
"""

url = f"https://https://allo.ua/"

xpaths = [

# Header
"//div[contains(@class,'ct-button') and normalize-space(text())='Каталог']"
"//button[normalize-space(text())='Отримати 100 ₴']"
"//a[normalize-space(text())='Магазини']"
"//a[normalize-space(text())='Акції'][1]"
"(//a[normalize-space(text())='Алло Гроші'])[1]"
"//a[normalize-space(text())='Алло Обмін'][1]"
"//a[normalize-space(text())='Покупцям']"
"//img[contains(@class,'logo')]"
"//input[@id='search-form__input']"
"//form[contains(@class,'search-form__form')]//button[@type='submit']"


# Лідери продажу
"(//a[contains(@class,'product-categories__link') and normalize-space(text())='Смартфони'])[1]"
"//a[normalize-space(text())='Стайлери для волосся']"
"//a[normalize-space(text())='Мультипечі']"
"(//div[contains(@class,'h-products__categories') and contains(@class,'product-categories')]//a[contains(@class,'product-categories__link')])[5]"
"(//div[contains(@class,'h-products__categories') and contains(@class,'product-categories')]//a[contains(@class,'product-categories__link')])[6]"
"(//div[contains(@class,'h-products__categories') and contains(@class,'product-categories')]//a[contains(@class,'product-categories__link')])[7]"
"(//div[contains(@class,'h-products__categories') and contains(@class,'product-categories')]//a[contains(@class,'product-categories__link')])[8]"
"(//div[contains(@class,'h-products__categories') and contains(@class,'product-categories')]//a[contains(@class,'product-categories__link')])[9]"
"//a[normalize-space(text())='Набори посуду']"
"(//div[contains(@class,'h-products__categories') and contains(@class,'product-categories')]//a[contains(@class,'product-categories__link')])[11]"


#Банер
"//a[.//img[@alt='5% знижка при оплаті карткою онлайн']]"
"//a[contains(@class,'header-line-banner__item') and contains(@class,'is-active')]"
"//img[@alt='-12% на товари бренду Apple при оплаті карткою Sense Bank від Mastercard']"

#Каталог
"//img[@alt='Новинки Apple']"
"//p[normalize-space(text())='Новинки Apple']"
"//img[@alt='Xiaomi']"
"//p[normalize-space(text())='Xiaomi']"
"//p[normalize-space(text())='Транспорт та велотовари']"
"//img[@alt='Транспорт та велотовари']"
"//p[normalize-space(text())='Смартфони та телефони']"
"//img[@alt='Смартфони та телефони']"
"//p[normalize-space(text())='Телевізори та мультимедіа']"
"//img[@alt='Телевізори та мультимедіа']"
"//p[normalize-space(text())='Побутова техніка']"
"//img[@alt='Побутова техніка']"

#Footer
"//a[normalize-space(text())='Вакансії']"
"//a[normalize-space(text())='Новини']"
"//a[normalize-space(text())='Про нас']"
"//a[normalize-space(text())='Мережа магазинів']"
"//a[normalize-space(text())='Контакти']"
"//a[normalize-space(text())='Доставка та оплата']"
"//a[normalize-space(text())='Гарантія та сервіс']"
"//a[normalize-space(text())='Блог']"
"//a[normalize-space(text())='Питання та відповіді']"
"//a[normalize-space(text())='Умови сайту']"
"//h3[normalize-space(text())='Сертифікати безпеки']"
"//h3[normalize-space(text())='Офіційні представники']"
"//button[.//span[normalize-space(text())='Підписатися']]"
"//input[@name='email']"

#Товари
"//img[@alt='Придбати -  Робот-пилосос Dreame Vacuum L40 Ultra CE White EUA']"
"//a[normalize-space(text())='Робот-пилосос Dreame Vacuum L40 Ultra CE White EUA']"
"//img[@alt='Придбати -  Електрична бігова доріжка UREVO Strol U1 URTM013']"
"//a[normalize-space(text())='Електрична бігова доріжка UREVO Strol U1 URTM013']"
"//img[@alt='Придбати -  Телевізор Xiaomi TV S Mini LED 65 2025']"
"//a[normalize-space(text())='Телевізор Xiaomi TV S Mini LED 65 2025']"

]

