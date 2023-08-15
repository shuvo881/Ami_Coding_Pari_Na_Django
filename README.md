# Project Name: ‘Ami Coding Pari Na’

## Project Description: This is a web application. It is made by the Django framework and the rest framework.
### features :
   1. User Authentication/Registration Page(app name: Authentication): 
  A user login and registration section. You can use whatever input fields you want (maintaining a standard)
   2. Khoj the search Page(app name: Khoj_the_search_Page): 
After login, users can access this page. Khoj the search: In this segment(page), there will be two input fields
Input Values: User can input comma separated integers
Search Value: User can input only one integer 
Output: Will print True if the search value is in the input values. Otherwise print False.
Sample ![image](https://github.com/shuvo881/Ami_Coding_Pari_Na_Django/assets/68312838/b441ffe7-7935-472a-b923-c864bd62041c)
Now, before showing the output, you have to store the input values in the database in sorted order(descending) along with the logged in user id and the input timestamp. That means, when the user press the button “Khoj”, the Input values (9, 1, 5, 7, 10, 11, 0) will be stored in the database as follows : 11, 10, 9, 7, 5, 1, 0
So the rough workflow for this section is as follows
Take the “Input Values”
Take the “Search Value”
Sort the “Input values” in descending order.
Store the sorted “Input Values” in the database.
Check if the “Search Value” is in the “Input Values”
Print the output
  3. API Endpoints(app name: api):
     In this section, there will be only one API endpoints.
Endpoint 1: Get All Input Values.
Parameters: start_datetime, end_datetime, user_id.
Returns: All the Input Values the user ever entered within start_datetime(inclusive) and end_datetime (inclusive).
Check the following response format.<img width="455" alt="Screenshot 2023-08-15 221441" src="https://github.com/shuvo881/Ami_Coding_Pari_Na_Django/assets/68312838/b50b5c06-588b-48e1-b2d1-5420f084af20">


