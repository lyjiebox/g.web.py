-- For web.py learning --
/*
create table movie (id, title, year, country);

insert into movie values (1, 'FG', 1994, 'US');
insert into movie values (2, 'SJ', 1995, 'US');
insert into movie values (3, 'FGSJ', 2001, 'UK');
insert into movie values (5, 'FJ', 1973, 'CN');

select * from movie;
*/
select * from movie where title like '%G%';