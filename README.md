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

> - http://localhost:8000/categories/\<id>
>
>> Available request methods: **[GET]**

***

### Running application with Docker:

1. Make sure nothing is running on port 8000
2. Navigate in your terminal to the project's root directory
3. Rut the following commands:

        docker-compose run web python manage.py migrate
4. Start the docker container:

        docker-compose up
        
5. Done! Navigate in your browser to the links indicated above and 
test the endpoints. :tada: :fireworks:
        
***

### Running application locally without Docker: