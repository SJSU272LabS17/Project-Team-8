# Project-Team-8

Abstract 3 - Music Analysis Web App - APPROVED

Traditional music players mostly focus on play music and music recommendation, but we want to give you more. Our music analysis web app combines a traditional music player with place recommendation using our unique analysis algorithm based on machine learning, more specifically, neural network.

UI: there are three parts of User Interface, one part is for music play, second part is for recommendation info bulletin and the last part is left blank for commercial ads or business fairs.

Backend: Using AWS EC2 container to hold our app online and S3 to store our data.

Algorithm: A neural network specifically trained for music analysis. Music files uploaded by users are fed to the network which output the type of the music and user's mood. The recommendation system will then suggest point of interest based on user’s mood and location

The model will be trained using pre-labelled music data of each type and mood and then stored in the cloud. When a user uploads a music file to our app, it will analyse it and determine the user’s mood. By combining user’s mood, current location, weather and time, the app will give related place suggestions based on our recommendation algorithm.  



![alt text](https://github.com/Adamkzh/Project-Team-8/pic/pr.jpeg)
-----------------------------------------------------------------------------
Old Idea

Idea resource: http://ranjanr.blogspot.com/2017/02/brand-new-project-ideas-for-class-of.html

Abstract 1 - IoT proof of concept:

> A mobile dashboard (android tablet) to control all connected IoT devices in the house. This dashboard should allow control of lights, toaster oven, music player, thermostat or anything else connected via wifi in the house.

Recently, the idea of “smart home” have become more and more popular. We are trying to use Raspberry Pi to prototype this goal. First connect a Wi-Fi adapter or Ethernet cable to a Raspberry Pi to make sure it have internet access. Second, connect a couple of LEDs to it, in this case these LEDs will be controlled by Raspberry Pi . Then we will develop a mobile dashboard (mobile app or web app) to turn the LEDs on or off by sending request through a server (a server deployed to cloud or Raspberry Pi itself) which will in turn tell the Raspberry Pi which LEDs to control. So the process is basically “mobile dashboard” -> “server” -> “Raspberry Pi” -> “LEDs”.

Abstract 2 - Digital loyalty program app for small businesses:

> 80% of small businesses (specially mom & pop) can not afford to have sophisticated program to collect customer data and make them return to their businesses repeatedly. This app allows coffee shops, local grocery vendors, barbers and hair salons to create a digital loyalty program for their visitors and customers. 

Implementation: Design and develop a mobile application that runs on a mobile phone or a tablet for small and medium business to manage their loyalty membership program. The data can be stored in a database either locally or from the data center. We can then later retrieve those data and use tools like R to analyze them and present the result in the mobile app so that it can be visualized. Or we can create a interactive web application using JQuery or JavaScript. This mobile web app will focus on helping business owners keep an eye on every customers' purchase pattern and decide how to satisfy the customers' need by recommending relavent products or delivering vendors' marketing materials. 
