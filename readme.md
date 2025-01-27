## Project structure and API routes

<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  This project is part of the
  <a href="https://www.coursera.org/learn/apis">APIs</a> course offered by <a href="https://www.coursera.org/professional-certificates/meta-back-end-developer">Meta</a>
  on Coursera. It serves as the final project required to complete the course.
  The goal is to build an API from scratch that meets the specified tasks, demonstrating the knowledge and skills gained throughout the course.
  This course is also one of the nine requirements for earning the <b>Professional Certificate</b> in Meta Back-End Developer program.
</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  โปรเจคนี้เป็นส่วนหนึ่งของคอร์สเรียน
  <a href="https://www.coursera.org/learn/apis">APIs</a> ที่จัดโดย <a href="https://www.coursera.org/professional-certificates/meta-back-end-developer">Meta</a>
  บนแพลตฟอร์ม Coursera และเป็นโปรเจคชิ้นสุดท้ายที่ใช้เพื่อจบคอร์ส ในโปรเจคนี้ ผู้สอนจะไม่ให้ตัวอย่างโค้ดใดๆ โดยจะต้องเริ่มสร้าง API จากศูนย์และทำให้สำเร็จตาม task ที่มอบหมาย
  คอร์สนี้ยังเป็น 1 ใน 9 เงื่อนไขที่ต้องสำเร็จเพื่อได้รับประกาศนียบัตร <b>Professional Certificate</b> จากโปรแกรม Back-End Developer ของ Meta
</p>

<p>
  In this project, the APIs should allow end-users to perform the following tasks
</p>

1.	The admin can assign users to the manager group
2.	You can access the manager group with an admin token
3.	The admin can add menu items 
4.	The admin can add categories
5.	Managers can log in 
6.	Managers can update the item of the day
7.	Managers can assign users to the delivery crew
8.	Managers can assign orders to the delivery crew
9.	The delivery crew can access orders assigned to them
10.	The delivery crew can update an order as delivered
11.	Customers can register
12.	Customers can log in using their username and password and get access tokens
13.	Customers can browse all categories 
14.	Customers can browse all the menu items at once
15.	Customers can browse menu items by category
16.	Customers can paginate menu items
17.	Customers can sort menu items by price
18.	Customers can add menu items to the cart
19.	Customers can access previously added items in the cart
20.	Customers can place orders
21.	Customers can browse their own orders

### User registration and token generation endpoints

You can use Djoser in your project to automatically create the following endpoints and functionalities for you.

| Endpoint                   | Role                                      | Method     | Purpose                                                                     |
| -------------------------- | ----------------------------------------- | ---------- | --------------------------------------------------------------------------- |
| **`/api/users`**           | No role required                          | **`POST`** | Creates a new user with name, email and password                            |
| **`/api/users/users/me/`** | Anyone with a valid user token            | **`GET`**  | Displays only the current user                                              |
| **`/token/login/`**        | Anyone with a valid username and password | **`POST`** | Generates access tokens that can be used in other API calls in this project |

##  Menu-items endpoints

| Endpoint                         | Role                    | Method                                           | Purpose                                                             |
| -------------------------------- | ----------------------- | ------------------------------------------------ | ------------------------------------------------------------------- |
| **`/api/menu-items`**            | Customer, delivery crew | **`GET`**                                        | Lists all menu items. Return a **`200 – Ok`** HTTP status code      |
| **`/api/menu-items`**            | Customer, delivery crew | **`POST`**, **`PUT`**, **`PATCH`**, **`DELETE`** | Denies access and returns **`403 – Unauthorized`** HTTP status code |
| **`/api/menu-items/{menuItem}`** | Customer, delivery crew | **`GET`**                                        | Lists single menu item                                              |
| **`/api/menu-items/{menuItem}`** | Customer, delivery crew | **`POST`**, **`PUT`**, **`PATCH`**, **`DELETE`** | Returns **`403 - Unauthorized`**                                    |
| **`/api/menu-items`**            | Manager                 | **`GET`**                                        | Lists all menu items                                                |
| **`/api/menu-items`**            | Manager                 | **`POST`**                                       | Creates a new menu item and returns **`201 - Created`**             |
| **`/api/menu-items/{menuItem}`** | Manager                 | **`GET`**                                        | Lists single menu item                                              |
| **`/api/menu-items/{menuItem}`** | Manager                 | **`PUT`**, **`PATCH`**                           | Updates single menu item                                            |
| **`/api/menu-items/{menuItem}`** | Manager                 | **`DELETE`**                                     | Deletes menu item                                                   |

