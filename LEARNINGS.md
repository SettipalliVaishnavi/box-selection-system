# What I learned

> TEMPLATE: write this yourself, in your own words. Do not use AI for it.
# What I Learned

Building this Box Selection System was a good learning experience for me. I learned many things while developing the project, especially how to solve real development problems, debug errors, improve code quality, and test an application.

## 1. Technical Things I Learned

- I learned how to structure a Django project properly and organize applications, models, views, templates, static files, and URLs.
- I understood how to create REST API endpoints and handle JSON requests and responses.
- I learned how to work with Django models and database migrations.
- I improved my understanding of Python functions, conditions, exception handling, and modular programming.
- I learned how box selection works based on dimensions, volume, weight, and cost.
- I understood why checking only the total volume is not enough to determine whether items physically fit inside a box.
- I learned about 3D packing, item rotation, boundary checking, and overlapping objects.
- I learned how to connect the frontend with the Django backend using JavaScript.
- I understood the importance of input validation and handling different HTTP status codes.

## 2. Challenges I Faced and How I Solved Them

During development, I faced several errors and configuration issues.

- **Installation issue:** Windows blocked `pip.exe` because of an Application Control policy. I solved this by using `python -m pip install`.
- **Project folder issue:** Initially, I was running commands from the wrong directory and received a `requirements.txt not found` error. I checked the folder structure and moved into the correct project directory.
- **404 error:** Initially, the application did not have a home page at the root URL. I added a web page at `/` instead of relying only on the API and admin pages.
- **Missing order data:** I received an "Order not found: ORD-1001" error because the sample data was not loaded. I ran migrations and the seed data command to create the required records.
- **Frontend changes:** When some page changes were not visible, I checked whether the files were saved and refreshed the browser using Ctrl + F5.
- **Terminal confusion:** I learned that the Django development server occupies its terminal, so I used another PowerShell terminal for API commands and other operations.
- **Test case issue:** I found that one geometry test was not checking the intended situation. I corrected it using two 6 cm cubes inside a 10 × 10 × 10 cm box.
- **Security improvement:** I changed the hardcoded secret key and DEBUG setting to environment-based configuration.
- **Performance improvement:** I added a maximum limit of 100 items to avoid unnecessarily slow packing operations.
- **Output formatting:** I improved the volume formatting to display two decimal places instead of unnecessary decimal digits.
- **Project organization:** I separated CSS and JavaScript from HTML and organized the test cases into separate files.
- **Packaging issue:** I corrected the nested folder problem and removed unnecessary files from the project.

## 3. What I Improved

I did not stop after getting the application running. I also worked on improving its quality.

- Improved the packing algorithm to check actual item arrangements instead of relying only on volume.
- Added support for item rotation to find valid box arrangements.
- Improved box selection to choose the cheapest box that physically fits all items.
- Added deterministic tie-breaking rules when multiple boxes have the same cost.
- Added validation for invalid quantities, empty orders, unknown products, and excessive item counts.
- Improved API error responses and output formatting.
- Added a proper frontend page for interacting with the application.
- Improved code organization by separating business logic, API functionality, frontend files, and tests.

## 4. What I Learned from Testing

Testing was one of the most important parts of this project.

Initially, I faced issues with test setup and some test cases did not check the expected conditions correctly. Instead of ignoring those problems, I reviewed the test logic, corrected the test data, and worked on the implementation.

I learned how to test:

- Exact box-fitting conditions.
- Item rotation and different orientations.
- Weight and volume restrictions.
- Items that cannot physically fit inside a box.
- Empty orders and invalid quantities.
- Unknown product SKUs.
- API validation and HTTP status codes.
- Cheapest box selection and tie-breaking conditions.
- Frontend page loading and static file integration.

**Final testing result:**

- Total tests: 41
- Passed: 41
- Failed: 0

The final test run completed successfully using `python manage.py test -v 2`.

## 5. What I Learned from Errors and Success

One important thing I learned is that getting an error does not mean the project is failing. Sometimes the problem is with the environment, folder structure, configuration, test data, or even the test case itself.

I learned to read error messages carefully, identify the actual reason, try different solutions, and test again.

When I finally got all 41 tests passing, it gave me confidence that the application was working as expected for the tested scenarios.

I also understood that successful development is not just about writing code. It involves debugging, testing, improving, and checking whether the application meets the requirements.

## 6. My Overall Experience

This project helped me improve my practical knowledge of Python, Django, REST APIs, JavaScript, database management, and software testing.

I also became more comfortable working with errors and solving problems independently. I learned that a project needs multiple rounds of improvements before it becomes properly organized and reliable.

Overall, I am happy that I was able to build the Box Selection System, solve the problems I encountered, improve the implementation, and achieve a final result with all 41 tests passing.

This project gave me more confidence in developing real-world applications and motivated me to keep improving my programming and problem-solving skills.