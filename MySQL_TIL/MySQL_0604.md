# MySQL 

## 설치
    [MySQL Community version 설치 링크](https://dev.mysql.com/downloads/mysql/)

    [HeidiSQL 설치]

## 명령어

1. 작업용 DB 생성
```SQL
CREATE DATABASE [DB_name]
    default character set utf8 
    default collate utf8_general_ci; /* 기본 문자열을 utf8로 설정 */
```

2. 테이블 조작

```SQL
/* DB 사용 */
USE [DB_name];

/* 테이블 생성 */
CREATE TABLE if not exists add_book (
    no int unsigned not null auto_increment, 
    name varchar(10) not null, 
    tel varchar(14), 
    primary key(no)
) auto_increment=10001 default charset=utf8;
```

 * add_book이라는 테이블이 존재하지 않을 때 테이블 생성
 * [칼럼 이름] [자료형] [공백가능 유뮤] 
 * auto_increment : 
 * primary : 기본키 제약. NULL 불가능.

 3. 명령어
    * SHOW tables
        - DB의 테이블을 보여줌
    * DESC [table_name]
        - 테이블의 description을 보여줌
    * DROP TABLE [table_name]
        - 테이블 제거
    * CREATE TABLE [table_name]
        - 테이블 생성
    * RENAME TABLE [old_tb_name] to [new_tb_name]
        - 테이블 이름 변경
    
    테이블 변경
    * ADD : 추가
        - ALTER TABLE [table_name] ADD [column_name]
    * DROP : 삭제
        - ALTER TABLE [table_name] DROP [column_name]
    * CHANGE : 이름 변경
        - ALTER TABLE [old_cl_name] CHANGE [new_cl_name] [data_type]
    * MODIFY : 순서 변경
        - alter table [table_name] modify [column_name] [data_type] first
        - alter table [table_name] modify [column_name] [data_type] after [other_cl_name]

4. 데이터 조작 (SELECT)
    select [column_name] from [table_name] where [data_type]