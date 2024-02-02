### **4. 삭제 (DELETE) -- 25 문제**

### 초급

-- (1) customers 테이블에서 특정 고객을 삭제하세요.
    
    DELETE FROM customers WHERE customerNumber = 1;
    
-- (2) products 테이블에서 특정 제품을 삭제하세요.
    select * from products;
    DELETE FROM products WHERE productCode = 'S10_1678';
    
-- (3) employees 테이블에서 특정 직원을 삭제하세요.
    select * from employees;
    DELETE FROM employees WHERE employeeNumber = 1002;
    
-- (4) offices 테이블에서 특정 사무실을 삭제하세요.
    select * FROM offices ;
    DELETE FROM offices WHERE officeNumber = 1;
    
-- (5) orders 테이블에서 특정 주문을 삭제하세요.
    select * FROM orders ;
    DELETE FROM orders WHERE orderNumber = 10100;
    
-- (6) orderdetails 테이블에서 특정 주문 상세를 삭제하세요.
    select * FROM orderdetails;
    DELETE FROM orderdetails WHERE orderNumber = 10100;
    
-- (7) payments 테이블에서 특정 지불 내역을 삭제하세요.
    select * FROM payments;
    DELETE FROM payments WHERE customerNumber = 103;
    
-- (8) productlines 테이블에서 특정 제품 라인을 삭제하세요.
select * FROM productlines ;
    DELETE FROM productlines WHERE productLine = 'Classic Cars';
    
-- (9) customers 테이블에서 특정 지역의 모든 고객을 삭제하세요.
    select * FROM customers ;
    DELETE FROM customers WHERE city = 'San Francisco';
    
-- (10) products 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.
    select * FROM products;
    DELETE FROM products WHERE productLine = 'Classic Cars';
    

### 중급

-- (1) employees 테이블에서 특정 부서의 모든 직원을 삭제하세요.
    
    DELETE FROM employees WHERE department = 'Sales';
    
-- (2) offices 테이블에서 특정 국가의 모든 사무실을 삭제하세요.
    
    DELETE FROM offices WHERE country = 'USA';
    
-- (3) orders 테이블에서 지난 달의 모든 주문을 삭제하세요.
    
    DELETE FROM orders WHERE orderDate BETWEEN '2022--12--01' AND '2022--12--31';
    
-- (4) orderdetails 테이블에서 특정 주문의 모든 상세 정보를 삭제하세요.
    
    DELETE FROM orderdetails WHERE orderNumber = 2;
    
-- (5) payments 테이블에서 특정 고객의 모든 지불 내역을 삭제하세요.
    
    DELETE FROM payments WHERE customerNumber = 2;
    
-- (6) productlines 테이블에서 여러 제품 라인을 한 번에 삭제하세요.
    
    DELETE FROM productlines WHERE productLine IN ('Motorcycles', 'Planes');
    
-- (7) customers 테이블에서 가장 오래된 5명의 고객을 삭제하세요.
    
    DELETE FROM customers WHERE customerNumber IN (SELECT customerNumber FROM customers ORDER BY customerNumber DESC LIMIT 5);
    
-- (8) products 테이블에서 재고가 없는 모든 제품을 삭제하세요.
    
    DELETE FROM products WHERE quantityInStock = 0;
    
-- (9) employees 테이블에서 특정 직급의 모든 직원을 삭제하세요.
    
    DELETE FROM employees WHERE jobTitle = 'Sales Rep';
    
-- (10)offices 테이블에서 가장 작은 사무실을 삭제하세요.
    
    DELETE FROM offices WHERE officeSize < 10;
    

### 고급

-- (1) orders 테이블에서 지난 해의 모든 주문을 삭제하세요.
    
    DELETE FROM orders WHERE orderDate BETWEEN '2022--01--01' AND '2022--12--31';
    
-- (2) orderdetails 테이블에서 가장 적게 팔린 제품의 모든 주문 상세를 삭제하세요.
    
    DELETE FROM orderdetails WHERE productNumber IN (SELECT productNumber FROM products ORDER BY quantityInStock ASC LIMIT 5);
    
-- (3) payments 테이블에서 특정 금액 이하의 모든 지불 내역을 삭제하세요.
    
    DELETE FROM payments WHERE amount < 50;
    
-- (4) productlines 테이블에서 제품이 없는 모든 제품 라인을 삭제하세요.
    
    DELETE FROM productlines WHERE productLine NOT IN (SELECT DISTINCT productLine FROM products);
    
-- (5) customers 테이블에서 최근 1년 동안 활동하지 않은 모든 고객을 삭제하세요.
    select * FROM customers;
    DELETE FROM customers WHERE customerNumber IN (SELECT customers.customerNumber FROM customers JOIN orders ON customers.customerNumber = orders.customerNumber WHERE orders.orderDate < '2023-01-01' GROUP BY customers.customerNumber ORDER BY MAX(orders.orderDate) DESC);
    

    