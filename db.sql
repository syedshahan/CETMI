CREATE DATABASE IF NOT EXISTS geeklogin DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
use geeklogin;

CREATE TABLE IF NOT EXISTS accounts (
   id int(11) NOT NULL AUTO_INCREMENT,
   username varchar(50) NOT NULL,
   password varchar(255) NOT NULL,
   email  varchar(100) NOT NULL,
   PRIMARY KEY ( id )
) ENGINE= INNODB AUTO_INCREMENT=2 DEFAULT CHARSET utf8;

select * from geeklogin.accounts;


CREATE TABLE IF NOT EXISTS users (
   id int(11) NOT NULL AUTO_INCREMENT,
   username varchar(50) NOT NULL,
   email  varchar(100) NOT NULL,
   PRIMARY KEY ( id )
) ENGINE= INNODB AUTO_INCREMENT=2 DEFAULT CHARSET utf8;

select * from geeklogin.users;

CREATE TABLE IF NOT EXISTS redZone (
   lat decimal(10, 8) NOT NULL,
   lng decimal(11, 8) NOT NULL,
   population int(255) NOT NULL
)

select * from geeklogin.redZone;

CREATE TABLE IF NOT EXISTS Hospital (
HId int not null,
Hname nvarchar(25) not null,
Haddress nvarchar(40),
hphonenumber varchar(22),
primary key(HId)
);

insert into geeklogin.Hospital Values (1, 'Jinnah Hospital', 'Lahore', '03221234567');
insert into geeklogin.Hospital Values (2, 'Hamid Hospital', 'Lahore', '03002134567');
insert into geeklogin.Hospital Values (3, 'Asaaf Hospital', 'Lahore', '03397654321');
insert into geeklogin.Hospital Values (4, 'Lifeline Hospital', 'Lahore','03457162534');
insert into geeklogin.Hospital Values (5, 'Family Hospital', 'Lahore', '03114536271');
insert into geeklogin.Hospital Values (6, 'Niazi Hospital', 'Lahore', '03098765243');
insert into geeklogin.Hospital Values (7, 'Latif Hospital', 'Lahore', '03234352761');
insert into geeklogin.Hospital Values (8, 'Saadan Hospital', 'Lahore','03471234765');
insert into geeklogin.Hospital Values (9, 'Johar Hospital', 'Lahore', '03198712634');
insert into geeklogin.Hospital Values (10, 'Hafeez Hospital', 'Lahore','03011237654');
select * from geeklogin.hospital;





CREATE TABLE IF NOT EXISTS Isolationward (
isoiD int not null,
HId int not null,
isobeds int not null,
primary key (isoiD),

foreign key (HId) references hospital(HId)
);

insert into isolationward values (001,1,5),(002,1,4),
(003,2,7),(004,2,1),
(005,3,5),(006,3,4),
(007,4,2),(008,4,2),(009,4,1),
(010,5,10),
(011,6,1),(012,6,1),(013,6,1),
(014,7,5),(015,7,5),
(016,8,1),(017,8,2),(0118,8,2),(019,8,1),
(020,9,4),(021,9,1),(022,9,2),(023,9,5),
(024,10,5),(025,10,10);


select * from isolationward;

select hospital.hid,hospital.hname,hospital.haddress,hospital.hphonenumber,isolationward.isoid,isolationward.isobeds 
from hospital
inner join 
isolationward on hospital.hid=isolationward.hid order by hid;


CREATE TABLE IF NOT EXISTS Doctors (
   docID int not null,
   docname nvarchar(30),
   docaddress nvarchar(40),
   
   primary key(docID)

);


