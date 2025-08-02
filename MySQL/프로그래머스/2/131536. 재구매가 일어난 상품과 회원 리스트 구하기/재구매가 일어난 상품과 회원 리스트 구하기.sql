-- user_id, prod_id 같은 row 갯수 2개 이상, id 오름차순, prod 내림차순 정렬
SELECT os.USER_ID, os.PRODUCT_ID
FROM ONLINE_SALE AS os
GROUP BY os.USER_ID, os.PRODUCT_ID
HAVING COUNT(*) >= 2
ORDER BY os.USER_ID ASC, os.PRODUCT_ID DESC;
