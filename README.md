# La Galleria
#### La Galleria - a Django based personal gallery , 22/03/2021.
#### By Ryan Rotich
<img src="./static/images/landing.png"
     alt="landing"
     style="width=100%;" />
## Description
La Galleria is a Django based personal gallery. 
Noteable features of the app include:
<table>
<tr>
<td>
1. Admin portal:
Here, the app owner is required to login in by providing necessary credentials. Upon succesful login, they can then proceed to upload, update or delete an image. They can also create, delete and edit image loactions and categories.
<br>
2. Image details:
To view the image details, click on the respective image and a modal pops up. The modal has various features which are:
- Modal header: This contains the image name
- Modal body: This contains the magnified image, share icon, the category tag, image location, date and time the image was posted and last but not least, the image description
<br>
3. Image filtering by category and location:
- By category: To view images in the same category, one can search by category name in the search form located in the navbar or by clicking on the category tag located in the image modal
- By location: To view images from the same location, the user can click on the location name which is in the image modal
<br>
4. Image sharing: 
Spotted an image you'd love to share? The application allows for image sharing. To share a specific image, click on the image to reveal the image modal then click on the share icon which copies the share link to your clipboard.
</td>
</tr>
</table> 

## Live link
Visit the application on  https://instagram-ryan.herokuapp.com/.

## Development
To make advancements/modifications, follow these steps:

- Fork the repository
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request 

## Setup & Run instructions
- Create and activate a virtual environment
- Install the dependencies listed in the `requirements.txt`
- Create a `.env` file. This will contain environment variables as listed in the `.env.sample` file.
- Finally, run your app on `MODE='dev'` config for debugging purposes

## Technologies Used
Technologies used to develop this application:

1. Python v3.9.0
2. Django 3.0.7
3. Javascript
4. Cloudinary
5. Bootstrap
6. HTML 
7. CSS


## Support and contact details

Should you be unable to access the website, have any recommendations and/or questions, feel free to email me:[austinbrian005@gmail.com](mailto:austinbrian005@gmail.com)

### [License](LICENSE)
MIT license
Copyright (c) 2020 **Ryan Rotich**