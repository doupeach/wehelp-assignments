## Assignment 3 - SQL CRUD

### ● 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。

SELECT * FROM website.member;
INSERT INTO website.member(name, username, password)
VALUES('testuser','test', 'test');
INSERT INTO website.member(name, username, password)
VALUES('AG','AGUN', 'AGPW');
INSERT INTO website.member(name, username, password)
VALUES('AK','AKUN', 'AKPW');
INSERT INTO website.member(name, username, password)
VALUES('Kanka','KankaUN', 'KankaPW');
INSERT INTO website.member(name, username, password)
VALUES('Molly','MollyUN', 'MollyPW');

### ● 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
SELECT * FROM website.member;

#### Select all data in member
  ![Select all data in member](/week-5/screenshots/A3_01.png)

### ● 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
SELECT * FROM website.member
ORDER BY time DESC;

####  data order by time desc
  ![data order by time desc](/week-5/screenshots/A3_02.png)


### ● 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
SELECT * FROM website.member
ORDER BY time DESC
LIMIT 3 OFFSET 1;

####  data order by time desc limit 3 offset 1
  ![data order by time desc limit 3 offset 1](/week-5/screenshots/A3_03.png)


### ● 使用 SELECT 指令取得欄位 username 是 test 的會員資料。
SELECT * FROM website.member
WHERE username='test';

####  data where username is test
  ![data where username is test](/week-5/screenshots/A3_04.png)

### ● 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
SELECT * FROM website.member
WHERE username='test' AND password='test';

####  data where username & password are test
  ![data where username & password are test](/week-5/screenshots/A3_05.png)


### ● 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
SET SQL_SAFE_UPDATES=0;
UPDATE website.member
SET name='test2'
WHERE username = 'test';
SET SQL_SAFE_UPDATES=1;
SELECT * FROM website.member;

####  change name to test2
  ![change name to test2](/week-5/screenshots/A3_06.png)


## Assignment 4 - SQL Aggregate Functions
更新資料表follower_count
#### updated follower_count of data
  ![updated follower_count of data](/week-5/screenshots/A4_00.png)

### ● 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
SELECT COUNT(*) FROM website.member;

#### count number of member
  ![count number of member](/week-5/screenshots/A4_01.png)

### ● 取得 member 資料表中，所有會員 follower_count 欄位的總和。
SELECT SUM(follower_count) FROM website.member;

#### count sum of follower_count
  ![count sum of follower_count](/week-5/screenshots/A4_02.png)


### ● 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
SELECT AVG(follower_count) FROM website.member;
#### count avg of follower_count
  ![count avg of follower_count](/week-5/screenshots/A4_03.png)

## Assignment 5 - SQL JOIN (Optional)
在資料庫中，建立新資料表，取名字為 message。資料表中必須包含以下欄位設定：
#### table message
  ![table message](/week-5/screenshots/A5_01.png)

### ● 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
SELECT * FROM website.message
JOIN website.member ON website.member.id = website.message.member_id;
#### message JOIN member_id = id
  ![message JOIN member_id = id](/week-5/screenshots/A5_02.png)

### ● 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。
SELECT * FROM website.message
JOIN website.member ON website.member.username = 'test' AND website.member.id = website.message.member_id;

#### message JOIN username = test from member
  ![message JOIN username = test from member](/week-5/screenshots/A5_03.png)