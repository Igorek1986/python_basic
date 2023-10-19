# Python Basic (Skillbox)

<details>
<summary>Модуль 14</summary>
<h2>Задача 1. Информация о системе</h2>
<p>
Чтобы преподавателям было проще помогать вам при возникновении различных ошибок, нужно собрать информацию об операционной системе и версии Python. Для этого используйте код ниже.
</p>
<pre>
  <code>
    import platform
    import sys
    info = 'OS info is \n{}\n\nPython version is {} {}'.format(
        platform.uname(),
        sys.version,
        platform.architecture(),
    )
    print(info)  
    with open('os_info.txt', 'w', encoding='utf8') as file:
        file.write(info)
  </code>
</pre>
<h2>Задача 2. Сессия</h2>
<p>
Решите задачу из четвёртого урока данного модуля. Вот текст самой задачи:
Для сдачи зачёта студент Пётр написал программу, которая по координатам двух точек определяет уравнение прямой, проходящей через эти две точки, в виде y = k * x + b, где k и b — числа, означающие угловой коэффициент и вертикальное смещение прямой. Вот текст этой программы:
</p>
<p>
<pre>
Пример работы программы (содержимое консоли):
Введите первую точку
X: 10
Y: 20
Введите вторую точку
X: 15
Y: 25
Уравнение прямой, проходящей через эти точки:
y =  1.0  * x +  10.0
Однако вечером накануне сдачи Пётр обнаружил, что программа не всегда работает правильно. 
Например, она не выдаёт корректное уравнение, если координаты первой точки равны (10, 20), а координаты второй точки равны (10, 45).
Отчаявшись и предвидя бессонную ночь, Пётр обратился к вам за помощью. 
Помогите ему найти и исправить ошибку в коде с помощью брейк-поинтов, чтобы уравнение прямой составлялось правильно во всех случаях.
</pre>
</p>
<h2>Задача 3. Сумма и разность</h2>
<p>
Напишите две функции: первая принимает одно целое положительное число N и находит сумму всех цифр числа N; вторая принимает число N и считает количество цифр в числе. В ответе выводится разность суммы чисел и количества.
</p>
<p>
<pre>
Пример работы программы:
Введите число: 500

Сумма цифр: 5
Кол-во цифр в числе: 3
Разность суммы и кол-ва цифр: 2
</pre>
</p>
<h2>Задача 4. Число наоборот 3</h2>
<p>
Пользователь вводит два вещественных числа — N и K. Напишите программу, которая отдельно заменяет сначала целую часть на число, которое получается из исходного записью его цифр в обратном порядке, затем то же самое делает с дробной частью. После этого числа складываются и сумма выводится на экран.
</p>
<p>
<pre>
Пример: 
Введите первое число: 102.12
Введите второе число: 123.34

Первое число наоборот: 201.21
Второе число наоборот: 321.43
Сумма: 522.64
</pre>
</p>

<h2>Задача 5. Наименьший делитель</h2>
<p>
Дано натуральное число n>1. Напишите функцию, которая находит его наименьший делитель, отличный от 1.
</p>
<p>
<pre>
Пример 1: 
Введите число: 6
Наименьший делитель, отличный от единицы: 2

Пример 2:
Введите число: 17
Наименьший делитель, отличный от единицы: 17
</pre>
</p>

<h2>Задача 6. Монетка 2</h2>
<p>
Практиканту снова дали задание найти старую металлическую монетку по заданным координатам. Но теперь металлоискатель сканирует местность вокруг пользователя в виде круга и при обнаружении/отсутствии металла прибор отображает на экране соответствующее сообщение.

Даны два действительных числа x и y и радиус r. Напишите функцию, которая проверяет, лежит ли точка с координатами (x, y) внутри круга с радиусом r (включая его границу). Координаты центра круга — (0, 0). Если точка принадлежит кругу, выведите сообщение «Монетка где-то рядом», иначе выведите сообщение «Монетки в области нет». 
</p>
<p>
<pre>
Пример 1:
Введите координаты монетки:
X: 0.5
Y: 0.5
Введите радиус: 1
Монетка где-то рядом