insert into geeklogin.Doctors Values (101,'Dr. Ghulam Mustafa',  'Allah Hoo Roundabout');
insert into geeklogin.Doctors Values (102,'Dr. Asif Mukhtar',  'PIA Road');
insert into geeklogin.Doctors Values (103,'Dr. Jahanzaib Nazir',  'Ideal Park');
insert into geeklogin.Doctors Values (104,'Dr. SHAHAN',  'Ideal Park');
insert into geeklogin.Doctors Values (105,'Dr. UIDREES ARIF',  'JOHAR TOWN');
select * from geeklogin.Doctors;

UPDATE DOCTORS
SET DOCNAME='Dr. M IDREES ARIF' WHERE DOCID=105;


create table IF NOT EXISTS docphonenumbers(
	docID int not null,
	docphonenumber varchar(22),

	foreign key (docID)
    references Doctors(docID)

);

INSERT INTO DOCPHONENUMBERS VALUES (101,'03001234567'),
(102,'03437654321'),
(103,'03012345713'),
(104,'03458735012'),
(105,'03026473134'),(105,'03204363213');

select * from docphonenumbers;

select doctors.docid,doctors.docname,doctors.docaddress,docphonenumbers.docphonenumber 
from doctors
inner join 
docphonenumbers on doctors.docid=docphonenumbers.docid order by docid;


CREATE TABLE IF NOT EXISTS QuarantineCenter(
QId int not null,
QName varchar(40),
Qbeds int not null,
Qlocation nvarchar(40) not null
);




insert into geeklogin.QuarantineCenter Values (1,'Xpo Center', 100, 'Johar Town');
insert into geeklogin.QuarantineCenter Values (2, 'ABC Center',50, 'Johar Town');
insert into geeklogin.QuarantineCenter Values (3,'Gulshan foundation center', 60, 'Johar Town');
insert into geeklogin.QuarantineCenter Values (4,'Cakes and bakes center', 80, 'Johar Town');
insert into geeklogin.QuarantineCenter Values (5, 'Gorment Center',200, 'Johar Town');
select * from geeklogin.QuarantineCenter;




insert into geeklogin.Isolationward Values (1, 2, 'Johar Town');
insert into geeklogin.Isolationward Values (2, 3, 'Johar Town');
insert into geeklogin.Isolationward Values (3, 5, 'Johar Town');
insert into geeklogin.Isolationward Values (4, 6, 'Johar Town');
insert into geeklogin.Isolationward Values (5, 4, 'Johar Town');
select * from geeklogin.Isolationward;



CREATE TABLE IF NOT EXISTS EmergenyContact (
amb nvarchar(22) not null,
police nvarchar(22) not null,
covidcontact nvarchar(33) not null
);

insert into EmergenyContact values ('1122','15','+92 (51) 9245717');

select * from EmergenyContact;



CREATE TABLE IF NOT EXISTS labs (
LId int not null,
lname varchar(20),
lcontact nvarchar(22),
ldocname nvarchar(25)

);



insert into geeklogin.labs Values (1, 'Fatima Lab', '03450981264' , 'Dr. Jahanzaib Nazir');
insert into geeklogin.labs Values (2, 'Jinnah Lab', '0349163794', 'Dr. Ali Ahmad');
insert into geeklogin.labs Values (3, 'Bismillah Lab', '03420836471' , 'Dr. idrees Arif');
insert into geeklogin.labs Values (4, 'Arisha Lab', '03326482911' , 'Dr. Jabbar Rafiq');
select * from geeklogin.labs;



CREATE TABLE IF NOT EXISTS Survey (

   Uname nvarchar(30),
   uphonenumber nvarchar(22),
   bloodgroup varchar(50),
   age int,
   uaddress nvarchar(40),
   CovidTEST nvarchar(15),
   diabatiesTEST varchar(15),
   cancerTEST varchar(15),
   heartPATIENT varchar(15)
   
);

select Survey.Uname, users.username
from Survey
inner join users on Survey.Uname = users.username;


insert into  Survey Values('Shahan', '0322433', 'Ab+', 20, 'jj', 'A', 'A', 'A', 'A');


select * from geeklogin.Survey;



