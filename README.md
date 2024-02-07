# Truth in Tech
The Website
https://truth-in-tech.gitlab.io/truth-in-tech/

The Team
Adedeji "Toon" Adetunji - Software Developer
Matt Archbold - Software Developer
Cory Egan - Software Developer
Zach Walkowiak - Software Developer
![alt text](<docs/Truth In Tech Logo.png>)

## What is Truth in Tech?

"Truth in Tech" is a platform dedicated to providing unbiased and informative reviews about technology companies.  This helps our users to make informed decisions about their career choices and work environments.  This website is intended for anyone who is currently in or interested in breaking into the Technology career field.

## Project Initialization

1. In your terminal make sure you are in the directory you want to clone the project into.
2. Clone the repository typing:
      git clone https://gitlab.com/truth-in-tech/truth-in-tech.git
3. Switch into the your project directory by typing cd truth-in-tech
4. Run docker volume create truth-in-tech-data
5. Run docker compose build
6. Run docker compose up

Now you should see 3 containers up and running locally in your Docker Desktop.
7. To view the backend functionality go to http://localhost:8000/docs
8. To view the frontend functionality go to http://localhost:3000

# Design

## Functionality through React Routes

# Home Page http://localhost:3000
  - Here you can see our top ten companies reviewed.  A carousel of excellent reviews.  Also a button to create your own review.
  ![alt text](image.png)
# Login/Logout http://localhost:3000
  - Through our Navigation Bar you can log in and out of an account.

# Create Account http://localhost:3000/accounts/create
  - Here you can create an account with a user name, first name, last name, email, and password.  This will automatically give you an Avatar picture as well.

# Account Page http://localhost:3000/accounts/update
  - Here you can edit your account page.
  ![alt text](image-2.png)

# Create a Company http://localhost:3000/Comanies/create
  - On this page you can create a Company if you have an account.
  ![alt text](image-4.png)

# Create a Review http://localhost:3000/reviews/create
- We built a page where you can Anonymously post a review.  You can only post a review when you have an account.
  ![alt text](image-5.png)

# Company List Page http://localhost:3000/Companies/list
- Functionality in this page shows all of our companies with their logos and has a button in order to write a review for a specific company.  If you click on the company name it will take you to that company's page.
![alt text](image-6.png)

# Company Page http://localhost:3000/reviews/id
- Here we can see all the reviews for one company.  If there are no reviews for a company you will get a sad face.
![alt text](image-7.png)

# Check out a Review http://localhost:3000/review/id
- We built this page to show one specific review for a company.
![alt text](image-9.png)


### FastAPI Endpoints
Here are all of the FastAPI Endpoints for Truth in Tech when a 200 OK status code is reached.  This will be the Response body.

##### Log In

<details>
<summary markdown="span">GET /token - Get Token</summary>
```
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJiNDM5MDA1Mi03YmRjLTRjZjgtYjYxMy0yZWIzY2RhNDczMjUiLCJleHAiOjE3MDcyNjcyNTAsInN1YiI6IlRydXRoSW5UZWNoIiwiYWNjb3VudCI6eyJpZCI6MSwidXNlcm5hbWUiOiJUcnV0aEluVGVjaCIsImZpcnN0X25hbWUiOiJKb2huIiwibGFzdF9uYW1lIjoiRG9lIn19.sOVkWcHazYSqyj1lJsYoMWIlzVJ-c_lQPuKKooHEqC4",
  "token_type": "Bearer",
  "account": {
    "id": 1,
    "username": "TruthInTech",
    "first_name": "John",
    "last_name": "Doe"
  }
}
```
</details>