Пример 2:
Введите координаты монетки:
X: 2
Y: 2
Введите радиус: 1
Монетки в области нет
</pre>
</p>


<h2>Задача 7. Годы</h2>
<p>
Недавно Костя прочитал какую-то научно-фантастическую книжку, где самые страшные события случались только в определённые годы, а именно когда в году были ровно три одинаковые цифры. Косте стало интересно, какие годы были или будут «особенными» в определённом промежутке.
Напишите программу, в которой у пользователя запрашивается два четырёхзначных числа A и B. Затем выведите в порядке возрастания все четырёхзначные числа в интервале от A до B, запись которых содержит ровно три одинаковые цифры.
</p>
<p>
<pre>
Пример:
Введите первый год: 1900
Введите второй год: 2100
Годы от 1900 до 2100 с тремя одинаковыми цифрами:
1911
1999
2000
2022
</pre>
</p>
</details>


<details>
<summary>Модуль 15</summary>
<h2>Задача 1. Генерация списка</h2>
<p>
Дано целое число N. Напишите программу, которая формирует список из нечётных чисел от 1 до N.
</p>

<h2>Задача 2. Турнир</h2>
<p>
Для турнира по волейболу необходимо сформировать турнирную сетку из восьми человек на два дня. На первый день из списка участников решили выбрать каждого второго.
Дан список из восьми имён: Артемий, Борис, Влад, Гоша, Дима, Евгений, Женя, Захар. Напишите программу, которая выводит элементы списка только с чётными индексами.
</p>

<h2>Задача 3. Клетки</h2>
<p>
В научной лаборатории выводят и тестируют новые виды клеток. Есть список из N этих клеток, где элемент списка — это показатель эффективности, а индекс списка — это ранг клетки. Учёные отбирают клетки по следующему принципу: если эффективность клетки меньше её ранга, то эта клетка не подходит.
Напишите программу, которая выводит на экран те элементы списка, значения которых меньше их индекса.
</p>
<p>
<pre>
Пример:
Кол-во клеток: 5
Эффективность 1 клетки: 3
Эффективность 2 клетки: 0
Эффективность 3 клетки: 6
Эффективность 4 клетки: 2
Эффективность 5 клетки: 10
Неподходящие значения: 0 2
</pre>
</p>

<h2>Задача 4. Видеокарты</h2>
<p>
В базе одного магазина электроники есть список видеокарт компании NVIDIA разных поколений. Для удобства в списке вместо полных названий хранятся только числа, они обозначают модель и поколение видеокарты. Недавно компания выпустила новую линейку видеокарт, и в итоге самые старшие поколения разобрали за пару дней.
Напишите программу, которая удаляет из этого списка видеокарт наибольшие элементы.
</p>
<p>
<pre>
Пример:
Кол-во видеокарт: 5
1 Видеокарта: 3070
2 Видеокарта: 2060
3 Видеокарта: 3090
4 Видеокарта: 3070
5 Видеокарта: 3090
Старый список видеокарт: [ 3070 2060 3090 3070 3090 ]
Новый список видеокарт: [ 3070 2060 3070 ]
</pre>
</p>

<h2>Задача 5. Кино</h2>
<p>
Илья зашёл на один любительский киносайт, где пользователи пишут рецензии на фильмы. Вот, кстати, список этих фильмов: 
<pre>
films = [‘Крепкий орешек’, ‘Назад в будущее’, ‘Таксист’, ‘Леон’, ‘Богемская рапсодия’, ‘Город грехов’, ‘Мементо’, ‘Отступники’, ‘Деревня’]
</pre>

Илья на сайте в первый раз, он хочет зарегистрироваться и сразу добавить некоторые фильмы в список своих любимых, чтобы потом почитать рецензии на них. Напишите программу, в которой пользователь вводит фильм, и если он есть в списке, то он добавляется в список любимых. Если его нет, то выводится ошибка. В конце выведите весь список любимых фильмов.
</p>

