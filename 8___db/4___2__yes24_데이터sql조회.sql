use yes24;
SELECT title, author FROM Books;

SELECT title, rating FROM Books WHERE rating >= 4;

SELECT title, review FROM Books WHERE review >= 100;

SELECT title, price FROM Books WHERE price < 20000;

SELECT title, ranking_weeks FROM Books WHERE ranking_weeks >= 4;

SELECT title FROM Books WHERE author = 'ETS 저';

SELECT title FROM Books WHERE publisher = '김영사';

SELECT author, COUNT(*) FROM Books GROUP BY author;

SELECT publisher, COUNT(*) AS num_books FROM Books GROUP BY publisher ORDER BY num_books DESC LIMIT 1;

SELECT author, AVG(rating) AS avg_rating FROM Books GROUP BY author ORDER BY avg_rating DESC LIMIT 1;

SELECT title, author FROM Books WHERE ranking = 1;

SELECT title, sales, review FROM Books ORDER BY sales DESC, review DESC LIMIT 10;

SELECT title, publishing FROM Books ORDER BY publishing DESC LIMIT 5;

SELECT author, AVG(rating) FROM Books GROUP BY author;

SELECT publishing, COUNT(*) FROM Books GROUP BY publishing;

SELECT title, AVG(price) FROM Books GROUP BY title;

SELECT title, review FROM Books ORDER BY review DESC LIMIT 5;

SELECT ranking, AVG(review) FROM Books GROUP BY ranking;

SELECT title, rating FROM Books WHERE rating > (SELECT AVG(rating) FROM Books);

SELECT title, price FROM Books WHERE price > (SELECT AVG(price) FROM Books);

SELECT title, review FROM Books WHERE review > (SELECT MAX(review) FROM Books);

SELECT title, sales FROM Books WHERE sales < (SELECT AVG(sales) FROM Books);

SELECT title, publishing FROM Books WHERE author = (SELECT author FROM Books GROUP BY author ORDER BY COUNT(*) DESC LIMIT 1) ORDER BY publishing DESC LIMIT 1;

select * from Books where title = '2024 큰별쌤 최태성의 별별한국사 기출 500제 한국사능력검정시험 심화 (1,2,3급)';

SET SQL_SAFE_UPDATES = 0;
UPDATE Books SET price = 30000 WHERE title = '2024 큰별쌤 최태성의 별별한국사 기출 500제 한국사능력검정시험 심화 (1,2,3급)';

select * from Books where author = '최태성 저';
UPDATE Books SET title = '한국사 마스터' WHERE author = '최태성 저';

SELECT title, MIN(sales) as min FROM Books group by title order by min asc limit 1; -- 남의 시선에 아랑곳하지 않기
SELECT MIN(sales) FROM Books;
SET @minSales = (SELECT MIN(sales) FROM Books);
DELETE FROM Books WHERE sales = @minSales;

select * from books WHERE publisher = '민음사';
UPDATE Books SET rating = rating + 1 WHERE publisher = '민음사';

SELECT author, AVG(rating) as avg_rating, AVG(sales) as avg_sales FROM Books GROUP BY author;

SELECT publishing, AVG(price) as avg_price FROM Books GROUP BY publishing;

SELECT publisher, COUNT(*) as num_books, AVG(review) as avg_review FROM Books GROUP BY publisher;

SELECT ranking, AVG(sales) as avg_sales FROM Books GROUP BY ranking;

SELECT price, AVG(review) as avg_review, AVG(rating) as avg_rating FROM Books GROUP BY price;

-- 난이도 있는 문제
-- 출판사별 평균 판매지수가 가장 높은 저자 찾기
-- 각 출판사별로 평균 판매지수가 가장 높은 저자의 이름과 그 평균 판매지수를 조회하세요.
SELECT publisher, author, AVG(sales) as avg_sales FROM Books GROUP BY publisher, author ORDER BY publisher, avg_sales DESC;

-- 리뷰 수가 평균보다 높으면서 가격이 평균보다 낮은 책 조회
-- 리뷰 수와 가격의 전체 평균을 계산한 후, 이보다 리뷰 수는 높고 가격은 낮은 책들을 조회하세요.

SELECT title, review, price FROM Books WHERE review > (SELECT AVG(review) FROM Books) AND price < (SELECT AVG(price) FROM Books);


-- 가장 많은 종류의 책을 출판한 저자 찾기
-- 서로 다른 제목의 책을 가장 많이 출판한 저자를 찾으세요.
SELECT author, COUNT(DISTINCT title) as num_books
FROM Books
GROUP BY author
ORDER BY num_books DESC
LIMIT 1;

-- 각 저자별로 가장 높은 판매지수를 기록한 책 조회
-- 각 저자별로 가장 높은 판매지수를 기록한 책의 제목과 그 판매지수를 조회하세요.

-- SELECT author, title, MAX(sales) as max_sales FROM Books GROUP BY author;
SELECT b.author, 
       (SELECT title FROM Books WHERE author = b.author ORDER BY sales DESC LIMIT 1) as title,
       MAX(b.sales) as max_sales
FROM Books b
GROUP BY b.author;
-- David Cho 저	해커스 토익 기출 VOCA 보카	347076
select * from books where author = 'David Cho 저';

-- 연도별 출판된 책 수와 평균 가격 비교
-- 연도별로 출판된 책의 수와 그 해 출판된 책들의 평균 가격을 비교 분석하세요.
SELECT YEAR(publishing) as year, COUNT(*) as num_books, AVG(price) as avg_price
FROM Books
GROUP BY year;


-- 출판사가 같은 책들 중 평점 편차가 가장 큰 출판사 찾기
-- 같은 출판사에서 출판된 책들 중 평점 편차가 가장 큰 출판사와 그 편차를 조회하세요.
SELECT publisher, MAX(rating) - MIN(rating) as rating_difference
FROM Books
GROUP BY publisher
ORDER BY rating_difference DESC
LIMIT 1;



-- 특정 저자의 책들 중 판매지수 대비 평점이 가장 높은 책 찾기
-- 특정 저자의 책들 중 판매지수 대비 평점이 가장 높은 책의 제목과 그 비율을 조회하세요.
SELECT title, rating / sales as ratio
FROM Books
WHERE author = '특정 저자'
ORDER BY ratio DESC
LIMIT 1;