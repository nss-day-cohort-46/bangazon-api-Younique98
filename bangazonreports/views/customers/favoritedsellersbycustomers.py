"""Module for generating games by user report"""
import sqlite3
from django.shortcuts import render
from bangazonapi.models import Customer
from bangazonreports.views import Connection


def favoritesellersbycustomers_list(request):
    """Function to build an HTML report of favorited sellers by customers"""
    if request.method == 'GET':
        # Connect to project database
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # Query for all customers, with favorited sellers
            db_cursor.execute("""
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
            
            """)

            dataset = db_cursor.fetchall()

            favorites_by_customer = {}

            for row in dataset:
                # Create a favorite seller instance and set its properties
                customer = Customer()
                customer.id = row['id']
                customer.phone_number = row['phone_number']
                customer.address = row['address']
                customer.user_id = row['user_id']
                customer.customer_id = row['customer_id']
                customer.seller_id = row['seller_id']
                customer.username = row['username']
                customer.full_name = row['full_name']
                customer.email = row['email']
                customer.seller_user_name = row['seller_user_name']
                customer.seller_full_name = row['seller_full_name']

                # Store the customer's id
                uid = row['customer_id']

                # if the customer's id is already a key in the dict.
                if uid in favorites_by_customer:

                    # Add the current customer to the `customers` list
                    favorites_by_customer[uid]['sellers'].append(customer)

                else:
                    # Otherwise, create the key and dict value
                    favorites_by_customer[uid] = {}
                    favorites_by_customer[uid]['id'] = uid
                    favorites_by_customer[uid]['full_name'] = row['full_name']
                    favorites_by_customer[uid]['sellers'] = [customer]

        # Get only the values from the dictionary and create a list from them
        list_of_favorite_sellers_by_customer = favorites_by_customer.values()

        # Specify the Django template and provide data context
        template = 'list_with_fav_sellers.html'
        context = {
            'customer_fav_list': list_of_favorite_sellers_by_customer
        }

        return render(request, template, context)
