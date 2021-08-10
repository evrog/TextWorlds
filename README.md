# TextWorlds

AUTHORS: Elena Mikhalkova, Timofei Protasov, Polina Gavin, Anastasiya Bashmakova, Anastasiya Drozdova
Univesity of Tyumen, 2018-2021

This repository contains data and processing files of our project "Text Worlds".

## About the project

We design annotation schemes and create a corpus of annotated literary narratives based on the theory of text worlds. 
The Text World Theory is developed in cognitive linguistics. A text world is a stretch of text characterized by the 
union of characters, time and space. Whenever there is a significant change in time and space, a new text world opens 
to hold all of its participants.

The theory opens a perspective to computationally study and model narrative structures.

## Annotation schemes

This repository contains XML-files annotated with two annotation schemes. The first one was employed in annotation of "The 
Gift of the Magi" (see files starting with "Magi"). The guidelines for this scheme are in the text file in this repository.
The second scheme was used in the rest of the files (all in Russian). This scheme separates two levels of annotation:
that of the world text elements (characters, space and time) and shifts (switches between the text worlds). The Russian 
guidelines to this scheme are given here:

1. Annotation of elements: https://docs.google.com/document/d/e/2PACX-1vRUhO_ab4AFz1lSIuqf_ZifZWZQZyQJeNR2FHv720vUTgHkAhr1lmtrduMSK8KeJA/pub
2. Annotation of shifts: https://docs.google.com/document/d/e/2PACX-1vS2HPn-MjWZhMp-wF8sMH4uyq4Jjo0DQ0-eecR92XlRWd3Ph495KpYDyV9t66Dk3g/pub 

## Sources of texts in XML-files

