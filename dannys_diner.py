import pandas as pd

#create dictionary variables to read into dataframes
sales_data = {
    'customer_id':('A','A','A','A','A','A','B','B','B','B','B','B','C','C','C'),
    'order_date':('2021-01-01','2021-01-01','2021-01-07','2021-01-10','2021-01-11','2021-01-11',
                 '2021-01-01','2021-01-02','2021-01-04','2021-01-11','2021-01-16','2021-02-01',
                 '2021-01-01','2021-01-01','2021-01-07'),
    'product_id':(1,2,2,3,3,3,2,2,1,1,3,3,3,3,3)
}

menu_data = {
    'product_id':(1,2,3),
    'product_name':('sushi','curry','ramen'),
    'price': (10,15,12)
}

member_data = {
    'customer_id':('A','B'),
    'join_date':('2021-01-07', '2021-01-09')
}

#read data into dataframes
sales_df = pd.DataFrame(sales_data)
menu_df = pd.DataFrame(menu_data)
member_df = pd.DataFrame(member_data)

#change strings into date format
sales_df['order_date'] = pd.to_datetime(sales_df['order_date'])
member_df['join_date'] = pd.to_datetime(member_df['join_date'])


''' --------------------
   Case Study Questions
   --------------------

-- 1. What is the total amount each customer spent at the restaurant?
-- 2. How many days has each customer visited the restaurant?
-- 3. What was the first item from the menu purchased by each customer?
-- 4. What is the most purchased item on the menu and how many times was it purchased by all customers?
-- 5. Which item was the most popular for each customer?
-- 6. Which item was purchased first by the customer after they became a member?
-- 7. Which item was purchased just before the customer became a member?
-- 8. What is the total items and amount spent for each member before they became a member?
-- 9.  If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?
-- 10. In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi - how many points do customer A and B have at the end of January?
'''
