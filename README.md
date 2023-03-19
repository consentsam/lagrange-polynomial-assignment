# Lagrange Polynomial Assignment

Given a set of points find the **Lagrange Polynomial** that interpolates those points in base field with prime number **17**. 

## Steps

* Complete the `calculate_lagrange_polynomial` function. Given a list of points, each point of form [x, y], return the lagrange polynomial that interpolates the given points in base field with prime number **17**
* The function should return the coefficients of lagrange polynomial. The coefficient of the lowest power of x should be the first element of list
* Example

  Given points = [[1, 3], [4, 4], [16, 5], [13, 9]], the returned value calculated on base field of 17 should be list - [1, 13, 3, 3]

## Evaluation

-   Clone this repo

    ```
    git clone CLONE_URL
    ```
    
-   Create a new branch with your name. You can use the following command

    ```
    git checkout -b my-name
    ```

-   Make changes to the [main.py](main.py) file

-   Run the [main.py](main.py) file. This is required to populate the [solution.csv](solution.csv) file 
    ```
    python3 main.py
    ```

-   Create a pull request from your branch to the main branch of the repo to run the github workflow
