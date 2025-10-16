# Ex.06 Book Front Cover Page Design
## Date:11.10.2025

## AIM:
To design a book front cover page using HTML and CSS.

## DESIGN STEPS:

### Step 1:
Create a Django Admin project.

### Step 2:
Create an app in the Django interface.

### Step 3:
Create a folder named 'static' in the app folder.

### Step 4:
Create a new HTML file in the static folder.

### Step 5:
Write the HTML code with relevant CSS properties.

### Step 6:
Choose the appropriate style and color scheme.

### Step 7:
Insert the images in their appropriate places.

### Step 8:
Publish the website in the LocalHost.

## PROGRAM:
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Title - Front Page with Photo</title>
    
    <style>
        /* Basic CSS for the 'book cover' effect */
        body {
            font-family: 'Georgia', serif; /* Classic book font */
            display: flex;
            justify-content: center; 
            align-items: center; 
            min-height: 100vh; 
            margin: 0;
            background-color: #f0f0f0; 
        }

        .book-cover {
            width: 410px; 
            height: 550px; 
            background-color: #074965; /* Dark background for the cover */
            color: #fff; 
            padding: 20px;
            box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.5); 
            display: flex;
            flex-direction: column; 
            justify-content: space-between; 
            text-align: center;
        }

        /* --- Photo Styling --- */
        
        /* --------------------- */

        .book-title {
            font-size: 2em;
            margin-top: 30px; 
            text-transform: uppercase;
            letter-spacing: 2px;
            border-bottom: 2px solid #fff;
            padding-bottom: 10px;
        }

        .book-subtitle {
            font-size: 1.2em;
            margin-top: 10px;
        }

        .book-author {
            font-size: 1.5em;
            font-style: italic;
        }

        .footer-content {
             margin-bottom: 30px; 
        }
    </style>
    <style>
        .author-photo {
            width: 100px; 
            height: 100px; 
          
            object-fit: cover; 
            border: 3px solid #fff; 
            margin-bottom: 10px; 
        }
    </style>
</head>
<body>

    <div class="book-cover">
        
        <div class="cover-element">
            <p style="font-size: 0.8em;">A Classic Novel</p>
        </div>

        <header>
            <h1 class="book-title">
                The HTML Adventure
            </h1>
            <h2 class="book-subtitle">
                A Journey Into Web Structure and Design
            </h2>
        </header>
        
        <div class="footer-content">
            <img src="me.jpg" alt="Author's Photo" class="author-photo">
            
            <footer class="book-author">
                By Jane Doe
            </footer>
        </div>
        </div>

</body>
</html>

```

## OUTPUT:
![alt text](<Screenshot 2025-10-08 005105.png>)

## RESULT:
The program for designing book front cover page using HTML and CSS is completed successfully.
