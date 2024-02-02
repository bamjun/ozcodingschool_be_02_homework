use classicmodels;

-- 고객 목록 조회: 모든 고객의 이름과 이메일을 조회하세요.
-- TABLE: customers
select * from customers;

-- 특정 제품 라인의 제품 조회: 'Classic Cars' 제품 라인에 속하는 모든 제품의 이름과 가격을 조회하세요.
-- TABLE: products, COL: productLine
select * from products where productLine = 'Classic Cars';

-- 최근 주문: 가장 최근에 주문된 10개의 주문을 주문 날짜(orderDate)와 함께 조회하세요.
-- TABLE: orders, COL: orderDate
select * from orders order by orderDate desc limit 10;

-- 최소 금액 이상의 결제: 100달러 이상 결제된 거래(amount)만 조회하세요.
-- TABLE: payments, COL: amount 
select * from payments where amount >= 100;

-- 주문과 고객 정보 조합: 각 주문에 대한 주문 번호(orders-orderNumber)와 
-- 주문한 고객(customers-customerName)의 이름을 조회하세요.
select * from orders join customers on orders.orderNumber = customers.customerName;

-- 제품과 제품 라인 결합: 각 제품의 이름(products-productName)과 
-- 속한 제품 라인의 설명(productlines-textDescription)을 조회하세요.
select p.productName, p.productLine, l.textDescription from products p join productlines l on p.productLine = l.productLine;

-- 직원과 상사 정보: 각 직원의 이름과 직속 상사의 이름을 조회하세요.
SELECT e1.employeeNumber, e1.firstName, e1.lastName, e2.firstName AS 'ManagerFirstName', e2.lastName AS 'ManagerLastName'
FROM employees e1
LEFT JOIN employees e2 ON e1.reportsTo = e2.employeeNumber;

-- 특정 사무실의 직원 목록: 'San Francisco' 사무실에서 근무하는 모든 직원의 이름을 조회하세요.
SELECT e.employeeNumber, e.lastName, e.firstName, e.extension, e.email, e.officeCode, e.reportsTo, e.jobTitle
FROM employees e
JOIN offices o ON e.officeCode = o.officeCode
WHERE o.city = 'San Francisco';

-- 제품 라인별 제품 수: 각 제품 라인에 속한 제품의 수를 조회하세요.
SELECT productLine, COUNT(*) AS productCount FROM products GROUP BY productLine;

-- 고객별 총 주문 금액: 각 고객별로 총 주문 금액을 계산하세요.
SELECT customers.customerNumber, 
       customers.customerName, 
       SUM(orderdetails.quantityOrdered * orderdetails.priceEach) AS totalAmount
FROM customers
JOIN orders ON customers.customerNumber = orders.customerNumber
JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber
GROUP BY customers.customerNumber, customers.customerName;

-- 가장 많이 팔린 제품: 가장 많이 판매된 제품의 이름과 판매 수량을 조회하세요.
select p.productName, sum(d.quantityOrdered) as oderedp
from orderdetails d
join products p on d.productCode = p.productCode
group by p.productName order by oderedp desc limit 1; 

-- 매출이 가장 높은 사무실: 가장 많은 매출을 기록한 사무실의 위치와 매출액을 조회하세요.
select offices.officeCode, offices.country, offices.city, sum(d.quantityOrdered * d.priceEach) as totalAmount
from orders o
join orderdetails d on o.orderNumber = d.orderNumber
join customers c on c.customerNumber = o.customerNumber
join employees e on e.employeeNumber = c.salesRepEmployeeNumber
join offices on offices.officeCode = e.officeCode
group by offices.officeCode, offices.country, offices.city order by totalAmount desc;


-- 특정 금액 이상의 주문: 500달러 이상의 총 주문 금액을 기록한 주문들을 조회하세요.
select orders.orderNumber, sum(orderdetails.quantityOrdered * orderdetails.priceEach) as totalAmount
from orders
join orderdetails on orders.orderNumber = orderdetails.orderNumber
group by orders.orderNumber
HAVING totalAmount > 500
order by totalAmount asc;


-- 평균 이상 결제 고객: 평균 결제 금액보다 많은 금액을 결제한 고객들의 목록을 조회하세요.
SELECT customerNumber, SUM(amount) AS totalPayment
FROM payments
GROUP BY customerNumber
HAVING totalPayment > (SELECT AVG(amount) FROM payments);

-- 주문 없는 고객: 아직 주문을 하지 않은 고객의 목록을 조회하세요.
SELECT customerName
FROM customers
WHERE customerNumber NOT IN (SELECT customerNumber FROM orders);

-- 최대 매출 고객: 가장 많은 금액을 지불한 고객의 이름과 총 결제 금액을 조회하세요.
SELECT c.customerName, SUM(od.quantityOrdered * od.priceEach) AS totalSpent
FROM customers c
JOIN orders o ON c.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
GROUP BY c.customerName
ORDER BY totalSpent DESC
LIMIT 1;

-- 신규 고객 추가: 'customers' 테이블에 새로운 고객을 추가하는 쿼리를 작성하세요.
INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)
VALUES (497, 'kim beomjun', 'kim', 'beomjun', '010-1234-1234', '광화대로112', '광화문빌딩', '서울', '서울', '1234', 'korea', 1002, 100000.00);

-- 제품 가격 변경: 'Classic Cars' 제품 라인의 모든 제품 가격을 10% 인상하는 쿼리를 작성하세요.
DESCRIBE products;
ALTER TABLE products MODIFY COLUMN buyPrice DECIMAL(20,10);
   -- 0.99999999999999999999 이럴때는 9개수 20개 만큼 decimal 뒤에 늘리기,, DECIMAL(12,20);
   -- 곱셈이나, 나눗셈할때, 0. 뒤에 처리 잘해야함. 자동으로 짤라서 저장하지 않음.
UPDATE products
SET buyPrice = buyPrice * 1.10
WHERE productLine = 'Classic Cars';


-- 고객 데이터 업데이트: 특정 고객의 이메일 주소를 변경하는 쿼리를 작성하세요. (이메일 주소가 없음)
select * from customers order by customerNumber desc limit 1;
UPDATE customers
SET addressLine1 = '천계천로191'
WHERE customerNumber = 497;


-- 직원 전보: 특정 직원을 다른 사무실로 이동시키는 쿼리를 작성하세요.
select * from employees order by employeeNumber desc limit 1;
select distinct officeCode from offices;

UPDATE employees
SET officeCode = '1' -- 오피스 코드 1~7
WHERE employeeNumber = 1702;



