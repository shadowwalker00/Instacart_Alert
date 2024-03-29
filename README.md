# Instacart_Alert
## Intro
Selenium web bot to check availability of delivery slots from online groceries, including Amazon Fresh, Wholefoods and Instacart during this difficult quarantine period.
The scripts are not that generalized. Thus, welcome to pull requests.

## Usage
1. clone the repo to local
2. cd into the folder and activate the virtual env ```source bin/activate```
3. change the email and password in ```credential.json```
4. run the scripts
   1. [check instacart] ```python3 check_instacart.py```
   2. [check wholefoods] ```python3 check_wholefoods.py```
   3. [check amazon fresh] ```python3 check_fresh.py```
5. When available slot found, the speaker will make a sound saying, such as "Whole Food Find Slot GO GET IT". (Based on mac's say command. There might be other alternatives on windows and linux)
6. Then check out yourself manually.

**NOTE**: in order to checkout as fast as possible, you need to add items into cart before hand.
## Reference
https://medium.com/better-programming/build-amazonfresh-delivery-slot-alerts-c9e12a429e23

## Update
- [x] Fix bug for instacart after refresh
- [x] add windows platform sound alert (Thanks for @qwertyva1's contribution)
