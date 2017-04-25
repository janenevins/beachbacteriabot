# Beach Bot 

BeachBot tells users if ocean beaches in San Mateo County have unsafe levels of fecal bacteria.  

When a user enters the name of a San Mateo County beach into the web app, the bot will return one of two messages: 

“{beach_name} has an Entero bacteria count of {e_count} on the date of {process_date}. This is {number}times the safe limit.” 

But if the user enters the wrong beach name, it will return a list of beaches with this message: 'You must pick a beach from this list' followed by a list of beaches. 

This bot is inspired by the L.A. Times Quakebot and a story I’m writing about Pillar Point Harbor, which has the dirtiest beach in San Mateo County, Capistrano beach. 

Quakebot uses USGS data to write a brief story about recent earthquakes. The bot also tweets out information about earthquakes. Here’s a recent excerpt of a story written by the L.A. Times Quakebot, “Shallow magnitude 3.5 earthquake was reported Friday morning six miles from Yucaipa, Calif., according to the U.S. Geological Survey. The temblor occurred at 2:10 a.m. PST at a depth of 5.6 miles.”

San Mateo county has some of the most polluted beaches in California. I’m reporting on Pillar Point Harbor, the launch point for the world famous Titians of Mavericks big-wave surf contest. In 2014 the Harbor District spent a million dollars studying the source of the contamination, yet the beach at West Point Avenue made Heal the Bay’s top-ten list of the worst beaches in California again this year. 

This bot accompanies a story that investigates why it’s so hard to clean up Pillar Point Harbor using water sampling data from San Mateo County and the Surfrider Foundation, an environmental group. 

In the course of my reporting, I learned that after a rainfall, bacteria levels in the water can be several orders of magnitude over the safe limit. As someone who regularly disregarded the warning signs and surfed in contaminated water, I wanted to build a bot that provides the public with more information on just how bad the contamination is and how often the bacteria levels spike. 

When levels are too high, San Mateo County posts a tiny sign on the beach that many surfers and swimmers ignore. 
Like the Quakebot, future iterations of the BeachBot can proactively tweet when levels are too high, reaching people who might not seek out water quality information. The goal is to better inform the public about the local beach environment. 

The bot shows the Entero bacteria levels. I choose Entero bacteria because both the county and Surfrider, Entero bacteria as a standard measure of water quality. In the future, I’d like to add water sample data from Surfrider to the bot because Surfrider samples on the weekend, when the data is most relevant to swimmers and surfers. 

Enterococcus bacteria is found in the gut of warm blooded animals. It is an indicator that bacteria and viruses found in human and animal waste may be found in the water. The safe level is 104 ppm, but beaches in Pillar Point regularly post bacteria levels in the 1000s. Germs that cause gastrointestinal diseases like Giardia, Noro Virus and E. Coli can be found in contaminated waters. 

According to recent study by the Surfrider foundation in Southern California, high bacteria levels are correlated with illness. Twelve in 1000 surfers will get sick from surfing when bacteria levels are too high.   

The data comes from San Mateo County’s open data portal https://data.smcgov.org/Environment/Beach-and-Creek-Monitoring-Results/kpd9-xf4h/data.  

