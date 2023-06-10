1.Выбрать всех студентов, обучающихся на курсе "Математика":
SELECT
	s.first_name as first_name,
	s.last_name as last_name,
	s.address as address,
	c.course as course
	FROM student s
	LEFT JOIN course c ON s.course_id = c.id WHERE c.course = 'Математика'

2.Обновить оценку студента по курсу:
Обновить оценку у конкретного студента по курсу
UPDATE
	grades g
	SET score = 3 WHERE g.id = (
	SELECT g.id
	FROM grades g LEFT JOIN student s ON g.student_id = s.id
	LEFT JOIN exam e ON g.exam_id = e.id
	LEFT JOIN academic_plan ap ON e.id = ap.exam_id
	LEFT JOIN course c ON ap.course_id = c.id
	WHERE s.id = 1 AND c.course = 'Программирование'
	)

Получить оценки всех студентов по курсу
SELECT
	s.id as id,
	s.first_name as firs_name,
	e.title as title,
	c.course as course,
	grd.score as grades
	FROM grades grd
	LEFT JOIN student s	ON grd.student_id = s.id
	LEFT JOIN exam e ON grd.exam_id = e.id
	LEFT JOIN academic_plan ap ON e.id = ap.exam_id
	LEFT JOIN course c ON ap.course_id = c.id

3.Выбрать всех преподавателей, которые преподают в здании №1.
SELECT
    p.id as id,
    p.first_name as first_name,
    p.last_name as last_name,
    b.number as build_number
FROM schedule sch
LEFT JOIN build b ON b.id = sch.build_id
LEFT JOIN professor p ON p.id = sch.professor_id
WHERE b.number = 1

4.Удалить задание для самостоятельной работы, которое было создано более года назад.
DELETE FROM self_work WHERE created < NOW() - INTERVAL '1 year';

5.Добавить новый семестр в учебный год.
INSERT INTO semester (title) VALUES ('Третий семестр')