<h2>Задача 6. Анализ слова</h2>
<p>
Мы пишем программу — анализатор слов, чтобы потом, возможно, использовать её для тренировки нейросети, которая будет генерировать нужный нам текст.
Пользователь вводит слово. Напишите программу, которая считает количество уникальных букв в слове. Уникальные буквы — это те, которые встречаются всего один раз.
</p>
<p>
<pre>
Пример 1:
Введите слово: привет
Кол-во уникальных букв: 6

Пример 2:
Введите слово: лава
Кол-во уникальных букв: 2
</pre>
</p>

<h2>Задача 7. Контейнеры</h2>
<p>
Контейнеры на складе лежат в ряд в порядке невозрастания своей массы (в килограммах). На склад привезли ещё один контейнер, который также нужно положить на определённое место.
Напишите программу, которая получает на вход невозрастающую последовательность натуральных чисел, означающих массу каждого контейнера в ряду. После этого вводится число X — масса нового контейнера. Программа выводит номер, под которым будет лежать новый контейнер. Если в ряде есть контейнеры с одинаковой массой, такой же, как у нового, то его нужно положить после них.
Обеспечьте контроль ввода: все числа не превышают 200.
</p>
<p>
<pre>
Пример:
Кол-во контейнеров: 8
Введите вес контейнера: 165 
Введите вес контейнера: 163 
Введите вес контейнера: 160 
Введите вес контейнера: 160 
Введите вес контейнера: 157 
Введите вес контейнера: 157 
Введите вес контейнера: 155 
Введите вес контейнера: 154 
Введите вес нового контейнера: 162
Номер, куда встанет новый контейнер: 3
</pre>
</p>

<h2>Задача 8. Бегущие цифры</h2>
<p>
Вы пишете программу для маленького табло, в котором циклически повторяется один и тот же текст или числа — прямо как в каком-нибудь метро, автобусах или трамваях.

Дан список из N элементов и целое число K. Напишите программу, которая циклически сдвигает элементы списка вправо на K позиций. Используйте минимально возможное количество операций присваивания.
</p>
<p>
<pre>
Пример 1:
Сдвиг: 1
Изначальный список: [1, 2, 3, 4, 5]
Сдвинутый список: [5, 1, 2, 3, 4]

Пример 2:
Сдвиг: 3
Изначальный список: [1, 4, -3, 0, 10]
Сдвинутый список: [-3, 0, 10, 1, 4]
</pre>
</p>

<h2>Задача 9. Анализ слова 2</h2>
<p>
Мы продолжаем писать программы — анализаторы для текста, и теперь от нас требуется реализовать код, с помощью которого можно будет определять, является ли слово палиндромом — словом, которое одинаково читается слева направо и справа налево. 
Напишите такую программу.
</p>
<p>
<pre>
Пример 1:
Введите слово: мадам
Слово является палиндромом

Пример 2:
Введите слово: abccba
Слово является палиндромом

Пример 3:
Введите слово: abbd
Слово не является палиндромом
</pre>
</p>

<h2>Задача 10. Сортировка (по желанию)</h2>
<p>
Дан список из N чисел. Напишите программу, которая сортирует элементы списка по возрастанию и выводит его на экран. Дополнительный список не использовать.
Постарайтесь придумать и написать как можно более эффективный алгоритм сортировки.
</p>
<p>
<pre>
Пример:
Изначальный список: [1, 4, -3, 0, 10]
Отсортированный список: [-3, 0, 1, 4, 10]
</pre>
</p>
</details>
<details>
<summary>Модуль 16</summary>
<h2>Задача 1. Страшный код</h2>
<p>
Вашему другу, который тоже начал изучать Python, преподаватель дал такую задачу: есть три списка — основной и два побочных. В основном лежат элементы [1, 5, 3], а в побочных [1, 5, 1, 5] и [1, 3, 1, 5, 3, 3] соответственно. 
Первый побочный закидывается в основной, там считается количество цифр 5, количество выводится на экран, и затем они удаляются из основного списка. После этого в основной закидывается второй побочный список, там считается количество цифр 3 и выводится на экран. В конце также выводится и сам список.
Из интереса вы попросили вашего друга показать код его программы и поняли, что сделали это не зря — то, что вы увидели, повергло вас в шок и ужас. Вот сам код:
<pre>
<code>
a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
for i in b:
    a.append(i)