- Magi: "The Gift of the Magi" by O. Henry. https://en.wikisource.org/wiki/The_Four_Million/The_Gift_of_the_Magi
- Визит: "Визит", автор Саша Чёрный (1880—1932). https://ru.wikisource.org/wiki/%D0%92%D0%B8%D0%B7%D0%B8%D1%82_(%D0%A1%D0%B0%D1%88%D0%B0_%D0%A7%D1%91%D1%80%D0%BD%D1%8B%D0%B9)
- Волк: "Сказка о сером волке", Старая погудка на новый лад: Русская сказка в изданиях конца XVIII века. — 
Полное собрание русских сказок; Т. 8. Ранние собрания. — СПб.: Тропа Троянова, 2003. — Т. 8. 
https://ru.wikisource.org/wiki/%D0%A1%D1%82%D0%B0%D1%80%D0%B0%D1%8F_%D0%BF%D0%BE%D0%B3%D1%83%D0%B4%D0%BA%D0%B0_%D0%BD%D0%B0_%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9_%D0%BB%D0%B0%D0%B4/%D0%A1%D0%BA%D0%B0%D0%B7%D0%BA%D0%B0_%D0%BE_%D1%81%D0%B5%D1%80%D0%BE%D0%BC_%D0%B2%D0%BE%D0%BB%D0%BA%D0%B5
- Дочь: "Дочь Севера", автор Дорошевич В. М. Собрание сочинений. Том III. Крымские рассказы. — М.: Товарищество И. Д. Сытина, 1906. — С. 69.
https://ru.wikisource.org/wiki/%D0%94%D0%BE%D1%87%D1%8C_%D1%81%D0%B5%D0%B2%D0%B5%D1%80%D0%B0_(%D0%94%D0%BE%D1%80%D0%BE%D1%88%D0%B5%D0%B2%D0%B8%D1%87)
- Иванушка: "Про Иванушку-дурачка", русская народная сказка в обработке М. Горького / Художник Н. Шеварев — М.: Малыш, 1990. — 15 с. — ISBN 5-213-00180-7.
https://ru.wikisource.org/wiki/%D0%9F%D1%80%D0%BE_%D0%98%D0%B2%D0%B0%D0%BD%D1%83%D1%88%D0%BA%D1%83-%D0%B4%D1%83%D1%80%D0%B0%D1%87%D0%BA%D0%B0_(%D0%93%D0%BE%D1%80%D1%8C%D0%BA%D0%B8%D0%B9)
- Лампа: "Зеленая лампа", автор Александр Грин. Собрание сочинений в шести томах. — М.: Правда, 1980. — Т. 6. — С. 459—464
https://ru.wikisource.org/wiki/%D0%97%D0%B5%D0%BB%D1%91%D0%BD%D0%B0%D1%8F_%D0%BB%D0%B0%D0%BC%D0%BF%D0%B0_(%D0%93%D1%80%D0%B8%D0%BD)
- Лисичка: "Лисичка-сестричка и волк". Народные русские сказки А. Н. Афанасьева: В 3 т. — Лит. памятники. — М.: Наука, 1984—1985.
https://ru.wikisource.org/wiki/%D0%9D%D0%B0%D1%80%D0%BE%D0%B4%D0%BD%D1%8B%D0%B5_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B5_%D1%81%D0%BA%D0%B0%D0%B7%D0%BA%D0%B8_(%D0%90%D1%84%D0%B0%D0%BD%D0%B0%D1%81%D1%8C%D0%B5%D0%B2)/%D0%9B%D0%B8%D1%81%D0%B8%D1%87%D0%BA%D0%B0-%D1%81%D0%B5%D1%81%D1%82%D1%80%D0%B8%D1%87%D0%BA%D0%B0_%D0%B8_%D0%B2%D0%BE%D0%BB%D0%BA
- Лягушка: "Лягушка-путешественница", автор Всеволод Михайлович Гаршин (1855—1888). Дата создания: 1887, опубл.: 1887. Источник: Библиотека Максима Мошкова.
https://ru.wikisource.org/wiki/%D0%9B%D1%8F%D0%B3%D1%83%D1%88%D0%BA%D0%B0-%D0%BF%D1%83%D1%82%D0%B5%D1%88%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%B8%D1%86%D0%B0_(%D0%93%D0%B0%D1%80%D1%88%D0%B8%D0%BD)
- Мирная: "Мирная вонйа", автор Саша Черный. Опубл.: Сегодня (Рига). 1930. 27 апреля. Источник: cherny-sasha.lit-info.ru.
https://ru.wikisource.org/wiki/%D0%9C%D0%B8%D1%80%D0%BD%D0%B0%D1%8F_%D0%B2%D0%BE%D0%B9%D0%BD%D0%B0_(%D0%A1%D0%B0%D1%88%D0%B0_%D0%A7%D1%91%D1%80%D0%BD%D1%8B%D0%B9)
- Они: "Они выросли рядом", автор Ксения Алексеевна Морозова. Из сборника «В царстве сказки». Опубл.: 1911. Источник: Commons-logo.svg К. А. Морозова. В царстве сказки. — М.: Издание Т-ва И. Д. Сытина, 1911.
https://ru.wikisource.org/wiki/%D0%9E%D0%BD%D0%B8_%D0%B2%D1%8B%D1%80%D0%BE%D1%81%D0%BB%D0%B8_%D1%80%D1%8F%D0%B4%D0%BE%D0%BC_(%D0%9C%D0%BE%D1%80%D0%BE%D0%B7%D0%BE%D0%B2%D0%B0)/1911_(%D0%92%D0%A2)
- Попугай: "Попугай : Майкина сказка", автор Николай Георгиевич Гарин-Михайловский. Сказки для детей. — СПб.: Товарищество «Общественная польза», 1909. — С. 53.
https://ru.wikisource.org/wiki/%D0%9F%D0%BE%D0%BF%D1%83%D0%B3%D0%B0%D0%B9_(%D0%93%D0%B0%D1%80%D0%B8%D0%BD-%D0%9C%D0%B8%D1%85%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9)
- Потец: "Потец", автор Введенский Александр Иванович. «Стихи и пьесы». http://mirpoezylit.ru/books/7371/1/
- Умный: "Умный работник : Русская народная сказка". Сказки народов мира. Том 1. Русские народные сказки - Москва: Детская литература, 1987 - с.719; http://skazka.mifolog.ru/books/item/f00/s00/z0000020/index.shtml
https://ru.wikisource.org/wiki/%D0%A3%D0%BC%D0%BD%D1%8B%D0%B9_%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BD%D0%B8%D0%BA

We also have a collection of "We Can Remember It for You Wholesale" by PK Dick annotated by 6 annotators in Russian and 2 in English, but due to copyright issues
we cannot share it publically.

## Annotators

Elena Mikhalkova, Timofei Protasov, Polina Gavin, Anastasiya Bashmakova, Anastasiya Drozdova, Daria Bormova, Alexander Dmitrienko, Oleg Evseyev,
Madina Alimtaeva, Anzhelika Gornnova, Anastasiya Kuzminykh

## Our publications

1. Mikhalkova, E., Protasov, T., Drozdova, A., Bashmakova, A., & Gavin, P. (2019). 
Towards Annotation of Text Worlds in a Literary Work. In Computational Linguistics and Intellectual Technologies. 
Papers from the Annual International Conference “Dialogue” (Компьютерная лингвистика и интеллектуальные технологии) (pp. 101-110).
2. Mikhalkova, E., Protasov, T., Sokolova, P., Bashmakova, A., & Drozdova, A. (2020, May). Modelling Narrative Elements in a Short Story:
A Study on Annotation Schemes and Guidelines. In Proceedings of the 12th Language Resources and Evaluation Conference (pp. 126-132).

## Contacts

e.v.mikhalkova@utmn.ru
