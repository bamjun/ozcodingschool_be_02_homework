use classicmodels;

-- ### **1. 생성 (CREATE) - 25 문제**
-- ### 초급
-- - (1) **`customers`** 테이블에 새 고객을 추가하세요.
--     **`INSERT INTO customers (name, address, ...) VALUES ('John Doe', '123 Main St', ...);`**
desc customers;
select * from customers  order by customerNumber desc;
INSERT INTO customers (
    customerNumber,
    customerName,
    contactLastName,
    contactFirstName,
    phone,
    addressLine1,
    addressLine2,
    city,
    state,
    postalCode,
    country,
    salesRepEmployeeNumber,
    creditLimit
) VALUES (
    498,
    '홍길동',
    '길동',
    '홍',
    '123-456-7890',
    '123 Example St.',
    'Suite 100',
    'Example City',
    'CA',
    '12345',
    'USA',
    1501,
    10000.00
);


-- - (2) **`products`** 테이블에 새 제품을 추가하세요. 
--     **`INSERT INTO products (name, price, ...) VALUES ('Toy Car', 19.99, ...);`**
desc products;
select * from products  order by productCode desc;
INSERT INTO products (
    productCode,
    productName,
    productLine,
    productScale,
    productVendor,
    productDescription,
    quantityInStock,
    buyPrice,
    MSRP
) VALUES (
    'S72_3213',
    '1969 Harley Davidson Ultimate Chopper',
    'Motorcycles',
    '1:10',
    'Min Lin Diecast',
    'This replica features working kickstand, front suspension, gear-shift lever, foot-brake lever, and drive chain. It comes with its own stand, informative booklet, and authenticity certificate.',
    7933,
    48.8100000000,
    95.70
);



-- - (3) **`employees`** 테이블에 새 직원을 추가하세요.
--     **`INSERT INTO employees (firstName, lastName, ...) VALUES ('Alice', 'Johnson', ...);`**
desc employees;
select * from employees  order by employeeNumber desc;   
INSERT INTO employees (
    employeeNumber,
    lastName,
    firstName,
    extension,
    email,
    officeCode,
    reportsTo,
    jobTitle
) VALUES (
    1705,
    'Doe',
    'John',
    'x1234',
    'jdoe@example.com',
    '1',
    1088,
    'Sales Rep'
);





-- - (4) **`offices`** 테이블에 새 사무실을 추가하세요.
--     **`INSERT INTO offices (city, phone, ...) VALUES ('San Francisco', '123-456-7890', ...);`**
desc offices;
select * from offices  order by officeCode desc;   
INSERT INTO offices (
    officeCode,
    city,
    phone,
    addressLine1,
    addressLine2,
    state,
    country,
    postalCode,
    territory
) VALUES (
    '8',
    '서울',
    '+82 010-3322-1234',
    '천계천로151',
    'Suite 600',
    '서울',
    'korea',
    '94080',
    'ko'
);




-- - (5) **`orders`** 테이블에 새 주문을 추가하세요.
--     **`INSERT INTO orders (orderDate, customerID, ...) VALUES ('2023-01-01', 1, ...);`**
desc orders;
select * from orders  order by orderNumber desc;   
INSERT INTO orders (
    orderNumber,
    orderDate,
    requiredDate,
    shippedDate,  
    status,
    comments,  
    customerNumber
) VALUES (
    10427,          -- 1씩증가해야함.
    '2005-05-31',
    '2005-06-07', 
    NULL,
    'In Process',
    '',
    119
);




-- - (6) **`orderdetails`** 테이블에 주문 상세 정보를 추가하세요.
--     **`INSERT INTO orderdetails (orderID, productID, quantityOrdered, priceEach) VALUES (1, 1, 2, 20.00);`**
desc orderdetails;
select * from orderdetails  order by orderNumber desc;   
INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber)
VALUES (10427, 'S10_1678', 30, 95.70, 1);






-- - (7) **`payments`** 테이블에 지불 정보를 추가하세요.
--     **`INSERT INTO payments (customerID, amount, paymentDate) VALUES (1, 200.00, '2023-01-01');`**
desc payments;
select * from payments  order by customerNumber desc;   
select * from customers order by customerNumber desc;
INSERT INTO payments (customerNumber, checkNumber, paymentDate, amount) 
VALUES (498, 'HQ336338', '2024-02-02', 5000.00);


