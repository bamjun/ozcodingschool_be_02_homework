-- ### **3. 갱신 (UPDATE) - 25 문제**
-- ### 초급
-- - (1) **`customers`** 테이블에서 특정 고객의 주소를 갱신하세요.
select * from customers;
UPDATE customers SET addressLine1 = '달나라' WHERE customerNumber = 101;


-- - (2) **`products`** 테이블에서 특정 제품의 가격을 갱신하세요.
select productCode, buyPrice from products;
UPDATE products SET buyPrice = 29.99 WHERE productCode = 'S10_1678';

-- - (3) **`employees`** 테이블에서 특정 직원의 직급을 갱신하세요.
select * from employees;
UPDATE employees SET jobTitle = 'Manager' WHERE employeeNumber = 1002;

-- - (4) **`offices`** 테이블에서 특정 사무실의 전화번호를 갱신하세요.
SET SQL_SAFE_UPDATES = 0;
select * from offices;
UPDATE offices SET phone = '12345' WHERE officeCode = 1;


-- - (5) **`orders`** 테이블에서 특정 주문의 상태를 갱신하세요.
select * from orders order by orderNumber desc;
UPDATE orders SET status = 'Shipped' WHERE orderNumber = 10430;



-- - (6) **`orderdetails`** 테이블에서 특정 주문 상세의 수량을 갱신하세요.
select * from orderdetails;
UPDATE orderdetails SET quantityOrdered = 301 WHERE orderNumber = 10100 AND productCode = 'S18_1749';



-- - (7) **`payments`** 테이블에서 특정 지불의 금액을 갱신하세요.
select * from payments;
UPDATE payments SET amount = 250.00 WHERE customerNumber = 103 AND paymentDate = '2004-10-19';



-- - (8) **`productlines`** 테이블에서 특정 제품 라인의 설명을 갱신하세요.
select * from productlines;
UPDATE productlines SET textDescription = 'Updated description' WHERE productLine = 'Classic Cars';



-- - (9) **`customers`** 테이블에서 특정 고객의 이메일을 갱신하세요.
select * from customers;
UPDATE customers SET addressLine2 = 'john_updated@email.com' WHERE customerNumber = 103;


-- - **`products`** 테이블에서 여러 제품의 가격을 한 번에 갱신하세요.
UPDATE products SET price = price * 1.1;


-- ### 중급
-- - (1) **`employees`** 테이블에서 여러 직원의 부서를 한 번에 갱신하세요.
UPDATE employees SET officeCode = 2 WHERE department = 'Sales';



-- - (2) **`offices`** 테이블에서 여러 사무실의 위치를 한 번에 갱신하세요.
UPDATE offices SET city = 'Updated City' WHERE country = 'USA';

-- - (3) **`orders`** 테이블에서 지난 달의 모든 주문의 배송 상태를 갱신하세요.
UPDATE orders SET status = 'Cancelled' WHERE orderDate BETWEEN '2022-12-01' AND '2022-12-31';

 
-- - (4) **`orderdetails`** 테이블에서 여러 주문 상세의 가격을 한 번에 갱신하세요.
UPDATE orderdetails SET priceEach = priceEach * 0.9 WHERE orderID IN (SELECT orderID FROM orders WHERE orderDate BETWEEN '2023-01-01' AND '2023-01-31');



-- - (5) **`payments`** 테이블에서 특정 고객의 모든 지불 내역을 갱신하세요.
UPDATE payments SET amount = amount * 1.05 WHERE customerID = 2;


-- - (6) **`productlines`** 테이블에서 여러 제품 라인의 설명을 한 번에 갱신하세요.
UPDATE productlines SET textDescription = 'New description' WHERE productLine IN ('Classic Cars', 'Trains');



-- - (7) **`customers`** 테이블에서 특정 지역의 모든 고객의 연락처를 갱신하세요
UPDATE customers SET phone = '999-999-9999' WHERE city = 'San Francisco';



-- - (8) **`products`** 테이블에서 특정 카테고리의 모든 제품 가격을 갱신하세요.
UPDATE products SET price = price * 0.95 WHERE productLine = 'Classic Cars';



-- - (9) **`employees`** 테이블에서 특정 직원의 모든 정보를 갱신하세요.
UPDATE employees SET salary = salary + 5000 WHERE employeeID = 2;



-- - (10) **`offices`** 테이블에서 특정 사무실의 모든 정보를 갱신하세요.
UPDATE offices SET address = '1234 New Address St', phone = '987-654-3211' WHERE officeID = 2;


-- ### 고급
-- - (1) **`orders`** 테이블에서 지난 해의 모든 주문 상태를 갱신하세요.
UPDATE orders SET status = 'On Hold' WHERE orderDate BETWEEN '2022-01-01' AND '2022-12-31';



-- - (2) **`orderdetails`** 테이블에서 특정 주문의 모든 상세 정보를 갱신하세요.
UPDATE orderdetails SET priceEach = priceEach * 1.1 WHERE orderID = 3;



-- - (3) **`payments`** 테이블에서 지난 달의 모든 지불 내역을 갱신하세요.
UPDATE payments SET paymentDate = '2023-02-01' WHERE paymentDate BETWEEN '2023-01-01' AND '2023-01-31';



-- - (4) **`productlines`** 테이블에서 모든 제품 라인의 정보를 갱신하세요.
UPDATE productlines SET textDescription = 'New updated description' WHERE productLine IN (SELECT productLine FROM products WHERE quantityInStock < 10);



-- - (5) **`customers`** 테이블에서 모든 고객의 주소를 갱신하세요.
select * from customers;
UPDATE customers SET addressLine1 = '주소 갱신';