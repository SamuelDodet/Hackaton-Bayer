<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Hackaton Bayer</h3>

  <p align="center">
    Project Done during the hackaton weekend organize by Bayer.
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong> Event Page </strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">Video Presentation</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Hunger For None][product-screenshot]](https://example.com)

This hackathon took place during last weekend of May 2021, with more than 400 participation. 
The purpose of this project is to use object detection 
and image processing in order to give the type of disease that the plant have. The farmer will with this information
have the possibility to threat it accurately.

I would like to precise that this project has been done during the second month of my bootcamp
in BeCode and any of these technologies have been seen before.

We use the PlantVillage dataset [1] by Hughes et al. consists of about 87,000 healthy and unhealthy leaf images divided 
into 38 categories by species and disease. Here we provide a subset of our experiments on working with this data. 
We also end up transfer learning from MobileNet and use the weights from pre-training on ImageNet.




### Built With

To achieve this challenge, here are the main framework use in it:

* [tensorflow](https://www.tensorflow.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [cv2](https://opencv.org/)



<!-- GETTING STARTED -->
## Getting Started



### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
2. Install NPM packages
   ```sh
   pip install requirement.txt
   ```
   or
   ```sh
   pip3 install requirement.txt
   ```
3. Data Sources
   
    * To add to main directory : https://www.kaggle.com/vipoooool/new-plant-diseases-dataset



<!-- USAGE EXAMPLES -->
## Usage

First, we will need to train the model by running model.py in app directory. 

Modelling steps:
   * Preprocessing Images
     * randomly translate pictures vertically or horizontally
      * rescale
      * randomly applying shearing transformations
      * randomly zooming inside pictures
      * fill_mode : filling in newly created pixels
   * generate batches of image data 
     
   * Training
     * get the base MobileNet model without including the top layers
      * create a small upstream model on top of the MobileNet using the functional API
      * Add Adam Optimizer
      * Training the model
      ![First Epoch](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)
        ![Last Epoch](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)
      * Review the process (plot)
        ![review](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)
      * Save the model    
   * Train Model on our dataset
   * Plotting Loss/Accuracy graph (informative purpose)
   * Saving Model

Flask api :

   * Run app.py
   * Loading Model
   * Add images from the list of test fruit and see result





<!-- ROADMAP -->
## Conclusion

This project has been an amazing experience and very stressful one. I had the opportunity to learn
so much in a short period of time.  
This is a disappointment that Covid-19 is still with us at this time and that i was unable to attempt 
other hackathon in Belgium as they all have been canceled.

Even with the fact that this project is not finished, it will stay as it is to keep the spirit of the
hackathon time limit.


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