## User group management endpoints

| Endpoint                                       | Role    | Method       | Purpose                                                                                                                                                            |
| ---------------------------------------------- | ------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`/api/groups/manager/users`**                | Manager | **`GET`**    | Returns all managers                                                                                                                                               |
| **`/api/groups/manager/users`**                | Manager | **`POST`**   | Assigns the user in the payload to the manager group and returns **`201-Created`**                                                                                 |
| **`/api/groups/manager/users/{userId}`**       | Manager | **`DELETE`** | Removes this particular user from the manager group and returns **`200 – Success`** if everything is okay. If the user is not found, returns **`404 – Not found`** |
| **`/api/groups/delivery-crew/users`**          | Manager | **`GET`**    | Returns all delivery crew                                                                                                                                          |
| **`/api/groups/delivery-crew/users`**          | Manager | **`POST`**   | Assigns the user in the payload to delivery crew group and returns **`201-Created`** HTTP                                                                          |
| **`/api/groups/delivery-crew/users/{userId}`** | Manager | **`DELETE`** | Removes this user from the manager group and returns **`200 – Success`** if everything is okay. If the user is not found, returns  **`404 – Not found`**           |

## Cart management endpoints

| Endpoint                   | Role     | Method       | Purpose                                                                                         |
| -------------------------- | -------- | ------------ | ----------------------------------------------------------------------------------------------- |
| **`/api/cart/menu-items`** | Customer | **`GET`**    | Returns current items in the cart for the current user token                                    |
| **`/api/cart/menu-items`** | Customer | **`POST`**   | Adds the menu item to the cart. Sets the authenticated user as the user id for these cart items |
| **`/api/cart/menu-items`** | Customer | **`DELETE`** | Deletes all menu items created by the current user token                                        |

## Order management endpoints

| Endpoint                    | Role          | Method                 | Purpose                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------- | ------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`/api/orders`**           | Customer      | **`GET`**              | Returns all orders with order items created by this user                                                                                                                                                                                                                                                                                                                  |
| **`/api/orders`**           | Customer      | **`POST`**             | Creates a new order item for the current user. Gets current cart items from the cart endpoints and adds those items to the order items table. Then deletes all items from the cart for this user.                                                                                                                                                                         |
| **`/api/orders/{orderId}`** | Customer      | **`GET`**              | Returns all items for this order id. If the order ID doesn’t belong to the current user, it displays an appropriate HTTP error status code.                                                                                                                                                                                                                               |
| **`/api/orders`**           | Manager       | **`GET`**              | Returns all orders with order items by all users                                                                                                                                                                                                                                                                                                                          |
| **`/api/orders/{orderId}`** | Customer      | **`PUT`**, **`PATCH`** | Updates the order. A manager can use this endpoint to set a delivery crew to this order, and also update the order status to 0 or 1. <br>If a delivery crew is assigned to this order and the **`status = 0`**, it means the order is out for delivery. <br>If a delivery crew is assigned to this order and the **`status = 1`**, it means the order has been delivered. |
| **`/api/orders/{orderId}`** | Manager       | **`DELETE`**           | Deletes this order                                                                                                                                                                                                                                                                                                                                                        |
| **`/api/orders`**           | Delivery crew | **`GET`**              | Returns all orders with order items assigned to the delivery crew                                                                                                                                                                                                                                                                                                         |
| **`/api/orders/{orderId}`** | Delivery crew | **`PATCH`**            | A delivery crew can use this endpoint to update the order status to 0 or 1. The delivery crew will not be able to update anything else in this order.                                                                                                                                                                                                                     |