t = 0
for i in a:
    if i == 5:
        t += 1
print(t)
d = []
for i in a:
    if i != 5:
        d.append(i)
for i in c:
    d.append(i)
t = 0
for i in d:
    if i == 3:
        t += 1
print(t)
print(d)
</code>
</pre>
</p>
<p>
Используя знания о методах списков, а также о стиле программирования, помогите другу переписать программу. Не используйте дополнительные списки.
</p>
<p>
<pre>
Результат работы программы:
Кол-во цифр 5 при первом объединении: 3
Кол-во цифр 3 при втором объединении: 4
Итоговый список: [1, 3, 1, 1, 1, 3, 1, 5, 3, 3]
</pre>
</p>

<h2>Задача 2. Шеренга</h2>
<p>
Два класса стоят в две отдельные шеренги. В каждом классе ученики выстроены по росту (по возрастанию): в одном классе от 160 см до 176 см с шагом 2, во втором классе — от 162 см до 180 см с шагом 3. Спустя какое-то время два класса объединяют в одну шеренгу и тоже выстраивают их по возрастанию.
Напишите программу, которая генерирует списки роста для каждого в классе, затем объединяет их в один список и сортирует его в порядке возрастания. Выведите отсортированный список на экран.
</p>

<h2>Задача 3. Детали</h2>
<p>
В базе данных магазина всякой всячины хранится список названий деталей и их стоимостей:
</pre>
shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
</pre>
Продавец решил, что считать количество и стоимость деталей вручную не очень удобно, поэтому решил попросить помощи у программиста, чтобы оптимизировать этот процесс.
Напишите программу, которая запрашивает у пользователя деталь, считает их количество, а также общую стоимость.
</p>
<p>
</pre>
Пример:
Название детали: седло

Кол-во деталей - 3  
Общая стоимость - 4500
</pre>
</p>

<h2>Задача 4. Вечеринка</h2>
<p>
В честь своего дня рождения Артём решил закатить вечеринку у себя на даче. Он не стал рассылать приглашения, а просто сообщил всем: «Если хотите — приходите и своих друзей тоже зовите». В ходе вечеринки люди приходили и уходили, ночевать остались не все. К тому же и сама дача не резиновая — на ней помещается всего шесть человек.
Дан изначальный список гостей — имена тех, кто пришёл к началу:
<pre>
guests = [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’]
</pre>
Напишите программу, которая спрашивает у пользователя, ушёл человек или пришёл новый гость, и исходя из ответа добавляет в список или удаляет из него нужное имя. При этом гостей может быть не больше шести. Имена запрашиваются до тех пор, пока пользователь не введёт сообщение «Пора спать».
</p>
<p>
<pre>
Пример:
Сейчас на вечеринке 5 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’]
Гость пришёл или ушёл? пришёл
Имя гостя: Алекс
Привет, Алекс!

Сейчас на вечеринке 6 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’, ‘Алекс’]
Гость пришёл или ушёл? пришёл
Имя гостя: Гоша
Прости, Гоша, но мест нет.

Сейчас на вечеринке 6 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’, ‘Алекс’]
Гость пришёл или ушёл? ушёл
Имя гостя: Ваня
Пока, Ваня!

Сейчас на вечеринке 5 человек: [‘Петя’, ‘Саша’, ‘Лиза’, ‘Катя’,  ‘Алекс’]
Гость пришёл или ушёл? Пора спать

Вечеринка закончилась, все легли спать.
</pre>
</p>

<h2>Задача 5. Песни</h2>
<p>
Мы пишем приложение для удобного прослушивания музыки. У Вани есть список из девяти песен группы Depeche Mode. Каждая песня состоит из названия и продолжительности с точностью до долей минут:
</p>
<pre>
violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
</pre>
Из этого списка Ваня хочет выбрать N песен и закинуть их в особый плейлист с другими треками. И при этом ему важно, сколько времени в сумме эти N песен будут звучать.
Напишите программу, которая запрашивает у пользователя количество песен из списка и затем названия этих песен, а на экран выводит общее время их звучания.
<p>
<pre>
Пример:
Сколько песен выбрать? 3
Название 1 песни: Halo
Название 2 песни: Enjoy the Silence
Название 3 песни: Clean

