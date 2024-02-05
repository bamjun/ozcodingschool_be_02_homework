//use testmongodb;
//몽고db생성, use를 사용하면, 없을시 생성해줌.
//
//db;
//현재 db를 나타내줌.
//
//show dbs;
//서버안의 db리스트 보여줌

//db.dropDatabase();
//현재 db 삭제

//db.stats();
//현재 db의 상태를 통계적으로 표시

//db.createCollection("users", { capped: false });
//콜랙션생성

//show collections;
//콜랙션목록 조회

//db.users.renameCollection("customers");
//콜랙션 이름 변경

//db.customers.drop();
//콜랙션 삭제



//db.createCollection("users", { capped: false });

//// 단일 문서 삽입
//db.users.insertOne({ name: "Alice", age: 30, address: "123 Maple St" })
//
//// 여러 문서 삽입
db.users.insertMany([
    { name: "Bob1", age: 215, address: "456 Oak St1" },
    { name: "Charlie1", age: 315, address: "789 Pine St1" }
])


//MYsql
//-- 단일 레코드 삽입
//INSERT INTO users (name, age, address) VALUES ('Alice', 30, '123 Maple St');
//
//-- 여러 레코드 삽입
//INSERT INTO users (name, age, address) VALUES
//    ('Bob', 25, '456 Oak St'),
//    ('Charlie', 35, '789 Pine St');


//#read
// 모든 문서 조회
db.users.find()

// 특정 필드 조회
db.users.find({}, { name: 1, address: 1 })

// 조건에 맞는 문서 조회
db.users.find({ address: "789 Pine St" })
//mysql
//-- 모든 레코드 조회
//SELECT * FROM users;
//
//-- 특정 열 조회
//SELECT name, address FROM users;
//
//-- 조건에 맞는 레코드 조회
//SELECT * FROM users WHERE address = '789 Pine St';

db.users.find()
//###update
// 특정 문서 업데이트
db.users.updateOne({ name: "Alice" }, { $set: { age: 31 } })

// 여러 문서 업데이트
db.users.updateMany({ address: "789 Pine St" }, { $set: { address: "부산" } })
//mysql
//-- 특정 레코드 업데이트
//UPDATE users SET age = 31 WHERE name = 'Alice';
//
//-- 조건에 맞는 여러 레코드 업데이트
//UPDATE users SET address = '부산' WHERE address = '789 Pine St';

db.users.find()
//###delete
// 특정 문서 삭제
db.users.deleteOne({ name: "Alice" })

// 조건에 맞는 여러 문서 삭제
db.users.deleteMany({ address: "부산" })

//mysql
//-- 특정 레코드 삭제
//DELETE FROM users WHERE name = 'Alice';
//
//-- 조건에 맞는 여러 레코드 삭제
//DELETE FROM users WHERE address = '부산';



//### 연습문제
//
//### **초급 레벨**
//
//**(1) 생성**
//
//**`sports`** 컬렉션에 **`name: "Football"`**, **`players: 11`**인 문서를 삽입하세요.

use sports

db.sports.insertOne({ name: "Football", players: 11 })

db.sports.find()


//
//**(2) 읽기**
//
//**`products`** 컬렉션에서 **`price`**가 500보다 작거나 같은 모든 문서를 찾으세요.

db.products.find({ price: { $lte: 500 } })

//**`books`** 컬렉션에서 **`author`**가 "John Doe"인 모든 문서를 찾으세요.
db.books.find({ author: "John Doe" })
//    
//
//**(3) 업데이트**
//
//**`orders`** 컬렉션에서 **`status`**가 "Pending"인 모든 문서를 "Complete"로 변경하세요.
db.orders.updateMany({ status: "Pending" }, { $set: { status: "Complete" } })
//    
//
//**`movies`** 컬렉션에서 **`genre`**가 "comedy"인 모든 문서의 **`rating`**을 5로 변경하세요.
db.movies.updateMany({ genre: "comedy" }, { $set: { rating: 5 } })
//    
//
//**(4) 삭제**
//
//**`customers`** 컬렉션에서 **`age`**가 30 미만인 모든 문서를 삭제하세요.
db.customers.deleteMany({ age: { $lt: 30 } })





//
//### **중급 레벨**
//
//**생성**
//
//**`myCollection`** 컬렉션에 새로운 문서를 생성하세요. 문서는 **`name: "Gadget"`**, **`type: "Electronics"`**, **`price: 300`**, **`ratings: [4, 5, 5]`** 필드를 포함해야 합니다.
db.myCollection.insertOne({ name: "Gadget", type: "Electronics", price: 300, ratings: [4, 5, 5] })
//    
//
//**읽기**
//
//**`employees`** 컬렉션에서 **`department`**가 "Sales"이면서 **`age`**가 30 이상인 모든 문서를 찾으세요.
db.employees.find({ department: "Sales", age: { $gte: 30 } })
//    
//
//**`employees`** 컬렉션에서 **`salary`**가 50000 이상인 문서를 찾되, **`name`**과 **`title`** 필드만 표시하세요.
db.employees.find({ salary: { $gte: 50000 } }, { name: 1, title: 1 })
//    
//
//**업데이트**
//
//**`products`** 컬렉션에서 **`stock`** 필드가 없는 모든 문서에 **`stock: 10`**을 추가하세요.
db.products.updateMany({ stock: { $exists: false } }, { $set: { stock: 10 } })
//    
//
//**`vehicles`** 컬렉션에서 **`type`**이 "car"인 모든 문서에 **`wheels: 4`** 필드를 추가하세요.
db.vehicles.updateMany({ type: "car" }, { $set: { wheels: 4 } })

