-- ### **2. 읽기 (READ) - 25 문제**
-- ### 초급
-- - (1) **`customers`** 테이블에서 모든 고객 정보를 조회하세요.
SELECT * FROM customers;


-- - (2) **`products`** 테이블에서 모든 제품 목록을 조회하세요.
SELECT * FROM products;

    
-- - (3) **`employees`** 테이블에서 모든 직원의 이름과 직급을 조회하세요.
SELECT firstName, lastName, jobTitle FROM employees;


-- - (4) **`offices`** 테이블에서 모든 사무실의 위치를 조회하세요.
desc offices;
SELECT city, addressLine1, phone FROM offices;


-- - (5) **`orders`** 테이블에서 최근 10개의 주문을 조회하세요.
SELECT * FROM orders ORDER BY orderDate DESC LIMIT 10;


-- - (6) **`orderdetails`** 테이블에서 특정 주문의 모든 상세 정보를 조회하세요.
SELECT * FROM orderdetails WHERE orderNumber = 10100;

-- - (7) **`payments`** 테이블에서 특정 고객의 모든 지불 정보를 조회하세요.
SELECT * FROM payments WHERE customerNumber = 103;

-- - (8) **`productlines`** 테이블에서 각 제품 라인의 설명을 조회하세요.
SELECT productLine, textDescription FROM productlines;

-- - (9) **`customers`** 테이블에서 특정 지역의 고객을 조회하세요.
SELECT * FROM customers WHERE city = 'Example City';

-- - (10) **`products`** 테이블에서 특정 가격 범위의 제품을 조회하세요.
SELECT * FROM products WHERE buyPrice BETWEEN 40 AND 50;

### 중급

-- - (1) **`orders`** 테이블에서 특정 고객의 모든 주문을 조회하세요.
SELECT * FROM orders WHERE customerNumber = 121;

-- - (2) **`orderdetails`** 테이블에서 특정 제품에 대한 모든 주문 상세 정보를 조회하세요.
SELECT * FROM orderdetails WHERE productCode = 'S10_1678';

-- - (3) **`payments`** 테이블에서 특정 기간 동안의 모든 지불 정보를 조회하세요.
SELECT * FROM payments WHERE paymentDate BETWEEN '2023-01-01' AND '2024-03-31';

-- - (4) **`employees`** 테이블에서 특정 직급의 모든 직원을 조회하세요.
SELECT firstName, lastName FROM employees WHERE jobTitle = 'Sales Rep';

-- - (5) **`offices`** 테이블에서 특정 국가의 모든 사무실을 조회하세요.
SELECT * FROM offices WHERE country = 'USA';

-- - (6) **`products`** 테이블에서 특정 제품 라인에 속하는 모든 제품을 조회하세요.
SELECT * FROM products WHERE productLine = 'Classic Cars';

-- - (7) **`customers`** 테이블에서 최근에 가입한 5명의 고객을 조회하세요.
SELECT * FROM customers ORDER BY customerNumber DESC LIMIT 5;

-- - (8) **`products`** 테이블에서 재고가 부족한 모든 제품을 조회하세요.
SELECT * FROM products WHERE quantityInStock < 10;

-- - (9) **`orders`** 테이블에서 지난 달에 이루어진 모든 주문을 조회하세요.
SELECT * FROM orders WHERE orderDate = '2003-01-06';

-- - (10) **`orderdetails`** 테이블에서 특정 주문에 대한 총 금액을 계산하세요.
SELECT orderNumber, SUM(quantityOrdered * priceEach) AS totalAmount FROM orderdetails WHERE orderLineNumber = 3 GROUP BY orderNumber;


### 고급
-- - (1) **`customers`** 테이블에서 각 지역별 고객 수를 계산하세요.
SELECT city, COUNT(*) AS customerCount FROM customers GROUP BY city;

-- - (2) **`products`** 테이블에서 각 제품 카테고리별 평균 가격을 계산하세요.
SELECT productLine, AVG(buyPrice) AS averagePrice FROM products GROUP BY productLine;

-- - (3) **`employees`** 테이블에서 각 부서별 직원 수를 계산하세요.
SELECT officeCode, COUNT(*) AS employeeCount FROM employees GROUP BY officeCode;

-- - (4) **`offices`** 테이블에서 각 사무실별 평균 직원 연봉을 계산하세요.
SELECT officeCode, AVG(salary) AS averageSalary FROM employees GROUP BY officeCode;

-- - (5) **`orderdetails`** 테이블에서 가장 많이 팔린 제품 5개를 조회하세요.
select productCode, sum(quantityOrdered * priceEach) amount from orderdetails group by productCode order by amount desc limit 5;