Общее время звучания песен: 14.93 минут
</pre>
</p>

<h2>Задача 6. Уникальные элементы</h2>
<p>
Даны два списка целых чисел, оба списка заполняются с клавиатуры. В первый список вводится три числа, во второй — семь чисел. Напишите программу, которая запрашивает у пользователя эти числа, затем расширяет первый список элементами второго и после этого оставляет в первом списке только уникальные элементы, то есть удаляет лишние повторы чисел. Условный оператор использовать нельзя.
<pre>
first_list = [1, 2, 3]
second_list = [2, 4, 6, 3, 3, 2, 1]
</pre>
</p>
<p>
<pre>
Пример:
# ввод чисел опустим
Первый список: [1, 2, 3]
Второй список: [2, 4, 6, 3, 3, 2, 1]

Новый первый список с уникальными элементами: [4, 6, 3, 2, 1]
</pre>
</p>

<h2>Задача 7. Ролики</h2>
<p>
Частная контора даёт в прокат ролики самых разных размеров. Человек может надеть ролики любого размера, которые не меньше размера его ноги. 
Пользователь вводит два списка размеров: N размеров коньков и K размеров ног людей. Реализуйте код, который определяет, какое наибольшее число человек сможет одновременно взять ролики и пойти покататься.
</p>
<p>
<pre>
Пример:
Кол-во коньков: 4
Размер 1 пары: 41
Размер 2 пары: 40
Размер 3 пары: 39
Размер 4 пары: 42
Кол-во людей: 3
Размер ноги 1 человека: 42
Размер ноги 2 человека: 41
Размер ноги 3 человека: 42

Наибольшее кол-во людей, которые могут взять ролики: 2
</pre>
</p>

<h2>Задача 8. Считалка</h2>
<p>
N человек, пронумерованных числами от 1 до N, стоят в кругу. Они начинают играть в считалку на выбывание, где каждый K-й по счёту человек выбывает из круга, после чего счёт продолжается со следующего за ним человека.

На вход подаётся количество человек N и номер K. Напишите программу, которая выводит число от 1 до N — это номер человека, который останется в кругу последним.
</p>
<p>
<pre>
Пример:
Кол-во человек: 5
Какое число в считалке? 7
Значит, выбывает каждый 7 человек

Текущий круг людей: [1, 2, 3, 4, 5]
Начало счёта с номера 1
Выбывает человек под номером 2

Текущий круг людей: [1, 3, 4, 5]
Начало счёта с номера 3
Выбывает человек под номером 5

Текущий круг людей: [1, 3, 4]
Начало счёта с номера 1
Выбывает человек под номером 1

Текущий круг людей: [3, 4]
Начало счёта с номера 3
Выбывает человек под номером 3

Остался человек под номером 4
</pre>
</p>

<h2>Задача 9. Друзья</h2>
<p>
N друзей постоянно берут в долг друг у друга деньги. В какой-то момент им надоело забывать, кто кому и сколько должен, и они придумали систему долговых расписок. И чтобы начать новый год «с чистого листа», друзья решили оплатить все долговые расписки, которые накопились у них друг к другу. Однако выяснилось, что иногда один и тот же человек в разные дни выступал как в роли должника, так и в роли кредитора.
Напишите программу, которая по заданным распискам вычислит, сколько всего должен каждый друг выплатить другим (или получить с других).
Сначала вводится число N — количество друзей, затем вводится число K — количество долговых расписок, после этого следует K троек чисел: номер друга, взявшего в долг, номер друга, давшего деньги, и сумма. Гарантируется, что ни один друг не брал в долг сам у себя.
Программа должна вывести «баланс друзей», то есть суммы, которые должны получить или отдать друзья. Положительное число означает, что друг должен получить деньги от других, отрицательное — должен отдать деньги.
</p>
<p>
<pre>
Пример 1:
Кол-во друзей: 2
Долговых расписок: 3
1 расписка
Кому: 1
От кого: 2
Сколько: 10

