CREATE TABLE `student` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`first_name` VARCHAR(255) NOT NULL,
	`last_name` VARCHAR(255) NOT NULL,
	`address` VARCHAR(255) NOT NULL,
	`phone` VARCHAR(255),
	`course_id` INT NOT NULL,
	`group_id` INT NOT NULL,
	`faculty_id` INT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `professor` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`first_name` VARCHAR(255) NOT NULL,
	`last_name` VARCHAR(255) NOT NULL,
	`branch_id` INT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `course` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`course` VARCHAR(255) NOT NULL UNIQUE,
	PRIMARY KEY (`id`)
);

CREATE TABLE `group` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(255) NOT NULL UNIQUE,
	PRIMARY KEY (`id`)
);

CREATE TABLE `branch` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `grades` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`student_id` INT NOT NULL,
	`score` INT NOT NULL,
	`exam_id` INT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `schedule` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`date` DATETIME NOT NULL,
	`build_id` INT NOT NULL,
	`group_id` INT NOT NULL,
	`professor_id` INT NOT NULL,
	`auditorium_id` INT NOT NULL,
	`subject` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `build` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`title` VARCHAR(255),
	`address` TEXT NOT NULL UNIQUE,
	`number` INT NOT NULL UNIQUE,
	PRIMARY KEY (`id`)
);

CREATE TABLE `course_program` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`faculty_id` INT NOT NULL,
	`course_id` INT NOT NULL,
	`description` TEXT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `auditorium` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`number` INT NOT NULL UNIQUE,
	`build_id` INT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `semester` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`title` VARCHAR(255) NOT NULL UNIQUE,
	PRIMARY KEY (`id`)
);

CREATE TABLE `faculty` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`branch_id` INT NOT NULL,
	`title` VARCHAR(255) NOT NULL UNIQUE,
	PRIMARY KEY (`id`)
);

CREATE TABLE `exam` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`title` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `self_work` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`date` DATETIME NOT NULL,
	`topic` VARCHAR(255) NOT NULL,
	`created` DATETIME NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `academic_plan` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`date` DATETIME NOT NULL,
	`exam_id` INT,
	`self_work_id` INT,
	`course_id` INT NOT NULL,
	`semester_id` INT NOT NULL,
	`professor_id` INT NOT NULL,
	`subject` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`id`)
);

ALTER TABLE `student` ADD CONSTRAINT `student_fk0` FOREIGN KEY (`course_id`) REFERENCES `course`(`id`);

ALTER TABLE `student` ADD CONSTRAINT `student_fk1` FOREIGN KEY (`group_id`) REFERENCES `group`(`id`);

ALTER TABLE `student` ADD CONSTRAINT `student_fk2` FOREIGN KEY (`faculty_id`) REFERENCES `faculty`(`id`);

ALTER TABLE `professor` ADD CONSTRAINT `professor_fk0` FOREIGN KEY (`branch_id`) REFERENCES `branch`(`id`);

ALTER TABLE `grades` ADD CONSTRAINT `grades_fk0` FOREIGN KEY (`student_id`) REFERENCES `student`(`id`);

ALTER TABLE `grades` ADD CONSTRAINT `grades_fk1` FOREIGN KEY (`exam_id`) REFERENCES `exam`(`id`);

ALTER TABLE `schedule` ADD CONSTRAINT `schedule_fk0` FOREIGN KEY (`build_id`) REFERENCES `build`(`id`);

ALTER TABLE `schedule` ADD CONSTRAINT `schedule_fk1` FOREIGN KEY (`group_id`) REFERENCES `group`(`id`);

ALTER TABLE `schedule` ADD CONSTRAINT `schedule_fk2` FOREIGN KEY (`professor_id`) REFERENCES `professor`(`id`);

ALTER TABLE `schedule` ADD CONSTRAINT `schedule_fk3` FOREIGN KEY (`auditorium_id`) REFERENCES `auditorium`(`id`);

ALTER TABLE `course_program` ADD CONSTRAINT `course_program_fk0` FOREIGN KEY (`faculty_id`) REFERENCES `faculty`(`id`);

ALTER TABLE `course_program` ADD CONSTRAINT `course_program_fk1` FOREIGN KEY (`course_id`) REFERENCES `course`(`id`);

ALTER TABLE `auditorium` ADD CONSTRAINT `auditorium_fk0` FOREIGN KEY (`build_id`) REFERENCES `build`(`id`);

ALTER TABLE `faculty` ADD CONSTRAINT `faculty_fk0` FOREIGN KEY (`branch_id`) REFERENCES `branch`(`id`);

ALTER TABLE `academic_plan` ADD CONSTRAINT `academic_plan_fk0` FOREIGN KEY (`exam_id`) REFERENCES `exam`(`id`);

ALTER TABLE `academic_plan` ADD CONSTRAINT `academic_plan_fk1` FOREIGN KEY (`self_work_id`) REFERENCES `self_work`(`id`);

ALTER TABLE `academic_plan` ADD CONSTRAINT `academic_plan_fk2` FOREIGN KEY (`course_id`) REFERENCES `course`(`id`);

ALTER TABLE `academic_plan` ADD CONSTRAINT `academic_plan_fk3` FOREIGN KEY (`semester_id`) REFERENCES `semester`(`id`);

ALTER TABLE `academic_plan` ADD CONSTRAINT `academic_plan_fk4` FOREIGN KEY (`professor_id`) REFERENCES `professor`(`id`);
