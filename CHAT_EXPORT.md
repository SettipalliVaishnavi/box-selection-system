

Assignment - Python_Django Developer _V1 (1).docx
Document
exaplin the whole proejct celarly neetly
Vaishnavi, I read your complete Python/Django Hiring Assignment. Let's understand the entire project from the beginning in simple English, step by step.

Your assignment is:

AI-Assisted Box Selection System
Seasonal Packaging: Scale Peak Orders Without Hiring (2026)
1. What is this project?
This is a Python + Django web application for an e-commerce company.

Imagine an online shopping website like Amazon.

A customer orders three products:

One laptop

One mobile phone

One pair of shoes

Now the warehouse team needs to pack these products into a shipping box.

But there is a problem.

The warehouse has different box sizes:

Small box

Medium box

Large box

Extra-large box

The warehouse team needs to identify:

Which box is suitable for packing all the products safely at the lowest possible cost?

Our project automatically recommends the most suitable box.

That's the main purpose of this application.

2. Why do we need this project?
Imagine a warehouse has 100 orders every day.

If employees manually select boxes for every order:

It takes more time.

They might select unnecessarily large boxes.

Shipping costs may increase.

Products might not fit inside the selected box.

Boxes may exceed their maximum weight capacity.

Our application solves these problems by automatically selecting a suitable box.

3. Understand the input data
Our system needs two main types of information.

A. Product details
Every product has:

Product

Length

Width

Height

Weight

Laptop

30 cm

20 cm

3 cm

2 kg

Mobile

15 cm

8 cm

1 cm

0.5 kg

Shoes

25 cm

15 cm

10 cm

1 kg

These are example values to understand the project.

B. Box details
Every shipping box has:

Box

Length

Width

Height

Max Weight

Cost

Small

20

15

10

2 kg

₹10

Medium

35

25

15

5 kg

₹20

Large

45

35

25

10 kg

₹35

These are also illustrative values.

The system compares product requirements with available box specifications.

4. How does the project work?
Retail Inventory Packing: Processes, Tools, and Best Practices
The complete workflow:

Step 1: Customer Order

Customer places an order containing multiple products.

Step 2: Product Information

Get product length, width, height and weight.

Step 3: Box Information

Get available box dimensions, weight capacity and cost.

Step 4: Selection Algorithm

Compare dimensions, total weight and box capacity.

Step 5: Best Box Recommendation

Choose the most suitable box based on the selection criteria.

Step 6: Display Result

Show the recommended box and its details to the warehouse team.

5. How does the box selection algorithm work?
This is the most important part of your project.

Let's understand with an example.

Suppose the customer orders:

Laptop: 2 kg

Mobile: 0.5 kg

Shoes: 1 kg

Total weight:

2
+
0.5
+
1
=
3.5
 kg
2+0.5+1=3.5 kg
Now the system checks available boxes.

First: Check weight capacity

Small box: 2 kg – Not suitable.

Medium box: 5 kg – Suitable.

Large box: 10 kg – Suitable.

Second: Check dimensions

The system must check whether all products can physically fit inside the box.

Third: Compare cost

Medium box: ₹20

Large box: ₹35

If both boxes satisfy all requirements, the medium box is the cheaper suitable option.

Recommended result: Medium Box
The application displays:

Recommended box: Medium

Maximum weight: 5 kg

Order weight: 3.5 kg

Box cost: ₹20

Status: Suitable

Important: This is an illustrative selection method. Your assignment does not specify the exact algorithm. You should also consider product arrangement, rotation and available internal space. Checking only total volume is not enough to guarantee that products physically fit.

6. Which technologies do we use?
Your assignment specifically asks you to build a Django-based system.

Here is a suggested technology structure:

Technology

Purpose

Python

Main programming language

Django

Backend development

HTML

Webpage structure

CSS

Styling

Bootstrap

Responsive design

SQLite

Database

JavaScript

Frontend interactions

GitHub

Project submission

What is Django doing here?

Django handles:

Receiving order information.

Retrieving product information.

