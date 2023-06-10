# Polymedica Task

#### Software development stack ####
Fastapi\
SQLAlchemy\
Alembic\
Pydantic



#### Build and run ####
1. Install **docker**: https://docs.docker.com/engine/install/ \
2. Install **docker-compose**: https://docs.docker.com/compose/install/

3. Run command in terminal:
> To execute the following commands you need to be in the root of the project
> 
>Для  выполнения указанных команд необходимо перейти в корневую директорию проекта cd path/to/project

3.1 Build containers:
```
docker-compose up --build
```
3.2 Fill DB test data:
```
psql -U polymedika -d polymedika -h localhost -f fill_test_data.sql
```
>Для выполнения команды **psql** необходимо ввести пароль как указано: password
#### URLs ###
FastApi Swagger: http://localhost:8080/docs
#### Task_answers ###
1. SQL код создания всех таблиц: *task_answers/CREATE_ALL_TABLE.sql*\
2. SQL код запросов из задания: *task_answers/SQL Queryes for task.sql*
3. ER диаграмма: *task_answers/ER.png*

#### ER Diagram Description ####
- **1.Student (студент):**\
**id** => integer pk increments\
**first_name** => Имя студента,\
**last_name** => Фамилия студента\
**address** => Адрес жительства студента\
**phone** => Телефон студента\
**course_id** => FK на курс студента, One To Many\
**group_id** => FK на группу студента, One To Many\
**faculty_id** => FK на факультет студента, One To Many


- **2.Professor (профессор):**\
**id** => integer pk increments\
**first_name** => Имя профессора\
**last_name** => Фамилия профессора\
**branch_id** => FK на отделение университета, на котором преподает 
профессор, One To Many


- **3. Course (курс):**\
**id** => integer pk increments\
**course** =>  Курс обучения


- **4.Group (группа):**\
**id** => integer pk increments\
**name** => Название группы, string unique 


- **5.Branch (Отделение университета)):**\
**id** => integer pk increments\
**name** => Название отделения, string

  
- **6.Grades (Оценки):**\
**id** => integer pk increments\
**student_id** => integer FK на таблицу Студенты\
**score** => Оценка студента, integer\
**exam_id** => FK на экзамен, за который поставлена оценка, integer


- **7.Schedule (Расписание)**\
**id** => id integer pk increments\
**date** => Дата проведения занятия, datetime\
**build_id** => FK на здание, integer\
**group_id** => FK на группу, integer\
**professor_id** => FK на преподавателя, integer\
**auditorium_id** => FK на аудиторию, integer\
**subject** => Предмет занятия


- **8.Build (Здание)**\
**id** => id integer pk increments\
**title** => Название здания (Библиотека, Корпус, и тд), null = true\
**address** => Адрес здания\
**number** => Номер здания, int


- **9.Course Program (Программа курса)**\
**id** => id integer pk increments\
**faculty_id** => FK на факультет\
**course_id** => FK на курс\
**description** => Описание программы


- **10. Auditorium (Аудитория)**\
**id** => id integer pk increments\
**number** => Номер аудитории\
**build_id** => FK на Здание\


- **11.Semester (Семестр)**\
**id** => id integer pk increments\
**title** => Название семестра, unique=True


- **12.Faculty (Факультет)**\
**id** => id integer pk increments\
**brand_id** => FK на отделение\
**title** => Заголовок, unique=True


- **13.Exam (Экзамен)\
**id** => id integer pk increments\
**title** => Заголовок


- *14.Self Work (Самостоятельная работа)\
**id** => id integer pk increments\
**date** => Дата выполнения\
**topic** => Тема\
**created** => Время создания, datetime


- **15.Academic Plan (Учебный план)**\
**id** => id integer pk increments\
**date** => Дата\
**exam_id** => FK на экзамен\
**self_work_id** => FK на самостоятельную работу\
**course_id** => FK на курс\
**semester_id** => FK на семестр\
**professor_id** => FK на преподавателя\
**subject** => Предмет