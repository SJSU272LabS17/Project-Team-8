# Project-Team-8

Idea resource: http://ranjanr.blogspot.com/2017/02/brand-new-project-ideas-for-class-of.html

Abstract 1 - IoT proof of concept:

> A mobile dashboard (android tablet) to control all connected IoT devices in the house. This dashboard should allow control of lights, toaster oven, music player, thermostat or anything else connected via wifi in the house.

Recently, the idea of “smart home” have become more and more popular. We are trying to use Raspberry Pi to prototype this goal. First connect a Wi-Fi adapter or Ethernet cable to a Raspberry Pi to make sure it have internet access. Second, connect a couple of LEDs to it, in this case these LEDs will be controlled by Raspberry Pi . Then we will develop a mobile dashboard (mobile app or web app) to turn the LEDs on or off by sending request through a server (a server deployed to cloud or Raspberry Pi itself) which will in turn tell the Raspberry Pi which LEDs to control. So the process is basically “mobile dashboard” -> “server” -> “Raspberry Pi” -> “LEDs”.

Abstract 2 - Digital loyalty program app for small businesses:

> 80% of small businesses (specially mom & pop) can not afford to have sophisticated program to collect customer data and make them return to their businesses repeatedly. This app allows coffee shops, local grocery vendors, barbers and hair salons to create a digital loyalty program for their visitors and customers. 

Implementation: Design and develop a mobile application that runs on a mobile phone or a tablet for small and medium business to manage their loyalty membership program. The data can be stored in a database either locally or from the data center. We can then later retrieve those data and use tools like R to analyze them and present the result in the mobile app so that it can be visualized. Or we can create a interactive web application using JQuery or JavaScript. This mobile web app will focus on helping business owners keep an eye on every customers' purchase pattern and decide how to satisfy the customers' need by recommending relavent products or delivering vendors' marketing materials. 