Retrieving available box information.

Running the selection algorithm.

Sending the recommended box to the webpage.

7. Suggested project folder structure
You can organize your project like this:

AI-Assisted-Box-Selection/
│
├── manage.py
│
├── box_selection/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── boxes/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── tests.py
│
├── templates/
│   ├── home.html
│   ├── products.html
│   └── result.html
│
├── static/
│   └── css/
│
├── requirements.txt
├── README.md
├── AI_USAGE.md
├── TEST_OUTPUT.md
└── test_cases.md
This is a suggested structure, not a mandatory structure from the assignment.

8. What database tables do we need?
I recommend starting with three main tables.

1. Product

Field

Meaning

id

Product ID

name

Product name

length

Product length

width

Product width

height

Product height

weight

Product weight

2. Box

Field

Meaning

id

Box ID

name

Box name

length

Internal length

width

Internal width

height

Internal height

max_weight

Maximum weight

cost

Box cost

3. Order

Field

Meaning

id

Order ID

customer_name

Customer name

created_at

Order date

You would also need an order-items relationship to store which products and quantities belong to each order.

9. What should the website look like?
Box Finder - Find the Perfect Shipping Box | OnlineShip
Prep Parcel - Multi carrier shipping rates, bulk labels, and live tracking | Shopify App Store
PackExpert — Packaging Configurator UI for Smurfit Westrock by Bootmine on Dribbble
How to print a UPS shipping label | Blog | Sticker Mule
Packsmith - Smarter fulfillment with packaging and address suggestions. | Shopify App Store
Saving Shipping Boxes – Easyship
The Sendle Parcel Size Guide | Canada
Warehouse Inventory Dashboard by Beadaptify on Dribbble
Shipping Platform For Ecommerce - Pack to the Future
¿Cómo crear mi guía? | Centro de ayuda
Suggested pages:

Home page: Project introduction.

Product page: Add and view products.

Box management: Add and view available boxes.

Order page: Select products and quantities.

Recommendation page: Display the best suitable box.

These pages are suggested features. The assignment itself only requires the box recommendation system.

10. Testing the project
Testing is very important because the assignment explicitly asks for test cases and test execution output.

Here are some examples:

Test case

Input

Expected result

TC01

Product fits in small box

Small box recommended if cheapest

TC02

Product requires medium box

Medium box recommended

TC03

Product exceeds all box dimensions

No suitable box

TC04

Product weight exceeds capacity

Reject that box

TC05

Multiple products

Check combined weight and physical fit

TC06

Empty order

Show validation error

TC07

Invalid dimensions

Show validation error

You should run these tests and record the actual results, including failed tests and corrections.

11. Understand all submission requirements
Your assignment asks for seven deliverables. 
Assignment - Python_Django Developer _V1 (1).docx

No.

File / Deliverable

What it means

1

GitHub repository

Upload your complete project

2

README.md

Explain the project, installation and usage

3

AI_USAGE.md

Explain how you used AI tools

4

Chat transcript

Export your actual AI conversation

5

What I learned

Write your own learning experience

6

Test cases

Document the test scenarios

7

TEST_OUTPUT.md or GitHub Actions

Provide actual test execution results

Very important instructions

Your assignment specifically says:

Do not use AI to generate your chat transcript.

Do not use AI to generate your personal learning experience.

Include AI prompts, accepted outputs, rejected outputs, mistakes and verification in AI_USAGE.md.

These are explicit assignment requirements. Write those personal documents yourself.

12. What skills will this project demonstrate in an interview?
When you complete this project, you can demonstrate:

Python programming.

Django backend development.

Database design.

CRUD operations.

Algorithm development.

Logical problem-solving.

Input validation.

Unit testing.

GitHub project management.

Responsible AI tool usage.

13. How I recommend building this project
Let's divide the work into phases so you don't get confused.

Phase

Work

Status

1

Understand requirements and design

To do

2

Setup Python virtual environment and Django

To do

3

Create Django application and database models

To do

4

Add product and box management

To do