2 расписка
Кому: 1
От кого: 2
Сколько: 20

3 расписка
Кому: 1
От кого: 2
Сколько: 20

Баланс друзей:
1 : -50
2 : 50

Пример 2:
Кол-во друзей: 3
Долговых расписок: 1
1 расписка
Кому: 3
От кого: 1
Сколько: 100
Баланс друзей:
1 : 100
2 : 0
3 : -100
</pre>
</p>

<h2>Задача 10. Симметричная последовательность</h2>
<p>
Последовательность чисел называется симметричной, если она одинаково читается как слева направо, так и справа налево. Например, следующие последовательности являются симметричными:
<pre>
1 2 3 4 5 4 3 2 1
1 2 1 2 2 1 2 1
</pre>
</p>
<p>
<pre>
Пример 1:
Кол-во чисел: 5
Число: 1
Число: 2
Число: 1
Число: 2
Число: 2

Последовательность: 1 2 1 2 2
Нужно приписать чисел: 3
Сами числа: 1 2 1

Пример 2:
Кол-во чисел: 5
Число: 1
Число: 2
Число: 3
Число: 4
Число: 5

Последовательность: 1 2 3 4 5
Нужно приписать чисел: 4
Сами числа: 4 3 2 1
</pre>
</p>
</details>
<details>
<summary>Модуль 17</summary>
<h2>Задача 1. Гласные буквы</h2>
<p>
Команде лингвистов понравилось качество ваших программ, и они решили заказать у вас функцию для анализатора текста, которая создавала бы список гласных букв текста, а заодно считала бы их количество.
Напишите программу, которая запрашивает у пользователя текст и генерирует список из гласных букв этого текста (сама строка вводится на русском языке). Выведите в консоль сам список и его длину.
</p>
<p>
<pre>
Пример:
Введите текст: Нужно отнести кольцо в Мордор!

Список гласных букв: ['у', 'о', 'о', 'е', 'и', 'о', 'о', 'о', 'о']
Длина списка: 9
</pre>
</p>

<h2>Задача 2. Генерация</h2>
<p>
Пользователь вводит целое число N. Напишите программу, которая генерирует список из N чисел, на чётных местах в нём стоят единицы, а на нечётных — числа, равные остатку от деления своего номера на 5.
</p>
<p>
<pre>
Пример:
Введите длину списка: 10
Результат: [1, 1, 1, 3, 1, 0, 1, 2, 1, 4]
</pre>
</p>

<h2>Задача 3. Случайные соревнования</h2>
<p>
Мы хотим протестировать работу электронной таблицы для участников некоторых соревнований. Есть два списка (то есть две команды), по 20 участников в каждом. В этих списках хранятся очки каждого участника (это вещественные числа с двумя знаками после точки, например 4.03). Участник одной команды соревнуется с участником другой команды под таким же номером. То есть первый соревнуется с первым, второй — со вторым и так далее.
Напишите программу, которая генерирует два списка участников (по 20 элементов) из случайных вещественных чисел (от 5 до 10). Для этого найдите подходящую функцию из модуля random. Затем сгенерируйте третий список, в котором окажутся только победители из каждой пары.
</p>
<p>
<pre>
Пример:
Первая команда: [7.86, 6.76, 9.97, 9.08, 5.45, 6.9, 8.65, 5.17, 8.17, 5.06, 7.56, 7.1, 7.18, 8.25, 5.53, 7.95, 8.91, 7.11, 8.29, 9.52]
Вторая команда: [7.13, 5.7, 8.89, 5.36, 5.62, 9.46, 5.82, 8.67, 8.41, 7.0, 5.31, 7.8, 9.93, 7.76, 7.4, 8.26, 7.94, 5.71, 7.89, 7.77]
Победители тура: [7.86, 6.76, 9.97, 9.08, 5.62, 9.46, 8.65, 8.67, 8.41, 7.0, 7.56, 7.8, 9.93, 8.25, 7.4, 8.26, 8.91, 7.11, 8.29, 9.52]
</pre>
</p>