-- - (8) **`productlines`** 테이블에 제품 라인을 추가하세요.
--     **`INSERT INTO productlines (productLine, textDescription) VALUES ('Classic Cars', 'Various classic cars models');`**
desc productlines;
select * from productlines  order by productLine desc;   
INSERT INTO productlines (productLine, textDescription, htmlDescription, image)
VALUES ('부릉부릉부릉이', '부릉이카', NULL, NULL);


-- - (9) **`customers`** 테이블에 다른 지역의 고객을 추가하세요.
--     **`INSERT INTO customers (name, address, city, ...) VALUES ('Jane Smith', '456 Elm St', 'New York', ...);`**
desc customers;
select * from customers  order by customerNumber desc;   
INSERT INTO customers (
    customerNumber,
    customerName,
    contactLastName,
    contactFirstName,
    phone,
    addressLine1,
    addressLine2,
    city,
    state,
    postalCode,
    country,
    salesRepEmployeeNumber,
    creditLimit
) VALUES (
    499,
    '홍만나',
    '만나',
    '홍',
    '123-456-7890',
    '둥덩이로112',
    'Suite 100',
    '크라운',
    '별나라',
    '12345',
    '문',
    1501,
    10000.00
);

-- - (10) **`products`** 테이블에 다른 카테고리의 제품을 추가하세요.
--     **`INSERT INTO products (name, price, productLine, ...) VALUES ('Vintage Train', 34.99, 'Trains', ...);`**

desc products;
select * from products  order by productCode desc;   
INSERT INTO products (    productCode,    productName,    productLine,    productScale,    productVendor,    productDescription,    quantityInStock,    buyPrice,    MSRP) 
VALUES (    '별슈퍼카1호',    '별나라 슈퍼카',    '부릉부릉부릉이',    '1:10',    'Min Lin Diecast',    'This replica features working kickstand, front suspension, gear-shift lever, foot-brake lever, and drive chain. It comes with its own stand, informative booklet, and authenticity certificate.',    7933,    48.8100000000,    95.70);


-- ### 중급
-- - (1) **`customers`** 테이블에 여러 고객을 한 번에 추가하세요.
--     **`INSERT INTO customers (name, address, ...) VALUES ('Bob Brown', '789 Oak St', ...), ('Sue White', '321 Pine St', ...);`**
desc customers;
select * from customers  order by customerNumber desc;   
INSERT INTO customers (customerNumber,customerName,    contactLastName,    contactFirstName,    phone,    addressLine1,    addressLine2,    city,    state,    postalCode,    country,    salesRepEmployeeNumber,    creditLimit) 
VALUES (    500,    '김대리',    '대리',    '김',    '123-456-7890',    '둥덩이로112',    'Suite 100',    '크라운',    '별나라',    '12345',    '문',    1501,    10000.00),
(    501,    '홍만나1',    '만나1',    '홍',    '123-456-7890',    '둥덩이로112',    'Suite 100',    '크라운',    '별나라',    '12345',    '문',    1501,    10000.00),
(    502,    '홍만나2',    '만나2',    '홍',    '123-456-7890',    '둥덩이로112',    'Suite 100',    '크라운',    '별나라',    '12345',    '문',    1501,    10000.00),
(    503,    '홍만나3',    '만나3',    '홍',    '123-456-7890',    '둥덩이로112',    'Suite 100',    '크라운',    '별나라',    '12345',    '문',    1501,    10000.00);


-- - (2) **`products`** 테이블에 여러 제품을 한 번에 추가하세요.
--     **`INSERT INTO products (name, price, productLine, ...) VALUES ('Model Ship', 22.99, 'Ships', ...), ('Model Plane', 18.99, 'Planes', ...);`**
desc products;
select * from products  order by productCode desc;   
INSERT INTO products (    productCode,    productName,    productLine,    productScale,    productVendor,    productDescription,    quantityInStock,    buyPrice,    MSRP) 
VALUES (    '별나라11',    '별나라 1호',    'Ships',    '1:10',    'Min Lin Diecast',    'This replica features working kickstand, front suspension, gear-shift lever, foot-brake lever, and drive chain. It comes with its own stand, informative booklet, and authenticity certificate.',    7933,    48.8100000000,    95.70),
(    '별나라21',    '별나라 2호',    'Ships',    '1:10',    'Min Lin Diecast',    'This replica features working kickstand, front suspension, gear-shift lever, foot-brake lever, and drive chain. It comes with its own stand, informative booklet, and authenticity certificate.',    7933,    48.8100000000,    95.70),
(    '별나라31',    '별나라 3호',    'Ships',    '1:10',    'Min Lin Diecast',    'This replica features working kickstand, front suspension, gear-shift lever, foot-brake lever, and drive chain. It comes with its own stand, informative booklet, and authenticity certificate.',    7933,    48.8100000000,    95.70),
(    '별나라41',    '별나라4 호',    'Ships',    '1:10',    'Min Lin Diecast',    'This replica features working kickstand, front suspension, gear-shift lever, foot-brake lever, and drive chain. It comes with its own stand, informative booklet, and authenticity certificate.',    7933,    48.8100000000,    95.70);