5

Develop box selection algorithm

To do

6

Connect algorithm with Django views

To do

7

Create frontend pages

To do

8

Write test cases and run tests

To do

9

Fix errors and verify results

To do

10

Prepare GitHub and submission documents

To do

14. Explain this project in an interview
Here is a simple explanation you can practise after completing the implementation:

"The project I worked on is an AI-Assisted Box Selection System developed using Python and Django. The main objective is to help e-commerce warehouses select suitable shipping boxes for customer orders.

The system considers product dimensions, product weight, box dimensions, maximum weight capacity and box cost. It compares the order requirements with available boxes and recommends a suitable box.

This application helps reduce manual work, avoid unsuitable packaging and optimize packaging costs.

Through this project, I demonstrate my Python, Django, database management, logical problem-solving and testing skills."

One important clarification: Although the assignment calls it an AI-Assisted system, it does not explicitly require a machine-learning model or an LLM. A rule-based recommendation algorithm is a reasonable starting point unless the employer provides additional AI requirements.

Let's start building it step by step.
Before we start, tell me your preference.

1. How do you want to build it?


Step-by-step from the beginning (recommended)

I know Django; focus on project implementation
2. Which frontend do you prefer?


HTML, CSS and Bootstrap

React.js + Django
We'll build the actual working project, understand every file, test it, fix errors and prepare your submission.

I am building a Box Selector application using Python and Django. The application should select a suitable box for an order based on item dimensions, weight and cost. Can you explain the important things I should consider before implementing the packing logic? Don't give me the complete code.
Before implementing the packing logic in your Python/Django Box Selector application, you should understand a few important concepts.

The main challenge is not simply finding a box that is bigger than the product. You need to make sure that all products in an order fit inside the box, the weight is within its capacity, and the box cost is reasonable.

Let's go through the important considerations.

1. Understand the input data
You have two main entities.

Product / Order Item

Each item should have:

Length

Width

Height

Weight

Quantity

Box

Each available box should have:

Box name or ID

Internal length

Internal width

Internal height

Maximum weight capacity

Box cost

Important: Use the box's internal dimensions, not external dimensions.

2. Dimension comparison
You need to check whether a product physically fits inside a box.

For example:

Product dimensions:

Length: 20 cm

Width: 15 cm

Height: 10 cm

Box dimensions:

Length: 25 cm

Width: 20 cm

Height: 15 cm

The product fits.

But consider rotation.

A product might not fit in its original orientation but may fit when rotated.

For example:

Product: 20 × 15 × 10

Box: 15 × 20 × 25

It can fit if you allow rotation.

Important considerations:

Should products be allowed to rotate?

Should all six possible orientations be checked?

Should the system allow products to be placed in different orientations?

For a basic implementation, checking all possible orientations is a useful starting point.

3. Multiple products in one order
This is one of the most important challenges.

Imagine an order contains:

Product

Quantity

Dimensions

Laptop

1

30 × 20 × 3

Mobile

2

15 × 8 × 2

Book

1

20 × 15 × 4

You cannot simply check each product separately and conclude that they all fit.

You must consider whether they can be arranged together inside the same box without overlapping.

Consider:

Combined dimensions

Product arrangement

Available space

Rotation

Products overlapping each other

This problem is commonly called 3D Bin Packing.

For your initial implementation, you can support one box per order and a simple packing strategy.

4. Weight validation
Dimensions alone are not enough.

Suppose:

Product

Weight

Laptop

2 kg

Mobile

0.5 kg

Book

1 kg

Total weight:

2
+
0.5
+
1
=
3.5
 kg
2+0.5+1=3.5 kg
Available boxes:

Box

Maximum weight

Small

2 kg

Medium

5 kg

Large

10 kg

The small box must be rejected because its weight capacity is insufficient.

Remember to multiply each product's weight by its quantity.

Also consider whether box weight itself should count toward the shipping weight. Your assignment does not specify this, so document your assumption.

5. Box cost optimization
Your objective should not be to select the biggest box.