<details>
<summary markdown="span">POST /token - Login</summary>
```
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI2YjE0ZDYwNy0xNGM5LTQwNTQtYTMxNC0wMDk3MWQ2NzY1ZWEiLCJleHAiOjE3MDcyNjg4MTMsInN1YiI6IlRydXRoSW5UZWNoIiwiYWNjb3VudCI6eyJpZCI6MSwidXNlcm5hbWUiOiJUcnV0aEluVGVjaCIsImZpcnN0X25hbWUiOiJKb2huIiwibGFzdF9uYW1lIjoiRG9lIn19.XNsTzvb40GxVS8Yi7JMY4GysRA1vRC2n0IbrAz7IDJM",
  "token_type": "Bearer"
}
```
</details>

<details>
<summary markdown="span">DELETE /token - Logout</summary>
```
{
  true
}
```
</details>

##### Accounts
<details>
<summary markdown="span">GET/accounts - Get Account</summary>
```
{
  "id": 1,
  "username": "TruthinTech",
  "first_name": "John",
  "last_name": "Doe",
  "email": "johndoe@gmail.com"
}
```
</details>

<details>
<summary markdown="span">PUT/accounts - Update Account</summary>
```
{
  "id": 1,
  "username": "John_Doe",
  "first_name": "John",
  "last_name": "Doe",
  "email": "johndoe@gmail.com"
}
```
</details>

<details>
<summary markdown="span">DELETE/accounts - Delete Account</summary>
```
{
  true
}
```
</details>

<details>
<summary markdown="span">POST/accounts - Create Account</summary>
```
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIwYmM2NzI1YS05MWRmLTQ1NTMtOTQ3ZS1kMWJhMWFjOTYwNmQiLCJleHAiOjE3MDcyNjkyMjksInN1YiI6IlRydXRoIiwiYWNjb3VudCI6eyJpZCI6MjAsInVzZXJuYW1lIjoiVHJ1dGgiLCJmaXJzdF9uYW1lIjoiSm9obiIsImxhc3RfbmFtZSI6IkRvZSJ9fQ.CzVvSVwx8dCU8OYr36YjO4rIT-FTCP68DFfnKPLahFQ",
  "token_type": "Bearer",
  "account": {
    "id": 1,
    "username": "TruthinTech",
    "first_name": "John",
    "last_name": "Doe"
  }
}
```
</details>

##### Reviews
<details>
<summary markdown="span">POST/reviews - Create Review</summary>
```
{
  "id": 1,
  "anonymous": false,
  "salary": 0,
  "job_title": "student",
  "location": "remote",
  "body": "Galvanize helps prepare you for getting a software engineer job through rigorous assessments and projects. Overall would highly recommend becoming a student at Galvanize.",
  "account_id": 1,
  "company_id": 1,
  "date_created": "2024-02-07"
}
```
</details>

<details>
<summary markdown="span">GET/reviews{review_id} - Get One Review</summary>
```
{
  "id": 1,
  "anonymous": false,
  "salary": 0,
  "job_title": "Student",
  "location": "remote",
  "body": "Galvanize helps prepare you for getting a software engineer job through rigorous assessments and projects. Overall would highly recommend becoming a student at Galvanize.",
  "account_id": 1,
  "company_id": 1,
  "date_created": "2024-02-07",
  "company_name": "Galvanize",
  "company_logo": "https://www.galvanize.com/wp-content/uploads/2022/12/Screen-Shot-2022-12-13-at-12.52.26-PM.png",
  "username": "TruthInTech",
  "first_name": "John",
  "last_name": "Doe"
}
```
</details>

<details>
<summary markdown="span">PUT/reviews{review_id} - Edit Review</summary>
```
{
  "anonymous": false,
  "salary": 70000,
  "job_title": "Software Engineer",
  "location": "Remote",
  "body": "After bootcamp I got hired to work remotely as a Software Engineer!"
}
```
</details>

<details>
<summary markdown="span">DELETE/reviews/{review_id} - Delete a Review</summary>
```
{
  true
}
```
</details>