-- - (3) **`employees`** 테이블에 여러 직원을 한 번에 추가하세요.
--     **`INSERT INTO employees (firstName, lastName, ...) VALUES ('Gary', 'Martin', ...), ('Laura', 'Green', ...);`**
desc employees;
select * from employees  order by employeeNumber desc;   
INSERT INTO employees (    employeeNumber,    lastName,    firstName,    extension,    email,    officeCode,    reportsTo,    jobTitle) 
VALUES (    1706,    '오징어',    '1',    '1',    '1@오징어.com',    '1',    1088,    'Sales Rep'),
(    1707,    '오징어',    '2',    '2',    '2@오징어.com',    '1',    1088,    'Sales Rep'),
(    1708,    '오징어',    '3',    '3',    '3@오징어.com',    '1',    1088,    'Sales Rep');


-- - (4) **`orders`**와 **`orderdetails`**에 연결된 주문을 한 번에 추가하세요.
--     **`INSERT INTO orders (orderDate, customerID, ...) VALUES ('2023-01-02', 2, ...); INSERT INTO orderdetails (orderID, productID, quantityOrdered, priceEach) VALUES (2, 3, 1, 15.00), (2, 4, 2, 35.00);`**
desc orders;
desc orderdetails;
select * from orders  order by orderNumber desc;   
select * from orderdetails order by orderNumber desc;   
select * from customers order by customerNumber desc;
select * from products order by productCode desc;

INSERT INTO orders (orderNumber, orderDate, requiredDate, status, customerNumber) VALUES (10428, '2024-02-02', '2024-02-02', 'In Process', 503);
INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber) VALUES (10428, '별나라11', 20, 444.00, 3), (10428, '별나라21', 21, 111.00, 2);



-- - (5)**`payments`** 테이블에 여러 지불 정보를 한 번에 추가하세요.
--     **`INSERT INTO payments (customerID, amount, paymentDate) VALUES (2, 100.00, '2023-01-02'), (3, 150.00, '2023-01-03');`**
desc payments;
select * from payments order by customerNumber desc;
INSERT INTO payments (customerNumber, checkNumber, paymentDate, amount) 
VALUES (498, 'AB123456', '2023-01-02', 1500.00);



-- - (6) **`customers`** 테이블에 고객을 추가하고 바로 주문을 추가하세요.
--     **`INSERT INTO customers (name, address, ...) VALUES ('Tom Black', '987 Walnut St', ...); INSERT INTO orders (customerID, orderDate, ...) VALUES (LAST_INSERT_ID(), '2023-01-04', ...);`**
desc customers;
select * from customers order by customerNumber desc;

INSERT INTO customers (customerNumber,customerName,    contactLastName,    contactFirstName,    phone,    addressLine1,    addressLine2,    city,    state,    postalCode,    country,    salesRepEmployeeNumber,    creditLimit) 
VALUES (    504,    '오징어',    '징어',    '오',    '화성1011',    '둥덩이로1132',    'Suite 100',    '크라운',    '별나라',    '12345',    '문',    1501,    10000.00);
INSERT INTO orders (orderNumber, orderDate, requiredDate, status, customerNumber) VALUES (10429, '2024-02-02', '2024-02-02', 'In Process', 504);
INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber) VALUES (10429, '별나라11', 20, 444.00, 3), (10429, '별나라21', 21, 111.00, 2);