It should be to select the cheapest box that satisfies all packing constraints.

Example:

Box

Cost

Suitable?

Small

₹10

No

Medium

₹20

Yes

Large

₹35

Yes

Recommended box: Medium.

You should define a clear selection rule:

Reject boxes that cannot physically fit the products.

Reject boxes that exceed weight capacity.

Compare the costs of remaining boxes.

Select the lowest-cost suitable box.

If two boxes have the same cost, you can use a secondary criterion such as smaller box volume.

6. Edge cases you must consider
Don't implement only normal situations. Think about unusual inputs too.

Scenario

Expected behaviour

Empty order

Display validation message

Zero dimensions

Reject invalid product

Negative weight

Reject invalid input

Product larger than every box

No suitable box

Weight exceeds every box

No suitable box

Multiple quantities

Calculate total weight correctly

Rotation required

Check alternative orientations

No available boxes

Display appropriate message

Equal-cost boxes

Apply tie-breaking rule

Exact dimension match

Allow if boundary contact is acceptable

7. Decide your packing strategy
There are different levels of packing algorithms.

Approach

Explanation

Difficulty

Basic dimension checking

Check whether individual items fit

Easy

Rotation checking

Check different orientations

Easy–Medium

First Fit

Place items into available space in an order

Medium

Best Fit

Choose the placement that uses space efficiently

Medium

3D Bin Packing

Optimize placement of multiple items in 3D space

Advanced

My recommendation: Start with dimension validation and rotation checking, then implement a simple multi-item placement strategy.

Do not claim that checking total product volume guarantees a valid packing arrangement. It doesn't.

8. Input validation
Before running the algorithm, validate your data.

Examples:

Dimensions must be positive.

Weight must be positive.

Cost cannot be negative.

Quantity must be a positive integer.

Required product and box fields must not be empty.

Also decide whether decimal dimensions and weights are allowed.

9. Django application design
Keep your application organized.

Component

Responsibility

models.py

Product, Box and Order database models

views.py

Receive requests and return results

forms.py

Validate user input

services.py

Implement packing and box selection logic

tests.py

Test algorithm behaviour

templates

Display input forms and recommendations

My suggestion: Keep the packing algorithm in a separate services.py file rather than writing all the logic inside Django views. This makes it easier to test and maintain.

10. Testing strategy
Before completing the project, prepare test cases for:

Single product.

Multiple products.

Different product quantities.

Product rotation.

Weight capacity.

Cheapest suitable box.

No suitable box.

Invalid dimensions.

Equal-cost boxes.

Test the packing algorithm independently before connecting it to Django.

Recommended implementation order
Your development checklist
Progress

0/12 completed


Understand Product and Box data models

Define measurement units (cm and kg)

Implement input validation

Implement individual dimension checking

Implement product rotation

Calculate total order weight

Implement multiple-item placement

Filter boxes by weight and dimensions

Select the lowest-cost suitable box

Handle cases where no box fits

Write unit tests

Connect the algorithm to Django views
My final advice: Focus on correctness before optimization. A box recommendation is valid only when every product can actually be placed inside it, without overlapping, and the weight and cost constraints are satisfied.

One important distinction for your assignment: the title says AI-Assisted Box Selection System, but the provided requirements do not mandate machine learning. A well-designed algorithm with clearly explained decisions is a perfectly reasonable starting point.

Next step: Design your packing algorithm in plain English or pseudocode first. Once the logic is clear, implementing it in Python will become much easier.

I understand volume calculation, but is checking total volume enough to decide whether products fit inside a box? Can you explain with a simple example?
No, checking total volume alone is NOT enough to decide whether products fit inside a box.

This is a very important concept in your Box Selector project.

Let's understand with a simple example.

1. What does volume checking mean?
Volume tells us how much space an object occupies.

Formula:

V
o
l
u
m
e
=
L
e
n
g
t
h
×
W
i
d
t
h
×
H
e
i
g
h
t
Volume=Length×Width×Height
Suppose you have two products.