//
//**삭제**
//
//**`orders`** 컬렉션에서 **`orderDate`**가 2023년 1월 1일 이전인 모든 문서를 삭제하세요.
db.orders.deleteMany({ orderDate: { $lt: new Date('2023-01-01') } })
//    
//
//**`restaurants`** 컬렉션에서 **`rating`**이 3 미만인 모든 문서를 삭제하세요.
db.restaurants.deleteMany({ rating: { $lt: 3 } })
//    
//
//### **고급 레벨**
//
//**읽기**
//
//**`customers`** 컬렉션에서 **`age`**가 30 이상인 문서를 찾고, 결과를 **`name`**으로 오름차순 정렬하세요.
db.customers.find({ age: { $gte: 30 } }).sort({ name: 1 })
//    
//
//**`users`** 컬렉션에서 **`birthdate`**가 1990년 이전인 사용자의 평균 **`age`**를 계산하는 집계 쿼리를 작성하세요.
db.users.aggregate([{ $match: { birthdate: { $lt: new Date('1990-01-01') } } }, { $group: { _id: null, avgAge: { $avg: "$age" } } }])
//    
//
//**업데이트**
//
//**`employees`** 컬렉션에서 **`department`**가 "HR"인 모든 문서의 **`department`**를 "Human Resources"로, **`title`**을 "HR Manager"로 변경하세요.
db.employees.updateMany({ department: "HR" }, { $set: { department: "Human Resources", title: "HR Manager" } })
//    
//
//**`orders`** 컬렉션에서 **`delivered`**가 **`false`**인 모든 문서에 현재 날짜를 나타내는 **`deliveryDate`** 필드를 추가하세요.
db.orders.updateMany({ delivered: false }, { $set: { deliveryDate: new Date() } })


//
//**삭제**
//
//**`products`** 컬렉션에서 **`lastModified`** 필드가 30일 이상 된 모든 문서를 삭제하세요.
db.products.deleteMany({ lastModified: { $lt: new Date(new Date() - 30 * 24 * 60 * 60 * 1000) } })
//    
//
//**`products`** 컬렉션에서 **`stock`**이 0인 모든 문서를 삭제하세요.
db.products.deleteMany({ stock: 0 })

//
//### 연습문제
//
//- **`products`** 컬렉션에서 **`price`**가 100보다 큰 모든 문서를 찾으세요.
db.products.find({ price: { $gt: 100 } })


//- **`employees`** 컬렉션에서 **`age`**가 30보다 작거나 **`department`**가 "HR"인 모든 문서를 찾으세요.
db.employees.find({ $or: [{ age: { $lt: 30 } }, { department: "HR" }] })


//- **`orders`** 컬렉션에서 **`quantity`**가 5 이상 10 이하인 모든 문서를 찾으세요.
db.orders.find({ quantity: { $gte: 5, $lte: 10 } })


//- **`customers`** 컬렉션에서 **`city`**가 "Seoul"이 아닌 모든 문서를 찾으세요.
db.customers.find({ city: { $ne: "Seoul" } })


//- **`movies`** 컬렉션에서 **`rating`**이 8 이상이고, **`genre`**가 "comedy" 또는 "drama"인 모든 문서를 찾으세요.
db.movies.find({ rating: { $gte: 8 }, genre: { $in: ["comedy", "drama"] } })


//- **`books`** 컬렉션에서 **`author`**가 "John Doe"이고 **`publishedYear`**가 2000 이후인 모든 문서를 찾으세요.
db.books.find({ author: "John Doe", publishedYear: { $gt: 2000 } })


//- **`vehicles`** 컬렉션에서 **`type`**이 "car"가 아니고, **`price`**가 20000보다 큰 모든 문서를 찾으세요.
db.vehicles.find({ type: { $ne: "car" }, price: { $gt: 20000 } })


//- **`restaurants`** 컬렉션에서 **`rating`**이 5이고, **`cuisine`**이 "Italian" 또는 "French"가 아닌 모든 문서를 찾으세요.
db.restaurants.find({ rating: 5, cuisine: { $nin: ["Italian", "French"] } })


//- **`users`** 컬렉션에서 **`age`**가 30 이상이지만 **`city`**가 "New York"이 아닌 모든 문서를 찾으세요.
db.users.find({ age: { $gte: 30 }, city: { $ne: "New York" } })


//- **`flights`** 컬렉션에서 **`departure`**가 "London"이거나 **`arrival`**이 "Tokyo"인 모든 문서를 찾으세요.
db.flights.find({ $or: [{ departure: "London" }, { arrival: "Tokyo" }] })