-- - (7) **`employees`** 테이블에 직원을 추가하고 바로 직급을 할당하세요.
--     **`INSERT INTO employees (firstName, lastName, ...) VALUES ('Nancy', 'Blue', ...); UPDATE employees SET jobTitle = 'Sales Rep' WHERE employeeNumber = LAST_INSERT_ID();`**
desc employees;
select * from employees order by employeeNumber desc;
INSERT INTO employees (    employeeNumber,    lastName,    firstName,    extension,    email,    officeCode,    reportsTo,    jobTitle) 
VALUES (    1709,    '화성장군',    '문',    '1',    '장군@화성.com',    '1',    1088,    'Sales Rep');
UPDATE employees SET jobTitle = '화성장군' WHERE employeeNumber = 1709;


-- - (8) **`products`** 테이블에 제품을 추가하고 바로 재고를 업데이트하세요.
--     **`INSERT INTO products (name, price, productLine, ...) VALUES ('RC Helicopter', 29.99, 'Helicopters', ...); UPDATE products SET quantityInStock = 30 WHERE productCode = LAST_INSERT_ID();`**
desc products;
select * from products order by productCode desc;

INSERT INTO products (    productCode,    productName,    productLine,    productScale,    productVendor,    productDescription,    quantityInStock,    buyPrice,    MSRP) 
VALUES (    '별슈퍼카4호',    '별나라 슈퍼카',    '부릉부릉부릉이',    '1:10',    '',    '',    7933,    48.8100000000,    95.70);
UPDATE products SET quantityInStock = 1 WHERE productCode = '별슈퍼카4호';




-- - (9) **`offices`** 테이블에 새 사무실을 추가하고 바로 직원을 할당하세요.
--     **`INSERT INTO offices (city, phone, ...) VALUES ('Los Angeles', '987-654-3210', ...); UPDATE employees SET officeCode = LAST_INSERT_ID() WHERE lastName = 'Blue';`**
desc offices;
select * from offices order by officeCode desc;
select * from employees order by employeeNumber desc;

INSERT INTO offices (    officeCode,    city,    phone,    addressLine1,    addressLine2,    state,    country,    postalCode,    territory) 
VALUES (    '111',    '화성',    '+82 010-3322-1234',    '웅덩이로1',    'Suite 600',    '화성',    'korea',    '94080',    '화성');
UPDATE employees SET officeCode = '111' WHERE employeeNumber = '1709';


-- - (10) **`productlines`** 테이블에 제품 라인을 추가하고 바로 여러 제품을 추가하세요.
--     **`INSERT INTO productlines (productLine, textDescription) VALUES ('Motorcycles', 'Various motorcycle models'); INSERT INTO products (name, price, productLine, ...) VALUES ('Harley Bike', 55.99, 'Motorcycles', ...), ('Yamaha Bike', 45.99, 'Motorcycles', ...);`**
desc productlines;
select * from productlines  order by productLine desc;   
select * from products  order by productLine desc;   

INSERT INTO productlines (productLine, textDescription, htmlDescription, image)
VALUES ('부릉부릉부릉이bc', '부릉이카b', NULL, NULL);
INSERT INTO products (    productCode,    productName,    productLine,    productScale,    productVendor,    productDescription,    quantityInStock,    buyPrice,    MSRP) 
VALUES (    '별나라111',    '별나라 1호',    '부릉부릉부릉이bc',    '1:10',    '',    ', informative booklet, and authenticity certificate.',    7933,    48.8100000000,    95.70),
(    '별나라221',    '별나라 2호',    '부릉부릉부릉이bc',    '1:10',    '',    '',    7933,    48.8100000000,    95.70),
(    '별나라331',    '별나라 3호',    '부릉부릉부릉이bc',    '1:10',    '',    'This replica features working kickstand, front suspension, gear-shift lever, foot-brake lever, and drive chain. It comes with its own stand, informative booklet, and authenticity certificate.',    7933,    48.8100000000,    95.70),
(    '별나라441',    '별나라4 호',    '부릉부릉부릉이bc',    '1:10',    '',    'This replica features working kickstand, front suspension, gear-shift lever, foot-brake lever, and drive chain. It comes with its own stand, informative booklet, and authenticity certificate.',    7933,    48.8100000000,    95.70);


