# Admiral Markets Test Assignment (Categories API)

## Test assignment: [link](https://drive.google.com/file/d/1HQlpS5UehAvrv5Ebn83c1vYF8jwL4oQo/view?usp=sharing)

>  Author: Deniss Astasitsev
>
>  Email: <astasitsev@gmail.com>

***

### Available endpoints:

> - http://localhost:8000/categories
>
>> Available request methods: **[POST]**

> - http://localhost:8000/categories/"id"
>
>> Available request methods: **[GET]**

***

### Running application with Docker:

1. Make sure nothing is running on port 8000
2. Navigate in your terminal to the project's root directory
3. Run the following command:

        docker-compose run web python manage.py migrate
4. Start the docker container:

        docker-compose up
        
5. Done! Navigate in your browser to the links indicated above and 
test the endpoints. :tada:
        
***

### Running application locally without Docker:

1. Clone this repository
2. Create virtual environment. Example:

       python3 -m venv ./venv

3. Activate virtual environment. Example:

        source ./venv/bin/activate
        
4. Install all required dependencies. Example:

        pip install -r requirements.txt
        
5. Apply all required db migrations:

        python3 manage.py migrate
        
6. Start your local server:

        python3 manage.py runserver
        
7. Done. Go to your browser and test the endpoints. :fireworks:

***