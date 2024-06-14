---
title: Running a Verizon SIM in a Netgear Nighthawk
tags: [project-301-tech]
date: 2024-05-14

---
The first thing I needed to prioritize was immediate, reliable internet. Yesterday a meeting was cut short when every wifi signal in Deltaville dropped to < 1mbps; I asked and this is pretty common in the early evening (when the town sits down to Netflix binge and slurps up all the bandwidth). 
I've had a Netgear Nighthawk M6, the go-to standard mobile hotspot for digital nomads, for a couple years now. AT&T brands the devices and has a pretty strong lockdown on the hotspot market (no hardware from Verizon or T-Mobile holds a candle), and that was fine in Puerto Rico where Liberty (an AT&T subsidiary) is the dominant carrier. 

But now that I'm roaming around the coasts there is no telling what carrier will be the strongest in any given locale. When it comes to the USA, Verizon has the winning footprint especially when things get rural - and such is the case in Deltaville. T-Mobile (Mint) phone and AT&T SIM cards both have zero service within a thirty minute drive of my motel. My guess is this will be a pretty common scenario going forward. 

There are lots of things I'll need to figure out in the coming months, and I have grand plans for a peplink-startlink-5G mesh service that will keep me connected in even the most remote of locations; but right now, today, I need bandwidth to keep working. So time to set up the Nighthawk for multiple carriers. 

This is not a remotely straightforward process. My eventual success is due to many hours of assembling clues from the Netgear/AT&T/Verizon forums, so I am streamlining my findings here to hopefully save you the hassle. 

## The Steps
1. Unlock your Nighthawk
2. Create a fake IMEI 
3. Obtain a Verizon SIM with active service
4. Add a Verizon APN to your Nighthawk 
5. Bask in the glory of Verizon 5G

### 1. Unlock your Nighthawk
First you need AT&T to bless the divorce of your device from their service. If you are not absolutely sure that your device is unlocked, it almost certainly is - and if it's a Nighthawk, it is likely AT&T that has it locked. Also if you have done a factory reset or the battery has gotten really, really dead, it may have re-locked 🤦.
Visit the [AT&T unlock request](https://www.att.com/deviceunlock/unlockstep1) page, and **using your device IMEI** submit a request. The IMEI is on the sticker under the battery inside your Nighthawk. Step through the email verification, confirm, and get the unlock code emailed to you. Save this. 

### 2. Create a fake IMEI
This is because Verizon has a weird process for activating new SIM cards. They need a device IMEI, and it is very unlikely that your real IMEI will work (feel free to try it though). It is important to know that _this IMEI check does nothing_ - it doesn't register or connect the device, it is just like the magnetic card strip readers at ATM vestibules that only check for a strip (you can open that door with a driver's license or a library card, it doesn't matter) - Verizon is checking that the IMEI is the correct format before letting an agent activate a SIM. So, make a fake one that'll work. You can use this [IMEI Checker](https://www.imei.info/) to build a fake one, or just use `99003291234561` Where: 

- `9900329` is a Verizon device
- `123456` is literally me being lazy and making a fake 6 digit number
- `1` is the checksum digit for the rest of the number

### 3. Obtain a Verizon SIM with service
You'll want to go into a Verizon store to get this done. You may be able to do it online but I had no luck. Sign up for a post-paid data plan - the prepaid plans are deprioritized and it defeats the whole purpose of having an additional card if it won't have reliable service. Give the agent that home-made IMEI as the device IMEI. Drop in the newly activated Verizon SIM (the slot is under the battery). The device _MAY_ prompt you for that unlock code, or it may not. Connect to the device WIFI and log in to the admin pannel at http://attwifimanager (the credentials are usually `admin` and `password` but definitely change those! Since you'll be out in the world with this thing the risk is real). Go to `security => sim security` and see if there is an option to add an unlock code. If yes, great add it! If not no worries. 

### 4. Add the Verizon APN to your Nighthawk
If you were prompted for that unlock code or had the option to add one in the security section, you may already have working internet and can skip adding a new APN. Most of us are not that lucky. To manually update the network APN, go to `advanced settings => cellular` and at the bottom where it says APN click "add." Then create a new APN using these settings: 
**APN Name**: VZWINTERNET
**apn**: vzwinternet

Save it and make it the active APN. Then restart your device. 💥 **INTERNET** 💥

This is a hack of sorts in that the APN will need to be swapped based on the SIM - but hey, it's a working internet solution. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc1MjY3ODQ5OF19
-->