-- ### 고급
-- - (1) **`customers`** 테이블에 새 고객을 추가하고 바로 주문을 추가하세요.
--     **`INSERT INTO customers (name, address, ...) VALUES ('Linda Grey', '654 Maple St', ...); INSERT INTO orders (customerID, orderDate, ...) VALUES (LAST_INSERT_ID(), '2023-01-05', ...); INSERT INTO orderdetails (orderID, productID, quantityOrdered, priceEach) VALUES (LAST_INSERT_ID(), 5, 2, 45.00);`**
desc customers;
select * from customers  order by customerNumber desc;   
select * from orders  order by orderNumber desc;   
INSERT INTO customers (customerNumber,customerName,    contactLastName,    contactFirstName,    phone,    addressLine1,    addressLine2,    city,    state,    postalCode,    country,    salesRepEmployeeNumber,    creditLimit) 
VALUES (    508,    '왜b자꾸사',    '대리',    '김',    '123-456-7890',    '둥덩이로112',    'Suite 100',    '크라운',    '별나라',    '12345',    '문',    1501,    10000.00);
INSERT INTO orders (orderNumber, orderDate, requiredDate, status, customerNumber) VALUES (10433, '2024-02-02', '2024-02-02', 'In Process', 508);
INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber) VALUES (10433, '별나라11', 20, 444.00, 3), (10433, '별나라21', 21, 111.00, 2);


-- - (2) **`employees`** 테이블에 새 직원을 추가하고 바로 그들의 매니저를 업데이트하세요.
--     **`INSERT INTO employees (firstName, lastName, ...) VALUES ('Rachel', 'Purple', ...); UPDATE employees SET reportsTo = (SELECT employeeNumber FROM employees WHERE lastName = 'Johnson') WHERE lastName = 'Purple';`**
desc employees;
select * from employees order by employeeNumber desc;
INSERT INTO employees (    employeeNumber,    lastName,    firstName,    extension,    email,    officeCode,    reportsTo,    jobTitle) 
VALUES (    1709,    '화성장군',    '문',    '1',    '장군@화성.com',    '1',    1088,    'Sales Rep');
UPDATE employees SET jobTitle = '화성장군' WHERE employeeNumber = 1709;


-- - (3) **`products`** 테이블에 새 제품을 추가하고 바로 그 제품에 대한 주문을 추가하세요.
--     **`INSERT INTO products (name, price, productLine, ...) VALUES ('Electric Train', 80.00, 'Trains', ...); INSERT INTO orders (orderDate, customerID, ...) VALUES ('2023-01-06', 2, ...); INSERT INTO orderdetails (orderID, productID, quantityOrdered, priceEach) VALUES (LAST_INSERT_ID(), LAST_INSERT_ID(), 1, 80.00);`**
INSERT INTO customers (customerNumber,customerName,    contactLastName,    contactFirstName,    phone,    addressLine1,    addressLine2,    city,    state,    postalCode,    country,    salesRepEmployeeNumber,    creditLimit) 
VALUES (    510,    '왜b자꾸사',    '대리',    '김',    '123-456-7890',    '둥덩이로112',    'Suite 100',    '크라운',    '별나라',    '12345',    '문',    1501,    10000.00);
INSERT INTO orders (orderNumber, orderDate, requiredDate, status, customerNumber) VALUES (10435, '2024-02-02', '2024-02-02', 'In Process', 510);
INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber) VALUES (10433, '별나라11', 20, 444.00, 3), (10435, '별나라21', 21, 111.00, 2);


-- - (4) **`orders`** 테이블에 새 주문을 추가하고 바로 지불 정보를 추가하세요.
--     **`INSERT INTO orders (orderDate, customerID, ...) VALUES ('2023-01-07', 3, ...); INSERT INTO payments (customerID, amount, paymentDate) VALUES (3, 200.00, '2023-01-07');`**
desc payments;
select * from payments order by customerNumber desc;


INSERT INTO orders (orderNumber, orderDate, requiredDate, status, customerNumber) VALUES (10437, '2024-02-02', '2024-02-02', 'In Process', 510);
INSERT INTO payments (customerNumber, checkNumber, paymentDate, amount) VALUES (510, 'AB123456', '2023-01-02', 1500.00);


-- - (5)**`orderdetails`** 테이블에 주문 상세 정보를 추가하고 바로 관련 제품의 재고를 감소시키세요.

INSERT INTO orders (orderNumber, orderDate, requiredDate, status, customerNumber) VALUES (10500, '2024-02-02', '2024-02-02', 'In Process', 510);
INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber) VALUES (10500, '별나라11', 20, 444.00, 3), (10500, '별나라21', 21, 111.00, 2);