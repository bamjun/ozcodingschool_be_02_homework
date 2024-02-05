use test_publicdata;
select * from spot limit 10;

select new_address, tag from spot;

select * from spot where lang_code_id = 'en';

select * from spot where cmmn_use_time like '%daily%';

select * from spot where new_address like '%jongno-gu%' limit 1;

select * from spot where cmmn_fax != 'None';

insert into spot (new_address, tag) value('광화문', '이순신동상');

select * from spot where new_address = '광화문';

update spot set post_url = 'somesite' where new_address = '광화문' limit 1;

delete from spot where new_address = '광화문' limit 1;

