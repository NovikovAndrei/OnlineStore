Реализация pet-проекта на Django по созданию интернет-доставки из ресторана и рассмотрению возможностей фреймворка Django.

 - Корректное отображение всех страниц приложения
 - Функционал авторизации и создания пользователя
 - Авторизация пользователя через GitHub
 - Вся информация хранится в БД. Созданы модели (User, Article, Comment, Cart, Wishlist, Testimony, User_profile, Category, Discount, Product)
 - Реализован постраничный вывод продуктов
 - Реализована возможность добавления/удаления товаров в корзину со страницы menu и со страницы товара
 - Реализована возможность добавления/удаления товаров в "Избранное"
 - При добавлении товара в корзину без перехода в корзину (кнопкой '+') реализован возврат на ту же страницу, той же категории
 - Отзывы (Testimonys) добавлены в отдельную модель БД
 - Реализована возможность добавлять статьи для blog и автоматически отобаражать их на странице через панель администратора
 - Реализована возможность для зарегистрированных пользователей оставлять комментарии под статьями
 - Реализован функционал удаления комментариев (удалять можно только свои комментарии)
 - Реализоан API для "корзины товаров" и "избранного"
 - Написаны тесты для API "корзины товаров" и "избранного"

Планируется:
 - Добавление возможности установки количества товара при добавлении в корзину
 - Добавление функционала применения скидочных купонов
 - Добавление локализации eng/ru
 - Добавление сслыки на локацию (карту) в разделе "контакты"