Mailing Box 80 x 80 x 660mm B32 Long Tube Carton
 | eBPak
Product A

10 × 2 × 2 cm

Volume = 40 cm³

Cardboard empty package box isolated on white background. Delivery carton box. Clipping path included. Little Box for Gift, Food, Candy.
Product B

10 × 2 × 2 cm

Volume = 40 cm³

Total volume:

40
+
40
=
80
 
c
m
3
40+40=80 cm 
3
 
Now suppose the box dimensions are:

10
×
4
×
2
10×4×2
Box volume:

10
×
4
×
2
=
80
 
c
m
3
10×4×2=80 cm 
3
 
Based on volume:

Products total volume = 80 cm³

Box volume = 80 cm³

So, the volumes are equal.

But let's think about the actual arrangement.

2. Why can volume checking give the wrong answer?
Imagine two products, each measuring:

10 × 2 × 2 cm.

The box measures:

10 × 4 × 2 cm.

These products can fit perfectly side by side.

But consider another example.

Two square products:

Product 1: 4 × 4 × 1 cm

Product 2: 4 × 4 × 1 cm

Box:

- 8 × 2 × 2 cm

Advise and register packaging - Picqer Support
Calculate volumes:

Products:

16
+
16
=
32
 
c
m
3
16+16=32 cm 
3
 
Box:

8
×
2
×
2
=
32
 
c
m
3
8×2×2=32 cm 
3
 
The volumes are equal.

But each product has a width of 4 cm, while the box has a width of only 2 cm.

Even after rotation, neither product can fit inside the box.

No valid packing
This proves that equal volume does not guarantee that objects fit.

3. What should you check instead?
For your Box Selector application, consider these checks:

Check

Purpose

Total volume

Check available space approximately

Dimension comparison

Check whether each product can fit

Rotation

Check alternative orientations

Product arrangement

Check whether multiple products fit together

Weight

Check maximum box capacity

4. Important concept: 3D Bin Packing
The problem of placing multiple 3D objects inside a container without overlapping is called 3D Bin Packing.

Pick and Pack Optimization Software | Pulse by Optioryx
It considers:

Length

Width

Height

Rotation

Position of each product

Overlapping

Available space

For example, if you have five products, the algorithm needs to determine where each product should be placed inside the box.

5. Remember this for your project
There are two different questions:

Volume check: Is the total product volume less than or equal to the box volume?

Packing check: Can all products physically fit inside the box without overlapping?

The first is a useful preliminary check. The second determines whether the box is actually suitable.

Small knowledge test
Question: A product measures 12 × 8 × 5 cm. A box measures 15 × 10 × 4 cm.

The product volume is smaller than the box volume.

Can the product fit inside the box, without cutting or deforming it?


Yes, because the product volume is smaller.

No, because the product height is 5 cm but the box height is 4 cm, and no rotation can solve this.
Key takeaway: Volume tells you how much space is needed. Dimensions and packing logic tell you whether the products can actually fit.

How can I handle different product orientations while checking whether products fit inside a box?
To handle different product orientations in your Box Selector application, you should use 3D Rotation Checking.

The idea is simple: A product can be rotated in different directions, so even if it doesn't fit in its original orientation, it might fit after rotation.

Let's understand step by step.

1. Understand the six possible orientations
Suppose a product has these dimensions:

Length = 10 cm

Width = 6 cm

Height = 4 cm

Normally, we represent it as:

(10, 6, 4)

But we can rotate the product and change which dimension is assigned to length, width and height.

There are six unique orientations:

All six possible orientations

Orientation

Length

Width

Height

1

10

6

4

2

10

4

6

3

6

10

4

4

6

4

10

5

4

10

6

6

4

6

10

Why six?

Because three different dimensions can be arranged in:

3
!
=
3
×
2
×
1
=
6
3!=3×2×1=6
different ways.

2. Check each orientation against the box
Suppose the box dimensions are:

Length = 8 cm

Width = 7 cm

Height = 5 cm

Product dimensions:

- 10 × 6 × 4 cm

