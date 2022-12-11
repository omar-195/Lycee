CREATE DATABASE Exam_Bac_Sport;
/*--------------------------
Table Epreuve ::
---------------*/
CREATE TABLE Epreuve (
	code_ep VARCHAR(10) NOT NULL CHECK code_ep LIKE "EP%" PRIMARY KEY,
	lib_ep 	VARCHAR(20) NOT NULL UNIQUE
);
/*--------------------------
Table Examen ::
---------------*/
CREATE TABLE "Examen" (
	code_exam 	VARCHAR(10) CHECK "code_exam" LIKE "Exam%" NOT NULL;
	date_exam 	VARCHAR(20) NOT NULL UNIQUE;
	lycee		VARCHAR(20) NOT NULL;
	nbr_ep		INT(4) NOT NULL DEFAULT 4;
	nbr_prof	INT(4) NOT NULL DEFAULT 4;
	CONSTRAINT PRIMARY KEY (code_exam);
);
/*--------------------------
Table Eleve ::
---------------*/
CREATE TABLE "Examen" (
	nom	 	VARCHAR(20) NOT NULL;
	prenom	 	VARCHAR(20) NOT NULL;
	CIN		INT(10) NOT NULL;
	lycee		VARCHAR(20) NOT NULL;
	code_exam	INT(4) NOT NULL  CHECK "code_exam" LIKE "Exam%" ON DELETE CASCADE ON UPDATE CASCADE;
	CONSTRAINT PRIMARY KEY (CIN);
);
/*--------------------------
Table Eleve ::
---------------*/
CREATE TABLE "Professeur" (
	code_prof	VARCHAR(10) NOT NULL CHECK "code_exam" LIKE "Exam%";
	nom	 		VARCHAR(20) NOT NULL;
	prenom		VARCHAR(20) NOT NULL;
	lycee		VARCHAR(20) NOT NULL;
);