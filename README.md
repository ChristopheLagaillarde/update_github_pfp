# change_github_pfp_daily_into_the_pic_of_a_cat_that_does_not_exist
A personal project that allow me to change my github profile picture daily with pictures of cats that do not exist, this use Selenium and a website that is based on the machine learning algorithm StyleGAN2

# How to make it work 
Install selenium with Microsoft edge web driver, the driver should be named "msedgedriver.exe"
Rename "Credential_template.py" into "Credential.py" and open it, edit the attribut of the class into your own github credential (follow the commented instruction)
Open the change_github_pfp.py and change the path_to_pic variable to the path you desire to save your cat pic to 
When everything work correctly configure the app task screduler (or equivalent) to run the program with the frequency that you desire.