Let's compare.

Orientation

Box comparison

Fits?

10 × 6 × 4

10 > 8

No

10 × 4 × 6

10 > 8

No

6 × 10 × 4

10 > 7

No

6 × 4 × 10

10 > 5

No

4 × 10 × 6

10 > 7

No

4 × 6 × 10

10 > 5

No

None fits.

Now change the box dimensions to 11 × 7 × 5 cm.

The original orientation (10 × 6 × 4) fits.

This is how orientation checking works.

3. How to implement this logic in Python
You don't need to write six separate conditions.

Python provides a useful concept called permutations.

You can generate all possible arrangements of three dimensions.

For example, the following is a small learning example, not your complete project code:

from itertools import permutations

product = (10, 6, 4)

orientations = list(permutations(product))

for orientation in orientations:
    print(orientation)

Output:

(10, 6, 4)
(10, 4, 6)
(6, 10, 4)
(6, 4, 10)
(4, 10, 6)
(4, 6, 10)
Now understand the checking condition:

if (
    product_length <= box_length
    and product_width <= box_width
    and product_height <= box_height
):
    print("Product fits")

You would apply this condition to each orientation.

4. Important: Rotation checking is not complete packing logic
There is one important difference.

For one product: Checking six orientations is enough to determine whether that product can fit inside an empty rectangular box.

For multiple products: It is not enough.

You must also consider:

Where each product is placed.

Whether products overlap.

Whether there is enough remaining space.

Whether different orientations allow all products to fit together.

For example, three products might each fit individually in a box, but they might not fit together.

This is where 3D Bin Packing algorithms become useful.

5. Recommended approach for your Django project
I suggest dividing your logic into separate functions:

Function

Responsibility

get_orientations()

Generate six orientations

check_dimensions()

Check whether an orientation fits

check_weight()

Validate maximum weight

check_packing()

Check multiple-item placement

select_best_box()

Select the cheapest valid box

This separation makes your code easier to understand, debug and test.

6. Test your understanding
Question: Product dimensions are 12 × 8 × 5 cm.

Box dimensions are 13 × 9 × 6 cm.

Does the product fit without rotation?


Yes

No
Remember: Generate orientations → Compare dimensions → Find a fitting orientation → Validate weight.

This is the first step toward building a reliable box selection algorithm.

My Django project is showing a 404 error when I open 127.0.0.1:8000. I can access the API, but I want a homepage also. What should I check?
This is a common Django issue, Vaishnavi. Don't worry! Your API is working, so your Django server is running. Most likely, you haven't configured a homepage URL.

Let's fix it step by step.

1. Understand why you are getting 404
When you open:

http://127.0.0.1:8000/

Django checks whether you have configured a URL for the root path /.

If you haven't configured it, Django displays:

404 – Page not found

Your API can still work because you may have configured API URLs separately.

2. Check your project structure
Your project might look something like this:

box_selector/
│
├── manage.py
│
├── box_selector/
│   ├── settings.py
│   ├── urls.py
│
├── boxes/
│   ├── views.py
│   ├── urls.py
│   └── models.py
3. Check your main urls.py
Open:

box_selector/urls.py

Check whether you have configured your homepage route.

For example:

from django.contrib import admin
from django.urls import path, include
from boxes import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('api/', include('boxes.urls')),
]

Understand these routes:

URL

Purpose

/

Homepage

/admin/

Django admin

/api/

Your API endpoints

4. Check your views.py
Open:

boxes/views.py

You need a homepage view.

For example:

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

This tells Django to display the home.html template.

5. Check your HTML template
Create this folder structure:

boxes/
    templates/
        home.html
Inside home.html, add a simple test:

<!DOCTYPE html>
<html>
<head>
    <title>Box Selector</title>
</head>
<body>
    <h1>Welcome to Box Selector</h1>
    <p>Find the best shipping box for your order.</p>
</body>
</html>

6. Check settings.py
Open your settings.py.

Check whether your Django app is registered:

INSTALLED_APPS = [
    # Other apps
    'boxes',
]

