# nuTROLLA
Hello there! this app provides a marketplace to sell refurbished controllers, from older gen, to new gen. A user will be able bask in the "Synthwave/Cyberpunk" theme of the site. There is something for every gamer here, the controller you receive, will look as fresh as the day it was released. Parts & tools are also sold so if you're a bit more hands on, you can replace those gummy joysticks with new one's

So feel free and have a browse, make an account, add item's to your basket, go wild!



# Demo

**A live demo of the site can be found** [HERE](https://tenbonks-nutrolla.herokuapp.com/)

![Desktop Demo](https://github.com/tenbonks/nuTROLLA/blob/master/project_info/nutrolla-screenshot.png "Desktop Demo")

---

# UX

The flow of this site is designed to be nothing out of the ordinary when it comes to e-commerce sites, with all the products easily findable, be that from searching the store via the search bar or using the navigation links to get to the products they want.

If the user wishes to buy something from the site, its a very simple process, and the user is given inputs to change the quantity of the item within the bag incase they change their mind on something.

A user can sign up, and keep an account for extra access to the site, these features are viewing past orders, and the ability to keep persistant delivery information between purchases.

The links shown to users will depend on if their logged in or not, so there are no links a user shouldn't be pressing, and there is authorisation checks on pages where users shouldn't be visiting, such as if a user who isn't signed in tries to access the profile app, they will be redirected to login, and if a user who is logged in, tries to access pages regarding product management, they will be notified that they aren't authorised.

The colours used for the site are inspired from "Vapourwave/Synthwave/Cyberpunk" themes, these correlate with gaming and pluck on the nostalgia strings, and really make the site stand out from other sites in the "Controller Refurbishment" business. The site reflows all the way down to 320px and looks just as good in mobile, as it does in desktop. To see the exact colour sheet I referenced, click [HERE](https://github.com/tenbonks/nuTROLLA/blob/master/project_info/cyber-punk-color-pallate.png)

During the development and planning of this project I took a lot of inspiration and guidance of the project Boutique Ado, as I found it fit really well with what I wanted to achieve from my site idea, so structurally there are lots of similarities, more about this in the aknowlegments at the bottom of this README


**User Stories can be found under the folder "project-information" in this repo, or [here](https://github.com/tenbonks/nuTROLLA/blob/master/project_info/nuTROLLA-User_Stories.png).**


**Mockup can be found under the folder "Mockup" in this repo, or [here](https://github.com/tenbonks/nuTROLLA/tree/master/mockup).**


there is no wireframe to show, as I adapted my wireframe into the mockup, mainly being because I was happy with the wireframe, so I started to style it.

---

# Features

* A simple, clear and responsive design, with a navbar always present allowing navigation to all relavent parts of the site.

- A vibrant header, with app's logo, drop down navigation links, this adapts to a bootsrap style dropdown on small devices.

- A responsive bag, which includes the grand total so a user can track their spending

- A back to top button, so users can get back to the top of the page with ease

- A searchbar, so the user can search through product names and categories, to find exactly what they want

- A vibrant design featuring Synthwave/Cyberpunk colours, and a neon light effect shining down on the page

- Full CRUD (Create, Remove, Update, and Delete) operations on product database for admin of the site

- A user can sign up and have a profile, allowing them to save default information to use when checking out

- Stripe for secure payments

- View past orders and save default info if user has an account

---

**Features to implement in the future**

<details>
<summary>Stock adjustment when order created</summary>
<br>
This feature was a tricky one, as without stripe, I found it quite straight forward to implement, but I had issues with if stock were  to change between page loads. An example is if a product goes out of stock, and a user checks out with it in their bag just after, the payment would be proccessed by stripe and the user charged for items that are out of stock.
I spent a fair amount of trial and error on this and in the end decided to take out the code that ammended stock levels, and the sections that would return a user back to the bag page and notify them of the stock issue.

NOTE: I ended up implementing this feature so it has no effect on stock issues during checkout, it is purely visual element of the site. there are some visual bugs as a drawback though, for example a user can have an item which shows out of stock if they already had it in their bag before the stock ran out. This isn't ideal but since I had stock in the model I wanted to use it for something.
</details>

<details>
<summary>The tags used for selecting a console name, or category on the product page</summary>
<br>
The tags I currently use work, but I want to implement them in a cleaner way as it's a rather manual way passing the values to filter via href, the url ends up    getting very long on pages which on all controller, all parts, and all tools, also the console name will show up as a link even if there are no products, so      really it shouldn't be appearing as a link, as it leads to a no products page, I can manually get around it by changing the href but that isn't practical.
</details>

- Add more products to the database, I felt the amount was sufficent to provide content on each page

- Write programmatic test's with Django's testing functions, I ended up doing manual testing after, and througout development, more on this in the testing section of this README

- Write more manual tests

- I had planned on filling out the footer with typical information found on a e-commerce site, this would include T&C's, Returns, and a contact form which I was going to implement with a bootstrap modal

- Route any unkown URL with the prefix "tenbonks-nutrolla.herokuapp.com" to the apps homepage (404 errors)

- I had planned on implementing using allauths social account login, so users would be able to create an account via their google account
  
All of these were mainly not imlemented due to time contraints.

---

# Technologies used

HTML, CSS, Javascript, Python (packages, these can be found in requirements.txt), postgres, Django, AWS (s3), Flask, Bootstrap 4, jQuery, Github, Heroku, Stripe, Figma (for design planning).

This site was built with Django at it's core, The Framework with batteries included provided a quick start to development and essential tools for developing this website, There is much to learn with it and will enjoy making more with it and getting more familiar with it's intricacies, as it truly is a powerful framework to have under your belt.

For getting the initial data to start working on my site I manually every file in the products/fixtures folder, and loaded my fixtures to my models, in the order of Manufacturer, Console, Categories, Products.

* [HTML](https://www.w3.org/html/) 
    - it is the structure of this site and with Django, elevated it's versatility with templating language.

- [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
    - Is used for all the styling of the site, other than the Bootstrap classes used.

- [Javascript](https://www.javascript.com/) 
    - Handles the Stripe element in checkout, handles the payment info passed through it with the Stripe API.

- [jQuery](https://jquery.com/) 
    - Handles the quantity selection icon buttons, back to top button, loading overlay, and some more intricate styling particularly the country field in delivery       info forms.

- [Python](https://www.python.org/) 
    - Handles the backend functions, Django is built on it and extends the functionality of Python with a plethora of tools to use.

- [Django](https://www.djangoproject.com/) 
    - The framework with batteries included, this handles one heck of a lot on this website, from which url does what and defining what that does in the views, it's the foundation to this site and made making something of this size a lot quicker.

- [django-crispyforms](https://django-crispy-forms.readthedocs.io/en/latest/index.html) 
    - Allows Django forms to be styled and formatted with ease, I used it to format forms using Bootstrap 4 classes

- [Bootstrap 4](https://getbootstrap.com/) 
    - Makes styling the site a breeze with it's components, easy classes and a simple grid layout.

- [SQlite3](https://www.sqlite.org/index.html)
    - The database used in development environment

- [Postgres](https://www.postgresql.org/) 
    - The database used in production environment.

- [AWS Services (s3)](https://aws.amazon.com/)
    - s3 is used to store the static and media files of the site.

- [Heroku](https://www.heroku.com/) 
    - This is where the app is deployed to.

- [ngrok](https://ngrok.com/) 
    - An essential tool for testing webhooks when on a localmachine, as a 'https' address is required

- [Figma](https://www.figma.com/)
    - Used to create Wireframe & Mockup

--- 
# Testing

During development of this project, I tested each function thoroughly for the expected outcome, to make sure eveything is working as expected before each commit.

For testing webhooks, due to me developing this app on a local machine using VScode, I had to get over the hurdle of not having a http address for testing Stripe Webhooks (http address is required), I used a handy application called [ngrok](https://ngrok.com/), which with one simple command I had my local address port forwarded to one with the correct protocol to test webhooks. Webhooks were tested to ensure that even if there was a problem on the code side, if a charge has been succeeded, then the webhook will create the order onto my database.

I sent this website out to friends to get a consumers opinion on it and the verdict was good, with one of them pointing out a small typo in one the "Why use nuTROLLA" cards, which this has been rectified

I sent out the app to the peer-review channel on slack, In which I had one response which was a positive mark on the end product (The user was on a Samsung s9), I also sent the deployed link out to a friend to get his verdict and he said the site ran well, he could buy something (I confirmed this came up on my order model), so from a consumer point of view I am happy with the outcome of this project.

I performed all the manual tests below once my website was in a production environment and I felt was ready for submission

<details><summary>CLICK HERE for testing process'</summary>
<p>

1. The content of the site should resize fluidly to specific breakpoints
    1. Load the website on a large desktop monitor.
    2. Check all pages of the site to check the layout is as expected.
    3. Open developer tools and repeat step 2 at xs, small, medium breakpoints
    4. The layout is as expected and elements will display to fit the device its being displayed on.
    5. This verifies that the site is responsive to different screen size, and aspect ratios.

<details><summary>BAG APP TESTS</summary>
<p>

1. If I click "Add To Bag", I expect that item to be added to the bag by the specified quantity
    1. From the Product Detail page, change the quanity to 2, and click "Add to Bag"
    2. Look at the bag icon to see if the grand total changes to the expected price
    3. It does and this confirms this is functioning as expected

test 2-6 follow on from test 2

2. If I click "Remove" in the bag page, I expect the item to be removed
    1. I click "remove", the item is removed from the bag and the bag view informs me there is nothing in my bag 
    2. It does and this confirms this is functioning as expected

3. If I click "Update" in the bag app without changing the field, I expect no change
    1. I dont change the value from 2, I expect there to be no increase in my grandtotal
    2. It does and this confirms this is functioning as expected

4. If I click "Update" in the bag app after changing the quantity to 1, I expect qty change to 1
    1. I change the quanity to 1, and click update
    2. The quantity changes to 1 and the grand total refelcts the price of the single item
    3. It does and this confirms this is functioning as expected

5. If I click "Update" in the bag app after changing the quantity to 0, I expect the item to be removed from the bag
    1. I change the quantity of the item to 0, and click update
    2. The item is removed from my bag, and am informed my bag is empty
    3. this confirms this is functioning as expected

6. If I click "Update" in the product description page with the item currently in my basket, The quantity is added to the existing amount
    1. The selected item already has the quantity of 2 in my bag,
    2. On the product detail page I change the quantity to 2 and click "Add to Bag"
    3. A notification shows me that the quantity has changed to 5
    4. This is what I expected as 2 + 3 = 5
    5. this confirms this is functioning as expected

</p>
</details>

<details><summary>PROFILE/ACCOUNT TESTS</summary>
<p>

1. If I complete registering for an account, I expect to receive an email for verification
    1. After filling out the register form correctly, I click "Sign Up"
    2. I am redirected to a verify email page
    3. I check my specified email address for an email
    4. I have received an email, and am provided a link to verify my email
    5. this confirms this is functioning as expected

2. If I register with an already registered email, I expect an error mesage
    1. I try to register for an account my admin account
    2. I am informed this email is already registered to a user
    3. this confirms this is functioning as expected

3. If I enter a weak password on registering, I expect an error mesage
    1. I fill out the register form correctly, but with the password as "password"
    2. I click "Sign Up"
    3. I am informed that this password is too common
    4. this confirms this is functioning as expected
    

4. If both my passwords don't match when registering, I expect an error message
    1. I fill out the register form correctly, but with the passwords not matching
    2. I click "Sign Up"
    3. I am informed you must type the same password each time
    4. this confirms this is functioning as expected

5. From the account page, if I change the password, I expect the password to of changed to what I specified
    1. I log in as a already registered user
    2. I proceed to the profile app
    3. I click the change password button
    4. I provide my current password, and what to change it to
    5. I log out, and login again with the new password
    6. I can do this, which confirms this is working as expected

6. If I logout, I expect to be redirected to the home page and be notified that I have been logged out
    1. I log in as a user
    2. I log out as a user
    3. I am redirected to the home page, and a toast notifies me I have logged out
    4. This confirms this functions as expected

7. After I have verified my email, I expect to be able to log on with the credentials I registered with
    1. After I have registered for an account, I reveived an email with a link to verify my account
    2. I click the link which verifies my account
    3. I log out
    4. I log back in with the credentials entered during registering

8. If I enter default delivery details I expect them to be kept after the session has stopped
    1. When I am logged in I proceed to the profile app
    2. I fill in the form with test information
    3. I click update information
    4. I close all browsers
    5. I reopen the app, login, and proceed to my profile
    6. The information has been kept consistent
    7. This verifies that this is functioning as expected

</p>
</details>

<details><summary>CHEKOUT TESTS</summary>
<p>

Checkout requires an item to be in the basket already, this function has been tested, if a user tries to go to the checkout page with nothing in basket they are redirected to the homepage, so all these test are performed when there is 1 item in the bag

1. If I try to submit the checkout form with a required field blank, I expect an error
    1. I fill out all required fields apart from name
    2. I click submit
    3. I am informed to fill out the name field
    4. This verifies validation is working

2. If I try to submit with a incorrect card number, I expect the error
    1. I fill out the checkout form
    2. I use the card number 4224 4224 4224 4224
    3. The card element is informing me that number is incorrect
    4. This verified it is working as expected

3. If I am signed in and have created default information, I expect it to be prefilled in the form
    1. I log in, go to my profile, and fill out the default info form
    2. After I have updated the information I proceed to the checkout form
    3. Upon loading the form the details I just saved as defualt are prefilling the checkout form
    4. This confirms that this functions as expected

4. If I'm not logged in, I expect there to be buttons to register/login in the checkout form
    1. As an guest user, I go to the checkout page
    2. I can see the links to "Sign Up" or "Create an Account"
    3. If I click either of them It takes me to the correct page
    4. This verifies the function is working as expected

5. When a order goes to checkout success, I expect the order to be present in Django Admin panel
    1. I proceed to checkout and fill out the checkout form, and confirm purchase
    2. after I am in the checkout success page, I proceed to go the Djano Admin Panel
    3. I look for the order number I was given in the checkout success page
    4. I confirm the details are correct
    5. This verifies it is functioning as expected

</p>
</details>

</p>
</details>

---

# Deployment

**I developed nuTROLLA using VScode on a local machine, I used GitHub for version control, and Heroku for hosting the deployed site**

**Connecting to GitHub**
- I logged into Github, and created a repository, named nuTROLLA.
- I used the CLI to add the created repo to my remotes | `git remote add origin https://github.com/tenbonks/nuTROLLA.git`
- Now I am connected to the repo, any small or major changes can be pushed to adhere to good version control.

**Creation of app in heroku, and connection**
- Log in to Heroku (account is required), within the dashboard, click the "new" button featured in the top right of the page.
- Pick the closest region to you
- Using the CLI, add the heroku app as the remote master branch | `heroku git: remote a [app name]`

**Deployment to heroku**
- In the created Heroku app, I installed Heroku Postgres (Free Plan) as an add-on in the Resources tab
- To use Postgres, I installed two packages in my project, dj_database_url and psycopg2 and added them to my requirements
- In the Heroku app, I set Config Vars, so any secret information was kept out of version control, the django secret key has been changed from the one that was exposed.
- In the settings.py file, I imported dj_database_url, and set it to be used in production environment
- I used loaddata to import the data from my fixture files into the data models used in production
- I created a superuser for use in production via the command line
- I installed gunicorn, for use as the web server, added it to requirements.txt
- Created a Procfile
- The deployed sites hostname was added to "ALLOWED_HOSTS"
- Before pushing to heroku, DISABLE_COLLECTSTATIC was set to 1, to stop static files being collected during deployment
- Before pushing to Heroku, I pushed my commits to Github
- I then procceded to push to heroku
- After the successful deploy set up Heroku to automatically deploy whenever I push the my nuTROLLA project on github.
- I set the SECRET_KEY in settings.py to get it from the environment
- Debug is set to false when not in development environment

**Creating an AWS account and setting up s3 and IAM**
- I navigated to AWS and proceeded to make a personal account
- Once signed in, I am redirected to the dashboard, from here I can search for s3 in "Find Services"
- Click the s3 link, and click create bucket, I named it to match the Heroku app name, and set region to the closest to me
- I unchecked the Block all public access option, and akwnowleged my actions, then clicked create
- I applied some settings to the bucket
    1. In the Properties tab, I turned on static website hosting. this will give me a new endpoint to access from the internet.
    2. In the permissions tab
        1. I set up the CORS configuration, this is required for connection between the Heroku app and S3
        2. In the Bucket Policy tab, I created a s3 policy, allowed all principles, and set GetObject as the action, Copied the ARN from the Bucket Policy tab. I then added the statement, and generated it so I can add it to the policy, "/*" was appended to the Resource key to allow access to all resources in the bucket
        3. In the access Access Control List tab, under Public Access, I checked everyone, and set the access to "List Objects"
- Setting up IAM to create a user who is able to access the bucket, that has just been set up.
    1. I created a group called "manage-nutrolla", for the user to be created in
    2. I created a policy for the group, by importing the AmazonS3FUllAccess Policy, and replaced the Resource Key with the Bucket ARN in the bucket tab, I reviewed the and created the policy
    3. I went back to the Group panel, clicked the manage-nutrolla group, under the Permissions tab, I clicked Attach Policy, and attached the policy that was just created
    4. I created a User, which will live in the manage-nutrolla group. On the Users panel, I clicked create user called, tenbonks-nutrolla-staticfiles-user, checked the Programmatic access option and clicked next, from here I was able to add the user into the manage-nutrolla group
    5. After the user was created, I was able to download a .csv file, this allowed me to add it to my Config Vars in Heroku

**Connecting Django to S3 and User Groups**
- To connect django the Bucket and User Groups, 2 new packages are needeed, "boto3" and "django-storages"
- I freeze these into requirements after installed into my venv
- I added 'storages' into the installed apps in settings.py
- Using a config var from Heroku, I can check if 'USE_AWS' is True and set Django to use the AWS Bucket by configuring its name and region, also by getting the secret variables from Heroku, these are the fields which are sent in a .csv file after creating a user
- I set AWS_S3_CUSTOM_DOMAIN in settings to use the tenbonks-nutrolla bucket
- I removed the DISABLE_COLLECTSTATIC from my Heroku config vars, as now it should collect static files and upload them to s3 when deployed
- To enable uploaded pictures on the site to be uploaded to the S3 bucket, these steps were taken
    1. Create a project level file names "custom_storages.py"
    2. Import settings, and S3Boto3Storage
    3. Create a class called StaticStorage which contains the path to the static files
    4. Create a class called MediaStorage which contains the path to the media files
    5. Back in settings.py, set the the static and media file storages to use the classed just made
    6. Add the location for the storage to use in settings.py
    7. The URLS for static and media files need to be overwritten using the custom domain and locations, so I created a new url for static, and another for media in settings.py
    8. Django will now be able to connect to S3

**Finishing up with S3**
- The final touches on S3 were simple, I went into my bucket within AWS
- I added a new folder called "media"
- Within the media folder, I uplaoded all the images in the media folder in my project
- Granted them with public read access during the upload process

After the app was deployed, I also logged into stripe, and added a new enpoint for the deployed site for webhooks to work

**If you want to run *nuTROLLA* locally, you can clone this repository into an editor of your choice**

* Paste this into the editors terminal - <code>git clone https://github.com/tenbonks/scriptio-qoutes-app.git</code>

- To install libraries for Python, create a virtual environment(for local machines), and use this code -  <code>pip install -r requirements.txt</code>

- To cut ties with this GitHub repository, type this into the terminal - <code>git remote rm origin</code>

There is no difference between the deployed version and the development version, other than the database used, there are a few product differences, but other than that the code and style is the same

---


# Credits

**Content**

The JSON fixture files were created by me, the product images used are accredited in the media section below

---

**Media**


- Product images that are Tools
    - Zacro 12pc, Open and Clean Kit | [Image URL](https://images-na.ssl-images-amazon.com/images/I/715iPtffiFL._AC_SL1000_.jpg) | [Amazon Page](https://www.amazon.co.uk/Magnetic-Phillips-Screwdriver-Storage-Controller/dp/B07FL1P3J8/ref=sr_1_6?crid=2I8PECKHA39F1&dchild=1&keywords=ps4+controller+screwdriver&qid=1598663627&sprefix=PS4+CONTROLLER+SCRE%2Caps%2C151&sr=8-6)
    - Alcohol Wipes | [Image URL](https://images-na.ssl-images-amazon.com/images/I/71V8pE%2BD04L._AC_SL1500_.jpg) | [Amazon Page](https://www.amazon.co.uk/OptiPro-Alcohol-Pre-Injection-Isopropyl-Wipes/dp/B08CL34XS7/ref=sr_1_8?crid=EBK5WIBE9F6E&dchild=1&keywords=alcohol+wipes&qid=1598667504&sprefix=alcohol+%2Caps%2C158&sr=8-8)
    - Tweezers 9pc | [Image URL](https://images-na.ssl-images-amazon.com/images/I/619tkWBMvkL._AC_SL1200_.jpg) | [Amazon Page](https://www.amazon.co.uk/PIXNOR-Precision-Anti-Static-Electronics-Laboratory/dp/B01MYBI01J/ref=sr_1_8?dchild=1&keywords=electronics+tweezers&qid=1598667717&sr=8-8)

- Product images that are Parts, all of these came from [Zedlabz](https://www.zedlabz.com/)
    - PS4 TRIGGERS | [Image URL](https://cdn.shopify.com/s/files/1/1810/1427/products/cd2j5opopc0_2048x2048.jpg?v=1582125020)
    - PS4 CONDUCTION PAD | [Image URL](https://cdn.shopify.com/s/files/1/1810/1427/products/1jyna1p3as5_2048x.gif?v=1582132455)
    - PS4 JOYSTICKS | [Image URL](https://cdn.shopify.com/s/files/1/1810/1427/products/qvbz5ht05wu_2048x2048.jpg?v=1582131570)
    - PS4 ALL WHITE BUTTON KIT | [Image URL](https://cdn.shopify.com/s/files/1/1810/1427/products/reh2hry4mqt_2048x.jpg?v=1582132369)

Product images which are controllers were acquired from a dataset called [controllers](https://www.kaggle.com/charcoal/controllers) in Kaggle, by [Aaron Styles](https://www.kaggle.com/charcoal)

The Synthwave image I used for the background of the homepage is from [WallpaperAccess](https://wallpaperaccess.com/synthwave)

no image icon is from [Flaticon/Freepik](Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>)

---

**Acknowledgements**

During this development I took a heavy amount of inspiration and guidance from the mini project featured in the learning material to learn about how to make production ready Django project, the planning and development were all aided by this project, the creator of the project is [ckz8780 Chris Z](https://github.com/ckz8780), a link to the project he made for Code Institute, [Botique Ado](https://github.com/ckz8780/boutique_ado_v1).

Code Institute Tutors for their valuable opinions during development

My mentor, Maranatha Ilesanmi for valuable sessions during key points of development 
