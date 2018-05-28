# Перевірка фактів на достовірність

Для завдання про перевірку фактів я обрав задачу пошуку альбомів (з роками видання) для музичних виконавців. Існує кілька відкритих музичних баз для отримання "ground truth" - AllMusic, MusicBrainz, Discogs, усі зі своїми проблемами. Я витягнув альбоми для тренувального і тестового сетів через Discogs API. Як виявилось, Discogs не зовсім коректно позначає власне студійні альбоми (на відміну від синглів, компіляцій, живих записів), а мене цікавили саме студійні альбоми. Тому я зробив cross-check із даними з вікіпедії (таблиця "Дискографія" наприкінці сторінки групи - ця таблиця, як і всі інші, не бралась до уваги у моїй подальшій програмі).

Формування тестового набору даних відбувається окремим скриптом (construct_test_set.py), але оскільки це довга процедура (у Discogs API діє обмеження на кількість запитів у хвилину), готовий тестовий набір присутній як файл test_albums.csv. Файл retrieve_albums.py містить бейзлайнову та "повну" системи отримання назв альбомів за правилами, а evaluate.py оцінює отримані альбоми за метриками (див. далі) та друкує детально всю статистику - рекомендую запускати саме його. 

Проблеми, з якими я зіткнувся (або які для себе створив, щоб задача була складнішою):

- Я не зберігав html-розмітку, тому не міг вирізнити назви альбомів через курсив та наявність лінку на іншу вікі-сторінку. Англійською назви альбомів пишуться курсивом без лапок, але з капіталізацією, як у всіх інших заголовках - тому досвід капіталізації заголовків із домашнього завдання #2 мені пригодився.

- Якогось писаного чи неписаного шаблону, яким послуговуються автори вікі-сторінок про музикантів, не існує. Тому паттерни опису альбомів кардинально відрізняються: інколи всі альбоми з роками випуску впорядковано перераховані в одному з перших абзаців, інколи назви розкидані в тексті й не завжди поруч із роками випуску.

- Використання парсингу залежностей та частин мови не дуже допомагає в цій задачі, тому що назви альбомів часто є сформованими фразами (Strangeways, Here We Come), з якими парсер губиться. Я також пробував NER, але він часто бачить сутність лише в частині назви альбому. Я застосував POS-tagging, але в усьому іншому довелось обмежитись регулярними виразами.

- Додання нових правил часто помітно погіршує precision: на вікі-сторінці виконавця часто згадуються альбоми, які вплинули на виконавця / які випустили сольно учасники групи / у запису яких взяли участь учасники групи тощо. Тому правил не дуже багато: спроби додавати складніші правила призводили до погіршення більшості метрик, інколи навіть recall.

Для оцінювання програми використано precision, recall, F1 measure, а також F1.5 - F-метрика, яка надає більшу вагу покриттю (recall). Гіпотетичний користувач програми, швидше за все, не засмутиться через присутність "зайвих альбомів" у результатах пошуку (до того ж вони все одно дотичні до основного виконавця), і для нього/неї краще мати кілька зайвих результатів, ніж не мати кількох релевантних.

Крім оцінювання за назвою альбому і роком випуску, я оцінюю також частковий збіг - тільки за назвою альбому.

Повні результати оцінювання програми, усереднені дані для 10-12 виконавців у кожному з двох наборів даних:

|                                           | Precision | Recall | F1    | F1.5  |
|-------------------------------------------|-----------|--------|-------|-------|
| Baseline, train set, full evaluation      | 0.397     | 0.41   | 0.367 | 0.373 |
| Rule-based, train set, full evaluation    | 0.37      | 0.759  | 0.468 | 0.533 |
| Baseline, train set, partial evaluation   | 0.441     | 0.448  | 0.406 | 0.412 |
| Rule-based, train set, partial evaluation | 0.409     | 0.823  | 0.517 | 0.586 |
| Baseline, test set, full evaluation       | 0.522     | 0.281  | 0.344 | 0.315 |
| Rule-based, test set, full evaluation     | 0.258     | 0.547  | 0.339 | 0.392 |
| Baseline, test set, partial evaluation    | 0.641     | 0.34   | 0.423 | 0.384 |
| Rule-based, test set, partial evaluation  | 0.326     | 0.657  | 0.419 | 0.48  |

Як бачимо, на тестових даних результати, очікувано, суттєво гірші. Крім того, не завжди система з великою кількістю правил діє краще, ніж бейзлайн (одне просте правило) - особливо це стосується precision, тому що нові правила зазвичай додають нові false positives. Тим не менш, програма збільшила покриття для тестових даних з 0.281 до 0.547 - покращення майже вдвічі; F1.5 виросла з 0.315 до 0.392, покращення на 8 відсоткових пунктів. При частковому оцінюванні покращення ще більше - 10 відсоткових пунктів.

Результати дуже скромні, але, як на мене, крім браку часу на розробку правил, це свідчить про обмеженість систем, заснованих на правилах - особливо у випадках, коли вхідні дані неструктуровані та не відповідають шаблону (єдина формальна ознака альбомів у тексті - великі літери, і то цю саму ознаку має багато інших сутностей у тексті).

Загалом процес пошуку правил, які б додавали нові правильні результати і нічого не псували, нагадує [гіфку](https://media.giphy.com/media/FmNXeuoadNTpe/giphy-downsized-large.gif)