<details>
<summary markdown="span">GET/reviews/companies/{company_id} - Get all reviews from one company</summary>
```
[
  {
    "id": 1,
    "anonymous": false,
    "salary": 7000,
    "job_title": "Software Engineer",
    "location": "Remote",
    "body": "After bootcamp I got hired to work remotely as a Software Engineer!",
    "account_id": 1,
    "company_id": 1,
    "date_created": "2024-02-07",
    "company_name": "Galvanize",
    "company_logo": "https://www.galvanize.com/wp-content/uploads/2022/12/Screen-Shot-2022-12-13-at-12.52.26-PM.png",
    "username": "TruthInTech",
    "first_name": "John",
    "last_name": "Doe"
  }
]
```
</details>

<details>
<summary markdown="span">GET/reviews/top10/ - Get Top 10 Reviews</summary>
```
This has are 10 hardcoded reviews for our carousel.
```
</details>

##### Companies
<details>
<summary markdown="span">GET/reviews/top10 - Get Top 10 Reviews based on how many reviews they have.</summary>
```
[
  {
    "id": 8,
    "company_name": "Samsung Electronics",
    "company_logo": "",
    "number_of_reviews": 10
  },
  {
    "id": 4,
    "company_name": "Amazon",
    "company_logo": "",
    "number_of_reviews": 10
  },
  {
    "id": 6,
    "company_name": "Tencent",
    "company_logo": "",
    "number_of_reviews": 9
  },
  {
    "id": 1,
    "company_name": "Google",
    "company_logo": "",
    "number_of_reviews": 9
  },
  {
    "id": 7,
    "company_name": "Tesla",
    "company_logo": "",
    "number_of_reviews": 6
  },
  {
    "id": 2,
    "company_name": "Apple",
    "company_logo": "",
    "number_of_reviews": 6
  },
  {
    "id": 10,
    "company_name": "IBM",
    "company_logo": "",
    "number_of_reviews": 2
  },
  {
    "id": 17,
    "company_name": "Sony",
    "company_logo": "",
    "number_of_reviews": 2
  },
  {
    "id": 11,
    "company_name": "Oracle",
    "company_logo": "",
    "number_of_reviews": 2
  },
  {
    "id": 15,
    "company_name": "Salesforce",
    "company_logo": "",
    "number_of_reviews": 2
  }
]
```
</details>

<details>
<summary markdown="span">GET/companies/{company_id} - Get One Company</summary>
```
{
  "id": 1,
  "company_name": "Galvanize",
  "company_logo": "https://www.galvanize.com/wp-content/uploads/2022/12/Screen-Shot-2022-12-13-at-12.52.26-PM.png"
}
```
</details>

<details>
<summary markdown="span">DELETE/companies/{company_id} - Delete Company</summary>
```
{
  true
}
```
</details>

<details>
<summary markdown="span">GET/companies - Get Companies</summary>
```
{
  "companies": [
    {
      "id": 1,
      "company_name": "Galvanize",
      "company_logo": "https://www.galvanize.com/wp-content/uploads/2022/12/Screen-Shot-2022-12-13-at-12.52.26-PM.png"
    },
    {
      "id": 2,
      "company_name": "Adobe Inc.",
      "company_logo": "https://1000logos.net/wp-content/uploads/2021/04/Adobe-logo.png"
    }
  ]
}
```
</details>

<details>
<summary markdown="span">POST/companies - Create Company</summary>
```
{
    "id": 1,
    "company_name": "Galvanize",
    "company_logo": "https://www.galvanize.com/wp-content/uploads/2022/12/Screen-Shot-2022-12-13-at-12.52.26-PM.png"
}
```
</details>

<details>
<summary markdown="span">PUT/companies/update/{company_id} - Update Company</summary>
```
{
    "id": 1,
    "company_name": "Hack Reactor",
    "company_logo": "https://www.galvanize.com/wp-content/uploads/2022/12/Screen-Shot-2022-12-13-at-12.52.26-PM.png"
}
```
</details>
