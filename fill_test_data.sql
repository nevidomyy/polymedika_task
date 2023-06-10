INSERT INTO build (title, address, number) VALUES ('Библиотека', 'ул.Московская', 3);
INSERT INTO build (title, address, number) VALUES ('Здание факультета', 'ул.Пирогова', 1);
INSERT INTO auditorium (number, build_id) VALUES (404, 1);
INSERT INTO auditorium (number, build_id) VALUES (304, 2);
INSERT INTO semester (title) VALUES ('Первый семестр');
INSERT INTO semester (title) VALUES ('Второй семестр');
INSERT INTO course (course) VALUES ('Математика');
INSERT INTO course (course) VALUES ('Программирование');
INSERT INTO "group" (name) VALUES ('Первая группа');
INSERT INTO "group" (name) VALUES ('Вторая группа');
INSERT INTO branch (name) VALUES ('Отделение разработки');
INSERT INTO branch (name) VALUES ('Отделение дизайна');
INSERT INTO exam (title) VALUES ('Первый экзамен');
INSERT INTO exam (title) VALUES ('Второй экзамен');
INSERT INTO self_work (date, topic, created) VALUES ('2023-10-23 10:37:22', 'Первая домашняя работа', '2021-05-10
10:50:22');
INSERT INTO self_work (date, topic, created) VALUES ('2023-12-10 15:30:00', 'Вторая домашняя работа', '2023-05-10
10:50:22');
INSERT INTO faculty (title, branch_id) VALUES ('Основы Python', 1);
INSERT INTO faculty (title, branch_id) VALUES ('Asyncio и конкурентность', 2);
INSERT INTO student (first_name, last_name, address, phone, course_id, group_id, faculty_id) VALUES ('Иван', 'Петров',
'ул.Вяземская д.3', '+7 998 334 12 32', 1, 2, 1);
INSERT INTO student (first_name, last_name, address, phone, course_id, group_id, faculty_id) VALUES ('Саша', 'Иванов',
'ул.Пушкина д.27', '+7 333 999 22 11', 2, 1, 2);
INSERT INTO professor (first_name, last_name, branch_id) VALUES ('Сергей', 'Александров', 1);
INSERT INTO professor (first_name, last_name, branch_id) VALUES ('Алексей', 'Фонарев', 1);
INSERT INTO professor (first_name, last_name, branch_id) VALUES ('Петр', 'Комаров', 2);
INSERT INTO grades (student_id, exam_id, score) VALUES (1, 1, 5);
INSERT INTO grades (student_id, exam_id, score) VALUES (1, 2, 5);
INSERT INTO grades (student_id, exam_id, score) VALUES (2, 1, 3);
INSERT INTO course_program (faculty_id, course_id, description) VALUES (1, 1, 'Описание программы 1 курса');
INSERT INTO course_program (faculty_id, course_id, description) VALUES (1, 2, 'Описание программы 2 курса');
INSERT INTO course_program (faculty_id, course_id, description) VALUES (2, 1, 'Описание программы 1 курса 2');
INSERT INTO course_program (faculty_id, course_id, description) VALUES (2, 2, 'Описание программы 1 курса 2');
INSERT INTO schedule (datetime, build_id, group_id, professor_id, auditorium_id, subject) VALUES ('2023-09-10 12:30:00',
 1, 1, 1, 1, 'Математика');
INSERT INTO schedule (datetime, build_id, group_id, professor_id, auditorium_id, subject) VALUES ('2023-09-15 14:30:00',
 2, 2, 3, 2, 'Русский язык');
INSERT INTO academic_plan (date, exam_id, self_work_id, course_id, semester_id, professor_id, subject) VALUES
('2023-08-23 12:30:00', 1, 1, 1, 1, 2, 'Русский язык');
INSERT INTO academic_plan (date, exam_id, self_work_id, course_id, semester_id, professor_id, subject) VALUES
('2023-08-23 12:30:00', 2, 2, 2, 2, 1, 'Математика');

