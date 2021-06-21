# Djongo-api-endpoints
djongo (django+mongoDB) basic API endpoints


Documentation
Himanshu Yadav


Starting the project
API endpoint documentation

Starting the Project
1.	Download the .zip or clone the repository
2.	Use pipenv shell command to make virtual environment.
 ![image](https://user-images.githubusercontent.com/54714942/122696311-706fca80-d260-11eb-940d-2a9192fadb9a.png)

3.	Use pip install –r Requirements.txt in the directory to install the required libraries.
4.	Use manage.py runserver command in the same directory as manage.py file.
 ![image](https://user-images.githubusercontent.com/54714942/122696353-7fef1380-d260-11eb-8e53-4203fea655e0.png)





## API Endpoints’ documentation
 ![image](https://user-images.githubusercontent.com/54714942/122696384-9006f300-d260-11eb-924a-2eb6cf73bf58.png)

1.	View information of Pizzas:
  ![image](https://user-images.githubusercontent.com/54714942/122696400-96956a80-d260-11eb-8264-c73345dfc0f6.png)
![image](https://user-images.githubusercontent.com/54714942/122696407-99905b00-d260-11eb-8fa8-b2a404042378.png)

 
Description:
It takes all the information of Pizzas in the database and returns it as response_dict dictionary.
Input : takes no input
Output : List of all the Pizzas
 ![image](https://user-images.githubusercontent.com/54714942/122696417-9eeda580-d260-11eb-9808-18ce241ee427.png)

2.	Create Pizza
 ![image](https://user-images.githubusercontent.com/54714942/122696426-a2812c80-d260-11eb-95fa-2f241ba9fb5d.png)

It takes value for input for a pizza and creates object for it in database, if type is not one of the two specified, it will not make the entry in DB.
Input data: 
		 ![image](https://user-images.githubusercontent.com/54714942/122696435-a745e080-d260-11eb-92b9-f931cb50ca04.png)


Output  and Result: 
				 ![image](https://user-images.githubusercontent.com/54714942/122696442-ab71fe00-d260-11eb-9e0e-37baf36b0254.png)

If TYPE mentioned wrong, result is failure
					 ![image](https://user-images.githubusercontent.com/54714942/122696452-b2007580-d260-11eb-89fc-d2634ebacb93.png)
![image](https://user-images.githubusercontent.com/54714942/122696463-b9278380-d260-11eb-94ed-4ee69f58df63.png)







3.	Edit or Delete Pizza
 ![image](https://user-images.githubusercontent.com/54714942/122696471-bdec3780-d260-11eb-90a3-1f8ee3a14caf.png)

It takes the value of primary key to identify the record to be edited or deleted, and then it updates or deletes the record as per new info provided. Process input determines the process to be performed.
 ![image](https://user-images.githubusercontent.com/54714942/122696477-c3498200-d260-11eb-92e4-fbcac464f9d3.png)

Input (edit) :
 ![image](https://user-images.githubusercontent.com/54714942/122696481-c80e3600-d260-11eb-9edb-6b8191b23e01.png)

OUTPUT:
Before:
  ![image](https://user-images.githubusercontent.com/54714942/122696486-cba1bd00-d260-11eb-96e0-9d30e4b03e4f.png)

After:
 ![image](https://user-images.githubusercontent.com/54714942/122696494-ce9cad80-d260-11eb-8d19-743768ddf2fc.png)


4.	Use manage.py runserver command in the same directory as manage.py file.
![image](https://user-images.githubusercontent.com/54714942/122696503-d5c3bb80-d260-11eb-8d96-e212b8a4e4aa.png)


Input (delete):
 

Output:
Before:
 
After:
 







5.	Filter:  
This takes no input and traverses through all entries and creates classification and filtering and returns a dictionary with three entities:
					Filtered by Type
					Filtered by Size
					Filtered by Toppings


Output:
{
    "bytype": {
        "square": {
            "pizSize": [
                "medium"
            ],
            "pTops": [
                "nuts,sauce,"
            ]
        }
    },
    "bysize": {
        "too small": {
            "pizType": [
                "square"
            ],
            "pTops": [
                "nuts,sauce,"
            ]
        },
        "medium": {
            "pizType": [
                "square"
            ],
            "pTops": [
                "nuts,sauce,"
            ]
        }
    },
    "bytops": {
        "nuts,sauce,": {
            "pizSize": [
                "medium"
            ],
            "pizType": [
                "square"
            ]
        }
    }
}

