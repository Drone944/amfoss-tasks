# POKE-SEARCH

I haven't heard about pyside6 and qt before, so I looked it up in google and read some stuff about it.
Then I followed all the installation guides given in the github repo. After that I went to the poke api website, got the api and used  the requests module to get the data of pikachu.

I learned how to read input from the textbox and stored it in a variable and updated the url to get the data of the pokemon that the user enters. This should only happen when the user clicks the search button, so I defined a function which is activated only when the user clicks the search button.
Then I learned how to get and display the image of the required pokemon for which I had to learn about QPixmap. When the user clicks the search button the pokemon's images is stored as a png file in the same directory and that png gets displayed on the GUI.

After that, I defined another function which is called when the capture button is clicked. his function saves the displayed Pokémon's PNG image in a folder named 'captured' and displays 'GOTCHA!!!,' signifying that the Pokémon has been successfully captured.

Then, I defined another function which is called when the display button is clicked. It creates a popup window, which is done by using QDialog. Two buttons 'next' and 'previous' are displayed on the window.
The 'Next' button reveals the next Pokémon that the user has captured, while the 'Previous' button displays the previous one.. This is done by putting all the file locations of the pngs(captured/NAME.png) in a list and iterating through the list using the indices.

Then I tried to add background image. At first the setStyleSheet didn't work as the background image appeared distorted as i was acting as the background images for all the widgets. I asked my friend who finished this task about the nackground image and he specified about "QPalette".
So I googled ,how to use QPalette, and setup the Background image and completed the task.
