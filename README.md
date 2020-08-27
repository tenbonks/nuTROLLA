# nuTROLLA
Hello there! this app provides a marketplace to sell refurbished controllers, from older gen, to new gen. A user will be able bask in the "Synthwave/Cyberpunk" theme of the site. There is something for every gamer here, the controller you receive, will look as fresh as the day it was released. Parts & tools are also sold so if you're a bit more hands on, you can replace those gummy joysticks with new one's

So feel free and have a browse, make an account, go wild!



# Demo

**A live demo of the site can be found** <a href="#" rel="nofollow" target="_blank">Here!</a>

![Desktop Demo](linktogohere# "Desktop Demo")

---

# UX

The flow of the site is designed so the user can find the type of product they want effortlessly, the three categories of the site will be presented by stylish buttons to get to what you want, the nav features all the categories which can be dropped down to filter by consoles or all of that category.

The category and console is shown on each product as a link, this will get all the category of that console, so for example it will let the user browse all "Playstation 1 Controllers"

Everything the user does, they will be notified of it with a nice little notification box, whether that be adjusting the bag, signing in or out or any errors, warnings or information.

During the development and planning of this project I took a lot of inspiration and guidance of the project Boutique Ado, as I found it fit's really well with what I wanted to achieve from my site idea, so structurally there are lots of similarities


USER STORIES, I have an external spreadsheet that will be linked here


**Mockup can be found under the folder "Mockup" in this repo, or [here](linktoimagehere#).**


there is no wireframe to show, as I adapted my wireframe into the mockup, mainly being because I was happy with the wireframe, so I started to style it.

---

# Features

* A simple, clear and responsive design, with a navbar always present allowing navigation to all relavent parts of the site.

- A vibrant header, with app's logo, drop down navigation links, this adapts to a bootsrap style dropdown on small devices.

- A responsive bag, which includes the grand total so a user can track their spending

- A paginated response, as to not bog down the system with a high amount of data

- A searchbar, so the user can search through product names and categories, to find exactly what they want

- A vibrant design featuring Synthwave/Cyberpunk colours, and a neon light effect shining down on the page

- Full CRUD (Create, Remove, Update, and Delete) operations on product database for admin of the site

- A user can sign up and have a profile, allowing them to save default information to use when checking out

- Stripe for secure payments

- If the user has a profile, then they will be able to view past purchases

---

**Features to implement in the future**

<details>
<summary>Stock adjustment when order created</summary>
<br>
This feature was a tricky one, as without stripe, I found it quite straight forward to implement, but I had issues with if stock were  to change between page loads. An example is if a product goes out of stock, and a user checks out with it in their bag just after, the payment would be proccessed by stripe and the user charged for items that are out of stock.
I spent a fair amount of trial and error on this and in the end decided to take out the code that ammended stock levels, and the sections that would return a user back to the bag page and notify them of the stock issue.
</details>

<details>
<summary>The tags used for selecting a console name, or category</summary>
<br>
The tags I currently use work, but I want to implement them in a cleaner way as it's a rather manual way passing the values to filter via href, the url ends up    getting very long on pages which on all controller, all parts, and all tools, also the console name will show up as a link even if there are no products, so      really it shouldn't be appearing as a link, as it leads to a no products page, I can manually get around it by changing the href but that isn't practical.
</details>
  
   
---

# Technologies used

Sum up all the technologies used in this line

* HTML 
    - give a quick sumup for what it was used for in the site

- CSS 
    - Is used for the styling of the site (as a basic example).

- Javascript 
    - handles stripe elements, and passing payment info

- jQuery 
    - handles the quantity selection icon buttons, back to top button, loading overlay, and some more intricate styling particularly the country field in delivery       info forms

- Python 
    - Handles the backend functions

- Django 
    - The framwork with batteries included, this handles one heck of a lot on this website, from which url does what and defining what that does in the views,           it's the bfoundation to this site and made making something of this size a lot quicker.

- Bootstrap 4 
    - Makes styling the site a breeze with it's components, easy classes and a simple grid layout

- Postgres -

- AWS Services - 

- Heroku 
    - Where the app is deployed

- ngrok 
    - An essential tool for testing webhooks when on a localmachine, as a 'https' address is required

--- 
# Testing

talk about the testing process here, I have put a dropdown menu for this in the readme to hide it as it is a long section of the page

<details><summary>CLICK HERE for testing process'</summary>
<p>

1. The content of the site should resize fluidly to specific breakpoints
    1. Load the website on a large desktop monitor.
    2. Check all pages of the site to check the layout is as expected.
    3. Open developer tools and repeat step 2 at xs, small, medium breakpoints
    4. The layout is as expected and elements will display to fit the device its being displayed on.
    5. This verifies that the site is responsive to different screen size, and aspect ratios.

2. Just keep adding numbered lists for each process taken when testing the site
    1. indent the subitem of the list for each stage of testing
</p>
</details>

---

# Deployment

**I developed this project on a local machine using VScode, And deployed it to Django for production via these steps**

**Connecting to GitHub**
- I logged into Github, and created a repository, named nutrolla.
- I used the CLI to add the created repo to my remotes | `git remote add origin https://github.com/tenbonks/nutrolla.git`
- Now I am connected to the repo, any small or major changes can be pushed to adhere to good version control.

Follow this along with the format used above

---


# Credits

**Content**

The JSON fixture files were created by me, the product images used are accredited in the media section below

---

**Media**

Product images were acquired from a dataset called [controllers](https://www.kaggle.com/charcoal/controllers) in Kaggle, by [Aaron Styles](https://www.kaggle.com/charcoal)

The Synthwave image I used for the background of the homepage is from [WallpaperAccess](https://wallpaperaccess.com/synthwave)

---

**Acknowledgements**

During this development I took a heavy amount of inspiration and guidance from the mini project featured in the learning material to learn about how to make production ready Django project, the planning and development were all aided by this project, the creator of the project is [ckz8780 Chris Z](https://github.com/ckz8780), a link to the project he made for Code Institute in [Botique Ado](#).


My mentor, Maranatha Ilesanmi for valuable sessions during key points of development 
