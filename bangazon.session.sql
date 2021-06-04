SELECT c.id,
    c.phone_number,
    c.address,
    c.user_id,
    f.customer_id,
    f.seller_id,
    u.username,
    u.first_name || ' ' || u.last_name AS full_name,
    u.email,
    a.username AS seller_user_name,
    a.first_name || ' ' || a.last_name AS seller_full_name
FROM bangazonapi_favorite f
    JOIN bangazonapi_customer c ON f.customer_id = c.id
    JOIN bangazonapi_customer cu ON f.seller_id = cu.id
    JOIN auth_user u ON cu.user_id = u.id
    JOIN auth_user a ON c.user_id = a.id;
SELECT c.id,
    c.phone_number,
    c.address,
    c.user_id,
    o.id,
    o.customer_id,
    o.created_date,
    a.email,
    a.username AS customer_name,
    a.first_name || ' ' || a.last_name AS customer_full_name
FROM bangazonapi_order o
    JOIN bangazonapi_customer c ON o.customer_id = c.id
    JOIN auth_user a ON c.user_id = a.id;