Also check the template configuration. If you use an app-level templates folder, APP_DIRS should be True.

'APP_DIRS': True,

7. Restart your Django server
In your terminal:

python manage.py runserver

Now open:

Homepage

Expected
http://127.0.0.1:8000/

API

http://127.0.0.1:8000/api/

Admin

http://127.0.0.1:8000/admin/

If you still get a 404
Send me these three things:

Your main urls.py.

Your app's views.py.

Your project folder structure (screenshot or text).

I can identify exactly where the problem is without changing your existing API logic.

One recommendation: For your Box Selector assignment, keep the homepage and API separate. The homepage will be used by warehouse users, while the API will handle the box selection operations.

I am getting Order not found: ORD-1001. My application is running, but it cannot find the sample order. How do I check whether my database contains the required data?
This error usually means your Django application is working, but it cannot find an order with the ID ORD-1001 in the database.

Let's debug it step by step. Don't change your packing logic yet. First, confirm that the required sample data exists.

1. Check which database your Django project is using
Open your project's settings.py.

Find the DATABASES section.

For example, if you see:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

Your project is using SQLite.

If you see django.db.backends.mysql, your project is using MySQL.

This matters because you must inspect the same database that Django is connected to.

2. Check whether your database contains orders
Open your terminal in the folder containing manage.py.

Run:

python manage.py shell

This opens the Django interactive shell.

Then import your Order model. For example:

from boxes.models import Order

Replace boxes with your actual Django app name if different.

Now check:

Order.objects.count()

This tells you how many orders exist.

Then check:

Order.objects.all()

This displays the existing order records.

3. Search specifically for ORD-1001
First, check which field stores the order number.

In Django shell:

[f.name for f in Order._meta.fields]

You might see fields such as:

['id', 'order_number', 'customer_name', 'created_at']
If your field is called order_number, run:

Order.objects.filter(order_number="ORD-1001").exists()

Possible results:

True – The order exists.

False – The order does not exist.

You can also retrieve it:

Order.objects.get(order_number="ORD-1001")

If it doesn't exist, Django raises Order.DoesNotExist.

4. Check your related order items
Even if the order exists, check whether it has products.

For example, if your relationship is called items:

order = Order.objects.get(order_number="ORD-1001")

order.items.all()

Check the number of items:

order.items.count()

The relationship name depends on your actual Django model.

5. Check database migrations
Sometimes your database tables haven't been created.

Exit the Django shell:

exit()

Run:

python manage.py showmigrations

Look for migrations marked [X].

If migrations are pending, run:

python manage.py makemigrations
python manage.py migrate

Remember: migrations create or update database structure. They do not automatically insert your sample order.

6. Check whether sample data needs to be inserted
Look through your project for files such as:

fixtures/
    sample_data.json

seed.py
populate_db.py
Also check your README for instructions to load sample data.

If your project uses Django fixtures, the command might be:

python manage.py loaddata sample_data.json

Only run this if that fixture actually exists and matches your models.

7. Check your database through Django Admin
You can also inspect records visually.

Start your server:

python manage.py runserver

Open:

http://127.0.0.1:8000/admin/

Log in and check whether the Orders section contains ORD-1001.

If Orders isn't visible, check whether your model is registered in admin.py.

8. Debugging checklist
Check

Expected result

Database configuration

Correct database

Order count

Greater than zero

ORD-1001 search

True

Order items

At least one item

Migrations

Applied

Sample data

Successfully inserted

9. Let's identify your exact problem
Run these commands first:

python manage.py shell

Then:

from boxes.models import Order
print(Order.objects.count())
print([f.name for f in Order._meta.fields])

Replace boxes with your actual app name.

Send me these three details:

Output of Order.objects.count().

Output of [f.name for f in Order._meta.fields].

Your Order model from models.py.

Debugging approach
We will identify whether the problem is missing sample data, an incorrect field name, or a database configuration issue.

Important: Don't manually modify the database or rewrite your existing code until we identify the actual cause.