<h2>Задача 4. Тренируемся со срезами</h2>
<p>
Дана строка, в которой хранятся первые семь букв английского алфавита. 
<pre>
alphabet = 'abcdefg'
</pre>
Напишите программу, которая выводит на экран 10 вот таких результатов:
<pre>
1.	Копия строки.
2.	Элементы строки в обратном порядке.
3.	Каждый второй элемент строки (включая самый первый).
4.	Каждый второй элемент строки после первого.
5.	Все элементы до второго.
6.	Все элементы, начиная с конца до предпоследнего.
7.	Все элементы в диапазоне индексов от 3 до 4 (не включая 4).
8.	Последние три элемента строки.
9.	Все элементы в диапазоне индексов от 3 до 4 (не включая 5).
10.	То же, что и в предыдущем пункте, но в обратном порядке.
</pre>
Для получения и вывода результатов используйте только команду print и срезы.
</p>
<p>
<pre>
Результаты работы программы:

1: abcdefg
2: gfedcba
3: aceg
4: bdf
5: a
6: g
7: d
8: efg
9: de
10: ed
</pre>
</p>

<h2>Задача 5. Разворот</h2>
<p>
На вход в программу подаётся строка, в которой буква h встречается как минимум два раза. Реализуйте код, который разворачивает последовательность символов, заключённую между первым и последним появлением буквы h, в противоположном порядке.
</p>

<h2>Задача 6. Сжатие списка</h2>
<p>
Дан список из N целых чисел. Напишите программу, которая выполняет «сжатие списка» — переставляет все нулевые элементы в конец массива. При этом все ненулевые элементы располагаются в начале массива в том же порядке. Затем все нули из списка удаляются.
</p>

<h2>Задача 7. Двумерный список</h2>
<p>
Как мы говорили ранее, в программировании часто приходится писать код исходя из результата, который требует заказчик. В этот раз заказчику нужно получить вот такой двумерный список
<pre>
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
</pre>
Напишите программу, которая генерирует такой список и выводит его на экран. Используйте только list comprehensions.
</p>

<h2>Задача 8. Развлечение</h2>
<p>
N палочек выставили в один ряд, пронумеровав их слева направо числами от 1 до N. Затем по этому ряду бросили K камней, при этом i-й камень сбил все палки с номерами от L_i до R_i включительно. Определите, какие палки остались стоять на месте.
Напишите программу, которая получает на вход количество палок N и количество бросков K. Далее идёт K пар чисел L_i, R_i, при этом 1≤ L_i≤ R_i≤ N.
Программа должна вывести последовательность из N символов, где j-й символ есть “I”, если j-я палка осталась стоять, или “.”, если j-я палка была сбита.
</p>
<p>
<pre>
Пример:
Кол-во палок: 10 
Кол-во бросков: 3
Бросок 1. Сбиты палки с номера 8 
по номер 10
Бросок 2. Сбиты палки с номера 2 
по номер 5
Бросок 3. Сбиты палки с номера 3 
по номер 6

Результат: I.....I...
</pre>
</p>

<h2>Задача 9. Список списков</h2>
<p>
Дан вот такой (уже многомерный!) список:
<pre>
nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
</pre>
Напишите код, который «раскрывает» все вложенные списки, то есть оставляет только внешний список. Для решения используйте только list comprehensions.
</p>
<p>
<pre>
Ответ: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
</pre>
</p>

<h2>Задача 10. Шифр Цезаря (сделайте по желанию)</h2>
<p>
Юлий Цезарь использовал свой способ шифрования текста. Каждая буква заменялась на следующую по алфавиту через K позиций по кругу. Если взять русский алфавит и k = 3, то в слове, которое мы хотим зашифровать, буква А станет буквой Г, Б станет Д и так далее.

Пользователь вводит сообщение, а также значение сдвига. Напишите программу, которая зашифрует это сообщение при помощи шифра Цезаря.
</p>
<p>
<pre>
Пример:
Введите сообщение: это питон
Введите сдвиг: 3
Зашифрованное сообщение: ахс тлхср
</pre>
</p>
</details>
